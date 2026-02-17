# reStructuredText

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# reStructuredText (reST) 

reStructuredText is a complete rewrite of [StructuredText](StructuredText) by David Goodger.

It is distributed as part of Docutils.

- Project page: [http://docutils.sourceforge.net/](http://docutils.sourceforge.net/)

- Release download: [http://sourceforge.net/project/showfiles.php?group_id=38414](http://sourceforge.net/project/showfiles.php?group_id=38414)

- Development snapshots: [http://docutils.sourceforge.net/#development-snapshots](http://docutils.sourceforge.net/#development-snapshots)

More information:

- [An Introduction to reStructuredText](http://docutils.sourceforge.net/spec/rst/introduction.html) - goals & history

- [A reStructuredText Primer](http://docutils.sourceforge.net/docs/rst/quickstart.html) - how to write reST text

- [reStructuredText Markup Specification](http://docutils.sourceforge.net/spec/rst/reStructuredText.html) - details on writing reST text

- [Brett Cannon\'s PyCon Tutorial](http://www.ocf.berkeley.edu/~bac/rest_tutorial.html)

![{i}](/wiki/europython/img/icon-info.png "{i}") [MoinMoin](MoinMoin) contains an (incomplete) bridge to the docutils\'s parser, you can try this by using \"#format rst\" as the first line of a wiki page. See [RestSample](http://moinmo.in/RestSample "MoinMoin") for an example. This of course only works when you use the current CVS version, and when docutils is installed.

## Reading reST, Writing HTML 

There\'s surprisingly little on the web and in the documentation about reading reST, and writing HTML.

There\'s documentation on how to read reST, and output an entire HTML document. But if you want just a fragment of HTML, there\'s almost nothing.

Here are two approaches that have been found.

### The \"Official\" Way 

There is no \"official\" way, but here\'s a method that works with the reST system.

:::: 
::: 
``` 
   1 from docutils import core
   2 from docutils.writers.html4css1 import Writer,HTMLTranslator
   3 
   4 class HTMLFragmentTranslator( HTMLTranslator ):
   5     def __init__( self, document ):
   6         HTMLTranslator.__init__( self, document )
   7         self.head_prefix = ['','','','','']
   8         self.body_prefix = []
   9         self.body_suffix = []
  10         self.stylesheet = []
  11     def astext(self):
  12         return ''.join(self.body)
  13 
  14 html_fragment_writer = Writer()
  15 html_fragment_writer.translator_class = HTMLFragmentTranslator
  16 
  17 def reST_to_html( s ):
  18     return core.publish_string( s, writer = html_fragment_writer )
  19 
  20 if __name__ == '__main__':
  21     test = """
  22 H1 text
  23 =======
  24 
  25 *Italic* and **Bold.**
  26 
  27 ::
  28 
  29   # Preformatted,
  30   # For communicating code.
  31 
  32   # Yes, it can have spaces.
  33 
  34 Here's a `link to Python.org.`
  35 
  36 _ http://www.python.org/
  37 
  38 List items:
  39 
  40 - item 1
  41 - item 2
  42 - item 3
  43 """
  44     print reST_to_html(test)
```
:::
::::

If you want everything wrapped in a div tag, (perhaps to, say, delineate a \"comment\" tag,) you can add the following to the `HTMLFragmentTranslator` class:

:::: 
::: 
``` 
   1     def visit_document(self,node):
   2         self.body.append(self.starttag(node,"div",CLASS="comment"))
```
:::
::::

These techniques were culled from [an ASPN article,](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/193890) and connected comments.

### The \"Easy\" Way 

[IanBicking](IanBicking) has contributed this code, which reads a source text (in reST), and writes HTML:

:::: 
::: 
``` 
   1 html = docutils.core.publish_string(
   2            source=text,
   3            writer_name='html')
   4 html = html[html.find('<body>')+6:html.find('</body>')].strip()
```
:::
::::

\"It may feel wrong, but it works, and works reliably.\"

### The \"Cool\" Way 

\"This sure is a lot cooler and generates a nice and more kosher html fragment from the \'official\' reST-to-html fragment example above.\"-[MaxPa](MaxPa)

:::: 
::: 
``` 
   1 from docutils import core
   2 
   3 def reST_to_html_fragment(a_str):
   4     parts = core.publish_parts(
   5                           source=a_str,
   6                           writer_name='html')
   7     return parts['body_pre_docinfo']+parts['fragment']
```
:::
::::

### See Also: 

[PyTextile](PyTextile) is a similar, but different, text-to-html converter. It was originally intended for HTML fragments, unlike reStructuredText.

## Discussion 

I\'ve been having problems getting reST to work from a blog script I\'ve written. It seems that there\'s a part in Publisher where I\'m triggering an exception, and then Publisher calls *exit,* so I can\'t see what\'s wrong.

I\'ll leave notes here if I figure out how to get around this problem. \-- [LionKimbro](LionKimbro)

No luck finding a way to get around the publisher\'s exit, but I did find something interesting: [http://sourceforge.net/mailarchive/forum.php?thread_id=3740457&forum_id=8812](http://sourceforge.net/mailarchive/forum.php?thread_id=3740457&forum_id=8812) \-- [LionKimbro](LionKimbro)
