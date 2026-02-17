# Distutils/VersionComparison

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distutils Version comparison 

## Draft final proposal 

From Trent Mick,

At the second distutils open space we agreed on the following format for a \"rational version\":

     N.N[.N]+[abc]N[.N]+[.(dev|post)N+]

Some examples probably make it clearer:

    >>> from verlib import RationalVersion as V
    >>> (V('1.0a1')
    ...  < V('1.0a2.dev456')
    ...  < V('1.0a2')
    ...  < V('1.0a2.1.dev456')  # e.g. need to do a quick post release on 1.0a2
    ...  < V('1.0a2.1')
    ...  < V('1.0b1.dev456')
    ...  < V('1.0b2')
    ...  < V('1.0c1.dev456')
    ...  < V('1.0c1')
    ...  < V('1.0.dev456')
    ...  < V('1.0')
    ...  < V('1.0.post456'))
    True

The trailing \".dev123\" is for pre-releases. The \".post123\" is for post-releases \-- which apparently is used by a number of projects out there (e.g. twisted). For example \*after\* a \"1.2.0\" release there might be a \"1.2.0-r678\" release. We used \"post\" instead of \"r\" because the \"r\" is ambiguous as to whether it indicates a pre- or post-release.

The attached verlib.py has the parsing and comparison (using [lt], [eq], et al on the RationalVersion class). There are a lot of doctests in the main docstring with examples.

There is also a `suggest_rational_version(s)`{.backtick} method that can be used to suggest a rational version string for a lot of version strings that are close. Using this suggest method I managed to get 81% of the versions currently on PyPI (from Martin\'s list) to match the RationalVersion scheme \-- which I think is pretty good.

Implementation : [verlib.py](attachments/Distutils(2f)VersionComparison/verlib.py)

## Proposals 

### Larry Hastings 

Sorry for the crazy moon proposal here, but I have example code that I think even works. (Though I\'m not operating on enough sleep, so sorry \'cause I already know the code is crappy.) [lch.version.py](attachments/Distutils(2f)VersionComparison/lch.version.py)

The basic idea:

- A version string should be transformable into a version tuple.
- Version tuples are tuples of arbitrary length containing only integers.
- A version tuple conceptually ends with an infinite number of 0 fields; (1,3) == (1, 3, 0, 0, 0)
- While you see integers, accumulate them, and when it\'s done int().
- While you see alphanumerics, accumulate them, and when it\'s done map it if it\'s a known string (\"alpha\", \"beta\") otherwise break up the characters into individual numbers.
- Pre-releases (alpha, beta) are represented by having a negative number in the version tuple.
- When you compare version tuples, if there are any negative fields, split there and compare the non-negative parts first.

I doubt y\'all will go for this. But I thought you should at least consider supporting a more flexible format. People like to express their version numbers a wide variety of ways, and most folks could find a way to map their personal weird approach to something this approach would make consistent.

(Setuptools implements almost exactly what you\'ve described, except that it produces tuples that can be compared by the standard comparison operators; see pkg_resources.parse_version() \--PJE)

#### Larry Hastings: Round 2\--Fight! 

You want strict? I can do *strict*. Peep dis, my homies. First we define a \"version number\".

- A \"version number\" is a sequence of numbers punctuated by periods.
  - You may have an arbitrary number of fields in a version number.
  - You may not use negative numbers.
  - You may not use a leading zero unless the number is 0.
  - You may not use two (or more) periods in a row.
  - You may not end with a period.

Now we can define a \"version string\":

- A \"version string\" must begin with a \"version number\". This identifies the \"release version\".
- If you follow the \"release version number\" with one of the letters \"a\", b\", or \"c\", this \"version string\" represents a \"pre-release\".
  - The characters \"a\", \"b\", and \"c\" are called \"pre-release markers\".

  - A \"pre-release marker\" must be followed by another \"version number\". \"1.0c\" is not a legal version.

  - Collectively the \"pre-release marker\" followed by a \"version number\" identifies the \"pre-release version\".

  - You may only use at most one \"pre-release\" marker.

  - \"a\" maps to Alpha, \"b\" to Beta, and \"c\" to Release Candidate.

  - Any version with a \"pre-release marker\" is older than one without; lower-ord() letters represent \"older\" releases. \"1.0\" \> \"1.0c1\" \> \"1.0b2\" \> \"1.0b1\" \> \"1.0a1\".
- If you follow a \"pre-release marker\" (and subsequent \"version string\") with \"dev\", \"r\", or \"\~\", this version represents a \"development release\".
  - The strings \"dev\", \"r\", and \"\~\" are called \"development release markers\".

  - You may use at most one \"development release marker\".

  - *You may only use a \"development release marker\"* after *a \"pre-release marker\".* \"1.0dev4095\" is not a valid version.

  - You must follow the \"development release marker\" with another \"version number\". \"1.0c48dev\" is not a valid version.

  - Any version with a \"development release marker\" is older than one without.

  - All the \"development release markers\" are equivalent. \"1.0c1r400\" == \"1.0c1dev400\" == \"1.0c1\~400\".
- Any characters not specifically permitted are hereby illegal. For instance, no whitespace is allowed. Upper-case characters are not allowed.

Though I think we should relent and allow dashes to be *equivalent* to periods. But I\'m not going to fight about it.

For comparison purposes, a version string should be converted to a \"version tuple\". If we have a free hand to specify this, I suggest:

- The version tuple should *always* contain three tuples. Those tuples represent the \"release version\", the \"pre-release version\", and the \"development release version\" respectively.

- The sub-tuples are of arbitrary length.

- If a version string did not specify a particular sub-version (\"1.0\" does not specify a pre-release version), then that tuple is empty.

- All tuples contain only integers, with one exception: the first entry in a non-empty pre-release tuple is the \"pre-release marker\" used.

- Trailing zero fields are removed.

For example:

- \"1.0\" -\> ( (1,), (), () )

  \"1.0.1\" -\> ( 1, 0, 1), (), () )

  \"1.0a3\" -\> ( 1,), (\"a\", 3), () )

  \"1.2b1\~20090401\" -\> \"(1, 2), (\"b\", 1), (20090401) )

When you compare two version tuples, for each sub-tuple:

- If the tuples are equivalent, go to the next field.
- If one tuple is empty, that version is newer.
- Otherwise, the larger of the two tuples indicates the newer version.
- If you run out of tuples, the two versions are equivalent.

\@Larry: See \'Trent Mick\' section below for code that now does this (with the exception of allowing the \'\~\' and \'r\' aliases for \'dev\'). \--[TrentMick](./TrentMick.html)

### Erik LaBianca 

Just throwing this out there since it\'s a little different from what was discussed earlier, but I think has some merit:

\* Versions are a series of integers. Ie 0.0.1, 1.0.0, or 12.5.7.9. Versions define the \"intended API level\" of the software in question.

Pre-release versions are denoted by a version, followed by a string (I suggest \"pre\" but it doesn\'t really matter), followed by a series of integers, seperated by periods if needed. Pre-releases are important because while they may be an implementation of a future API version, they are likely to be buggy or incomplete.

\* For instance 1.0.0pre2.1 \> 1.0.0pre2 \> 1.0.0pre1 \< 1.0.0.

\* Or for the case of daily builds, 1.0.0pre1 \> 1.0.0pre0.20090327 \< 1.0.0

This obviously trades away the flexibility of roll-your-own naming entirely, but makes up for it by defining a standard that leaves enough flexibility to represent most cases easily. It is easy to parse and explain, extensible, and able to cover most use cases aside from that of \"backported bug fixes\". I believe that eliminating words will be a net positive because it eliminates any complaints along the lines of \"you included alpha, beta, and rc but where\'s pre-release or testing?!\".

### Trent Mick 

**Code for the version format discussed at the second distutils open space (Sat evening): [verlib.py](attachments/Distutils(2f)VersionComparison/verlib.py)**

Run the script to run all its doctests.

Some stats against the list of current `PyPI`{.backtick} versions that MvL provided:

    -- matches againsts current PyPI versions
    count: 4975
    RationalVersion1 matches: 1986 (39.92%)
    RationalVersion2 matches: 2386 (47.96%)
    -- with some naive cleaning up of PyPI versions (e.g. '1.0-alpha1' -> '1.0a1')
    cleaned RationalVersion1 matches: 2499 (50.23%)
    cleaned RationalVersion2 matches: 3003 (60.36%)

A link from [RubyGems](./RubyGems.html) that might be interesting:

\* Version Policy: [http://rubygems.org/read/chapter/7](http://rubygems.org/read/chapter/7)

- Because [RubyGems](./RubyGems.html) provides support for version comparisons, we want to pick a policy that works well with the [RubyGems](./RubyGems.html) comparisons and gives the end user what they expect. We call such a policy "rational". Also, if we call non-working policies "irrational", then we apply a little bit of social engineering to gently prod offenders to conform.

### Georg Brandl 

I just spoke with Holger Krekel and we discussed an important point: when we reject a version number on upload, we should provide at least examples for valid version numbers, or even better, if the version can be automatically normalized like 0.5-alpha1 to 0.5a1, suggest that instead. Just saying \"it\'s irrational\" or pointing to the PEP (which will probably contain much more than version numbering specs) is not user-friendly.

Just nothing this here so that it doesn\'t get lost.

\[I\'ve added that to my list. I already have some code for this when I was calculating some stats on the current pypi versions list. \--[TrentMick](./TrentMick.html)\]

### Tom Crawley 

The setuptools versioning scheme is described [here](http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version). It is pretty similiar to the schemes which have been proposed so far. The setuptools versioning scheme should meet most of our needs and has found wide acceptance in the community. Neither of the two current distuils versioning schemes are widely used. The setuptools versioning scheme is geared to the needs of developers who are the primary audience of distuils and provides a useful scheme for controlling software releases.

Third party packagers each have their own version schemes with their own features and idiosyncracies . We cannot accomodate every third party packager within the Python versioning scheme. We should focus primarily on the needs of developers as without developer buyin the scheme will not be adopted. We can accomodate third parties by allowing inclusion of packager specific version numbers with the metadata that is distributed with the Python application distribution. This would look something like:

    version = 1.0.pre1

    [rpm]
    version = 1.0

This would enable a version numbering scheme per packaging scheme and would also allow for extensibility as new packaging schemes are developed. The information in the tags can be processed downstream by packaging organisations.

The idea put forward by Larry Hastings is an excellent method for converting pre-release and post release tags to a numeric based schema. It could be included as an example of tag scheme conversion from the setuptools versioning scheme to a completely numeric packaging scheme.

### Dan Callahan 

Rough sketch of an idea:

A version is a series of \".\"-separated numeric fields. The introduction of a non-numeric character anywhere in the version string marks the version as a pre-release.

For sorting: Compare numeric fields as tuples of integers. For equivalent numeric versions, prefer ones that do not have any trailing non-numeric fields.

In essence: \'3.1\' == \'3.1.0\' \> \'3.1.rc\' \> \'3.1.0.funtime32\'

This simply and flexibly handles pre-release versioning. Post-releases are handled by incrementing the least significant numeric field.

This is, in essence, the inverse of Loose Version in distutils \-- it handles pre-releases instead of post-releases, but still has room for \"non-standard\" annotations.

### Matthias Klose 

Pointing to the [version numbering scheme used by Debian](http://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version), which is in production use for many years. Pointing out some points:

- It is a strict system, not relying on heuristics and any special meanings of strings like alpha, beta, rc, pre.

- It allows correction of a bad version number by allowing prefixing the version by an epoch (: character).

- It allows to write a version number very close to the upstream version, handling parts of the version number which should be considered less than another version (using the tilde character), e.g. 1.0\~alpha1 \< 1.0.

- The paragraph about the \"debian_revision\" mentioned in the referenced URL is not appropriate for a python version. It would be nice if the version system could handle this revisions usually by packages for distributions of operating systems.

- Characters which cannot directly be encoded on the filesystem can be encoded using %\<hexvalue\> and be used when the version number needs to be encoded in a file name.

Examples:

      1.0 < 1.0.0 < 1.0.1 < 1.1 < 1.10

      2.1 < 1:1.0

      3.1~~svn20090328 < 3.1~alpha1 < 3.1

### Marc-Andre Lemburg 

The approach I\'d like to see is simple and avoids all complicated and error prone parsing of string versions:

- The package *must* provide a string version of the package version in any format the author likes to use This is for humans to read and should provide enough information for a potential user to identify the version as right for his or her use.

- The package *must* provide a tuple version which follows a strict ordering The tuple may contain integers and/or ASCII strings and can (theoretically) have arbitrary length. It is meant for computers to read and must therefore provide the version information in a lexically correct order. The Python sys.version_info and its approach to providing the version information in lexically correct order is a good example of such a version tuple: (major, minor, patch_level, status, status_version). Some authors may also want to include the release date/time and/or the repository revision used to cut the release as extra tuple entries.

Package management software should always use the tuple version for version comparison and display the string version to the user.

Package repositories must provide a way to:

- get a list of available versions (in tuple form)
- convert a version tuple for a package to a download URL

Ideally, they should display the version string to the user and allow searches based on these as well.

\@MAL: One of the issues is being able to specify dependencies (e.g. in the current \"setup_requires\" or whatever). For example: \"simplejson \> 3.0.1\". That means either a deterministic translation btwn version tuple and version string is necessary OR dependencies need to specify version \*tuples\*. The latter might be painful. \--[TrentMick](./TrentMick.html)

\@Trent: Right, dependency definitions will need to use the tuple version, probably using a version matching function or instance, e.g. requires=[PythonPackage](./PythonPackage.html)(\'simplejson\', supported_versions=((3,0), (3,1))). Note that just specifying a minimum version is likely not going to provide a robust setup, e.g. \"simplejson \> 3.0.1\" would also match simplejson 4.0, but that may have a completely incompatible interface. \-- [MarcAndreLemburg](MarcAndreLemburg)

### Brian Sutherland 

This is more a statement of what we want/don\'t want than a specific implementation:

- A method of expressing \"alpha\", \"beta\"\... releases in ways that sort lower than the final release
- Would be nice if python version numbers were directly usable by system packagers, or, in the worst case, reliably transformed
- No special casing of certain words, i.e. \"pre\" or \"alpha\". i.e. A simple/reliable sorting that you can explain to people
- A standard way to format the version number to fit on the filesystem

### Toshio Kuratomi 

Something that could be important is specifying a meaning for the version numbers (especially the first three version numbers). Blessing something like Enthought\'s Versioning would have several advantages.

- [https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers](https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers)

<!-- -->

- Version numbers then provide a clue to consumers (users, app developers, packagers) whether the new version is compatible with the former version. \[Could easily add `major`{.backtick}, `minor`{.backtick}, `patch`{.backtick} attributes to the `RationalVersion`{.backtick} class in my `verlib.py`{.backtick} above. \--[TrentMick](./TrentMick.html)\]

- Using this scheme will let people specify version dependencies in the metadata better by reliably being able to say you\'re dependent on `foo >= X.Y foor < (X+1).0`{.backtick}.

- If we ever get to the point where we use this consistently, we can write more intelligent import loaders that can use the MAJOR/MINOR version to load different versions automatically.

### Kay Schluehr 

I basically like the initial versioning scheme proposed by Trent Mick and would just stick to it. However I wouldn\'t interpret too much into it. Version numbers are an incredibly poor way to express compatibility issues and they serve as a simplistic heuristics at best that is open to interpretation.

The WP article about [versioning](http://en.wikipedia.org/wiki/Software_versioning) also mentions political and psychological implications of using version numbers. Remember that Django was long considered unstable due to not having reached v1.0. Better stick to static metadata for more reliable information and to [DAGs](http://en.wikipedia.org/wiki/Directed_acyclic_graph) for modeling dependencies. OO did the latter about 30 years ago. It\'s time to grow up.
