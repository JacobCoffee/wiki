# State Machine via Decorators

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## State Machine Decorator Module 

### Overview 

This module provides a set of decorators that are useful for implementing state machines of the type described by UML 2.0 state charts. The overhead of these decorators may be too high for them to be useful in parsing applications.

The code for the state machine decorator module is given below. Examples are given following the code.

### License 

    Copyright (C) 2010, 2011 Rodney Drenth
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:
    1. Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
    3. Neither the name of the project nor the names of the author
       may be used to endorse or promote products derived from this software
       without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTERS``AS IS''
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.

### Python Code 

    import types
    import itertools

    import logging
    logging.basicConfig(
        filename="gf_info.txt",
        format = "%(levelname)-10s %(message)s",
        level = logging.ERROR )
    from functools import wraps

    def truncated(alist, cmprsn):
        for  x in alist:
            if x.__name__ == cmprsn: break
            yield x

    class ContextBase(object):
       pass

    class _StateVariable(object):
       """ Attribute of a class to maintain state .
         
       State Variable objects are instantiated indirectly via calls to the
       TransitionTable class's initialize method.  TransitionTable objects are created
       at the class level.
       """

       def __init__(self, transTable, context):
          """Constructor - set to initial state"""
          self.__current_state = transTable.initialstate
          self.__next_state = transTable.initialstate
          self.sTable = transTable
          self.__statestack=[]
          self.__ctxClass = context.__class__

       def toNextState(self, context):
          """Transition to next state, if a next_state is differnt.
          
          In addition to the actual state transition, it invokes onLeave 
          and onEnter methods as required.
          """
          if self.__next_state is not self.__current_state:
             cc = context.__class__
             tt_name = self.sTable.inst_state_name
             logging.debug("Transitioning to state %s"%self.__next_state.__name__)

             def callInState(methName, crnt_state):
                if (hasattr(crnt_state, methName) or hasattr(context, methName)):
                   nmro = [crnt_state,]
                   nmro.extend(cc.__mro__)
                   psudoClassName = "%s_%s"%(cc.__name__, crnt_state.__name__)
                   stCls = type( psudoClassName, tuple(nmro), {})
                   context.__class__ = stCls
                   getattr(context, methName)()     # call the onEnter or onLeave method here
                   context.__class__ = cc

             callInState('onLeave', self.__current_state)
             self.__setState( context )
             callInState('onEnter', self.__current_state)

       def __setState(self, context ):
          """low level funky called from toNextState"""
          cc = context.__class__
          mro = cc.__mro__
          if ( self.__current_state not in mro):
             self.__current_state = self.__next_state
             return

          logging.debug("Current state %s in mro"% self.__current_state.__name__)
          def f(anc):
             return self.__next_state if anc == self.__current_state else anc
          newmro = tuple(f(anc) for anc in cc.__mro__)
          tt_name = self.sTable.inst_state_name
          cls_name ="%s_%s"%(self.__ctxClass.__name__, self.__next_state.__name__) 
          context.__class__ = type(cls_name, newmro, {})

       def pushState(self, newState, context = None):
          """PushState - allows going to another state with intent of returning
             to the current one."""
          self.__statestack.append(self._current_state)
          self.__next_state = newState
          if context:
             self.toNextState(context)

       def popState(self, context = None):
          """Pop back to the previously pushed state (pushState)"""
          self.__next_state = self.__statestack.pop()
          if (context):
             self.toNextState( context)

       def name(self):
          """Return name of current state"""
          return self.__current_state.__name__

       def setXition(self, func):
          """ Sets the state to transition to upon seeing a transtion event
          
          This method should only be called by the decorators impl'd in this module.
          """
          nxState = self.__current_state.nextStates[func.__name__]
          if nxState is not None:
             self.__next_state = nxState;

       def getFunc(self, func, contxt):
          """Gets the state dependant action method, wrapped in a try-catch block.

          This method should only be called by the decorators impl'd in this module.
          """
          crnt = self.__current_state
          svar_name = self.sTable.inst_state_name
          svCtxt = self.__ctxClass
          
          cc = contxt.__class__
          pseudoclas = "%s_%s"%(cc.__name__, crnt.__name__)

          nmro = [crnt]
          lhead = itertools.takewhile( lambda x: x != svCtxt, crnt.__mro__)

          if svCtxt in cc.__mro__:
             ltail = itertools.dropwhile( lambda x: x!= svCtxt, cc.__mro__)
          else:
             ltail = cc.__mro__
          nmro.extend(ltail)
             
          logging.debug("%s - %s - %s - [%s]\n"%(func.__name__, cc.__name__,
            svar_name,  ", ".join( cls.__name__ for cls in truncated(nmro,'TopLevelWindow' ))))
          stCls = type( pseudoclas, tuple(nmro), {})

          contxt.__class__ = stCls

          try:
             funky = getattr(contxt, func.__name__)
          except:
             funky = None
             
          contxt.__class__ = cc   # revert...
          if funky is None:
             t = "'%s' has no attribute '%s' in state %s" % (self.name(), 
                         func.__name__, crnt.__name__)
             raise NotImplementedError(t)

          # function with wrapping attribute means we've recursed all the way back
          #   to the context class and need to call the func as a default.
          if  hasattr(funky, "wrapping") and (funky.wrapping == self.sTable.inst_state_name):
             def funcA(*args, **kwargs):
                return func(contxt, *args, **kwargs)
             funky = funcA

          def wrappd2( self, *args, **kwargs):
             # wrap in try - except in event that funky() does something funky
             try:         
                self.__class__ = stCls
                retn = funky( *args, **kwargs)
             finally:
                self.__class__ = cc  
             return retn

          return wrappd2

    # -----------------------------------------------------------------------------
    class TransitionTable(object):
       """Defines a state table for a state machine class

       A state table for a class is associated with the state variable in the instances
       of the class. The name of the state variable is given in the constructor to the 
       StateTable object.  StateTable objects are attributes of state machine classes, 
       not intances of the state machine class.   A state machine class can have more
       than one StateTable.
       """
       def __init__(self, stateVarblName):
          """Transition Table constructor - state varblName is name of associated
          instance state variable.  """
          self.inst_state_name = stateVarblName
          self.eventList = []
          self.initalState = None
          nextStates = {}

       def initialize(self, ctxt):
          """Create a new state variable in the context.  State variable refs this
          transition table."""
         
          ctxt.__dict__[self.inst_state_name] = _StateVariable(self, ctxt)

       def _addEventHandler(self, funcName):
          """Notifies the current object of a metho that handles a transition.

          This is called by two of the decorators implemented below
          """
          self.eventList.append(funcName)

       def nextStates(self, subState, nslList):
          """Sets up transitions from the state specified by substate

          subState is one of the derived state classes, subclassed from the
          context state machine class. nslList is a list of states to which 
          the context will transition upon the invocation of one of the 
          transition methods.  'None' may be specified instead of an actual
          state if the context is to remain in the same state upon invocation
          of the corresponding method.
          """
          if len(nslList) != len(self.eventList):
             j = "Expected %s Got %s."%(len(self.eventList), len(nslList))
             raise RuntimeError("Wrong number of states in transition list.\n%s"%j)
          subState.nextStates = dict(zip(self.eventList, nslList))


    # -----------------------------------------------------------------------------
    def event( state_table):
       """Decorator for indicating an Event or 'Action' method.

       The decorator is applied to the methods of the state machine class to 
       indicate that the method will invoke a state dependant behavior. States
       are implemented as subclasses of the context(state machine) class .
       """
       stVarName = state_table.inst_state_name
       def wrapper(func):
          @wraps(func)
          def objCall(self, *args, **kwargs):
             state_var = getattr(self, stVarName)
             rtn = state_var.getFunc(func, self)(self, *args, **kwargs)
             return rtn 

          objCall.wrapping = stVarName
          return objCall
       return wrapper


    def transition( state_table ):
       """Decorator used to set up methods which cause transitions between states.

       The decorator is applied to methods of the context (state machine) class. 
       Invoking the method may cause a transition to another state.  To define
       what the transitions are, the nextStates method of the TransitionTable class
       is used.
       """
       stVarName = state_table.inst_state_name

       def wrapper(func):
          state_table._addEventHandler( func.__name__)

          @wraps(func)
          def objCall(self, *args, **kwargs):
             state_var = getattr(self, stVarName)
             state_var.setXition(func)
             rtn = func(self, *args, **kwargs)
             state_var.toNextState(self)
             return rtn

          objCall.wrapping  =stVarName
          return objCall

       return wrapper

    def transitionevent( state_table):
       """A decorator which is essentially the combination of the above two. 
       
       Can both invoke state dependent method and trigger a state 
       transition.  Mostly equivalent to :
       @Transition(xitionTable)
       @Event(xitionTable)
       """
       stVarName = state_table.inst_state_name
       def wrapper(func):
          state_table._addEventHandler( func.__name__)

          @wraps(func)
          def objCall(self, *args, **kwargs):
             state_var = getattr(self, stVarName)
             state_var.setXition(func)
             rtn = state_var.getFunc(func, self)(self, *args, **kwargs)
             state_var.toNextState(self)
             return rtn

          objCall.wrapping = stVarName
          return objCall

       return wrapper

## Examples of Use 

### Simple Example 

The example has three states, which rotate to the next state whenever the writeName method is called. In StateA, the text is printed out in lower case. In states StateB and StateC the text is printed out in upper case.

    import DecoratorStateMachine as dsm
    class StateContext( dsm.ContextBase):
            ttable = dsm.TransitionTable('myState')

            def __init__(self):
                    self.ttable.initialize(self)

            @dsm.transitionevent(ttable)
            def writeName(self, name):
                    pass

    class StateA(StateContext):
            def writeName(self, name):
                    print name.lower()

    class StateB(StateContext):
            def writeName(self, name):
                    print name.upper()

    class StateC(StateB):
            pass

    # Set up transition table to cause states totoggle
    StateContext.ttable.nextStates(StateA, (StateB,))
    StateContext.ttable.nextStates(StateB, (StateC,))
    StateContext.ttable.nextStates(StateC, (StateA,))
    StateContext.ttable.initialstate = StateA

    if __name__=='__main__':
       days=("Monday","Tuesday","Wednesday","Thursday",
          "Friday","Saturday","Sunday")
       ctxt = StateContext()
       for day in days:
          ctxt.writeName(day)
       x = raw_input("done>")

#### Output 

    monday
    TUESDAY
    WEDNESDAY
    thursday
    FRIDAY
    SATURDAY
    sunday

### Miss Grant\'s Controller 

The specification for this controller comes from Martin Fowler. This example uses wxPython as well as the state machine module.

    import wx
    import DecoratorStateMachine as dsm
    class MyFrame(wx.Frame, dsm.ContextBase):

       xtable = dsm.TransitionTable('pstate')
       dtable = dsm.TransitionTable('dstate')

       def __init__(self):
          self.xtable.initialize(self)
          self.dtable.initialize(self)

          wx.Frame.__init__(self, None, -1, "My Frame", size=(410,250))
          family = wx.SWISS
          style = wx.NORMAL
          weight = wx.BOLD
          font = wx.Font(12,family,style,weight, False, "Verdana")
          self.SetFont(font)

          panel = wx.Panel(self, -1)

          self.btnDoor = self.makeButton(panel,  "Door", (50,20), self.onToggleDoor)
          self.btnLight = self.makeButton(panel, "Light", (180,20), self.onLightOn )
          self.btnDrawer = self.makeButton(panel, "Drawer", (50,60), self.onOpenDrawer)
          self.btnPanel = self.makeButton(panel, "Panel", (180,60), self.onClosePanel)
          self.btnPanel.Disable()

          self.textArea = wx.StaticText(panel, -1, "Locked", pos=(50,100), size=(100,35))

          # onEnter called here would invoke MyFrame.onEnter (below)
          # call the current state's onEnter method indirectly through onInit()
          self.onInit()     

       def onEnter(self):
          print "Shouldn't get here. Should call some state's onEnter functions instead."

       @dsm.transitionevent(dtable)
       def onToggleDoor(self, event): pass

       @dsm.event(dtable)
       def onInit(self):
          self.onEnter()            # calls onEnter for current dtable/dstate state

       @dsm.transition(xtable)
       def onOpenDoor(self): pass

       @dsm.transition(xtable)
       def onCloseDoor(self): pass

       @dsm.transition(xtable)
       def onLightOn(self, event): pass

       @dsm.transition(xtable)
       def onOpenDrawer(self, event): pass

       @dsm.transition(xtable)
       def onClosePanel(self, event): pass

       def makeButton( self, panel, label, positn, handler ):
          button = wx.Button(panel, -1, label, pos=positn, size=(120,35))
          self.Bind(wx.EVT_BUTTON, handler, button)
          return button

    class DoorOpen(MyFrame):
       doorLabel = "Close Door"
       def onEnter(self):
          print self.dstate.name()
          self.btnDoor.SetLabel( self.doorLabel )
          
       def onToggleDoor(self, event):
          self.onCloseDoor()

    class DoorClosed(DoorOpen):
       doorLabel = "Open Door"

       def onToggleDoor(self, event):
          self.onOpenDoor()

    MyFrame.dtable.nextStates(DoorOpen, (DoorClosed,))
    MyFrame.dtable.nextStates(DoorClosed, (DoorOpen,))
    MyFrame.dtable.initialstate = DoorOpen

    class Idle(MyFrame):
       """this is an initial state"""
       def onEnter(self):
          print self.pstate.name()

    class Unlocked(Idle):
       def onEnter(self):
          print self.pstate.name()
          self.btnPanel.Enable()
          self.btnDoor.Disable()
          self.textArea.SetLabel("Unlocked")
       def onLeave(self):
          self.textArea.SetLabel("Locked")
          self.btnPanel.Disable()
          self.btnDoor.Enable()

    class Active(Idle):
       pass
    class LightOn(Idle):
       pass
    class DrawerOpen(Idle):
       pass

    MyFrame.xtable.nextStates(Idle, (Idle, Active, Idle, Idle, Idle))
    MyFrame.xtable.nextStates(Active, (Idle, Active, LightOn, DrawerOpen, None))
    MyFrame.xtable.nextStates(LightOn, (Idle, None,  None, Unlocked, None ))
    MyFrame.xtable.nextStates(DrawerOpen, (Idle, None, Unlocked, None, None))
    MyFrame.xtable.nextStates(Unlocked, (Idle, None, None, None, Idle))
    MyFrame.xtable.initialstate = Idle

    if __name__=='__main__':
       app = wx.PySimpleApp()
       frame = MyFrame()
       frame.Show(True)
       app.MainLoop()

#### Explanation 

There are actually two states in the context. One is for the state of the door, opened or closed. The other is for the main controller. The DoorOpen and DoorClosed states simply translate the onToggleDoor event to invoke either onCloseDoor or onOpenDoor.

The \@transition decorator indicates the method can cause a state transition. The method body will be invoked if one is provided. The parameter on the decorator is the state table that governs the transition. When leaving a state, the state\'s onLeave method is called, if one is defined. When entering a state the state\'s onEnter method is called.

The \@event decorator indicates the method is state dependent. The parameter on the decorator is used to determine which state variable (via the transition table) in the context (there may be multiple) contains the state whose method is to be invoked.

The \@transitionevent decorator is a combination of the above two. A state dependent method is invoked, and it may cause a transition to a new state. The transition happens after the event method is invoked.

Since states are subclasses of the context, or subclasses of other states, rules governing method or attribute resolution apply. For instance DoorClosed is a subclass of DoorOpened, so when \'onEnter\' of the DoorClosed state is called, it uses the one for DoorOpened. Since DoorClosed has defined a different value for doorLabel, the correct label is set on the door button.

### Alternative Miss Grant\'s Controller Example 

    import wx
    import DecoratorStateMachine as dsm
    class MyFrame(wx.Frame, dsm.ContextBase):

       dtable = dsm.TransitionTable('dstate')

       def __init__(self):
          self.dtable.initialize(self)

          wx.Frame.__init__(self, None, -1, "My Frame", size=(410,250))
          font = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False, "Verdana")
          self.SetFont(font)

          panel = wx.Panel(self, -1)

          self.btnDoor = self.makeButton(panel,  "Door", (50,20), self.onToggleDoor)
          self.btnLight = self.makeButton(panel, "Light", (180,20), self.onLightOn )
          self.btnDrawer = self.makeButton(panel, "Drawer", (50,60), self.onOpenDrawer)
          self.btnPanel = self.makeButton(panel, "Panel", (180,60), self.onClosePanel)
          self.btnPanel.Disable()

          self.textArea = wx.StaticText(panel, -1, "Locked", pos=(50,100), size=(100,35))

          # onEnter called here would invoke MyFrame.onEnter (below)
          # call the current state's onEnter method indirectly through onInit()
          self.onInit()     

       def onEnter(self):
          print "Shouldn't get here. Should call some state's onEnter function instead."

       @dsm.transition(dtable)
       def onToggleDoor(self, event): pass

       @dsm.event(dtable)
       def onInit(self):
          self.onEnter()            # calls onEnter for current dtable/dstate state

       @dsm.event(dtable)
       def onLightOn(self, event): pass

       @dsm.event(dtable)
       def onOpenDrawer(self, event): pass

       @dsm.event(dtable)
       def onClosePanel(self, event): pass

       def makeButton( self, panel, label, positn, handler ):
          button = wx.Button(panel, -1, label, pos=positn, size=(120,35))
          self.Bind(wx.EVT_BUTTON, handler, button)
          return button

    class DoorOpen(MyFrame):
       doorLabel = "Close Door"

       def onEnter(self):
          print self.dstate.name()
          self.btnDoor.SetLabel( self.doorLabel )
          
    class DoorClosed(DoorOpen):
       doorLabel = "Open Door"
       xtable = dsm.TransitionTable('pstate')

       def onEnter(self):
          # Check self's class and return if it's not DoorClosed.
          # otherwise if one of the xtable substates hasn't defined 'onEnter', we 
          # could go into infinite recursion.
          if  self.__class__.__name__ != "MyFrame_DoorClosed":
             return
          DoorOpen.onEnter(self)
          self.xtable.initialize(self)
          self.doEnter()

       @dsm.event(xtable)
       def doEnter(self):
          self.onEnter()

       @dsm.transition(xtable)
       def onLightOn(self, event): pass

       @dsm.transition(xtable)
       def onOpenDrawer(self, event): pass

       @dsm.transition(xtable)
       def onClosePanel(self, event): pass

    MyFrame.dtable.nextStates(DoorOpen, (DoorClosed,))
    MyFrame.dtable.nextStates(DoorClosed, (DoorOpen,))
    MyFrame.dtable.initialstate = DoorOpen

    class Active(DoorClosed):
       def onEnter(self):
          print self.pstate.name()

    class LightOn(Active):
       pass
    class DrawerOpen(Active):
       pass
    class Idle(Active):
       pass

    class Unlocked(Active):
       def onEnter(self):
          print self.pstate.name()
          self.btnPanel.Enable()
          self.btnDoor.Disable()
          self.textArea.SetLabel("Unlocked")

       def onLeave(self):
          self.textArea.SetLabel("Locked")
          self.btnPanel.Disable()
          self.btnDoor.Enable()

    DoorClosed.xtable.nextStates(Active, (LightOn, DrawerOpen, None))
    DoorClosed.xtable.nextStates(LightOn, (None, Unlocked, None ))
    DoorClosed.xtable.nextStates(DrawerOpen, (Unlocked, None, None))
    DoorClosed.xtable.nextStates(Unlocked, (None, None, Idle))
    DoorClosed.xtable.nextStates(Idle, (None, None, None))
    DoorClosed.xtable.initialstate = Active

    if __name__=='__main__':
       app = wx.PySimpleApp()
       frame = MyFrame()
       frame.Show(True)
       app.MainLoop()

#### Explanation 

There are also two state tables in this example. The difference being that the DoorClosed state acts as the context for the second set of states. The onEnter method of the DoorClosed state re-initializes the second state to Active. In the DoorClosed state, the onLightOn, onOpenDrawer, and onClosePanel can cause transitions on the second state varible. These methods are events on the first state variable(dstate), and when in the DoorOpen state, the events do not get invoked for the xtable related state.
