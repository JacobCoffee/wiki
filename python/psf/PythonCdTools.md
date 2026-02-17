# PythonCdTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Wiki 

You said you wanted to mirror the Python wiki on the CD, here is a little script to suck the pages from the wiki to a folder:

:::: 
::: 
``` 
   1 import socket, os, sys, urllib2
   2 socket.setdefaulttimeout(15)
   3 from time import sleep
   4 
   5 def suckwiki(pagelist, #url to plain text list of wiki pages
   6              rawpage, #url to raw wiki text of a page
   7              foldername="wikifiles", #name of folder to save files to
   8              sleeptime=1 #seconds to sleep between page accesses
   9              ):
  10     foldername = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), foldername)
  11     if not os.path.exists(foldername): os.mkdir(foldername)
  12     opener = urllib2.build_opener()
  13     listrequest = urllib2.Request(pagelist)
  14     listresponse = opener.open(listrequest)
  15     sleep(sleeptime)
  16     for pagename in listresponse:
  17         pagename = pagename.strip()
  18         pagename = pagename.replace('_','_5f')
  19         pagename = pagename.replace(' ','_20')
  20         print pagename
  21         fullpagename = rawpage % {'pagename':pagename}
  22         pagerequest = urllib2.Request(fullpagename)
  23         page = opener.open(pagerequest)
  24         f = open(os.path.join(foldername,pagename),"wb")
  25         f.write(page.read())
  26         f.close()
  27         page.close()
  28         sleep(sleeptime)
  29 
  30 if __name__ == '__main__':
  31     pagelist = "http://www.python.org/cgi-bin/moinmoin/TitleIndex?action=titleindex"
  32     rawpage = r"http://www.python.org/cgi-bin/moinmoin/%(pagename)s?action=raw"
  33     foldername = "pythonwiki" #name of folder to save pages to
  34     suckwiki(pagelist,rawpage,foldername)
```
:::
::::

Thanks! \-- [ThomasWaldmann](ThomasWaldmann) 2004-06-22 05:23:14
