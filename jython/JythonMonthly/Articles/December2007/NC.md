# JythonMonthly/Articles/December2007/NC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Better Living Through More Obvious Coding Practices 

## Flagging Records in Fixed-Length Data Columns 

#### Submitted By: Rob Andrews 

Most of the day-to-day programming I see in the real world does not consist of 50,000-line applications. And even the larger applications consist of functions and smaller blocks of code that work together to produce the more sophisticated behavior of the larger application.

I advise novice programmers to master smaller common tasks, such as handling text, files, and directories. The skills learned in so doing will be used over and over, even in more specialized software development later on.

The following is a very simple example of a common task. Each line in the file \"states.txt\" begins with a two-letter state abbreviation of the variety we use here in the U.S.

The file consists of fixed-length columns, and the task at hand is to add a flag character to each record to indicate whether the state code is in a list of target states.

:::: 
::: 
``` 
   1 infile = open('c:/sandbox/states.txt','r')
   2 outfile = open('c:/sandbox/states.new','a')
   3 
   4 targetStates = ['AL','MS','LA']
   5 
   6 for line in infile:
   7     stateCode = line[0:2]
   8     if stateCode in targetStates:
   9         targetFlag = 'y'
  10     else:
  11         targetFlag = 'n'
  12     newLine = targetFlag + line
  13     outfile.write(newLine)
  14 
  15 infile.close()
  16 outfile.close()
```
:::
::::

A list of states is defined in Line 4.

Line 7 identifies the location of the state abbreviation in each line of the data file. \"line\[0:2\]\" refers to the first two characters in the line.

I usually use the variable name \"line\" when iterating through lines in a text file, as I have in this example, but this is an arbitrary personal choice (same for \"infile\" and \"outfile\"). The code could just as easily read \"for record in infile:\" in Line 6 and \"record\[0:2\]\" in Line 7, as long as the variable name is used consistently within the code block.

But you can not use:

:::: 
::: 
``` 
   1 for record in infile:        # variable name is "record"
   2     stateCode = line[0:2]    # variable name is "line", not "record", and will cause an error
   3     ....
   4     ....
```
:::
::::

It is also not strictly necessary to code in as \"wordy\" a manner as I have done in this script. In my code, variable names are created for handling the state abbreviation and flag field for each line, which I find easier to read.

In short scripts, it is easier to get by without actually assigning field data to variable names, but I usually prefer to err on the side of readability. Sooner or later someone may have to read your code, whether for debugging, modification, re-use, or some other purpose.

As code blocks become more sophisticated, longer, numerous, etc., meaningful comments also become more important.

But another critical reason to pass data into variables like I have done here is that in some subsequent run of the program, the state abbreviation or some other needed information may be located in a different location within the file. After running this program, for instance, the flag field will off-set all remaining characters in the line by one byte. Meaningful variable names can help manage the ever-changing data landscape as changes are made.

Over time, every programmer develops a unique style based on personal preference, coding conventions in place at one\'s place of employ, etc. I encourage the use of a relatively elegant, obvious approach, particularly during the earlier and steeper parts of the learning curve.

I believe doing so results in a considerably less stressful learning process. Programming may not always be pure fun, but we can make it much less unpleasant with good practices early on.

##### About the Author 

Rob Andrews is a Programmer Analyst at [Sourcelink](http://www.sourcelink.com).
