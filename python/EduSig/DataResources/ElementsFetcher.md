# EduSig/DataResources/ElementsFetcher

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 import urllib2
   2 from BeautifulSoup import BeautifulSoup
   3 
   4 class Element:
   5     "A simple container of arbitrary named attributes."
   6     def __init__(self, **kw):
   7         self.__dict__.update(kw)
   8     def __repr__(self):
   9         return str(self.__dict__)
  10 
  11 def FetchElements():
  12     """Chemical Elements
  13 
  14       Retrieves a list of the basic chemical elements, along with a few of
  15       their associated properties.
  16     """
  17 
  18     opener = urllib2.build_opener()
  19     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  20 
  21     page = opener.open("http://en.wikipedia.org/wiki/List_of_elements_by_atomic_number")
  22     soup = BeautifulSoup(page)
  23     page.close()
  24 
  25     elements = {}
  26     for element in soup.html.body.table.findAll('tr')[1:]:
  27         fields = element.findAll('td')
  28 
  29         number = int(fields[0].renderContents())
  30         name = fields[1].a.renderContents()
  31         symbol = fields[2].renderContents()
  32         series = fields[4].a.renderContents()
  33 
  34         elements[number] = Element(
  35             number=number,
  36             name=name,
  37             symbol=symbol,
  38             series=series)
  39 
  40     return elements
  41 
  42 elements = FetchElements()
  43 print elements
```
:::
::::

**Note(s):**

- This example uses standard Python except for

  [the BeautifulSoup package](http://www.crummy.com/software/BeautifulSoup/) which must be installed separately.

------------------------------------------------------------------------

[CategoryPythonInEducation](CategoryPythonInEducation)
