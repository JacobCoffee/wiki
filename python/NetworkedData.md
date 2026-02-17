# NetworkedData

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Networked Data 

I\'ve created something that fits the pattern of \"Networked Data\" which seems to be *the way* right now.

You can do things like this:

:::: 
::: 
``` 
   1 >>> import graph
   2 >>> store = graph.GraphStore()
   3 >>> some_data = { "a": 4547,
   4 ...               "b": 34,
   5 ...               "c": 976,
   6 ...               "other": store.new_ref( "http://taoriver.net/tmp/foo.txt" ) }
   7 >>> g = store.new_graph( "foo" )
   8 >>> g.accept( some_data )
   9 0
  10 >>> print g.serialize()
  11 0:DICT:1,2,3,4,5,6,7,8
  12 1:STR:a
  13 2:INT:4547
  14 3:STR:c
  15 4:INT:976
  16 5:STR:b
  17 6:INT:34
  18 7:STR:other
  19 8:REF:http://taoriver.net/tmp/foo.txt
  20 -1:FLAG:START 0
  21 
  22 >>> some_data["other"].resolve()
  23 >>> some_data["other"]
  24 [<reference into http://www.speakeasy.org/~lion/data/bar.txt>, 'hello', 'world!']
  25 >>> some_data["other"][0].resolve()
  26 >>> some_data
  27 {'a': 4547, 'c': 976, 'b': 34, 'other': [['the', 'river', 'of', 'hope', [...]], 'hello', 'world!']}
  28 >>> 
```
:::
::::

It\'s still messy, and it requires a little more work than it needs to, but it\'s really cool!

What this means is that you can use *native python data,* which includes \"Ref\" objects, and then resolve it or publish it over the Internet. It resolves *transparently!*

There are some limitations in the present code that I want to get rid of:

- You have to register the containers of References with the Graph store. I\'d like to find a way to use Python\'s internal object database, to get relatively quick access to objects that include references, to get around the registration requirement.
- The code sucks, and I\'m working to clean it up.

But it\'s really fun to think of things that you can do with this, or just- *this type of thing.*

For more on this particular work, see:

- [OneBigSoup:nLSDgraphs](http://onebigsoup.wiki.taoriver.net/moin.cgi/nLSDgraphs)

- [CommunityWiki:nLSD](http://communitywiki.org/nLSD)

# Discussion 

- (none yet!)
