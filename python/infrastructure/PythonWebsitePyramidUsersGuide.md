# PythonWebsitePyramidUsersGuide

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**This page is now largely irrelevant \-- the website no longer uses Pyramid to build.**

:::::::::::::::::::::::::::::::::::::::::::::::::::::: 
### [Pyramid User\'s Guide](#id7)

:::: 
#### [Overview](#id8)

Pyramid deals with fragments (of html) that can contain any number of slots, each identified by a name. Data are mapped into each slot in the fragment through a dictionary-like interface. A fragment is created by combining an html template and a data mapping. Created fragments may also have slots in them, allowing for further substitutions, and so on.

Fragments can map more complex structures than simple names. A slot can be filled by a list (using parameterised template html for each item in the list), for example. Even more flexibly, specific html tags can cause custom renderers (that can transform the html) to be invoked. Typical uses of of pyramid only use simple lists and mappings, but more is there when you need it.

The system\'s power comes from applying the same technique at multiple levels, allowing templating tasks of arbitrary complexity to be implemented without imposing arbitrary restrictions on html structure.

The final aspect of the system, that allows sites to be built around a common templated structure, is the ability for data items and templates to be inherited from parent directories. A single html \'skin\' can be defined at the root of a directory structure. Each child fragment will, if unable to find the specified template in its own directory, search back towards the root directory looking for the required template.

::: 
Table of Contents

- [Pyramid User\'s Guide](#pyramid-user-s-guide)
  - [Overview](#overview)
  - [Introduction](#introduction)
  - [The Templating System](#the-templating-system)
    - [Slots](#slots)
    - [Data Items](#data-items)
    - [Patterns](#patterns)
    - [Renderers](#renderers)
  - [Data Structure](#data-structure)
    - [fragment](#fragment)
    - [rest & restfile](#rest-restfile)
    - [url](#url)
  - [Using Pyramid](#using-pyramid)
  - [Viewing the Generated Pages](#viewing-the-generated-pages)
  - [Adding Pages to the Python Site - Full Description](#adding-pages-to-the-python-site-full-description)
    - [Adding initial files](#adding-initial-files)
      - [index.yml](#index-yml)
      - [content.yml](#content-yml)
      - [content.html](#content-html)
    - [Creating the Restructured Text Content](#creating-the-restructured-text-content)
  - [Alternative Ways to Add Pages](#alternative-ways-to-add-pages)
    - [Using htfiles within pyramid](#using-htfiles-within-pyramid)
      - [index.yml](#id1)
      - [content.yml](#id2)
    - [Using htfiles sourced directly from the pydotorg tree](#using-htfiles-sourced-directly-from-the-pydotorg-tree)
      - [index.yml](#id3)
      - [content.yml](#id4)
    - [Creating htfile pages from the command line](#creating-htfile-pages-from-the-command-line)
    - [Getting content out of wiki pages](#getting-content-out-of-wiki-pages)
  - [How the navigation works](#how-the-navigation-works)
    - [index.yml](#id5)
    - [one/index.yml](#one-index-yml)
  - [Adding Special Features](#adding-special-features)
    - [Sidebars](#sidebars)
      - [construction of typical content page](#construction-of-typical-content-page)
      - [Adding a sidebar to the content.html](#adding-a-sidebar-to-the-content-html)
    - [More complicated structures](#more-complicated-structures)
    - [Continuing navigation as a sidebar](#continuing-navigation-as-a-sidebar)
  - [Pyramid and the Python Site](#pyramid-and-the-python-site)
    - [Don\'t be scared by the homepage setup!!](#don-t-be-scared-by-the-homepage-setup)
    - [FAQ\'s](#faq-s)
      - [How do I include Images and other static assets?](#how-do-i-include-images-and-other-static-assets)
      - [A lot of links seem to be wrong?](#a-lot-of-links-seem-to-be-wrong)
    - [Can you tell me about the Homepage now?](#can-you-tell-me-about-the-homepage-now)
      - [index.yml](#id6)
      - [homepage.yml](#homepage-yml)
      - [sidebar.yml](#sidebar-yml)
      - [success.yml](#success-yml)
      - [quote.yml](#quote-yml)
      - [using-python-for.yml](#using-python-for-yml)
    - [written-in-python.yml](#written-in-python-yml)
:::
::::

::: 
#### [Introduction](#id9)

A simple example template, which perhaps would be used on the news page of a site for a list of news items, should demonstrate the basic concepts. Here is the data structure

    # file = news.yml
    --- !fragment
    template: news.html
    local:
      heading: The News
      welcome-message: Welcome to the news
      news: here is the news

and here is the html template:

    # file = news.html
    <h2><n:slot name="heading" /></h2>
    <n:slot name="welcome-message" />
    <div class="news">
      <n:slot name="news" />
    </div>

The !fragment in the data structure is a type identifier that tells the yaml parser that a data structure is expected. In this case the fragment data structure should have template, local and global keys.

The template key points to a filename for the html template to be used. The local and global keys point to the two data structures to be used.

To work out the data structure to be used to the website, the local data and global data are merged, with local data taking priority. (note for later: if the item is in a sub-directory of a site, the parents global data is also merged, this will be covered in a subsequent section).

The template will look for each fragments slot name in the keys of the merged data item. The heading, welcome message and news will be taken and inserted into the appropriate slots.

The result will be the following html:

    <h2>The News</h2>
    Welcome to the news
    <div class="news">
      here is the news
    </div>

If we wished to use a standalone template for the news item we would repeat the initial html template but change the \'news\' key from a string to a !fragment type:

    # file = news.yml
    --- !fragment
    template: news.html
    local:
      heading: The News
      welcome-message: Welcome to the news
      news: !fragment newsitem.yml

    # file = news.html
    <h2><n:slot name="heading" /></h2>
    <n:slot name="welcome-message" />
    <div class="news">
      <n:slot name="news" />
    </div>

The newsitem.yml fragment would then be used for the \'newsitem\' key:

    # file = newsitem.yml
    --- !fragment
    template: newsitem.html
    local:
      title: First News Title
      teaser: Here is my first item

    # file = newsitem.html
    <h3><n:slot name="title" /></h3>
    <n:slot name="teaser" />

This fragment is a single news item which itself is built in the same way as described for the main template. The results of this are placed into the \'newsitem\' slot on the previous fragment.

Using the above technique we can create html fragments for the \'skin\' of a site and templates for the different types of content page.

In addition to the plain string data type (which does not need a ! prefix) other types of data may be used. One of the more useful types of data for text documents is the !rest and !restfile data types. The !rest data type will parse the data item as [restructured text](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) (see [PEP 287](http://www.python.org/dev/peps/pep-0287/)). The !restfile will do the same but for an external file.
:::

::::::: 
#### [The Templating System](#id10)

The template system used in pyramid is twisted web\'s nevow. The documentation for this is available at [DivmodNevow](http://divmod.org/trac/wiki/DivmodNevow), but will be described in brief here.

Nevow has three primary types of directive. These are as follows

::: 
##### [Slots](#id11)

A marker into which data is extracted using the name of the slot as a key
:::

::: 
##### [Data Items](#id12)

The data directive changes the current \'context\' by drilling into the currently used data. For example, if a dictionary::

    {'a':1.'b':2,'c': {'news':3} }

was supplied to a fragment. a data item with a name of \'c\' would change the current top level data to be a dictionary with just \'news\' as a key. e.g.:

    <p><n:slot name="a" /></p>
    <p><n:slot name="b" /></p>
    <div n:data="c">
      <n:slot name="news" />
    </div>

would result in

    <p>1</p>
    <p>2</p>
    <div>
      3
    </div>

Here is an example with an extra level:

    {'a':1.'b':2,'c': {'news': {'title':4} } }

which with this html:

    <p><n:slot name="a" /></p>
    <p><n:slot name="b" /></p>
    <div n:data="c">
      <h1 n:data="news">
        <n:slot name="title" />
      </h1>
    </div>

would generate:

    <p>1</p>
    <p>2</p>
    <div>
      <h1>
        4
      </h1>
    </div>
:::

::: 
##### [Patterns](#id13)

A piece of html my be marked up as a pattern with an associated name. Renderers can extract patterns for use as fragments of html. The typical usage of the pattern is to mark a fragment of html as an item to be used repeatedly when rendering a list. An example of this is shown below.
:::

::: 
##### [Renderers](#id14)

renderers pass the enclosed data back to a python function for processing. The following example shows the \'sequence\' and \'mapping\' renderers, which are built in to nevow.

e.g. using the data:

    {'a':1.'b':2,'c': [ {'title':11},{'title':12} ] }

which could be represented in yaml as:

    # example.yml
    --- !fragment
    template: example.html
    local:
      a: 1
      b: 2
      c:
        - title: 11
        - title: 12

and the template:

    # file = example.html
    <p><n:slot name="a" /></p>
    <p><n:slot name="b" /></p>
    <ul n:data="c" n:render="sequence">
      <li n:pattern="item" n:render="mapping">
        <n:slot name="title" />
      </li>
    </ul>

This html is generated:

    <p>1</p>
    <p>2</p>
    <ul>
      <li>11</li>
      <li>12</li>
    </ul>
:::
:::::::

:::::: 
#### [Data Structure](#id15)

Although the pyramid idea is data agnostic, the only data reader being used is yaml (converted using the syck parser).

Yaml uses indentation to denote data structure. Two simple yaml documents are shown below:

    ---
    - item one
    - item two

    ---
    a: item one
    b: item two

The first returns a list:

    ['item one', 'item two']

Type guessing is not used and, as such, all values are strings unless explicitly cast.

The second returns a mapping:

    {'a': 'item one', 'b': 'item two'}

All structures in pyramid are mappings. Mappings may contain any other types. Examples of mappings containing lists of mappings is shown below:

    ---
    a: 1
    b:
      i: 10
      ii: 20
      iii: 30
    c:
      - 100
      - 200
      - 300

which would return:

    {'a': '1',
     'b': {'i': '10', 'ii': '20', 'iii':'30'},
     'c': ['100', '200', '300']
    }

In order to add a block of text (rather than inline) the following syntaxes can be used):

    ---
    a: |
      Anything indented by two
      spaces is now considered a block
      the preceding two spaces will
      be removed

      This line is kept


    b: >
      These
      lines
      are
      collapsed

      but a double new line is converted to a single newline

which will be converted to:

    {
     'a': 'Anything indented by two\nspaces is now considered a block\nthe preceding two spaces will\nbe removed\n\nThis line is kept\n',
     'b': 'These lines are collapsed\nbut a double new line is converted to a single newline\n'
    }

This is useful for blocks of text and also restructured text.

Apart from sequences and mappings, the following types are currently used in the python site configuration.

::: 
##### [fragment](#id16)

The fragment is the core type used. It is either a mapping with template, local and global keys (which default to None, {} and {} respectively); or it is a filename for a yml file which is itself a fragment.
:::

::: 
##### [rest & restfile](#id17)

The rest type ([http://docutils.sourceforge.net/docs/user/rst/quickref.html#escaping](http://docutils.sourceforge.net/docs/user/rst/quickref.html#escaping)) allows inline rst to be used. Two examples follow:

    ---
    data: !rest This is **bold**

would produce:

    {'data': 'This is <strong>bold</strong>'}

and this:

    ---
    data: | !rest
      This is *emphasised* and
      this is
      **bold**

would produce:

    {'data':'This is <em>emphasised</em> and\nthis is\n<strong>bold</strong>'}

The restfile type takes a filename for an argument and parses the contents as restructured text.
:::

::: 
##### [url](#id18)

The url type is used as a shortcut for a link and the link text:

    ---
    utility:
      - !url The Help Section /help
      - !url Our Sitemap /sitemap

The algorithm behind !url does split on spaces and uses the last segment as the url href and the remainder as the link text. This would produce:

    {'utility':
     [ '<a href="/help">The Help Section</a>','<a href="/sitemap">Our Sitemap</a>' ]
    }
:::
::::::

::: 
#### [Using Pyramid](#id19)

Pyramid is currently configured to create the whole of a website in one process. This can mean that it is quite processor intensive, taking over a minute to build the hundred or so pages that have already been created.

In the future, the process will be configured such that, when a page is changed, it will only have to rebuild the sub-pages; and then only if global data has changed.

The pyramid, if run without arguments, will show the following:

    -d DATA, --data=DATA  directory in which the fragment data is stored
    -o OUT, --out=OUT     directory in which to save output (will be emptied)
    -r RESOURCES, --resources=RESOURCES
                          comma separated list of resource directories to copy
    -v, --verbose         print status messages to stdout
    -R REBUILDDIRS, --rebuilddirs=REBUILDDIRS
                          only rebuild below these comma separated directories
    -c CONSTANTS, --constants=CONSTANTS
                          pass in the names constants (e.g.
                          PDO=/root/pdo,PSF=/psf

for example, if you were in the test folder, the following would build the simple test:

    pyramid -d simple -o simple-out

You can now check the simple-out directory and can see the results.

It is more informative to run with the verbose flag set (possibly a little too informative).
:::

::: 
#### [Viewing the Generated Pages](#id20)

Because you will have installed twistd as part of the pre-requisites of the software, there are a couple of simple commands that will allow you to create a fully functional web server. Firstly you can use the mktap command to generate a configuration file specifically for your usage:

    mktap web --path=out

This will generate a file called web.tap that can be used with the twistd command to run the server:

    twistd -nof web.tap

The standard mktap command generates a configuration file for a webserver running on port 8080. There is a man page for mktap that will allow you to change the port used and some other variables if necessary.
:::

:::::::: 
#### [Adding Pages to the Python Site - Full Description](#id21)

Adding new pages to the python site is fairly straightforward. For most types of page, a simple rest document is all that is needed. This section will talk through the addition of the \'new style classes\' page (currently in /doc/newstyle.html).

:::::: 
##### [Adding initial files](#id22)

First thing is to add a link to the new page into the navigation. If we open up the /doc/nav.yml file we can see the following:

    --- !fragment
    # Type of template to use
    template: nav.html

    # Contents of the template
    global:
      nav : !sectionnav |
        Current docs folder
        Beginner's Guide http://www.python.org/moin/BeginnersGuide
        FAQs faq
        Introductions intros
        Other doc resources other
        PEP Index http://python.org/peps
        Non-English docs nonenglish
        Book list books
        Topic guides topics
        New-style classes (aka descrintro) newstyle

We can see that the navigation has already been added. \'sectionnav\' is a custom data type that builds urls by adding the current directory to each url. In this case the line \'FAQs faq\' would be split on spaces and all but the last element would be concetenated for the link text. The last element would be appended onto the current directory (e.g. \'/doc/\' + \'faq\') to create the link href\'.

The newstyle section already as a link \'newstyle\' so we don\'t need to add this. You can also see that some links are absolute including the domain name. The sectionnav datatype knows to leave these alone.

Now we have a link pointing to the newstyle section, we need to add a folder to it (remembering that each folder in pyramid builds a single file for the final website.)

Create a folder \'newstyle\' under \'doc\' and add the following files

::: 
###### [index.yml](#id23)

the index.yml is the core filetype and is read first to work out how to build the page. Most content pages will just include a basic index.yml that defines the main template, a page title and where to find the content:

    --- !fragment
    template: index.html
    # The data to pass to the template
    local:
      title: Python Documentation Index
      content: !fragment content.yml

We can either create a new index.yml or typically we can copy one from another content page (typically most of these are very similar). In our case we\'ll copy the index.yml from the /doc folder and change the title attribute.
:::

::: 
###### [content.yml](#id24)

The content.yml file should be similar to the following:

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !restfile content.rst

This tells the system that we\'re using the content.html template and the text content will be read from the content.rst file. Again we can typically copy this file from another similar content page. Sometimes we might want to add a sidebar to a file, if you look at the \'/dev/doc\' you will see a content.yml similar to the following:

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !restfile content.rst
        externallinks: !fragment externallinks.yml

This file includes the \'externallinks.yml\' file which contains a list of external links with an associated externallinks.html template. If you want to create a sidebar of a similar nature, you can copy the same structure to your new page.
:::

::: 
###### [content.html](#id25)

A very simple template:

    <n:invisible n:data="content" n:render="mapping">
    <div id="breadcrumb" n:data="breadcrumb" n:render="breadcrumb" />
    <n:slot name="text" />
    </n:invisible>

If you need a new template, please contact one of the pydotorg webmasters or add a ticket to the trac at [http://psf.pollenation.net](http://psf.pollenation.net).
:::
::::::

::: 
##### [Creating the Restructured Text Content](#id26)

Now we need to create a restructured text file (the ideal format for web content). Our current newstyle.ht file is as follows:

    Title: New-style Classes
    Author: docs@python.org

    <h1>New-style Classes</h1>

    <p>
    Unfortunately, new-style classes have not yet been integrated into
    Python's standard documention.  Fear not, however; many people have
    worked to provide useful information on creating and using new-style
    classes: </p>

    <ul>

    <li><a href="../2.2.3/descrintro.html">Unifying types and classes</a>
    (aka descrintro) is Guido's essay on new-style classes and should be
    your starting point.</li>

    <li>Raymond Hettinger's
    <a href="http://users.rcn.com/python/download/Descriptor.htm">How-To
    Guide for Descriptors</a> focuses on the single most useful aspect of
    new-style classes (which includes properties).</li>

    <li><a href="../2.3/mro.html">Python 2.3 Method Resolution Order</a>
    (MRO) covers multiple inheritance.</li>

    <li>Metaclasses will make your head explode.  Here are several
    approaches to discussing them:

    <ul>
    <li>David Mertz and Michele Simionato's
    <a href="http://www-106.ibm.com/developerworks/linux/library/l-pymeta.html">DeveloperWorks
    article</a></li>
    <li>Alex Martelli's
    <a href="http://www.strakt.com/docs/ep03_meta.pdf">slideshow</a></li>
    <li>Mike Fletcher's
    <a href="http://members.rogers.com/mcfletch/programming/metaclasses.pdf">slideshow</a></li>
    </ul>
    </li>

    <li><a href="http://www.cafepy.com/articles/python_types_and_objects/index.html">Types
    and Objects</a> is the start of a new-style class tutorial with lots
    of figures and examples, but it's rough and not complete.</li>

    </ul>

This is a fairly simple html document in rfc822 format. If we delete the header, we can pass this through html2rst. The output of running this through the modified html2rst parser is:

    New-style Classes
    =================

    Unfortunately, new-style classes have not yet been integrated into Python's
    standard documention. Fear not, however; many people have worked to provide
    useful information on creating and using new-style classes:

    -   `Unifying types and classes`_ (aka descrintro) is Guido's essay on
        new-style classes and should be your starting point.
    -   Raymond Hettinger's `How-To Guide for Descriptors`_ focuses on the
        single most useful aspect of new-style classes (which includes
        properties).
    -   `Python 2.3 Method Resolution Order`_ (MRO) covers multiple
        inheritance.
    -   Metaclasses will make your head explode. Here are several approaches
        to discussing them:

        -   David Mertz and Michele Simionato's `DeveloperWorks article`_
        -   Alex Martelli's `slideshow`_
        -   Mike Fletcher's `slideshow`_

    -   `Types and Objects`_ is the start of a new-style class tutorial with
        lots of figures and examples, but it's rough and not complete.

    .. _Unifying types and classes: ../2.2.3/descrintro.html
    .. _How-To Guide for Descriptors:
        http://users.rcn.com/python/download/Descriptor.htm
    .. _Python 2.3 Method Resolution Order: ../2.3/mro.html
    .. _DeveloperWorks article:
        http://www-106.ibm.com/developerworks/linux/library/l-pymeta.html
    .. _slideshow: http://www.strakt.com/docs/ep03_meta.pdf
    .. _slideshow:
        http://members.rogers.com/mcfletch/programming/metaclasses.pdf
    .. _Types and Objects:
        http://www.cafepy.com/articles/python_types_and_objects/index.html

This can now be saved as content.rst and the website rebuilt.

NB it may be worth mentioning that the previous example will cause duplicate id problems in some builds of docutils. In the actual conversion, the slideshow references have been changed to include the authors name (e.g. Alex Martelli\'s slideshow)
:::
::::::::

::::::::::: 
#### [Alternative Ways to Add Pages](#id27)

Because the process of moving a lot of legacy content can be very protracted and in order to make sure content can be synchronised from the current python site to the beta site. A new directive has been introduced which allows content of the current site to be directly linked into the beta site. This new directive enhances the functionality of the htfile directive already in use. I will first discuss the htfile directive and then discuss how the expanded htfile directive can be used on htfiles that are not in the build tree.

::::: 
##### [Using htfiles within pyramid](#id28)

In order to include content in the htfile format that is used by ht2html, two new directives were added \'htfile\' and \'htfiledata\'.

To show how these work, we will use the example above (new style classes) but use a copy of the htfile instead of converting it to restructured text. So the first thing we will have in our new page directory will be the irc file renamed as \'content.ht\'.

NB In many cases throughout the site we have tried to use the files name \'content.\<suffix\> for the main body of content. This is not essential however and is just a convention to make reading the directory easier.

::: 
###### [index.yml](#id29)

Our new index.yml file will include the title directly from the htfile:

    --- !fragment
    template: index.html
    # The data to pass to the template
    local:
      title: !htfiledata
        file: content.ht
        key: title
      content: !fragment content.yml
:::

::: 
###### [content.yml](#id30)

This will now include the content directly from the htfile using the !htfile directive:

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !htfile content.ht

These are the only changes needed.
:::
:::::

::::: 
##### [Using htfiles sourced directly from the pydotorg tree](#id31)

Because the process of adding content can take such a long time, a new htfile parser has been added that can use the pydotorg tree root to reference files directory from the pydotorg current site. This will ensure that the files remain uptodate until such time as it is decided to move the content administration over to the new site.

NB: This may be useful at some point but only use it on the pydotorg site if specifically arranged.

::: 
###### [index.yml](#id32)

Just use the PDO string substitution and add the remaining path to the ht file:

    --- !fragment
    template: index.html
    # The data to pass to the template
    local:
      title: !htfiledata
        file: %{PDO}s/community/irc.ht
        key: title
      content: !fragment content.yml
:::

::: 
###### [content.yml](#id33)

Adding the PDO variable to the htfile path

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !htfile %{PDO}s/community/irc.ht

The variable expansion needs providing with a location for the pydotorg source tree. This is done using the pyramid argument -c

    pyramid -d data -o out -c PDO=<pathtowwwsvn>/trunk/pydotorg

This variable expansion currently only works for prefixes (i.e. you can\'t use it in the middle of a path) but that is it\'s only intended use case.
:::
:::::

::: 
##### [Creating htfile pages from the command line](#id34)

A command that generates the needed files for a remote htfile page is included in the pyramid distribution. This command is called mkpydir and the help file for it is as follows:

    usage: mkpydir -t <type (wikiurl|htfile|html|restfile)>
       [-d <prefixdirforsourcefile>]
        -p <pathtosourcefile>
        -o <outputdir> [-l]

    examples
    to create a page from a restructured text file assuming $PDO is the root of
    the pydotorg source files directory (without a trailing slash)
      mkpydir -t restfile -d $HOME/pydotorg/trunk -p /psf/weblog/pycon/intro.rst -o $BETAPYTHONDATA/weblog/pycon/intro
    to create a page from a htfile file (copying the contents into the pyramid dir)
       mkpydir -t htfile -d $HOME/pydotorg/trunk -p /Help.ht -o $HOME/beta.python.org/build/data/help
    to link in some content from the pydotorg tree such that it always builds from the original
       mkpydir -t htfile -l -d $PDO -p /Help.ht -o $HOME/beta.python.org/build/data/help
    to include a wiki page
       mkpydir -t wikiurl -d http://wiki.python.org/moin -p /Applications -o $HOME/beta.python.org/build/data/applications
    to perform the above operation and create the page below the current directory
       mkpydir -t wikiurl -d http://wiki.python.org/moin -p /Applications -o .

    options:
      -h, --help            show this help message and exit
      -t TYPE, --type=TYPE  the type of pydir content to be created
      -d DIR, --dir=DIR     the root directory for the an asset (to be used when
                            copying pydotorg or wiki content)
      -p PATH, --path=PATH  the path to the asset
      -o OUTPUTDIR, --outputdir=OUTPUTDIR
                            directory in which to create the pyramid directory
      -T TITLE, --title=TITLE
                            the page title
      -l, --link            use a link to an existing ht file
      -c, --copy            copy the htfile into the directory

For example, if I was in the community directory of my beta.python.org build folder and I wanted to create the a page from the \$PDO/community/irc.ht file I would use:

    mkpydir -t htfile -d $PDO -p /community/irc.ht -o irc

this would create a directory called irc with an index.yml (which would use the htfile for the page title) and a content.yml (which would use the htfile for the contents). It would also include the basic content.html template.

The -l option creates data files that pull in content from an original pydotorg source tree. This should only be used on the python site if specifically arranged.
:::

::: 
##### [Getting content out of wiki pages](#id35)

A lot of content on the site is managed through the python wiki. This makes managing the content a lot easier for the community. Content can be pulled into the site directly over the web using the wikiurl directive. The example below pulls in content from the the wiki Applications page

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
      breadcrumb: !breadcrumb nav.yml nav
      text: !wikiurl http://wiki.python.org/moin/Applications
:::
:::::::::::

::::: 
#### [How the navigation works](#id36)

In order to make the navigation as simple as possible to use and to refactor, a special directive has been added that can look at it\'s parent data file and work accumulate a nested navigation structure.

We\'ll start with a simple example.

::: 
##### [index.yml](#id37)

we\'ll put a basic index.yml data file in the root of a pyramid build:

    --- !fragment
    # Type of template to use
    template: index.html

    # Contents of the template
    global:
      nav : !sectionnav |
        Label One one
        Label Two two
        Label Three three

The main thing to note is the !sectionnav. This is telling the builder to look in parent directories to find work out what section we are in. If we now add a directory called \'one\'.
:::

::: 
##### [one/index.yml](#id38)

The second level file does pretty much the same thing and doesn\'t need to reference the parent (although it needs to be the same data key name, in this case \'nav\':

    --- !fragment
    # Type of template to use
    template: index.html

    # Contents of the template
    global:
      nav : !sectionnav |
        Sub Label Alpha alpha
        Sub Label Beta beta
        Sub Label Gamma gamma

So now when the system is building the page one/index.html, it will know it is in the one directory and so make this list a child of the \'one\' entry in the parent.

The data that is produced at the second level is as follows:

    [{'children': [{'children': [],
                    'data': {'breadcrumb': [{'href': '/one/alpha',
                                             'label': 'Sub Label Alpha'}],
                             'href': '/one/alpha',
                             'label': 'Sub Label Alpha'}},
                   {'children': [],
                    'data': {'breadcrumb': [{'href': '/one/beta',
                                             'label': 'Sub Label Beta'}],
                             'href': '/one/beta',
                             'label': 'Sub Label Beta'}},
                   {'children': [],
                    'data': {'breadcrumb': [{'href': '/one/gamma',
                                             'label': 'Sub Label Gamma'}],
                             'href': '/one/gamma',
                             'label': 'Sub Label Gamma'}}],
      'data': {'href': '/one', 'label': 'Label One'},
      'selected': 'selected'},
     {'data': {'href': '/two', 'label': 'Label Two'}, 'children': []},
     {'data': {'href': '/three', 'label': 'Label Three'}, 'children': []}]

As you can see, the two levels of data have been nested inside one another. A breadrumb value has been added also for use with the \'breadrumb\' renderer

The templates for rendering nested data are complicated and I wouldn\'t touch them with a bargepole unless you know what you\'re doing. If you want to create a nested template for yourself, you are better off copying an existing one and tweaking the html.
:::
:::::

:::::::: 
#### [Adding Special Features](#id39)

::::: 
##### [Sidebars](#id40)

Sidebars are included in the template by adding an extra slot in the content template and filling it with content as follows.

::: 
###### [construction of typical content page](#id41)

The content html for most pages is as follows:

    <n:invisible n:data="content" n:render="mapping">
    <div id="breadcrumb" n:data="breadcrumb" n:render="breadcrumb" />
    <n:slot name="text" />
    </n:invisible>

This moves the content key into the current scope (the data=content and render=mapping) and then uses the slot named text for the contents.

The content key is normally a fragment as per the following index.yml:

    --- !fragment
    template: index.html
    # The data to pass to the template
    local:
      title: Documentation Development
      content: !fragment content.yml

And so the content yaml file is generally as follows:

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !restfile content.rst
:::

::: 
###### [Adding a sidebar to the content.html](#id42)

Our new content.html should look like:

    <n:invisible n:data="content" n:render="mapping">
    <div id="breadcrumb" n:data="breadcrumb" n:render="breadcrumb" />
    <n:slot name="externallinks" />
    <n:slot name="text" />
    </n:invisible>

and so we have to fill the externallinks slot with some data from content.yml:

    --- !fragment
    # Type of template to use
    template: content.html

    # The data to pass to the template
    local:
      content:
        breadcrumb: !breadcrumb nav.yml nav
        text: !restfile content.rst
        externallinks: !fragment externallinks.yml

So the externallinks slot is going to be filled with the results of the externallinks.yml fragment which is as follows:

    --- !fragment
    # Type of template to use
    template: externallinks.html

    # The data to pass to the template
    local:
      title: External Links
      externallinks:
        - !url Sourceforge Project Page http://www.sf.net/projects/python/
        - !url PEP Index http://www.python.org/peps/
        - !url Bug Tracker http://sourceforge.net/tracker/?group_id=5470&amp;atid=105470
        - !url Patch Manager http://sourceforge.net/tracker/?group_id=5470&amp;atid=305470
        - !url Browse CVS http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/python/

Which will need a template that gets floated to the right hand side of the content, in this case the externallinks class applies the appropriate style:

    <div class="externallinks">
      <h4><n:slot name="title" /></h4>
      <ul n:data="externallinks" n:render="sequence">
        <li class="group" n:pattern="item" n:render="mapping"><a href="/web"><n:attr name="href"><n:slot name="href" /></n:attr><n:slot name="label" /></a></li>
      </ul>
    </div>

This is a real example from the python site and exists at /dev/doc.

If you only need a simple sidebar, the following could be used instead of the externallinks yml and html files.

get-sourceforge-item.yml:

    --- !fragment
    # Type of template to use
    template: get-sourceforge-item.html

get-sourceforge-item.html:

    <div id="document-navigation">
    <h4>SourceForge</h4>
    <form action="http://www.python.org/sf" method="post" id="sfidreq" name="sfidreq">
    <label for="id">Get a SourceForge item:</label>
    <input name="id" id="id" type="text" class="formtextinput" />
    <input type="submit" value="Submit" name="sfidbtn" id="sfidbtn" class="formbutton" />
    </form>
    </div>

This allows you to include arbitrary sidebars, in this case a form for the sourceforge item sidebar on the /dev page.
:::
:::::

::: 
##### [More complicated structures](#id43)

The pyramid system allows pretty much arbitray content to be included into sites but still keep the data separate from the presentation. An example of this is the /community/sigs pages where a set of data about the special interest groups is used on multiple pages.

The sigs data is stored in a yml file as follows (number of items reduced to three for brevity):

    --- !fragment
    # Type of template to use
    template: sigindex.html

    # The data to pass to the template
    global:
      sigs:
       -
        dir: c++-sig/
        id: c++-sig
        expires: June 2005
        link: mailto:rwgk@yahoo.com
        name: Ralf W. Grosse-Kunstleve
        description: Development of Python/C++ bindings
        details:
       -
        dir: catalog-sig/
        id: catalog-sig
        expires: June 2005
        link: mailto:catalog-sig@amk.ca
        name: A.M. Kuchling
        description: The Python software catalog
        details: Modules, Packages, other Resources
       -
        dir: db-sig/
        id: db-sig
        expires: June 2005
        link: andy47@halfcooked.com
        name: Andy Todd
        description: Databases
        details: Common tabular database API

This data can now be used to build the table of sigs using the following template (sigindex.html)

    <table cellspacing="0" id="sigindex" n:render="sequence" n:data="sigs">

    <thead n:pattern="header">
    <tr>
        <th>Name</th>
        <th>Coordinator</th>
        <th>Description</th>
        <th>Info</th>
        <th>Expires</th>
    </tr>
    </thead>

    <tr n:pattern="item" n:render="mapping">
        <td class="signame"><a><n:attr name="href">current/<n:slot name="id" />/</n:attr><n:slot name="id" /></a></td>
        <td class="coordinator"><a><n:attr name="href"><n:slot name="link" /></n:attr><n:slot name="name" /></a></td>
        <td class="description"><n:slot name="description" /></td>
        <td class="archivesubscribe">
          <a><n:attr name="href">http://mail.python.org/pipermail/<n:slot name="id" />/</n:attr>archive</a>,
          <a><n:attr name="href">http://mail.python.org/listinfo/<n:slot name="id" />/</n:attr>subscribe</a>
        </td>
        <td class="expires"><n:slot name="expires" /></td>
    </tr>
    </table>
:::

::: 
##### [Continuing navigation as a sidebar](#id44)

As some pages get deeper and deeper, presenting the hiearachical navigation in the left hand side nav becomes unusable. At this point, it makes sense to add a sidebar to continue the representation of the navigation structure on the right hand side of the page. The special interest groups use this to show the navigation around the different groups.

The sidebar (called subnav.yml) needs to use the data from the nav.yml file. It does this by using the !acquire directive as follows:

    --- !fragment
    # Type of template to use
    template: subnav.html

    # The data to pass to the template
    local:
      header: Sub-Navigation
      data: !acquire nav.yml nav

This takes gets the value of the \'nav\' key from the nav.yml data file and assigns it to \'data\'.

The subnav.html template now has access to the whole navigation hierarchy and can selectively show only the 3rd and 4th levels (see source code /community/sigs/current/db-sig/subnav.html for example template).
:::
::::::::

::::::::::::::: 
#### [Pyramid and the Python Site](#id45)

::: 
##### [Don\'t be scared by the homepage setup!!](#id46)

The homepage has a lot of yml data files and templates and some of them look pretty complicated. Don\'t let this worry you as it\'s definitely as complicated as it gets and for all of the other pages we\'ve built so far, nothing has come close.

My advice for now would be to leave the homepage alone unless you want to just edit some content. Instead, start by looking at some nice simple content pages.

However, if you really want to know a little more about the home page, look at the bottom of this document.
:::

::::: 
##### [FAQ\'s](#id47)

::: 
###### [How do I include Images and other static assets?](#id48)

Static directories are pulled into the final site which can be used for non content assets. At the moment there is a /files directory which is being used (this appears in the root of the build directory parralel with the data directory).
:::

::: 
###### [A lot of links seem to be wrong?](#id49)

Once the url rewriting is added, links can be mapped in the same way that the 301 redirects will be mapped. When adding content, if possible try to use absolute urls. These will be easier to parse and rewrite if content is moved around.
:::
:::::

::::::::: 
##### [Can you tell me about the Homepage now?](#id50)

As long as you\'ve read the rest of it.. If you just need to edit something then it should be straightforward. Lets start with the index.yml file.

::: 
###### [index.yml](#id51)

The index data file looks like this:

    --- !fragment
    # Type of template to use
    template: index.html

    # The data to pass to the template
    global:
      title: 'The Official Python Programming Language Website'
      metadata:
        keywords: python programming language object oriented web free source
        description: >
          Home page for Python, an interpreted, interactive, object-oriented, extensible
          programming language. It provides an extraordinary combination of clarity and
          versatility, and is free and comprehensively ported.
        robots: noindex, nofollow

      nav: !fragment nav.yml

    local:
      content: !fragment homepage.yml

This file setups up the main data for the page. The page title and metadata are in the globals sections so that they get inherited by all of the subpages. This means that anything you put in the keywords and description will get used (unless overridden) by the whole site This goes for the navigation too. If a section doesn\'t implement it\'s own navigation it will inherit from the next level up, eventually reaching this one if it can\'t find any other.

The content is in the local section as the homepage.yml file is very specific to this page and shouldn\'t be inherited.
:::

::: 
###### [homepage.yml](#id52)

The homepage yaml sets up all of the data for the homepage (surprisingly):

    --- !fragment
    # Type of template to use
    template: homepage.html

    global:
      title: The Official Python Programming Language Website

    # The data to pass to the template
    local:
      intro:
        header: What is Python?
        text: !rest |
          **NB** this is a beta site, if you want to contribute or make comments please
          go to `psf.pollenation.net <http://psf.pollenation.net>`_ and add to the wiki or raise a ticket.
          The beta is nearly complete, however the content of the home page is yet
          ********<snip>*************

      sidebar: !fragment sidebar.yml

      news:
        headlines:
          - href: /news/fred-award
            title: Fredrik Lundh wins the Frank Willison Award
            teaser: !rest |
              Fredrik Lundh received the Frank Willison Award for Contributions to the Python Community, July 8th at OSCON 2003

          - href: /news/europython-2004
            title: Europython in GÃ¶teborg, Sweden
            teaser: !rest |
              EuroPython_ 2004 is taking place in GÃ¶teborg, Sweden from June 7-9 2004. Register today or view the programme

              .. _EuroPython: http://www.europython.com
         announcements:
          - href: /news/new-website
            title: Python has a new website
            teaser: !rest |
              The Python Software Foundation is pleased to announce a major redesign of the python.org web site.

as you can see, all of the data is stored in the local section and the top level keys are intro and news. The news is made up of headlines and announcements and each of these is a list of dictionaries (href,title,teaser).

The content uses restructured text inline and also uses the \| symbol to allow you to use blocks of content (don\'t forget that the indent is stripped).
:::

::: 
###### [sidebar.yml](#id53)

The sidebar includes all of the boxes that appear on the right hand side of the home page:

    --- !fragment
    # Type of template to use
    template: sidebar.html

    local:
      success: !fragment success.yml
      quote: !fragment quote.yml
      written-in-python: !fragment written-in-python.yml
      using-python-for: !fragment using-python-for.yml

Each item in the sidebar is included explicitly (this should really use a list but that can wait for a refactoring later). Each sidebar is shown below
:::

::: 
###### [success.yml](#id54)

The success file merely includes a title image and link

> \-\-- !fragment \# Type of template to use template: success.html
>
> local:
> :   title: NASA uses python image: /images/success/nasa.jpg link: /about/success#nasa
:::

::: 
###### [quote.yml](#id55)

The quote yaml includes the quote in restructured text format:

    --- !fragment
    # Type of template to use
    template: quote.html

    local:
      title: What they are saying...
      quote: !rest |
        "When you're writing working code nearly as fast as you can type and your
        misstep rate is near zero, it generally means you've achieved mastery of the
        language. But that didn't make sense, because it was still day one and I was
        regularly pausing to look up new language and library features!"

        -- Eric Raymond, "`Why python? <http://www.linuxjournal.com/article/3882>`_"
:::

::: 
###### [using-python-for.yml](#id56)

This is a little complicated as it uses a nested hierarchical set of categories to show the different possible uses of python:

    --- !fragment
    # Type of template to use
    template: using-python-for.html

    local:
      using-python-for: !linktree |
        Web Programming /using-python-for/web
          CGI /using-python-for/web
          App Servers /using-python-for/web
        Scientific /using-python-for/scientific
          Genome /using-python-for/scientific
          Numerical /using-python-for/scientific
        Networking /using-python-for/networking
          Servers /using-python-for/networking
          Peer to Peer /using-python-for/networking
        Education /using-python-for/education
          Logic /using-python-for/education
          Programming /using-python-for/education
        Financial/Statistical /using-python-for/financial
          Banking /using-python-for/financial
          Shares /using-python-for/financial

The !linktree directive allows indentation based nesting of data and treats each item as a !url (see earlier in the docs for reference)
:::
:::::::::

::: 
##### [written-in-python.yml](#id57)

Similar to the using python for data but not hierarchical, hence a simple list of urls can be used:

    --- !fragment
    # Type of template to use
    template: written-in-python.html

    local:
      written-in-python:
        - !url Zope http://www.zope.org/
        - !url Reportlab http://www.reportlab.com/
        - !url Spambayes http://spambayes.sourceforge.net
        - !url Mailman http://www.gnu.org/software/mailman/
        - !url Bittorrent http://bitconjurer.org/BitTorrent/
:::
:::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

[CategoryArchive](CategoryArchive)
