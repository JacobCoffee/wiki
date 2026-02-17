# JythonMonthly/Articles/October2007/NC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Newbie Notes: Creating a Grid Layout of Data Distributed Among Files in a Directory 

#### Submitted By: Rob Andrews 

### Introducing Newbie Notes 

Welcome to my first article for "newbies" (non-derogatory, of course) to jython in Jython Monthly. Jython users often approach it with some expertise in one or more areas of software development, but lacking familiarity with some other relevant aspects of jython programming.

I hope to present in my articles some basic techniques, ideas, and gotchas to help save some time and frustration for the jython newcomer.

I will try to introduce some fundamental ideas in ways that should cause as little cross-platform trouble as possible and endeavor to keep each article concise enough to avoid a bog of details.

### Task Analysis 

In this first article, let\'s look at a common scripting task in which one has to produce a tab-delimited table of marketing information about a set of customers (a \*very\* common task for me, as I provide data services for marketing purposes).

In this case, one has a directory of data about a list of clients. Within the directory are an arbitrary number of text files with a .dat extension. Each file contains a number of lines including such information as the business name, current advertising slogan, etc.

An example of such a file (with descriptive comment per line):

    39762                      # client ID number
    Shamus Banjo Supply        # client location name
    123 Algo Lugar             # street address
    Nadie, NV 98765            # city, state, zip
    We beat your best deal!    # marketing slogan
    Julio Shamus               # manager name
    123-456-7890               # phone number

The task at hand is to produce a file in which each line contains the contents of one of the client information files, with each line in the source file written out as one of a series of tab-delimited fields in the created file. Additionally, the programmer appends a readable timestamp of when the record was inserted into the file.

### Implementation 

Let\'s look at the code:

:::: 
::: 
``` 
   1 # import of modules from standard library
   2 import time, glob
   3 
   4 # working directory and output file name
   5 demographicsDir = 'C:/demographics/'
   6 clientListFile = 'customers.xls'
   7 
   8 # a single file to display a grid of the combined contents of the .dat files
   9 outputFile = open(demographicsDir+clientListFile,'a')
  10 
  11 # iterate through list of *.dat files in the folder
  12 for clientInfoFilename in glob.glob(demographicsDir+'*.dat'):
  13 
  14   # read from each .dat file
  15   inputFile = open(clientInfoFilename,'r')
  16 
  17   # no special syntax for nested 'for' loop
  18   for line in inputFile:
  19     outputFile.write(line.replace('\n','\t'))
  20 
  21   # append time stamp
  22   outputFile.write(time.ctime()+'\n')
  23 
  24   # not safe to assume files will always close automatically
  25   inputFile.close()
  26 
  27 outputFile.close()
```
:::
::::

### Avoiding Headaches 

Notice in the creation of the demographicsDir variable that \'/\' is used instead of \'\\\', despite the fact that the \'C:\' suggests this is taking place on a computer running Windows. It is possible, and not amazingly difficult, to write code using the typical Windows \'\\\' character, but doing so introduces some potentially fussy details involving raw strings and/or having to escape one \'\\\' with another, so that \'\\\\\' produces the result one would expect from \'\\\'.

I also opted to wrap file and directory names in variables for a few different reasons. First off, doing so enables the programmer to change the name of a file or directory in one place instead of having to track down each reference to the file or directory and change it there. In programs of any meaningful size and sophistication, this can be a real headache.

Secondly, and of equal importance, is that using meaningful variable names in your code will make it easier to read and understand later. Someone (and that someone may well be you) will have to maintain that code sooner or later, and far fewer tears will be shed if good names were chosen right from the start.

### Using \'import\' to Add Functionality 

The code begins with an statement to import a couple of modules used in the code. The glob module makes available glob.glob(), which we used to match files ending in \'.dat\' at the beginning of the first \'for\' loop. The time module makes available time.ctime(), used to insert a human-readable timestamp into the grid file we\'re writing.

As a rule, it\'s desirable to import proven functionality already available instead of writing new code for old problems.

### Pythonic Whitespace 

If you are a java developer unfamiliar with python, you may be wondering where some of your various fine curly braces and semicolons have gone. In jython, whitespace is used to keep track of statements and code blocks, so the curly braces and semicolons may be used for other purposes.

One of the basic ideas involved in this use of whitespace is that well-written code is indented for readability anyway, so why include redundant characters when the proper indentation can get the job done nicely all by itself?

### Reading, Writing, and Looping Through Contents of Multiple Files 

Inside the first \'for\' loop, new statements are indented a certain amount, and each is indented the same amount as all other statements in the loop.

Also, one of the statements in the \'for\' loop is the initiation of an additional \'for\' loop. So statements within that loop will be indented further and consistently (even though this particular) \'for\' loop only contains one statement).

The single line (line 17) within that nested \'for\' loop writes each line of the input file to the output file, but replaces the newline character (\'\\n\') with a tab (\'\\t\'). Each line of the output file will be one record in a tab-delimited grid of information from the various input files.

Each output file line ends with the newline character inserted after the timestamp on line 20 in the code. If the indentation of line 20 were increased one level, it would belong to the nested \'for\' loop resulting in a significantly altered output file.

In the main \'for\' loop, each input file is opened once with the \'r\' argument to the file opening statement, so that the script may read its data. The output file has, by this point, been opened with the \'a\' argument, so new information from the input files is appended to it, or tacked onto the end. Of course, \'read\' and \'append\' are only two among various options for file opening.

So we start off with multiple input files, but only create one output file. And if the output file already exists, neither the file nor its current contents are over-written.

### Looking Ahead 

In future articles, we can build on these and other basic ideas, such as exception handling to deal with potential snags your scripts may encounter, various ways of obtaining variable data from outside the script\'s source file (shell arguments, raw user input, GUI form data, etc.), more sophisticated string formatting operations, incorporating java resources, etc.

I hope these articles will make jython more approachable to new users and welcome both comment and correction.

##### About the Author 

Rob Andrews is a Programmer Analyst at [Sourcelink](http://www.sourcelink.com).
