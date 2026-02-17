# DiacriticalEditor

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is the same as [http://code.activestate.com/recipes/286155/](http://code.activestate.com/recipes/286155/)

For newest version see that page.

------------------------------------------------------------------------

This module provides two standard [TkInter](TkInter) widgets, Entry and [ScrolledText](./ScrolledText.html), modified for text editing with key bindings that allow entering accented letters, umlauts, etc.

Usage: To enter an accented character, press Ctrl-\<accent\>, then press the character key. Example: to enter a with acute, press Ctrl-\', A.

Accent bindings are defined in the Diacritical.accent table. They should be pretty intuitional. Ctrl-= (equals sign) is used for tilde (\~) because the tilde key is somewhat stubborn on Windows keyboards. Not all accents exist on all letters. This is handled by gracefully falling back to the base letter.

No bindings for Icelandic eth & thorn, Swedish a-ring, nor German scharfes-s are available at the moment.

Additionally, some Tk key bindings are corrected on Windows platform to comply with the standard practice: Ctrl-A is now select-all.

:::: 
::: 
``` 
   1 from Tkinter import *
   2 from ScrolledText import ScrolledText
   3 from unicodedata import lookup
   4 import os
   5 
   6 class Diacritical:
   7     """Mix-in class that adds keyboard bindings for accented characters, plus
   8     other common functionality."""
   9 
  10     if os.name == "nt":
  11         stroke = '/'
  12     else:
  13         stroke = 'minus'
  14     accents = (('acute', "'"), ('grave', '`'), ('circumflex', '^'),
  15                ('tilde', '='), ('diaeresis', '"'), ('cedilla', ','),
  16                ('stroke', stroke))
  17 
  18     def __init__(self):
  19         # Fix some non-Windows bindings
  20         if os.name == 'nt':
  21             self.bind("<Control-Key-a>", self.select_all)
  22             self.bind("<Control-Key-/>", lambda event: "break")
  23         # Diacritical bindings
  24         for a, k in self.accents:
  25             self.bind("<Control-Key-%s><Key>" % k,
  26                         lambda event, a=a: self.insert_accented(event.char, a))
  27 
  28     def insert_accented(self, c, accent):
  29         if c.isalpha():
  30             if c.isupper():
  31                 cap = 'capital'
  32             else:
  33                 cap = 'small'
  34             try:
  35                 c = lookup("latin %s letter %c with %s" % (cap, c, accent))
  36                 self.insert(INSERT, c)
  37                 return "break"
  38             except KeyError, e:
  39                 pass
  40 
  41 class DiacriticalEntry(Entry, Diacritical):
  42     """Tkinter Entry widget with some extra key bindings for
  43     entering typical Unicode characters - with umlauts, accents, etc."""
  44 
  45     def __init__(self, master=None, **kwargs):
  46         Entry.__init__(self, master=None, **kwargs)
  47         Diacritical.__init__(self)
  48 
  49     def select_all(self, event=None):
  50         self.selection_range(0, END)
  51         return "break"
  52 
  53 class DiacriticalText(ScrolledText, Diacritical):
  54     """Tkinter ScrolledText widget with some extra key bindings for
  55     entering typical Unicode characters - with umlauts, accents, etc."""
  56 
  57     def __init__(self, master=None, **kwargs):
  58         ScrolledText.__init__(self, master=None, **kwargs)
  59         Diacritical.__init__(self)
  60 
  61     def select_all(self, event=None):
  62         self.tag_add(SEL, "1.0", "end-1c")
  63         self.mark_set(INSERT, "1.0")
  64         self.see(INSERT)
  65         return "break"
  66 
  67 
  68 def test():
  69     frame = Frame()
  70     frame.pack(fill=BOTH, expand=YES)
  71     if os.name == "nt":
  72         frame.option_add("*font", "Tahoma 8") # Win default, Tk uses other
  73     # The editors
  74     entry = DiacriticalEntry(frame)
  75     entry.pack(fill=BOTH, expand=YES)
  76     text = DiacriticalText(frame, width=76, height=25, wrap=WORD)
  77     if os.name == "nt":
  78         text.config(font="Arial 10")
  79     text.pack(fill=BOTH, expand=YES)
  80     text.focus()
  81     frame.master.title("Diacritical Editor")
  82     frame.mainloop()
  83 
  84 if __name__ == "__main__":
  85     test()
```
:::
::::
