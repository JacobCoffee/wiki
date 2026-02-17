# Asking for Help/How do I use gzip module with pickle?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## How to use the gzip module with the pickle module 

I have a python program which creates a list of prime numbers \[2L,3L,5L,7L,13L\]. This program save the list to a file on the hard disk.

### example of my code 

      fp=open('primes.data','r')
      # ListOfPrimes=[2L,3L,5L,7L]
      ListOfPrimes=cPickle.load(fp)
      fp.close()

      generate_more_primes()

      fp=open('primes.data','w')
      cPickle.dump(ListOfPrimes,fp)
      fp.close()

### What I want 

My problem is that the primes.data file is now 9 megabytes in size and I wanted to reduce the size taken by the file by first compressing the data with the gzip module before saving it. Hence I would also need to decompress the data after I read it from the file.

Any idea how I can do this?

### Solutions 

[lwickjr](lwickjr): I\'d have to research for details, but you\`d have to pickle the data to a string, then save the string to a file through gzip, and read the file from gzip into a string which is then unpickled.

[MarcChr](MarcChr): There is no need for an temporary string. Just `import gzip`{.backtick} and use `gzip.open`{.backtick} instead of `open`{.backtick}:

    import gzip, cPickle

    fp=gzip.open('primes.data','rb') # This assumes that primes.data is already packed with gzip
    ListOfPrimes=cPickle.load(fp)
    fp.close()

    generate_more_primes()

    fp=gzip.open('primes.data','wb')
    cPickle.dump(ListOfPrimes,fp)
    fp.close()

You could also use the binary pickle format which is more compact: `cPickle.dump(ListOfPrimes,fp,1)`{.backtick}.

#### use this module gzippickle.py 

    """Generic object pickler and compressor

    This module saves and reloads compressed representations of generic Python
    objects to and from the disk. Added Protocol field.
    """

    __author__ = "Bill McNeill <billmcn@speakeasy.net>"
    __version__ = "1.1"

    import pickle
    import gzip


    def save(object, filename, protocol = 0):
            """Saves a compressed object to disk
            """
            file = gzip.GzipFile(filename, 'wb')
            file.write(pickle.dumps(object, protocol))
            file.close()

    def load(filename):
            """Loads a compressed object from disk
            """
            file = gzip.GzipFile(filename, 'rb')
            buffer = ""
            while True:
                    data = file.read()
                    if data == "":
                            break
                    buffer += data
            object = pickle.loads(buffer)
            file.close()
            return object

    if __name__ == "__main__":
            import sys
            import os.path
            
            class Object:
                    x = 7
                    y = "This is an object."
            
            filename = sys.argv[1]
            if os.path.isfile(filename):
                    data = load(filename)
                    z,l = data[0],data[1]
                    print "Loaded %s" % data
                    print "z.x = %d z.y = %s" % (z.x,z.y)
                    print "list = %s" % l
            else:
                    z = Object()
                    z.x = 666
                    l = [2,4,9]
                    data = (z,l)
                    save(data, filename)
                    print "Saved %s" % data

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
