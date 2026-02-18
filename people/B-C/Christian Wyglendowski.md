# Christian Wyglendowski

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Christian Wyglendowski 

I am a Network Administrator at a small college in Illinois. I began learning Python in 2002 while working as a PC Technician. It has been invaluable for systems administration and was just plain enjoyable to learn (or keep learning, I should say!).

## Code Clinic 

[BrianvandenBroek](BrianvandenBroek) came up with a great idea to do periodic programming problems with a group of others and then do a shared analysis afterwards to see the different approaches we all took on the problem. At this time, it is called the Python Code Clinic. Other participants with wiki pages are [ChadCrabtree](ChadCrabtree) and [DavidBroadwell](DavidBroadwell).

### Random Writer 

Our first project was the [Random Writer](http://nifty.stanford.edu/2003/randomwriter/) from the [Standford Nifty projects site](http://nifty.stanford.edu/). You can read more about the project at the Nifty site.

I chose to tackle the project from an object oriented perspective. I have slowy been \"getting it\" as far as OOP goes and this proved to be some more good practice. Here is my base class, RandomWriter \<\--\'how do I make that not link?\' asked Christian. See [HelpForBeginners](HelpForBeginners) for why what I did works\--[BrianvandenBroek](BrianvandenBroek):

    import random

    class RandomWriter:
        def __init__(self, seedLen, outLen, inName, outName):
            #initialize instance variables from parameters
            self.seedLen = seedLen              #seed length in characters
            self.outLen = outLen                #output file length in characters
            self.outTotal = 0                   #initialize total chars written to zero
            
            self.seed = None                    #initialize seed to None

            #open files        
            inFile = file(inName)               #open the input file
            self.outFile = file(outName, 'w')   #open the output file
            
            self.text = inFile.read()           #create string variable with contents of inFile
            inFile.close()                      #bye, inFile
            self.textLen = len(self.text)       #get the length in chars of the text to analyze
            self._selectSeed()                  #generate a seed from the text
            self.matches = []                   #iv for matches
            self.newChar = ''                   #iv for the next char from the text

            #write the initial seed to the output file
            for ch in self.seed:                
                self._writeChar(ch)
            

        def _selectSeed(self):
            """get a random seed that is self.seedLen long"""
            pos = random.randrange(self.textLen)
            self.seed = self.text[pos:pos+self.seedLen]

        def _getMatches(self):
            """build a list of indexes of the current seed in the text"""
            matches = []
            match = self.text.find(self.seed)
            matches.append(match)
            while match != -1:
                match = self.text.find(self.seed, match+1)
                matches.append(match)
            return matches

        def _getSubChars(self):
            """build a list of the chars that come after our current seed in the text"""
            subChars = []
            for index in self.matches:
                if index >= 0:
                    try:
                        ch = self.text[index+self.seedLen]
                    except IndexError: #oops! end of the text
                        ch = self.text[-1] #get last char
                    subChars.append(ch)
            return subChars

        def _writeChar(self, ch):
            """write char to output file and increment outTotal counter"""
            self.outFile.write(ch)
            self.outTotal += 1

        def _updateSeed(self, ch):
            """add the latest char to the end of the seed and drop the first char"""
            self.seed = self.seed[1:] + ch

        def Step(self):
            """process current seed, write probable subsequent char, build new seed"""
            self.matches = self._getMatches()
            subChars = self._getSubChars()
            nextChar = random.choice(subChars) #grab a "random" subsequent character
            self._writeChar(nextChar)
            #print "Wrote", nextChar
            self._updateSeed(nextChar)
            #print "New seed is", self.seed

        def Run(self):
            """do a Step for every char to be written"""
            for i in range(self.outLen - self.outTotal):
                self.Step()

Here is my implementation file:

    import sys
    import randomwriter

    def usage():
        print "python randomwrite.py SEEDLENGTH OUTLENGTH INFILE OUTFILE"
        
        
    def main():
    #check for proper number of args
        if len(sys.argv) != 5:
            usage()
            sys.exit(1)        
        
        seedLength = int(sys.argv[1])
        outLength  = int(sys.argv[2])
        inFile     = sys.argv[3]
        outFile    = sys.argv[4]

    #begin error checking --------------------
        if seedLength < 1 or outLength < 1:
            print "SEEDLENGTH and OUTLENGTH need to be greater than zero."
            sys.exit(1)

        try:
            rw = randomwriter.RandomWriter(seedLength, outLength, inFile, outFile)
        except IOError:
            print "Error reading or writing files.  Please double check file names and locations."
            sys.exit(1)

        if rw.seedLen > rw.textLen:
            print "The input file has to contain at least as many characters as SEEDLENGTH."
            sys.exit(1)
    #end error checking ----------------------

    ##    print "Initial seed is", rw.seed
    ##    print "Processing..."
        rw.Run()

    if __name__ == '__main__':
        import profile
        profile.run("main()")

#### Analysis 

[ChadCrabtree](ChadCrabtree) already did some great analysis on his wiki page, and I am not going to duplicate that here. I am going to focus on what he brought to light about my algorithm and what I did to improve it.

For his analysis, Chad ran everyones\' random writers through the Python profiler. When fed the command line args \"5 500 tom.txt out.txt\", my code faired better than the others by a small margin. However, when ran with these (10 5000 tom.txt out.txt) parameters, my code lagged far behind Chad\'s implementation and faired similarly to David Broadwell\'s (see Chad\'s wiki page for the analysis details).

In my approach, for every character to be written to the output file, I searched the input file for occurances of the seed and grabbed the next character. That means that at some level (Python C code I guess) I was looping over the input file for **every** output character! Not very efficient for large output files.

Chad\'s script was the fastest for large output values. He built a dictionary of seeds and subsequent characters and only had to loop over the source file once, no matter what the output size. I like this approach and have since wrote a subclass that incorporates such a cache, or index. Here is my subclass, [FastRandomWriter](./FastRandomWriter.html):

    class FastRandomWriter(RandomWriter):
        """Went Chad's route and implemented a one-pass cache of seeds->nextchars.
        This subclass actually lives up to its name, unlike the samples above."""
        def __init__(self, seedLen, outLen, inName, outName):
            RandomWriter.__init__(self, seedLen, outLen, inName, outName)
            self._cacheText()
            
        def _cacheText(self):
            chunkpos = 0
            chunk = self.text[:self.seedLen]
            self.cache = {}
            for i in range(self.textLen + 1 - self.seedLen):
                try:
                    nextchar = self.text[chunkpos+self.seedLen]
                except IndexError: #we've reached the end of the text
                    nextchar = '\n' #just stick a newline in as a value for the last key
                if self.cache.has_key(chunk):
                    self.cache[chunk].append(nextchar)
                else:
                    self.cache[chunk] = [nextchar]
                chunkpos += 1
                chunk = chunk[1:] + nextchar

        def Step(self):
            nextChar = random.choice(self.cache[self.seed])
            self._writeChar(nextChar)
            self._updateSeed(nextChar)

Here are the results from my original class:

    C:\Documents and Settings\Christian\Desktop\randomwriter>python randomwrite.py 1
    0 5000 ..\tom.txt out.txt
             29958 function calls in 11.322 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.002    0.002   11.308   11.308 <string>:1(?)
            1    0.013    0.013   11.322   11.322 profile:0(main())
            0    0.000             0.000          profile:0(profiler)
            1    0.000    0.000    0.000    0.000 random.py:135(randrange)
            1    0.000    0.000    0.000    0.000 random.py:198(randint)
         4990    0.063    0.000    0.063    0.000 random.py:229(choice)
            1    0.000    0.000   11.307   11.307 randomwrite.py:8(main)
            1    0.000    0.000    0.000    0.000 randomwriter.py:28(_selectSeed)
         4990   10.865    0.002   10.865    0.002 randomwriter.py:33(_getMatches)
            1    0.005    0.005    0.006    0.006 randomwriter.py:4(__init__)
         4990    0.069    0.000    0.069    0.000 randomwriter.py:43(_getSubChars)
         5000    0.049    0.000    0.049    0.000 randomwriter.py:55(_writeChar)
         4990    0.030    0.000    0.030    0.000 randomwriter.py:60(_updateSeed)
         4990    0.189    0.000   11.266    0.002 randomwriter.py:64(Step)
            1    0.036    0.036   11.301   11.301 randomwriter.py:74(Run)

And here are the results from [FastRandomWriter](./FastRandomWriter.html):

    C:\Documents and Settings\Christian\Desktop\randomwriter>python randomwrite.py 1
    0 5000 ..\tom.txt out.txt
             19980 function calls in 2.769 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.551    0.551    2.757    2.757 <string>:1(?)
            1    0.013    0.013    2.769    2.769 profile:0(main())
            0    0.000             0.000          profile:0(profiler)
            1    0.000    0.000    0.000    0.000 random.py:135(randrange)
            1    0.000    0.000    0.000    0.000 random.py:198(randint)
         4990    0.036    0.000    0.036    0.000 random.py:229(choice)
            1    0.000    0.000    2.205    2.205 randomwrite.py:8(main)
            1    0.000    0.000    1.955    1.955 randomwriter.py:115(__init__)
            1    1.949    1.949    1.949    1.949 randomwriter.py:119(_cacheText)
         4990    0.116    0.000    0.225    0.000 randomwriter.py:135(Step)
            1    0.000    0.000    0.000    0.000 randomwriter.py:28(_selectSeed)
            1    0.006    0.006    0.006    0.006 randomwriter.py:4(__init__)
         5000    0.045    0.000    0.045    0.000 randomwriter.py:55(_writeChar)
         4990    0.028    0.000    0.028    0.000 randomwriter.py:60(_updateSeed)
            1    0.026    0.026    0.250    0.250 randomwriter.py:74(Run)

I will write more later ![:-)](/wiki/europython/img/smile.png%20":-)")

------------------------------------------------------------------------

Email: `<christian AT SPAMFREE dowski DOT com>`

\...

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
