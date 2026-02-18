# DelegationEventModel

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Delegation Event Model** is \...

------------------------------------------------------------------------

**pro**

- ??

------------------------------------------------------------------------

**cons**

- ??

:::: 
::: 
``` 
   1 # Code is Public Domain.
   2 # Basic objects:
   3 
   4 class Event(object):
   5     """ Object that contain information on the event message """
   6     def __init__(self):
   7         self._source = None
   8         
   9     def getSource(self):
  10         return self._source
  11 
  12     def setSource(self,value):
  13         self._source = value
  14 
  15     source = property(getSource,setSource)
  16 
  17     def getEventType(self):
  18         return self.__class__.__name__
  19 
  20     eventType = property(getEventType)
  21 
  22 class Listener(object):
  23     """ Object that wait for Event Message """
  24     def processEvent(self,event):
  25         funcName = "process%sEvent" % event.eventType
  26         if hasattr(self,funcName):
  27             getattr(self,funcName)(event)
  28 
  29 class Source(object):
  30     """ Object that produce Event Message """
  31     def __init__(self):
  32         self._listeners = {}
  33 
  34     def _initListenersList(self,eventType):
  35         if not eventType in self._listeners:
  36             self._listeners[eventType] = []
  37 
  38     def addEventListener(self,eventType,listener):
  39         self._initListenersList(eventType)
  40         self._listeners[eventType].append(listener)
  41 
  42     def publishEvent(self,event):
  43         self._initListenersList(event.eventType)
  44         event.source = self
  45         for listener in self._listeners[event.eventType]:
  46             listener.processEvent(event)
  47 
  48 # let's go for subclassing all of this stuff:
  49 
  50 class Command(Event):
  51     """ a command has an action attribute that indicate what has to be done"""
  52     def __init__(self,action):
  53         super(Command,self).__init__()
  54         self.action = action
  55 
  56 class CommandListener(Listener):
  57     """ listen for command event.
  58     It call the method do<<Action>> when a command event occur...
  59     """
  60     def processCommandEvent(self,event):
  61         funcName = "do%s" % event.action.capitalize()
  62         if hasattr(self,funcName):
  63             getattr(self,funcName)(event)
  64 
  65 class CommandSource(Source):
  66     """ here the producer of command Event """
  67     addCommandListener = lambda self,listener: self.addEventListener('Command',listener)
  68 
  69     def push(self):
  70         # do stuf here
  71         e = Command('push')
  72         self.publishEvent(e)
  73 
  74     def move(self):
  75         # do stuff here
  76         e = Command('move')
  77         self.publishEvent(e)
  78 
  79     def sayHello(self):
  80         print "Hi! I'm the  Command source"
  81 
  82 # and now implement some listeners :
  83 
  84 class MyCommandListener(CommandListener):
  85     """ here one listener of command Event """
  86     def doPush(self,event):
  87         print 'MyCmdListener:\tpush\t',event.source
  88 
  89     def doMove(self,event):
  90         print 'MyCmdListener:\tmove\t',event.source
  91         # see how you can act on the source
  92         event.source.sayHello()
  93 
  94 class MyAllEventListener(Listener):
  95     """ here a special listener that wait for any event """
  96     def processEvent(self,event):
  97         print 'AllEvent:\t',event.eventType,'\t',event
  98 
  99 def test():
 100     s = CommandSource()
 101     # add both listener to the producer
 102     s.addCommandListener(MyCommandListener())
 103     s.addCommandListener(MyAllEventListener())
 104     # now do some stuf on the source
 105     print '-'*10,'push','-'*10
 106     s.push()
 107     print '-'*10,'move','-'*10
 108     s.move()
 109 
 110 
 111 test()
```
:::
::::

------------------------------------------------------------------------

I\'m no pattern expert, but I believe the accepted name for this pattern is [ObserverPattern](http://c2.com/cgi/wiki?ObserverPattern "Wiki"). You\'ve combined it in your example with the [CommandPattern](http://c2.com/cgi/wiki?CommandPattern "Wiki"), which I think is unnecessary for the point you are trying to make. (Which, I believe, is the ObserverPattern.)

I\'d make *two* pages on this wiki; One for the [CommandPattern](./CommandPattern.html), and one for the [ObserverPattern](../language/ObserverPattern), both demonstrating the code in Python, and talking about it specificly from the perspective of Python. I would link *both* pages to their [PortlandPatternRepository](http://c2.com/cgi/wiki?PortlandPatternRepository "Wiki") equivalents. It\'s true that it\'s messy over there, some times, but until we get a wiki with higher [DegreesOfEditorialControl,](http://www.emacswiki.org/cgi-bin/community/DegreesOfEditorialControl) C2 wiki is the canonical place for talking about design patterns in the abstract on [the public web.](http://www.emacswiki.org/cgi-bin/community/ThePublicWeb)

\-- [LionKimbro](../people/LionKimbro)

I do not think so. Look at [DEMAtSun](http://java.sun.com/j2se/1.4.2/docs/guide/awt/1.3/designspec/events.html). Note that the [CommandPattern](http://c2.com/cgi/wiki?CommandPattern "Wiki") is slightly different but not that far or it might also be an instanciation of the DelegationEventModel\... What I\'m trying to do is to add usefull code here so I may be wrong on the name\... ![;-)](/wiki/europython/img/smile4.png%20";-)")

\-- Loïc Fejoz

So, adjust [CommandPattern](http://c2.com/cgi/wiki?CommandPattern "Wiki"), to include your case, or make a new page on C2? I guess my basic idea is: I think it would be cool to cooperate with C2. ![:)](/wiki/europython/img/smile.png%20":)")

\-- [LionKimbro](../people/LionKimbro)
