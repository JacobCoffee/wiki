# JtreeExample

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Swing JTtee Example 

back to [SwingExamples](SwingExamples)

------------------------------------------------------------------------

:::: 
::: 
``` 
   1 """
   2 Swing JTree example in Jyhton.
   3 
   4 Sticking with my City theme, this createa a J tree with 2 branches
   5 one with cities starting with M and the other branch with cties starting
   6 with S. This examples using a button event to show the selected city.
   7 
   8 Greg Moore
   9 Sept 2007
  10 """
  11 
  12 from javax.swing import *
  13 from java.awt import *
  14 from javax.swing.tree import DefaultMutableTreeNode
  15 
  16 class Example:
  17 
  18   def __init__(self):
  19     mCitiesData = ['Memphis', 'Melbourne', 'Milan',
  20                    'Marrakech', 'Moscow', 'Munich']
  21 
  22     sCitiesData = ['San Francisco', 'Salzburg', 'Santiago',
  23                    'Sydney', 'Sandnessjoen', 'Stockholm']
  24 
  25     frame = JFrame("Jython JTree Example")
  26     frame.setSize(400, 350)
  27     frame.setLayout(BorderLayout())
  28 
  29     root = DefaultMutableTreeNode('Cities')
  30     mCities = DefaultMutableTreeNode('Cities starting with M')
  31     sCities = DefaultMutableTreeNode('Cities starting with S')
  32     root.add(mCities)
  33     root.add(sCities)
  34 
  35     #now add the cities starting with M & S
  36     self.addCities(mCities, mCitiesData)
  37     self.addCities(sCities, sCitiesData)
  38     self.tree = JTree(root)
  39 
  40     scrollPane = JScrollPane()  # add a scrollbar to the viewport
  41     scrollPane.setPreferredSize(Dimension(300,250))
  42     scrollPane.getViewport().setView((self.tree))
  43 
  44     panel = JPanel()
  45     panel.add(scrollPane)
  46     frame.add(panel, BorderLayout.CENTER)
  47 
  48     btn = JButton('Select', actionPerformed = self.citySelect)
  49     frame.add(btn,BorderLayout.SOUTH)
  50     self.label = JLabel('Select city')
  51     frame.add(self.label, BorderLayout.NORTH)
  52     frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  53     frame.setVisible(True)
  54     self.addCities
  55 
  56   def addCities(self, branch, branchData=None):
  57     '''  add data to tree branch
  58          requires branch and data to add to branch
  59     '''
  60     # this does not check to see if its a valid branch
  61     if branchData == None:
  62         branch.add(DefaultMutableTreeNode('No valid data'))
  63     else:
  64         for item in branchData:
  65           # add the data from the specified list to the branch
  66           branch.add(DefaultMutableTreeNode(item))
  67 
  68   def citySelect(self, event):
  69     selected = self.tree.getLastSelectedPathComponent()
  70     #check to make sure a city is selected
  71     if selected == None:
  72       self.label.text = 'No city selected'
  73     else:
  74       self.label.text = str(selected)
  75     #this is more Jythonic then:
  76     #self.label.text = selected.toString()
  77 
  78 if __name__ == '__main__':
  79  Example()
```
:::
::::

back to [SwingExamples](SwingExamples)
