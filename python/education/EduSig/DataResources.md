# EduSig/DataResources

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Relevant, Reusable Data for Education Exercises 

On this page is cataloged common data that may be useful to educators in constructing meaningful exercises. Often educators short on time use abstract data that lacks meaning to the student, or that requires the student to track down and extract his own data.

Fetch scripts are provided in some cases where the data is too large, changes periodically, or it wouldn\'t make sense to host it on python.org. The scripts are kept simple, so that students may benefit from reading them as well as the instructor, although it is expected that usually the instructor will extract the data once, perhaps repackage it and make it available in the classroom.

Contributions are welcome but content listed here must be distributable under an open license.

------------------------------------------------------------------------

**Content**

- A list of two-letter country codes and their descriptive name.

**Origin**

- [http://xml.coverpages.org/country3166.html](http://xml.coverpages.org/country3166.html)

**Fetch Script**

- [CountryCodeFetcher.py](DataResources/CountryCodeFetcher)

------------------------------------------------------------------------

**Content**

- A small set of cities tagged with the state within which they reside and their latitude/longitude.

**Origin**

- [http://www.4dsolutions.net/ocn/python/cities.xml](http://www.4dsolutions.net/ocn/python/cities.xml)

**Fetch Script**

- [CityLocationFetcher.py](DataResources/CityLocationFetcher)

------------------------------------------------------------------------

**Content**

- Dictionary of chemical elements from the Periodic Chart.

**Origin**

- [http://en.wikipedia.org/wiki/List_of_elements_by_atomic_number](http://en.wikipedia.org/wiki/List_of_elements_by_atomic_number)

**Fetch Script**

- [ElementsFetcher.py](DataResources/ElementsFetcher)

------------------------------------------------------------------------

**Content**

- Dictionary of of about 180.000 english words with hyphenations

**Origin**

- [http://www.gtoal.com/wordgames/oxford_wordlists/Moby/mhyph/mhyph.txt](http://www.gtoal.com/wordgames/oxford_wordlists/Moby/mhyph/mhyph.txt)

**Fetch Script**

- [http://bazaar.launchpad.net/\~martin.marcher/+junk/py-rds](http://bazaar.launchpad.net/~martin.marcher/+junk/py-rds) (bzr enabled)

- [http://code.launchpad.net/\~martin.marcher/+junk/py-rds](http://code.launchpad.net/~martin.marcher/+junk/py-rds)

------------------------------------------------------------------------

::: {}
  ----------------
  Suggestion Box
  ----------------
:::

- world temperature measurements
- distances between cities
- how to say \"I love you\" in different languages
- list of people names
- list of species
- geological epochs
- Python dictionary of planetary properties
- bones of the body as a tree structure

**Note**

- If you know *where* to obtain the information, in a freely reusable form, please provide a link. Often finding it is harder than processing it.

**Question**

## SQLite3 Data 

Would it be OK to provide sqlite3 Databases?

I do have a source of hyphenations under public domain (about 180.000 entries), and I think that sqlite3 (which is in 2.5) would also be nice to use as a data source.

------------------------------------------------------------------------

[CategoryPythonInEducation](CategoryPythonInEducation)
