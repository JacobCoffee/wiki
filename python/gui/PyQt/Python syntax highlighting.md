# PyQt/Python syntax highlighting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

If you need a code editor with syntax highlighting, but don\'t want something as heavyweight as [QsciScintilla](http://www.riverbankcomputing.co.uk/static/Docs/QScintilla2/classQsciScintilla.html), you can use the [QSyntaxHighlighter](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qsyntaxhighlighter.html) class to apply highlighting to a [QPlainTextEdit](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qplaintextedit.html) widget.

This example was based on existing work by [Carson Farmer](http://www.carsonfarmer.com/?p=333) and [Christophe Kibleur](http://lateral.netmanagers.com.ar/weblog/2009/09/21.html#BB831), and an [example on the SciPres wiki](http://artis.inrialpes.fr/Membres/Xavier.Decoret/resources/scipres/wiki/index.php/Python.py). One aspect not addressed by this prior work is handling of Python\'s triple-quoted strings, which may span multiple lines; the QSyntaxHighlighter documentation includes an example for C++ comments, but those have different beginning and ending delimiters `/* ... */`{.backtick}, whereas Python\'s triple-quoted strings have the same delimiter at the beginning and end. These are handled by the `match_multiline`{.backtick} method and by treating the triple-quotes within strings as an special case \--there may be an easier way to do this, but it seems to work pretty well.

I have placed this code under the [Modified BSD License](http://directory.fsf.org/wiki/License:BSD_3Clause) because I believe the author intended it to be freely used. However, I don\'t believe that I originally wrote this example, though I was responsible for migrating it to the Python Wiki. \-- [DavidBoddie](DavidBoddie) 2017-01-19 20:34:17

I modified this code to fix a problem when triple-quotes were embedded inside strings. \-- [Artemio Garza Reyna](./Artemio(20)Garza(20)Reyna.html) 2021-08-08 20:26:00

:::: 
::: 
``` 
   1 # syntax.py
   2 
   3 import sys
   4 
   5 from PySide2 import QtCore, QtGui, QtWidgets
   6 
   7 def format(color, style=''):
   8     """Return a QTextCharFormat with the given attributes.
   9     """
  10     _color = QtGui.QColor()
  11     _color.setNamedColor(color)
  12 
  13     _format = QtGui.QTextCharFormat()
  14     _format.setForeground(_color)
  15     if 'bold' in style:
  16         _format.setFontWeight(QtGui.QFont.Bold)
  17     if 'italic' in style:
  18         _format.setFontItalic(True)
  19 
  20     return _format
  21 
  22 
  23 # Syntax styles that can be shared by all languages
  24 STYLES = {
  25     'keyword': format('blue'),
  26     'operator': format('red'),
  27     'brace': format('darkGray'),
  28     'defclass': format('black', 'bold'),
  29     'string': format('magenta'),
  30     'string2': format('darkMagenta'),
  31     'comment': format('darkGreen', 'italic'),
  32     'self': format('black', 'italic'),
  33     'numbers': format('brown'),
  34 }
  35 
  36 
  37 class PythonHighlighter (QtGui.QSyntaxHighlighter):
  38     """Syntax highlighter for the Python language.
  39     """
  40     # Python keywords
  41     keywords = [
  42         'and', 'assert', 'break', 'class', 'continue', 'def',
  43         'del', 'elif', 'else', 'except', 'exec', 'finally',
  44         'for', 'from', 'global', 'if', 'import', 'in',
  45         'is', 'lambda', 'not', 'or', 'pass', 'print',
  46         'raise', 'return', 'try', 'while', 'yield',
  47         'None', 'True', 'False',
  48     ]
  49 
  50     # Python operators
  51     operators = [
  52         '=',
  53         # Comparison
  54         '==', '!=', '<', '<=', '>', '>=',
  55         # Arithmetic
  56         '\+', '-', '\*', '/', '//', '\%', '\*\*',
  57         # In-place
  58         '\+=', '-=', '\*=', '/=', '\%=',
  59         # Bitwise
  60         '\^', '\|', '\&', '\~', '>>', '<<',
  61     ]
  62 
  63     # Python braces
  64     braces = [
  65         '\{', '\}', '\(', '\)', '\[', '\]',
  66     ]
  67 
  68     def __init__(self, parent: QtGui.QTextDocument) -> None:
  69         super().__init__(parent)
  70 
  71         # Multi-line strings (expression, flag, style)
  72         self.tri_single = (QtCore.QRegExp("'''"), 1, STYLES['string2'])
  73         self.tri_double = (QtCore.QRegExp('"""'), 2, STYLES['string2'])
  74 
  75         rules = []
  76 
  77         # Keyword, operator, and brace rules
  78         rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
  79             for w in PythonHighlighter.keywords]
  80         rules += [(r'%s' % o, 0, STYLES['operator'])
  81             for o in PythonHighlighter.operators]
  82         rules += [(r'%s' % b, 0, STYLES['brace'])
  83             for b in PythonHighlighter.braces]
  84 
  85         # All other rules
  86         rules += [
  87             # 'self'
  88             (r'\bself\b', 0, STYLES['self']),
  89 
  90             # 'def' followed by an identifier
  91             (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
  92             # 'class' followed by an identifier
  93             (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),
  94 
  95             # Numeric literals
  96             (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
  97             (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
  98             (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
  99 
 100             # Double-quoted string, possibly containing escape sequences
 101             (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
 102             # Single-quoted string, possibly containing escape sequences
 103             (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),
 104 
 105             # From '#' until a newline
 106             (r'#[^\n]*', 0, STYLES['comment']),
 107         ]
 108 
 109         # Build a QRegExp for each pattern
 110         self.rules = [(QtCore.QRegExp(pat), index, fmt)
 111             for (pat, index, fmt) in rules]
 112 
 113     def highlightBlock(self, text):
 114         """Apply syntax highlighting to the given block of text.
 115         """
 116         self.tripleQuoutesWithinStrings = []
 117         # Do other syntax formatting
 118         for expression, nth, format in self.rules:
 119             index = expression.indexIn(text, 0)
 120             if index >= 0:
 121                 # if there is a string we check
 122                 # if there are some triple quotes within the string
 123                 # they will be ignored if they are matched again
 124                 if expression.pattern() in [r'"[^"\\]*(\\.[^"\\]*)*"', r"'[^'\\]*(\\.[^'\\]*)*'"]:
 125                     innerIndex = self.tri_single[0].indexIn(text, index + 1)
 126                     if innerIndex == -1:
 127                         innerIndex = self.tri_double[0].indexIn(text, index + 1)
 128 
 129                     if innerIndex != -1:
 130                         tripleQuoteIndexes = range(innerIndex, innerIndex + 3)
 131                         self.tripleQuoutesWithinStrings.extend(tripleQuoteIndexes)
 132 
 133             while index >= 0:
 134                 # skipping triple quotes within strings
 135                 if index in self.tripleQuoutesWithinStrings:
 136                     index += 1
 137                     expression.indexIn(text, index)
 138                     continue
 139 
 140                 # We actually want the index of the nth match
 141                 index = expression.pos(nth)
 142                 length = len(expression.cap(nth))
 143                 self.setFormat(index, length, format)
 144                 index = expression.indexIn(text, index + length)
 145 
 146         self.setCurrentBlockState(0)
 147 
 148         # Do multi-line strings
 149         in_multiline = self.match_multiline(text, *self.tri_single)
 150         if not in_multiline:
 151             in_multiline = self.match_multiline(text, *self.tri_double)
 152 
 153     def match_multiline(self, text, delimiter, in_state, style):
 154         """Do highlighting of multi-line strings. ``delimiter`` should be a
 155         ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
 156         ``in_state`` should be a unique integer to represent the corresponding
 157         state changes when inside those strings. Returns True if we're still
 158         inside a multi-line string when this function is finished.
 159         """
 160         # If inside triple-single quotes, start at 0
 161         if self.previousBlockState() == in_state:
 162             start = 0
 163             add = 0
 164         # Otherwise, look for the delimiter on this line
 165         else:
 166             start = delimiter.indexIn(text)
 167             # skipping triple quotes within strings
 168             if start in self.tripleQuoutesWithinStrings:
 169                 return False
 170             # Move past this match
 171             add = delimiter.matchedLength()
 172 
 173         # As long as there's a delimiter match on this line...
 174         while start >= 0:
 175             # Look for the ending delimiter
 176             end = delimiter.indexIn(text, start + add)
 177             # Ending delimiter on this line?
 178             if end >= add:
 179                 length = end - start + add + delimiter.matchedLength()
 180                 self.setCurrentBlockState(0)
 181             # No; multi-line string
 182             else:
 183                 self.setCurrentBlockState(in_state)
 184                 length = len(text) - start + add
 185             # Apply formatting
 186             self.setFormat(start, length, style)
 187             # Look for the next match
 188             start = delimiter.indexIn(text, start + length)
 189 
 190         # Return True if still inside a multi-line string, False otherwise
 191         if self.currentBlockState() == in_state:
 192             return True
 193         else:
 194             return False
```
:::
::::

Here\'s a simple editor application that demonstrates it (not including save/load features). Really all you need to do is instantiate the `syntax.PythonHighlighter`{.backtick} class, passing the `QPlainTextEdit`{.backtick} widget\'s document to the constructor:

:::: 
::: 
``` 
   1 # editor.py
   2 
   3 from PyQt4 import QtGui
   4 import syntax
   5 
   6 app = QtGui.QApplication([])
   7 editor = QtGui.QPlainTextEdit()
   8 highlight = syntax.PythonHighlighter(editor.document())
   9 editor.show()
  10 
  11 # Load syntax.py into the editor for demo purposes
  12 infile = open('syntax.py', 'r')
  13 editor.setPlainText(infile.read())
  14 
  15 app.exec_()
```
:::
::::
