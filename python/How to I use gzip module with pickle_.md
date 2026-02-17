# How to I use gzip module with pickle?

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
