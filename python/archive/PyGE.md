# PyGE

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python GUI application for the Gutenberg e-text project.

Homepage: [http://pyge.sourceforge.net/](http://pyge.sourceforge.net/) - including .deb package for Debian

First encounter problems (can those be solved?):

- installed the debian package, worked.

- tried to invoke pyge\<tab\> from the shell, nothing there. OK, found out that they use PyGE\* for their commands

- tried the reader, it can\'t fetch from the internet

- used PyGETS to try fetching from the internet:
  - first tried \"acquire\" as it didn\'t show me anything
    - acquire did download some stuff that I saved into \~/gutenberg.xml
    - but loading that file still doesn\'t show anything
  - then read the hint about using the !SampleData/ directory
    - but where is it? Had to use `dpkg -L pyge`{.backtick} to find out that it is /usr/share/PyGE/SampleData/. Of course I first tried /usr/share/doc/pyge, /usr/lib/pyge, and some others unsuccessfully.
  - OK, that helped, now I have at least a list of stuff on the screen.
  - But it shows me year and author by default, not the (maybe more interesting TITLE), so I switched to title view (but it then shows the title ONLY!?).
  - Tried to download some title, doesn\'t work, \"download\" button is greyed.
  - Switch back to other view (w/o title), there you can download stuff (without knowing what exactly it is).
  - Downloaded some 12345678.txt file from Jules Verne.

- But the reader, PyGERS, can only work on \*.pdb.

- So I have to convert it first, using the separate converter tool.

- Then finally loaded it using the reader, and it shows me the title page plus 200 BLANK WHITE pages!?
  - Looks like the default font doesnt work, so I configure some other, colours where ok at least.
  - I finally have Jules Verne readable - but in french X)

Is this a typical PyGE first encounter experience? If yes, why doesn\'t it work much easier? I can imagine many people having given up before they can see any e-text on their screen.

I think those 3 tools should:

- be integrated into one
- automatically find their index data locally and have some working \"acquire\" function to fetch fresh data from the internet (and maybe name it \"internet index update\" rather than \"acquire\")
- having a sane font default (or fallback) to avoid blank pages problem
- showing title also in download index
- automagically do conversion when needed

Doing this a \"start, click and read\" experience would be possible, also enabling wider use in education.

**The following comments are from the author of PyGE:**

The reason there is a separate utility for acquiring Gutenberg titles instead of having everything integrated into a single application has a lot to do with the lack of a good computer-readable index source from Project Gutenberg. The primary source of info about available Gutenberg e-texts is provided by a text file which is not easily parsed to provide accurate and complete information on individual e-texts. In order to work around the limitations of the official text index, I chose to implement a utility which essentially searches the Gutenberg web site for web pages which give more complete info, grabs the data, and stores the results into an XML data file. Because there are now over 10,000 e-texts available from Project Gutenberg, the search process can take several hours to complete. Because it takes so long to perform a full search, and the search process is not very friendly to the Gutenberg site in terms of bandwidth usage, it is not intended to be performed very frequently.

Another reason to have a separate utility for searching and downloading files from Project Gutenberg is the increasing number of offerings in formats other than plain text files. With a proper index file, PyGETS works well for finding and downloading books that have been converted into MP3 audio files, Adobe Acrobat PDF files, HTML files, and a number of other different formats. Placing this functionality into the e-text reader program which can only handle zTxt format files does not seem entirely logical.

I think a better solution for PyGE users would be for me (or other interested users) to perform a database update on the Gutenberg site at regular intervals (such as a couple of updates per month) and post the latest updates on the [SourceForge](SourceForge) site for download. Then the PyGETS application could be used to download the latest e-texts in various formats without the average user ever having to invoke the lengthy acquire function.

Integrating the conversion into the zTxt format used by PyGERS with the download step would have one undesireable result. One of the features of the zTxt format is that it allows for creation of named bookmarks, and one convenient use of bookmarks is to mark where natural divisions such as chapters occur within an e-text. It\'s nice to open up an e-text and see a clickable list of chapter headings. These allow you to easily navigate back and forth if you\'re just scanning the work to see if you might be interested in spending the time to read the whole thing. But creating the correct headings for a given e-text requires some humun intervention to get it right every time. This is because the default Gutenberg e-text is plain text with no markup included to indicate where the book, chapter, section, act, scene, etc. breaks occur. The conversion utility has some default patterns it can look for (such as \"Chapter x.\"), but sometimes needs some human input to know exactly what to look for. The conversion process is thus not completely automatic if you want the useful bookmarks included, and so cannot be activated with just a simple press of a button.

Again, the preferred solution may be to reduce the frequency that users are required to use the separate conversion tool, and to provide a repository of e-texts already converted to the zTxt format with the proper bookmarks inserted. These converted e-texts could even be resubmitted to Project Gutenberg so that they would be available directly for download using any available download method, including PyGETS.

In summary, the separate tools provided were not designed to provide a single integrated experience for performing all possible operations on Gutenberg e-texts. For the casual user, the PyGERS e-text reader application is the one they are most likely to be using on a day to day basis. The remaining two applications, the browser/downloader and the conversion tool, are intended to provide necessary tools to make Gutenberg e-texts more accessible, but are not necessarily intended to be used by everybody on a regular basis. The ideal solution would involve more infrastructure support for searching available e-texts and acquiring e-texts in a preferred format, either on the Project Gutenberg site itself, or from a third-party site. These are all things I intend to address at some time in the future.

I would agree that a simple start, click, and read experience would be an ideal situation with e-texts from Project Gutenberg. The reality is that there are a number of steps that must be taken to go from the plain text versions offered by PG to the more pleasantly formatted and more easily navigated experience offered by readers such as PyGERS. The PyGE Project is still a work in progress in the areas of making PG e-texts easy to browse, acquire, and read. Feedback from users or other interested parties on where further efforts should be applied is always appreciated.

**Addressing individual complaints**

The location of the PyGE [SampleData](./SampleData.html) follows conventional Linux distribution guidelines. Application data which is common for all users is intended to go under the directory /usr/share/applicationname by convention. This is true for applications such as gimp, ghostscript, emacs, etc. I don\'t understand the author\'s seeming complaint about the location of PyGE-specific data, other than lack of knowledge about common Linux practices which Debian distributions follow. Looking under a /usr/doc directory is suitable for documentation files, and under a /usr/lib directory is suitable for library files, but /usr/share is the logical place to look for data files.

One complaint raised about PyGETS is that the title was not shown in the view window. This is simply because the commenter did not notice that there was a scroll bar at the bottom of the window which would have allowed him to scroll the contents over to see the title information. Or he could have increased the size of the application window, or even used the mouse to shrink the size of other fields, such as the author field, to allow him to see the title information without scrolling. The only view which allows downloading is the one which shows all information (including the title), precisely because that is the only one where you can be sure about what you are actually getting. The other views only give summary information about things like available authors or text formats, which is why the Download button is disabled and greyed out in those views.

The one complaint about the main PyGERS application was that the default font produced an unreadable result. If this is true, it is a bug, but one which I was not aware of until now. Identifying the specific problem will require some additional information, such as the versions of Debian, Python, and wxPython used when running PyGERS. In any case, as was pointed out, it is an easily correctable problem using the built-in configuration options of PyGERS.
