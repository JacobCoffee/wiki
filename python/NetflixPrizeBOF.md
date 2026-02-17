# NetflixPrizeBOF

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Discuss approaches to the Netflix prize using Python, getting started with [PyFlix](http://pyflix.python-hosting.com/) for new people, algorithm + code performance, etc

Some Netflix code in Python will be shown/run (KNN, NMF, ARTmap, SVD, etc).

I will be posting the code later this month on my blog: [Data Wrangling](http://www.datawrangling.com)

Some links for those just getting started:

- [Register a Team](http://www.netflixprize.com/teams) in order to [download the Netflix data](http://www.netflixprize.com/download)

- [PyFlix](http://pyflix.python-hosting.com/) library for efficiently handling the dataset.

- [Movielens dataset](http://www.grouplens.org/node/73) - smaller dataset to debug your code with\...

Some approaches:

- [Simon Funk approach](http://sifter.org/~simon/journal/20061211.html)

- [Timely Development code for Simon Funk approach](http://www.timelydevelopment.com/demos/NetflixPrize.aspx)

- [Netflix forum KNN discussion](http://www.netflixprize.com/community/viewtopic.php?pid=4712#p4712) - includes numpy, weave specifics

- [Basic KNN in SQL](http://devlicio.us/blogs/billy_mccafferty/archive/2006/11/07/netflix-memoirs-using-the-pearson-correlation-coefficient.aspx)

- [Tivo KNN paper](http://mainline.brynmawr.edu/Courses/cs380/fall2006/TiVo.pdf)

- [Erik Shelly\'s approach](http://www.erikshelley.com/netflix/)

- [Dan Tillberg\'s page](http://www.tillberg.us/netflixprizejumpstart)

- [Paul Harrison\'s approach](http://www.logarithmic.net/pfh/blog/01176798503) - using numpy and weave

- [Dartmouth paper](http://www.siam.org/meetings/sdm06/proceedings/059zhangs2.pdf) - using EM/NMF approach with Movielens data

- [BellKor paper](http://www.research.att.com/~volinsky/netflix/ProgressPrize2007BellKorSolution.pdf) - Progress prize winner

- [Hadoop MapReduce code](http://code.google.com/p/canopy-clustering/) for working with the Netflix data

More here:

- [http://del.icio.us/pskomoroch/netflixprize](http://del.icio.us/pskomoroch/netflixprize)

- [http://del.icio.us/pskomoroch/collaborative%2Bfiltering](http://del.icio.us/pskomoroch/collaborative%2Bfiltering)

Performance pointers:

- [http://www.scipy.org/PerformancePython](http://www.scipy.org/PerformancePython)

- [http://wiki.python.org/moin/PythonSpeed/PerformanceTips](http://wiki.python.org/moin/PythonSpeed/PerformanceTips)

- [http://www.scipy.org/Weave](http://www.scipy.org/Weave)

- If you need to go parallel for Netlfix, [ElasticWulf](http://www.datawrangling.com/pycon-2008-elasticwulf-slides.html) public Amazon EC2 images come with mpi4py, IPython1, pyflix, numpy, scipy, weave, pyrex, etc. already installed and configured. The [python code](http://code.google.com/p/elasticwulf/) for launching your own beowulf on EC2 using the images is on google code.

Parallel Programming is useful for lots of ML algorithms. [How to Write Parallel Programs](http://www.dehora.net/journal/2005/02/two_classic_hardbacks.html) is a good book. [Amazon](http://www.amazon.com/How-Write-Parallel-Programs-Course/dp/026203171X/) Consider jython, since ML is often CPU-bound, and jython has no GIL.
