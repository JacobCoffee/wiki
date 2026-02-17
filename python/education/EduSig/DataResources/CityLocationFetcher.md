# EduSig/DataResources/CityLocationFetcher

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 import urllib2                                                                                                            
   2 from BeautifulSoup import BeautifulStoneSoup                                                                              
   3                                                                                                                           
   4 class City:                                                                                                               
   5     "A simple container of arbitrary named attributes."                                                                   
   6     def __init__(self, **kw):                                                                                             
   7         self.__dict__.update(kw)                                                                                          
   8     def __repr__(self):                                                                                                   
   9         return str(self.__dict__)                                                                                         
  10                                                                                                                           
  11 def FetchCityLocations():                                                                                                 
  12     """A Sampling of Location Information about Cities                                                                    
  13                                                                                                                           
  14        An example of fetching XML representing information about a handful                                                
  15        of cities along with the state within which they reside and their                                                  
  16        latitude/longitude.                                                                                                
  17     """                                                                                                                   
  18                                                                                                                           
  19     page = urllib2.urlopen("http://www.4dsolutions.net/ocn/python/cities.xml")                                            
  20     soup = BeautifulStoneSoup(page)                                                                                       
  21     page.close()                                                                                                          
  22                                                                                                                           
  23     cities = []                                                                                                           
  24     for city in soup.cities.findAll('city'):                                                                              
  25         c = City(                                                                                                         
  26                 name=city['name'],                                                                                        
  27                 state=city['state'],                                                                                      
  28                 latitude="%s.%s%s" % (                                                                                    
  29                     city.lat['deg'], city.lat['min'], city.lat['dir']),                                                   
  30                 longitude="%s.%s%s" % (                                                                                   
  31                     city.long['deg'], city.long['min'], city.long['dir']),                                                
  32                 )                                                                                                         
  33         cities.append(c)                                                                                                  
  34     return cities                                                                                                         
  35                                                                                                                           
  36 cities = FetchCityLocations()                                                                                             
  37 print cities                                                                                                              
```
:::
::::

**Note(s):**

- This example uses standard Python except for

  [the BeautifulSoup package](http://www.crummy.com/software/BeautifulSoup/) which must be installed separately.

------------------------------------------------------------------------

Here\'s a version which uses the built-in XML processing capabilities of Python:

:::: 
::: 
``` 
   1 import urllib, xml.dom.minidom
   2 
   3 class City:
   4     "A simple container of arbitrary named attributes."
   5     def __init__(self, **kw):
   6         self.__dict__.update(kw)
   7     def __repr__(self):
   8         return str(self.__dict__)
   9 
  10 def FetchCityLocations():                                                                                                 
  11     """A Sampling of Location Information about Cities                                                                    
  12                                                                                                                           
  13        An example of fetching XML representing information about a handful                                                
  14        of cities along with the state within which they reside and their                                                  
  15        latitude/longitude.                                                                                                
  16     """                                                                                                                   
  17 
  18     f = urllib.urlopen("http://www.4dsolutions.net/ocn/python/cities.xml")
  19     d = xml.dom.minidom.parse(f)
  20 
  21     cities = []
  22     for city in d.getElementsByTagName("city"):
  23         attr = city.getAttribute
  24         lat = city.getElementsByTagName("lat")[0]
  25         long = city.getElementsByTagName("long")[0]
  26         latAttr = lat.getAttribute
  27         longAttr = long.getAttribute
  28         cities.append(
  29             City(
  30                 name=attr("name"),
  31                 state=attr("state"),
  32                 latitude="%s.%s%s" % (
  33                     latAttr("deg"), latAttr("min"), latAttr("dir")
  34                     ),
  35                 longitude="%s.%s%s" % (
  36                     longAttr("deg"), longAttr("min"), longAttr("dir")
  37                     )
  38                 )
  39             )
  40 
  41     return cities
  42 
  43 cities = FetchCityLocations()                                                                                            
  44 print cities                                                                                                             
```
:::
::::

------------------------------------------------------------------------

[CategoryPythonInEducation](CategoryPythonInEducation)
