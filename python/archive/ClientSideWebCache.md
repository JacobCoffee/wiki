# ClientSideWebCache

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Is there an existing Python module that takes care of retrieving and caching web page contents?

Something like:

:::: 
::: 
``` 
   1 import cachedweb
   2 
   3 cache = cachedweb("/home/user/.web_cache")  # Maintain cache data in .web_cache
   4 print cache.get("http://example.net")
```
:::
::::

Perhaps there are different options for where and how to store cache data.

I have written at least three programs that do this, ([nLSD interpreter,](http://onebigsoup.wiki.taoriver.net/moin.cgi/nLSDgraphs) and two [Local Names servers,](http://ln.taoriver.net/)) and am about to embark on a fourth program.

Has anyone created a standard module or interface for this sort of thing?

Some things that would be nice:

- Optional attention to HTTP cache directives.
- Specify directory to store cache entries in.
- Optional compression, decompression, of cached data.
- Optional connection with a client-side Squid cache. (Pooling a web cache with other programs.)
- Conceivably, a caching module could be a drop-in replacement for urllib.

Some info for would-be cachers:

- [Caching Tutorial for Web Authors and Webmasters](http://www.mnot.net/cache_docs/) - talks about HTTP headers having to do with caching

- [urllib.urlretrieve](http://www.python.org/doc/current/lib/module-urllib.html) - performs some of what we want, though you have to do a lot of maintenance yourself

\-- [LionKimbro](LionKimbro) 2005-03-29 06:45:28

## Primitive Example 

Here\'s a very simple example:

:::: 
::: 
``` 
   1 #!/usr/bin/python
   2 """Retrieve and cache web pages.
   3 
   4 webcache retrieves and caches web pages. If the webpage has been
   5 retrieved before, the cached version is used.
   6 
   7 The module is primitive; it DOES NOT respect HTTP cache headers. Cached
   8 pages are stored in a BSD database.
   9 
  10 WebCache --  cache for web pages
  11 """
  12 
  13 import time
  14 import urllib
  15 import optparse
  16 import bsddb
  17 
  18 
  19 class WebCache:
  20 
  21     """BSD DB cache for web pages.
  22 
  23     get_page --  retrieve a page from cache or web
  24     dump_page --  dump a cache entry
  25     clean --  vet expired cache entries
  26     """
  27 
  28     def __init__(self, page_db_filename, time_db_filename, cache_ttl):
  29         """Initialize web cache.
  30 
  31         Berkeley databases are created if they don't already exist. The
  32         page database stores the contents of web pages. The time
  33         database stores the times that the pages were loaded.
  34 
  35         Times are stored in seconds since the epoch.
  36 
  37         page_db_filename --  filename of page database
  38         time_db_filename --  filename of load timestamp database
  39         cache_ttl --  cache time to live in seconds
  40         """
  41         self._page_db = bsddb.hashopen(page_db_filename)
  42         self._time_db = bsddb.hashopen(time_db_filename)
  43         self.cache_ttl = cache_ttl
  44 
  45     def get_page(self, url):
  46         """Retrieve a page from the web or the cache.
  47 
  48         get_page returns the page contents retrieved by urllib.urlopen.
  49 
  50         url --  URL of web page to retrieve
  51         """
  52 
  53         now = time.time()
  54         if url in self._time_db:
  55             last_read = float(self._time_db[url])
  56             if now < last_read + self.cache_ttl:
  57                 return self._page_db[url]
  58 
  59         contents = urllib.urlopen(url).read()
  60 
  61         self._page_db[url] = contents
  62         self._time_db[url] = str(now)
  63         self._page_db.sync()
  64         self._time_db.sync()
  65 
  66         return contents
  67 
  68     def dump_page(self, url):
  69         """Force a cache entry to expire."""
  70 
  71         del self._time_db[url]
  72         del self._page_db[url]
  73         self._time_db.sync()
  74         self._page_db.sync()
  75 
  76     def clean(self):
  77         """Vet cache of expired entries.
  78 
  79         Note that the BSD database file may not actually get smaller.
  80         (Rather, older data will be overwritten by new data.)
  81         """
  82 
  83         now = time.time()
  84         for (url, last_read) in self._time_db.items():
  85             last_read = float(last_read)
  86             if now >= last_read + self.cache_ttl:
  87                 del self._time_db[url]
  88                 del self._page_db[url]
  89         self._time_db.sync()
  90         self._page_db.sync()
  91 
  92 
  93 if __name__ == "__main__":
  94     parser = optparse.OptionParser("usage: %prog [options]\n"
  95                                    "cleans the cache if no URL is"
  96                                    " supplied")
  97     parser.add_option("-p", "--pages", dest="page_db_filename",
  98                       default="pages.db", type="string",
  99                       help="pages BSD database filename")
 100     parser.add_option("-t", "--times", dest="time_db_filename",
 101                       default="times.db", type="string",
 102                       help="timestamps BSD database filename")
 103     parser.add_option("-T", "--ttl", dest="ttl", default=60*60,
 104                       type="int", help="time to live (in seconds)")
 105     parser.add_option("-u", "--url", dest="url", type="string",
 106                       help="url of page to retrieve and display")
 107 
 108     (options, args) = parser.parse_args()
 109     if len(args) > 0:
 110         parser.error("incorrect number of arguments")
 111 
 112     cache = WebCache(options.page_db_filename, options.time_db_filename,
 113                      options.ttl)
 114     if options.url is None:
 115         cache.clean()
 116     else:
 117         print cache.get_page(args[0])
```
:::
::::
