# PyTextile

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## PyTextile 

[PyTextile](http://pypi.python.org/pypi/textile) is a *very* easy to use text-to-HTML converter.

You can test the following demonstration of Textile code, which can convert *this:*

    _This_ is a *test.*

    * One
    * Two
    * Three

    Link to "Slashdot":http://slashdot.org/

to *this:*

            <p><em>This</em> is a <strong>test.</strong></p>
     
     
    <ul>
            <li>One</li>
            <li>Two</li>
            <li>Three</li>
    </ul>
     
            <p>Link to <a href="http://slashdot.org/">Slashdot</a></p>

### Using PyTextile 

First, [download the latest PyTextile.](http://pypi.python.org/pypi/textile)

Untar it, and enter the `textile` directory. Start a python interpreter.

Type:

:::: 
::: 
``` 
   1 import textile
   2 
   3 s = """
   4 _This_ is a *test.*
   5 
   6 * One
   7 * Two
   8 * Three
   9 
  10 Link to "Slashdot":http://slashdot.org/
  11 """
  12 
  13 html = textile.textile( s )
  14 
  15 print html
```
:::
::::

You\'ll see beautiful HTML on the other side, ready for inclusion in a web page. ![:)](/wiki/europython/img/smile.png%20":)")

#### Options 

PyTextile takes 3 optional arguments:

    def textile(self, text, rel=None, head_offset=0, html_type='xhtml', sanitize=False):

### See Also: 

[reStructuredText](../archive/reStructuredText) as a markup format to convert text to HTML.

## Discussion 

(none yet!)
