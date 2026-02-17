# JythonNutpad

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Swing Sampler 

[SwingExamples](SwingExamples)

------------------------------------------------------------------------

From: Jeff Emanuel \<jemanuel \<at\> frii.com\>\
Subject: Re: Tranlating a simple Java editor into Jython\
Newsgroups: gmane.comp.lang.jython.user\
Date: 2007-03-24 19:07:37 GMT\
\
Anton Vredegoor wrote:\
\
\> Hello All,\
\>\
\> I\'m an experienced Python programmer with only a very basic\
\> understanding of Java. I\'m currently trying to translate this very\
\> simple Java editor into Jython.\
\> Any hints or complete or partial translations of\
\> the code are very welcome.\
\> [http://leepoint.net/notes-java/examples/components/editor/nutpad.html\[\[BR](http://leepoint.net/notes-java/examples/components/editor/nutpad.html%5B%5BBR)\]\] \>\
Here*s a quick translation. For the Java inner classes,\
translate them to top level classes that take the outer instance\
as a constructor argument. Java inner classes have an implicit\
pointer to the enclosing class instance. You must make that\
explicit.\
\*

:::: 
::: 
``` 
   1 from java.awt import *
   2 from java.awt.event import *
   3 from javax.swing import *
   4 from java.io import *
   5 from java.lang import System,Integer
   6  
   7 #/////////////////////////////////////////////////////////////////////// NutPad
   8 class NutPad(JFrame):
   9    #... Components
  10    _editArea=None
  11    _fileChooser = JFileChooser()
  12  
  13    #============================================================== constructor
  14    def __init__(self):
  15  
  16      #... Create actions for menu items, buttons, ...
  17      self._openAction = OpenAction(self)
  18      self._saveAction = SaveAction(self)
  19      self._exitAction = ExitAction(self)
  20  
  21      #... Create scrollable text area.
  22      self._editArea = JTextArea(15, 80)
  23      self._editArea.border=BorderFactory.createEmptyBorder(2,2,2,2)
  24      self._editArea.font=Font("monospaced", Font.PLAIN, 14)
  25      scrollingText = JScrollPane(self._editArea)
  26  
  27      #-- Create a content pane, set layout, add component.
  28      content = JPanel()
  29      content.setLayout(BorderLayout())
  30      content.add(scrollingText, BorderLayout.CENTER);
  31  
  32      #... Create menubar
  33      menuBar = JMenuBar()
  34      fileMenu = menuBar.add(JMenu("File"))
  35      fileMenu.setMnemonic('F')
  36      fileMenu.add(self._openAction)       # Note use of actions, not text.
  37      fileMenu.add(self._saveAction)
  38      fileMenu.addSeparator()
  39      fileMenu.add(self._exitAction)
  40  
  41      #... Set window content and menu.
  42      self.setContentPane(content)
  43      self.setJMenuBar(menuBar)
  44  
  45      #... Set other window characteristics.
  46      self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
  47      self.setTitle("NutPad")
  48      self.pack()
  49      self.setLocationRelativeTo(None)
  50      self.visible=1
  51  
  52 #//////////////////////////////////////////////// inner class OpenAction
  53 class OpenAction(AbstractAction):
  54    #============================================= constructor
  55    def __init__(self,outer):  # outer instance.
  56      AbstractAction.__init__(self,"Open...")
  57      self.outer=outer
  58      self.putValue(AbstractAction.MNEMONIC_KEY, Integer(ord('O')))
  59  
  60    #========================================= actionPerformed
  61    def actionPerformed(self, e):
  62      retval = self.outer._fileChooser.showOpenDialog(self.outer)
  63      if retval==JFileChooser.APPROVE_OPTION:
  64        f = self.outer._fileChooser.getSelectedFile()
  65        try:
  66          reader = FileReader(f)
  67          self.outer._editArea.read(reader, "")  # Use TextComponent read
  68        except IOException,ioex:
  69          System.out.println(e);
  70          System.exit(1);
  71  
  72 #////////////////////////////////////////////////// inner class SaveAction
  73 class SaveAction(AbstractAction):
  74    #============================================= constructor
  75    def __init__(self,outer):
  76      AbstractAction.__init__(self,"Save...")
  77      self.outer=outer
  78      self.putValue(AbstractAction.MNEMONIC_KEY, Integer(ord('S')))
  79  
  80    #========================================= actionPerformed
  81    def actionPerformed(self, e):
  82      retval = self.outer._fileChooser.showSaveDialog(self.outer)
  83      if retval == JFileChooser.APPROVE_OPTION:
  84        f = self.outer._fileChooser.getSelectedFile()
  85        try:
  86          writer = FileWriter(f)
  87          self.outer._editArea.write(writer)  # TextComponent write
  88        except IOException,ioex:
  89          JOptionPane.showMessageDialog(self.outer, ioex)
  90          System.exit(1)
  91  
  92 #/////////////////////////////////////////////////// inner class ExitAction
  93 class ExitAction(AbstractAction):
  94  
  95    #============================================= constructor
  96    def __init__(self,outer):
  97      AbstractAction.__init__(self,"Exit")
  98      self.outer=outer
  99      self.putValue(AbstractAction.MNEMONIC_KEY, Integer(ord('X')))
 100  
 101    #========================================= actionPerformed
 102    def actionPerformed(self, e):
 103      System.exit(0);
 104  
 105 #===================================================================== main
 106 if __name__=="__main__":
 107    NutPad()
```
:::
::::
