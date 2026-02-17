# SwingExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Swing Examples in Jython 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

Using Java Swing with Jython is a lot of fun and makes it really easy to develop a nice UI in much less code then a similar Java app. All of the examples below work with Jython 2.2 and a 1.5 (or greater) JVM is strongly recommended.

Many of these have been tested and will work using jdk/jre \<1.5. If you are using an older JVM will need to change the code from *frame.add* to *frame.contentPane.add*

Below there are several examples that cover various swing components. Some time in the past I found a Jython script on the Georgia Tech web site that showed off a number of components, being that the web is constantly changing I have provided a copy of the [SwingSampler](SwingSampler) with the permission of the professor who believes he is the author.

In March 2007, Anton Vredegoor asked the Jython mailing list for help converting [Java Simple Editor](http://leepoint.net/notes-java/examples/components/editor/nutpad.html) and Jeff Emanuel provided complete conversion to Jython. Here is the [JythonNutpad](JythonNutpad) that was posted.

The Jython Mailing list is a great source of help. If you have questions or problems the mailing list is a good place to look for help but there is no substitute for RTFM or Google searches before hand.

## Simple Swing examples 

These are fairly simple examples but show components.

### Hello, World! 

These are some ways of creating a simple frame with the title \'Hello, World!\' on it.

:::: 
::: 
``` 
   1 from javax.swing import JFrame
   2 JFrame('Hello, World!', defaultCloseOperation=JFrame.EXIT_ON_CLOSE, size=(300, 300), locationRelativeTo=None).setVisible(True)
```
:::
::::

:::: 
::: 
``` 
   1 from javax.swing import JFrame
   2 f = JFrame('Hello, World!', defaultCloseOperation=JFrame.EXIT_ON_CLOSE, size=(300, 300), locationRelativeTo=None)
   3 f.setVisible(True)
```
:::
::::

The above examples can also be done \"Java-style\", i.e. a bit more verbose as shown below:

:::: 
::: 
``` 
   1 from javax.swing import JFrame
   2 f = JFrame('Hello, World!')
   3 f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
   4 f.setSize(300, 300)
   5 f.setLocationRelativeTo(None)
   6 f.setVisible(True)
```
:::
::::

And yet another way of doing it is shown below:

:::: 
::: 
``` 
   1 from javax.swing import JFrame
   2 f = JFrame('Hello, World!')
   3 f.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
   4 f.size = (300, 300)
   5 f.locationRelativeTo = None
   6 f.visible = True
```
:::
::::

### JButton and Button events 

Just a simple example.

:::: 
::: 
``` 
   1 """
   2 A simple example that shows button event handling
   3 
   4 Greg Moore
   5 Sept 2007
   6 """
   7 
   8 from javax.swing import *
   9 from java.awt import BorderLayout
  10 
  11 class Example:
  12   def setText(self,event):
  13       self.label.text = 'Button clicked.'
  14 
  15   def __init__(self):
  16     frame = JFrame("Jython Example JButton")
  17     frame.setSize(100, 100)
  18     frame.setLayout(BorderLayout())
  19     self.label = JLabel('Hello from Jython')
  20     frame.add(self.label, BorderLayout.NORTH)
  21     button = JButton('Click Me',actionPerformed=self.setText)
  22     frame.add(button, BorderLayout.SOUTH)
  23     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  24     frame.setVisible(True)
  25 
  26 if __name__ == '__main__':
  27         Example()
```
:::
::::

### JTextField 

:::: 
::: 
``` 
   1 """
   2 Swing JTextField example in Jython.
   3 
   4 Creates 2 text fields and clicking the button copies text in one textfield
   5 to the other. 
   6 
   7 Greg Moore
   8 Sept 2007
   9 """
  10 
  11 from javax.swing import *
  12 from java.lang import *
  13 
  14 class Example:
  15 
  16   def copyText(self,event):
  17       self.textfield2.text = self.textfield1.text
  18 
  19   def __init__(self):
  20         # These lines setup the basic frame, size.
  21         # the setDefaultCloseOperation is required to completely exit the app
  22         # when you click the close button
  23     frame = JFrame("Jython JText Field Example")
  24     frame.setSize(200, 150)
  25     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  26 
  27     # Create Panel and add swing components and show it.
  28     pnl = JPanel()
  29     frame.add(pnl)
  30     self.textfield1 = JTextField('Type something here',15)
  31     pnl.add(self.textfield1)
  32     self.textfield2 = JTextField('and click Copy', 15)
  33     pnl.add(self.textfield2)
  34     copyButton = JButton('Copy',actionPerformed=self.copyText)
  35     pnl.add(copyButton)
  36     frame.pack()
  37     frame.setVisible(True)
  38 
  39 if __name__ == '__main__':
  40   #start things off.
  41   Example()
```
:::
::::

### JRadioButton 

:::: 
::: 
``` 
   1 """
   2 Swing JRadioButton example in Jython.
   3 
   4 Creates radio buttons and event handler
   5 
   6 Greg Moore
   7 Sept 2007
   8 """
   9 
  10 # Using import * is bad form but since this is just a example I'll take the
  11 # easy way out instead of specifing each package.
  12 from javax.swing import *
  13 from java.awt import *
  14 
  15 
  16 class RadioButtonExample:
  17   def radioBtnbCheck(self,event):
  18     # Process the events and update the label
  19     statusText = ""
  20     if self.radioBtn1.isSelected():
  21       statusText = "Radio Button 1 is selected "
  22     if self.radioBtn2.isSelected():
  23       statusText = statusText + "Radio Button 2 is selected "
  24     self.rbStatusLabel.text = statusText
  25 
  26   def __init__(self):
  27         # These lines setup the basic frame, size and layout
  28         # the setDefaultCloseOperation is required to completely exit the app
  29         # when you click the close button
  30     frame = JFrame("Jython Example JRadioButton")
  31     frame.setSize(400, 150)
  32     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  33     frame.setLayout(BorderLayout())
  34 
  35     # create 2 panels the top one containing radio buttons and the bottom one
  36     # has the label and button. add them to the frame and show it.
  37     rbPanel = JPanel()
  38     frame.add(rbPanel,BorderLayout.NORTH)
  39     self.radioBtn1 = JRadioButton('Radio Button 1')
  40     self.radioBtn2 = JRadioButton('Radio Button 2')
  41     rbPanel.add(self.radioBtn1)
  42     rbPanel.add(self.radioBtn2)
  43     rbBtnGroup = ButtonGroup()
  44     rbBtnGroup.add(self.radioBtn1)
  45     rbBtnGroup.add(self.radioBtn2)
  46 
  47     panel = JPanel()
  48     panel.setLayout(BorderLayout())
  49     frame.add(panel,BorderLayout.SOUTH)
  50     button = JButton('Check',actionPerformed=self.radioBtnbCheck)
  51     panel.add(button,BorderLayout.WEST)
  52     self.rbStatusLabel =JLabel()
  53     panel.add(self.rbStatusLabel,BorderLayout.EAST)
  54     frame.pack()
  55     frame.setVisible(True)
  56 
  57 if __name__ == '__main__':
  58   #start things off.
  59   RadioButtonExample()
```
:::
::::

### JCheckBox 

:::: 
::: 
``` 
   1 """
   2 Swing JCheckBox example in Jython.
   3 
   4 Creates a couple checkboxes and and event handler
   5 
   6 Greg Moore
   7 Sept 2007
   8 """
   9 
  10 # Using import * is bad form but since this is just a example I'll take the
  11 # easy way out instead of specifing each package.
  12 from javax.swing import *
  13 from java.awt import *
  14 
  15 class CheckBoxExample:
  16 
  17   def cbEvents(self,event):
  18         # Process the events and update the label
  19     cbStatusMsg=""
  20     if self.chkbox1.isSelected():
  21       cbStatusMsg = "checkbox1 is selected "
  22     if self.chkbox2.isSelected():
  23       cbStatusMsg = cbStatusMsg + "checkbox2 is selected"
  24     self.cbStatusLabel.text = cbStatusMsg
  25 
  26   def __init__(self):
  27         # These lines setup the basic frame, size and layout
  28         # the setDefaultCloseOperation is required to completely exit the app
  29         # when you click the close button
  30         frame = JFrame("Jython JCheckBox Example")
  31         frame.setLayout(BorderLayout())
  32         frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  33         
  34         # this could be done with only one JPanel or use different layout
  35         # create a panel for the checkboxes
  36         cbPanel = JPanel()
  37         frame.add(cbPanel,BorderLayout.NORTH)
  38         self.chkbox1 = JCheckBox('checkbox 1')
  39         self.chkbox2 = JCheckBox('checkbox 2')
  40         cbPanel.add(self.chkbox1)
  41         cbPanel.add(self.chkbox2)
  42 
  43         # create a second panel with the button and label
  44         panel = JPanel()
  45         panel.setLayout(BorderLayout())
  46         frame.add(panel,BorderLayout.SOUTH)
  47         button = JButton('check',actionPerformed=self.cbEvents)
  48         panel.add(button,BorderLayout.SOUTH)
  49         self.cbStatusLabel =JLabel('select one and click button')
  50         panel.add(self.cbStatusLabel,BorderLayout.CENTER)
  51 
  52         # now that the panels have been added to the frame show our creation
  53         frame.pack()
  54         frame.setVisible(True)
  55 
  56 if __name__ == '__main__':
  57   #start things off.
  58   CheckBoxExample()
```
:::
::::

### JList 

- Also see [http://www.jython.org/applets/list.html](http://www.jython.org/applets/list.html)

:::: 
::: 
``` 
   1 """
   2 Swing JList example in Jython.
   3 
   4 Creates a simple list of cities and then updates a JLabel based on the
   5 the city selected.
   6 
   7 Greg Moore
   8 Sept 2007
   9 """
  10 
  11 # Using import * is bad form but since this is just a example I'll take the
  12 # easy way out instead of specifing each package.
  13 from javax.swing import *
  14 from java.awt import *
  15 
  16 class JListExample:
  17 
  18   def listSelect(self,event):
  19         # Process the events from the list box and update the label
  20     selected = self.list.selectedIndex
  21     if selected >= 0:
  22       cityName = self.data[selected]
  23       self.label.text = cityName
  24 
  25   def __init__(self):
  26 
  27         # These lines setup the basic frame, size and layout
  28         # the setDefaultCloseOperation is required to completely exit the app
  29         # when you click the close button
  30     frame = JFrame("Jython JList Example")
  31     frame.setSize(200, 225)
  32     frame.setLayout(BorderLayout())
  33     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  34 
  35     # set up the list and the contents of the list
  36     # the python typle get converted to a Java vector
  37     self.data = ('Portland','San Francisco','Madrid','Venice','Starnberg','New York','Paris','London')
  38     self.list = JList(self.data)
  39     spane = JScrollPane()
  40     spane.setPreferredSize(Dimension(100,125))
  41     spane.getViewport().setView((self.list))
  42 
  43         # a panel is a bit over kill but this is a demo. :)
  44     panel = JPanel()
  45     panel.add(spane)
  46     frame.add(panel,BorderLayout.CENTER)
  47 
  48         # create the button, and city label and the show our work
  49         # with Jython only one line is needed create a button and attach an
  50         # event handler.
  51     btn = JButton('Select',actionPerformed=self.listSelect)
  52     frame.add(btn,BorderLayout.SOUTH)
  53     self.label = JLabel(' Select City and click select')
  54     frame.add(self.label,BorderLayout.NORTH)
  55     frame.pack()
  56     frame.setVisible(True)
  57 
  58 
  59 if __name__ == '__main__':
  60         #start things off.
  61         JListExample()
```
:::
::::

### JComboBox 

*under construction*

Here are a couple of combo box examples. one requires a button click and the other is more dynamic [ComboboxExample](./ComboboxExample.html).

:::: 
::: 
``` 
   1 """
   2 Swing JComboBox example in Jython.
   3 
   4 Creates a simple comboBox of cities and then updates a JLabel based on the
   5 the city selected after button click.
   6 
   7 Greg Moore
   8 Sept 2007
   9 
  10 """
  11 
  12 from javax.swing import *
  13 from java.awt import *
  14 
  15 class JComboBoxExample:
  16 
  17   def cbSelect(self,event):
  18     selected = self.cb.selectedIndex
  19     if selected >= 0:
  20       data = self.data[selected]
  21       self.label.text = data + " selected"
  22 
  23   def __init__(self):
  24     frame = JFrame("Jython JComboBox Example")
  25     frame.setSize(200, 250)
  26     frame.setLayout(BorderLayout())
  27 
  28     self.data = ('Portland','San Francisco','Madrid','Venice','Starnberg','New York','Paris','London')
  29     self.cb = JComboBox(self.data)
  30 
  31     pnl = JPanel()
  32     pnl.add(self.cb)
  33 
  34     frame.add(pnl,BorderLayout.NORTH)
  35 
  36     btn = JButton('click me',actionPerformed=self.cbSelect)
  37     frame.add(btn,BorderLayout.SOUTH)
  38     self.label = JLabel('Select a city then click button')
  39     frame.add(self.label,BorderLayout.CENTER)
  40     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  41     frame.setVisible(True)
  42 
  43 if __name__ == '__main__':
  44         JComboBoxExample()
```
:::
::::

### JTree 

This example is a bit long so here is the [JtreeExample](JtreeExample)

### JTable 

I think this is the most amazing example. This creates a small table that has editable cells, cursor movement and resizeable. The is at least 75% shorter then a comparable java version. Time is money, and here is proof the jython can save you money and make you more productive.

:::: 
::: 
``` 
   1 """
   2 
   3 Swing JTable example in Jython.
   4 
   5 Creates a simple table.
   6 
   7 Greg Moore
   8 Sept 2007
   9 
  10 
  11 """
  12 
  13 from javax.swing import *
  14 from java.awt import *
  15 from javax.swing.table import DefaultTableModel
  16 
  17 class Example:
  18 
  19   def __init__(self):
  20     frame = JFrame("Jython JTable Example")
  21     frame.setSize(400, 150)
  22     frame.setLayout(BorderLayout())
  23 
  24     self.tableData = [
  25       ['numbers', '67890' ,'This'],
  26       ['mo numbers', '2598790', 'is'],
  27       ['got Math', '2598774', 'a'],
  28       ['got Numbers', '1234567', 'Column'],
  29       ['got pi','3.1415926', 'Apple'],
  30        ]
  31     colNames = ('Col Labels','Go','Here')
  32     dataModel = DefaultTableModel(self.tableData, colNames)
  33     self.table = JTable(dataModel)
  34 
  35     scrollPane = JScrollPane()
  36     scrollPane.setPreferredSize(Dimension(300,100))
  37     scrollPane.getViewport().setView((self.table))
  38 
  39     panel = JPanel()
  40     panel.add(scrollPane)
  41 
  42     frame.add(panel, BorderLayout.CENTER)
  43     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  44     frame.setVisible(True)
  45 
  46 if __name__ == '__main__':
  47         Example()
```
:::
::::

### JTabbedPane 

This create a simple JTabbedPane example. Here is another [TabbedExample](TabbedExample).

:::: 
::: 
``` 
   1 """
   2 
   3 Swing JTabbedPane example in Jython.
   4 
   5 Greg Moore
   6 Sept 2007
   7 
   8 """
   9 
  10 from javax.swing import *
  11 from java.awt import *
  12 
  13 class Example:
  14 
  15   def __init__(self):
  16     frame = JFrame("Jython JTabbedPane Example")
  17     frame.setSize(400, 300)
  18     frame.setLayout(BorderLayout())
  19 
  20     tabPane = JTabbedPane(JTabbedPane.TOP)
  21 
  22     label = JLabel("<html><br>This is a tab1</html>")
  23     panel1 = JPanel()
  24     panel1.add(label)
  25     tabPane.addTab("tab1", panel1)
  26 
  27     label2 = JLabel("This is a tab2")
  28 
  29     panel2 = JPanel()
  30     panel2.add(label2)
  31     tabPane.addTab("tab2", panel2)
  32 
  33     frame.add(tabPane)
  34     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  35     frame.setVisible(True)
  36 
  37 if __name__ == '__main__':
  38         Example()
```
:::
::::

### JSplitPane 

This just creates a simple split pane. nothing fancy. ![:)](/wiki/modernized/img/smile.png ":)")

:::: 
::: 
``` 
   1 """
   2 Swing JSplitPane example in Jython.
   3 
   4 Greg Moore
   5 Sept 2007
   6 
   7 """
   8 
   9 from javax.swing import *
  10 from java.awt import *
  11 class Example:
  12 
  13   def __init__(self):
  14     frame = JFrame("Jython JTable Example")
  15     frame.setSize(400, 300)
  16     frame.setLayout(BorderLayout())
  17 
  18     splitPane = JSplitPane(JSplitPane.HORIZONTAL_SPLIT);
  19 
  20     label1 = JLabel("This is a panel1")
  21     panel1 = JPanel()
  22     panel1.add(label1)
  23     splitPane.setLeftComponent(panel1);
  24 
  25     label2 = JLabel("This is a panel2")
  26 
  27     panel2 = JPanel()
  28     panel2.add(label2)
  29     splitPane.setRightComponent(panel2);
  30     splitPane.setDividerLocation(150);
  31 
  32     frame.add(splitPane)
  33     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  34     frame.setVisible(True)
  35 
  36 if __name__ == '__main__':
  37     Example()
```
:::
::::

### JDesktopPane and JInternalFrame Demo 

:::: 
::: 
``` 
   1 from javax.swing import JFrame, JDesktopPane, JInternalFrame, JMenuBar, JMenu, JMenuItem, JScrollPane
   2 
   3 class DesktopPaneAndInternalFrameDemo(JFrame):
   4     """
   5 
   6     A demonstration of JDesktopPane() and JInternalFrame()
   7     By: astigmatik, Sept 2007
   8 
   9     """
  10     def __init__(self):
  11         """
  12         The JFrame.__init__ lines below don't have to be written in multiple lines.
  13         This is just for readability.
  14         """
  15         JFrame.__init__(self,
  16                         'JDesktopPane and JInternalFrame Demo',
  17                         size=(500, 500),
  18                         defaultCloseOperation=JFrame.EXIT_ON_CLOSE)
  19 
  20         self.internalFrameCounter = 0
  21         self.createDesktop()
  22         self.createMenus()
  23 
  24     def createDesktop(self):
  25         self.desktop = JDesktopPane()
  26         """
  27         Normally, it's not allowed to do a "self.object = value" inside the class
  28         if the self.object has not been instantiated. However, in this case, since we are
  29         calling self.createDesktopPane() on __init__(), then it is ok.
  30         """
  31 
  32         self.contentPane.add(JScrollPane(self.desktop)) # This is the same as self.getContentPane().add(...)
  33 
  34     def createMenus(self):
  35 
  36         menu = JMenu('File')
  37         menu.add(JMenuItem('Create new JInternalFrame', actionPerformed=self.createInternalFrame))
  38 
  39         menubar = JMenuBar()
  40         menubar.add(menu)
  41 
  42         self.setJMenuBar(menubar)
  43 
  44     def createInternalFrame(self, event):
  45         """
  46         event has to be supplied whenever there is an event generated, viz. from a menu being clicked,
  47         mouse button being clicked, or keypresses, etc.
  48         """
  49         self.internalFrameCounter += 1
  50 
  51         iframeName = 'JInternalFrame %s' % self.internalFrameCounter
  52         iframe     = JInternalFrame(iframeName, 1, 1, 1, 1, size=(400, 400), visible=1)
  53         """
  54         The 1's refer to boolean resizable, closable, maximizable, and iconifiable.
  55         Jython's True and False are 1 and 0 respectively. So all the 1's above can be replaced with True.
  56         """
  57 
  58         self.desktop.add(iframe)
  59         iframe.setSelected(1)
  60         iframe.moveToFront()
  61 
  62 
  63 if __name__ == '__main__':
  64     demo = DesktopPaneAndInternalFrameDemo()
  65     demo.setLocation(30, 30)
  66     demo.show()
```
:::
::::

### Decorator to add a function to SwingUtilities.invokeLater donated by Alex Grönholm 

:::: 
::: 
``` 
   1 from java.lang import Runnable
   2 from javax.swing import SwingUtilities
   3  
   4 class RunnableWrapper(Runnable):
   5     def __init__(self, func, *args, **kwargs):
   6         self.func = func
   7         self.args = args
   8         self.kwargs = kwargs
   9  
  10     def run(self):
  11         self.func(*self.args, **self.kwargs)
  12  
  13 def runswing(func):
  14     """Schedules the given function for execution in the Event Dispatch Thread."""
  15     def wrapper(*args, **kwargs):
  16         SwingUtilities.invokeLater(RunnableWrapper(func, *args, **kwargs))
  17     return wrapper
```
:::
::::
