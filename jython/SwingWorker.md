# SwingWorker

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# SwingWorker Examples in Jython 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

The [SwingExamples](SwingExamples) page shows some good examples of using Swing components from Jython.

However, all of the examples perform the majority of their processing on the Swing Event Dispatch Thread and this is not a good technique to use in a real world application which needs to do any significant processing.

Very briefly, a Swing program normally comprises of three different types of thread:

- *Initial Threads* which execute the intial application code

- *Event Dispatch Thread* which executes all the event-handling code

- *Worker Threads* which execute time-consuming background tasks

Only the Event Dispatch Thread should access Swing components (with certain exceptions). Swing components should not even be created by other threads \-- including the Initial Threads.

A good description of these threads is given in the [Concurrency in Swing](http://java.sun.com/docs/books/tutorial/uiswing/concurrency/index.html) lesson in the Swing Tutorial.

The SwingWorker class described in the above lesson is only available in Java 6. However, it has been backported to earlier versions see [https://swingworker.dev.java.net/](https://swingworker.dev.java.net/)

The remainder of this section shows a translation of two of the examples from the Swing Tutorial to Jython.

- [Flipper.py](SwingWorker#flipper) \-- this is an example where the the worker thread has intermediate results which should be reflected in the GUI. The operation of this example is given [here](http://java.sun.com/docs/books/tutorial/uiswing/concurrency/interim.html)

- [ProgressBarDemo.py](SwingWorker#progress) \-- this is an example showing how the worker thread can communicate with the Event Dispatch Thread using Property Change Listeners. For a description of the example see [here](http://java.sun.com/docs/books/tutorial/uiswing/concurrency/bound.html)

:::: 
::: 
``` 
   1 # Flipper.py
   2 
   3 from java.lang import Runnable
   4 from java.util import Random
   5 from java.util.concurrent import ExecutionException
   6 from javax.swing import SwingWorker, SwingUtilities
   7 from javax.swing import BorderFactory
   8 from javax.swing import JButton, JFrame, JTextField
   9 from java.awt import GridBagLayout as awtGridBagLayout
  10 from java.awt import GridBagConstraints as awtGridBagConstraints
  11 from java.awt import Insets as awtInsets
  12 
  13 
  14 ###########################################################################
  15 class FlipTask(SwingWorker):
  16     "Class implementing long running task as a SwingWorker thread"
  17 
  18     #######################################################################
  19     def __init__(self, gui):
  20         self.gui = gui
  21         SwingWorker.__init__(self)
  22 
  23 
  24     def doInBackground(self):
  25         heads = 0
  26         total = 0
  27         random = Random()
  28         while not self.isCancelled():
  29             total += 1
  30             if random.nextBoolean():
  31                 heads += 1
  32             #publish the number of heads and total tosses
  33             self.super__publish([(heads, total)])
  34 
  35 
  36     def process(self, pairs):
  37         pair = pairs[len(pairs)-1]
  38         self.gui.headsText.text = "%d" % pair[0]
  39         self.gui.totalText.text = "%d" % pair[1]
  40         self.gui.devText.text = "%f" % ((1.0*pair[0]/pair[1]) - 0.5)
  41 
  42 
  43     def done(self):
  44         try:
  45             self.get()  #raise exception if abnormal completion
  46         except ExecutionException, e:
  47             raise SystemExit, e.getCause()
  48 
  49 ###########################################################################
  50 class Flipper(JFrame):
  51 
  52     def __init__(self):
  53         JFrame.__init__(self, "Flipper",
  54                     defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
  55                     layout=awtGridBagLayout(),
  56                     )
  57 
  58         self.constraints = awtGridBagConstraints(
  59                     insets=awtInsets(3, 10, 3, 10)
  60                     )
  61 
  62         self.border = BorderFactory.createLoweredBevelBorder()
  63 
  64         #Make text boxes
  65         self.headsText = self.makeText()
  66         self.totalText = self.makeText()
  67         self.devText = self.makeText()
  68 
  69         #Make buttons
  70         self.startButton = self.makeButton("Start", self.startPressed)
  71         self.stopButton = self.makeButton("Stop", self.stopPressed)
  72         self.stopButton.enabled = False
  73 
  74         #Display the window.
  75         self.pack()
  76         self.visible = True
  77 
  78 
  79     def makeText(self):
  80         t = JTextField(
  81                 20,
  82                 editable=False,
  83                 horizontalAlignment=JTextField.RIGHT,
  84                 border = self.border,
  85                 )
  86         self.add(t, self.constraints)
  87         return t
  88 
  89 
  90     def makeButton(self, caption, action):
  91         b = JButton(caption, actionPerformed=action)
  92         self.add(b, self.constraints)
  93         return b
  94 
  95 
  96     def _setButtonStates(self, started):
  97         self.stopButton.enabled = started
  98         self.startButton.enabled = not started
  99 
 100 
 101     def stopPressed(self, e):
 102         self._setButtonStates(started=False)
 103         self.flipTask.cancel(True)
 104         self.flipTask = None
 105 
 106 
 107     def startPressed(self, e):
 108         self._setButtonStates(started=True)
 109         self.flipTask = FlipTask(self)
 110         self.flipTask.execute()
 111         
 112 
 113 ###########################################################################
 114 class Runnable(Runnable):
 115     def __init__(self, runFunction):
 116         self._runFunction = runFunction
 117 
 118 
 119     def run(self):
 120         self._runFunction()
 121 
 122 ###########################################################################
 123 if __name__ == '__main__':
 124     SwingUtilities.invokeLater(Runnable(Flipper))
```
:::
::::

:::: 
::: 
``` 
   1 # ProgressBarDemo.py
   2 
   3 from java.lang import InterruptedException, Runnable, Thread
   4 from java.beans import PropertyChangeListener
   5 from java.util import Random
   6 from java.util.concurrent import ExecutionException
   7 from javax.swing import SwingWorker, SwingUtilities
   8 from javax.swing import BorderFactory
   9 from javax.swing import JButton, JFrame, JPanel, JProgressBar, \
  10                     JScrollPane, JTextArea
  11 from java.awt import Toolkit as awtToolkit
  12 from java.awt import BorderLayout as awtBorderLayout
  13 from java.awt import Cursor as awtCursor
  14 from java.awt import Insets as awtInsets
  15 
  16 ###########################################################################
  17 class Task(SwingWorker):
  18 
  19     def __init__(self, gui):
  20         self.gui = gui
  21         SwingWorker.__init__(self)
  22 
  23     def doInBackground(self):
  24         random = Random()
  25         progress = 0
  26         #Initialize progress property.
  27         self.super__setProgress(progress)
  28         while progress < 100:
  29             #Sleep for up to one second.
  30             try:
  31                 Thread.sleep(random.nextInt(1000))
  32             except InterruptedException, e:
  33                 pass
  34 
  35             #Make random progress.
  36             progress += random.nextInt(10)
  37             self.super__setProgress(min(progress, 100))
  38 
  39 
  40     def done(self):
  41         try:
  42             self.get()  #raise exception if abnormal completion
  43             awtToolkit.getDefaultToolkit().beep()
  44             self.gui.taskOutput.append("Done!\n")
  45             self.gui.startButton.enabled = True
  46             self.gui.cursor = None  #turn off the wait cursor
  47         except ExecutionException, e:
  48             raise SystemExit, e.getCause()
  49 
  50 
  51 
  52 ###########################################################################
  53 class ProgressBarDemo(JPanel, PropertyChangeListener):
  54     def __init__(self):
  55         JPanel.__init__(self, awtBorderLayout(),
  56                         border = BorderFactory.createEmptyBorder(20, 20, 20, 20)
  57                         )
  58 
  59         #Create the demo's UI.
  60         self.startButton = JButton("Start", actionPerformed=self.startPressed)
  61 
  62         self.progressBar = JProgressBar(0, 100, value=0, stringPainted=True)
  63 
  64         self.taskOutput = JTextArea(5, 20,
  65                             margin=awtInsets(5,5,5,5),
  66                             editable=True
  67                             )
  68 
  69         panel = JPanel()
  70         panel.add(self.startButton)
  71         panel.add(self.progressBar)
  72 
  73         self.add(panel, awtBorderLayout.PAGE_START)
  74         self.add(JScrollPane(self.taskOutput), awtBorderLayout.CENTER)
  75 
  76 
  77     def startPressed(self, e):
  78         "Invoked when the user presses the start button"
  79         self.startButton.enabled = False
  80         self.cursor = awtCursor.getPredefinedCursor(awtCursor.WAIT_CURSOR)
  81         #Instances of javax.swing.SwingWorker are not reusuable, so
  82         #we create new instances as needed.
  83         task = Task(self)
  84         task.addPropertyChangeListener(self)
  85         task.execute()
  86 
  87 
  88     def propertyChange(self, e):
  89         # Invoked when task's progress property changes.
  90         if e.propertyName == "progress":
  91             self.progressBar.value = e.newValue
  92             self.taskOutput.append("Completed %d%% of task\n"% e.newValue)
  93 
  94 
  95 def createAndShowGUI():
  96     # Create the GUI and show it. As with all GUI code, this must run
  97     # on the event-dispatching thread.
  98     frame = JFrame("ProgressBarDemo",
  99                     defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
 100                     )
 101     #Create and set up the content pane.
 102     newContentPane = ProgressBarDemo()
 103     newContentPane.setOpaque(True)      #content panes must be opaque
 104     frame.contentPane = newContentPane
 105 
 106     #Display the window.
 107     frame.pack()
 108     frame.visible = True
 109 
 110 ###########################################################################
 111 class Runnable(Runnable):
 112     def __init__(self, runFunction):
 113         self._runFunction = runFunction
 114 
 115 
 116     def run(self):
 117         self._runFunction()
 118 
 119 ###########################################################################
 120 if __name__ == '__main__':
 121     SwingUtilities.invokeLater(Runnable(createAndShowGUI))
```
:::
::::
