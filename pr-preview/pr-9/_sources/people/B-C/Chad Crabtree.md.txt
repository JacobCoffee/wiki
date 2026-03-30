# Chad Crabtree

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Chad Crabtree 

I reside in Livonia, Michigan and I work at a coffee shop. I have been using python for about 5 years after reading [How to Become a Hacker] article. I have thus far written about 10k loc and feel that I\'m finally starting to get this programing thing. I recently took part in a Code Clinic from the Tutor mailing list check it out on [BrianvandenBroek](BrianvandenBroek)\'s page.

My company can be found at [http://www.imperialdata.net](http://www.imperialdata.net) all the development I do is in python.

## Random Writer Code Clinic 

------------------------------------------------------------------------

My Analysis

Thanks for your implementations. I looked it over interesting how differently we all ended up doing this and how similar they where also. I think Christian's object approach is the most elegant I\'ve seen thus far for this problem. Mine is object based with procedural driver code. David's is purely procedural. Brian's was objective. I did a little bench marking for the fun of it and I wanted to know why my implementation was so much slower than Christians and about the same as David's, I figured when I wrote this it would be very competitive on the timing because I only needed to loop through the file once. However the initial benchmark gave the below results with the parameters (5 500 tom.txt out.txt) Mine: 2.41900018019 David\'s: 2.3409288052 Christian\'s:1.92717454313 Brian's: 8.40194857168

I was thinking why are mine about the same even though I pre-cached all seed combinations? After looking through their code I saw that they looped through the file each time they needed a new character which is how I did it at first, however I did it like this approximately

s\[n:n+len(seed)\] for n,v in enumerate(s) if s\[n:n+len(seed)\]==seed\]

I did a pure python loop instead of the implied C loops that the other two did. This is why their implementation of looping through the file for each character is pretty fast.

So I thought \'Ah-ha I know how to hit their algorithms.' With the parameters of (10 5000 tom.txt out.txt) I got theses results. Mine:3.67060087246 David\'s:18.8382646398 Christian\'s:15.3224465679 Brian's: 143.980883604

Now here\'s some profiles with the settings (10 5000 tom.txt out.txt)

Mine:

            9988 function calls in 3.856 CPU seconds 

      Ordered by: standard name 

      ncalls  tottime  percall  cumtime  percall filename:lineno(function) 

           1    0.000    0.000    3.829    3.829 <string>:1(?) 
           1    0.026    0.026    3.856    3.856 profile:0(main()) 
           0    0.000             0.000          profile:0(profiler) 
        4991    0.057    0.000    0.057    0.000 random.py:229(choice) 
           1    2.637    2.637    2.637    2.637 randomwriter.py:11(index_text) 
           1    0.040    0.040    0.040    0.040 randomwriter.py:24(get_first_seed) 
        4990    0.180    0.000    0.237    0.000 randomwriter.py:36(get_next_letter) 
           1    0.000    0.000    2.637    2.637 randomwriter.py:4(__init__) 
           1    0.074    0.074    2.989    2.989 randomwriter.py:51(buildoutput) 
           1    0.840    0.840    3.829    3.829 randomwriter.py:59(main) 

David\'s:

            15010 function calls in 18.463 CPU seconds 

    Ordered by: standard name 

      ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
           1    0.000    0.000   18.436   18.436 <string>:1(?) 
           1    0.027    0.027   18.463   18.463 profile:0(main()) 
           0    0.000             0.000          profile:0(profiler) 
        5001    0.115    0.000    0.115    0.000 random.py:229(choice) 
           1    0.000    0.000    0.000    0.000 random.py:90(seed) 
           1    0.096    0.096   18.436   18.436 rwspiffy.py:102(main) 
           1    0.001    0.001    0.001    0.001 rwspiffy.py:38(validateArgs) 
           1    0.000    0.000    0.175    0.175 rwspiffy.py:65(newSeed) 
        5000   17.773    0.004   17.773    0.004 rwspiffy.py:76(nextAfterSeed) 
        5000    0.277    0.000   18.164    0.004 rwspiffy.py:85(doSeed) 
           1    0.000    0.000    0.000    0.000 sets.py:119(__iter__) 
           1    0.175    0.175    0.175    0.175 sets.py:356(_update) 
           1    0.000    0.000    0.175    0.175 sets.py:425(__init__) 

Christian\'s:

            29958 function calls in 16.217 CPU seconds 

      Ordered by: standard name 

      ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
           1    0.000    0.000   16.050   16.050 <string>:1(?) 
           1    0.166    0.166   16.217   16.217 profile:0(main()) 
           0    0.000             0.000          profile:0(profiler) 
           1    0.000    0.000    0.000    0.000 random.py:135(randrange) 
           1    0.000    0.000    0.000    0.000 random.py:198(randint) 
        4990    0.096    0.000    0.096    0.000 random.py:229(choice) 
           1    0.001    0.001   16.050   16.050 randomwrite.py:8(main) 
           1    0.000    0.000    0.000    0.000 randomwriter.py:28(_selectSeed) 
        4990   15.404    0.003   15.404    0.003 randomwriter.py:33(_getMatches) 
           1    0.004    0.004    0.005    0.005 randomwriter.py:4(__init__) 
        4990    0.094    0.000    0.094    0.000 randomwriter.py:43(_getSubChars) 
        5000    0.075    0.000    0.075    0.000 randomwriter.py:55(_writeChar) 
        4990    0.046    0.000    0.046    0.000 randomwriter.py:60(_updateSeed) 
        4990    0.281    0.000   15.995    0.003 randomwriter.py:64(Step) 
           1    0.049    0.049   16.045   16.045 randomwriter.py:74(Run) 

Brian's:

             81353 function calls in 141.329 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.089    0.089  141.303  141.303 <string>:1(?)
            1    0.000    0.000    0.000    0.000 brian_random_writer.py:177(__init__)
            1   50.521   50.521  141.208  141.208 brian_random_writer.py:192(get_randomwriter_text)
            1    0.001    0.001    0.001    0.001 brian_random_writer.py:228(get_input)
            1    0.116    0.116    0.130    0.130 brian_random_writer.py:255(get_orig_text)
            1    0.000    0.000    0.000    0.000 brian_random_writer.py:269(get_novel_seed)
        27871    0.908    0.000   90.555    0.003 brian_random_writer.py:287(get_new_character)
        25600   89.043    0.003   89.043    0.003 brian_random_writer.py:316(get_choices)
            1    0.006    0.006  141.214  141.214 brian_random_writer.py:365(main)
            1    0.014    0.014    0.014    0.014 brian_random_writer.py:79(reader)
            1    0.026    0.026  141.329  141.329 profile:0(main())
            0    0.000             0.000          profile:0(profiler)
            1    0.000    0.000    0.000    0.000 random.py:135(randrange)
            1    0.000    0.000    0.000    0.000 random.py:198(randint)
        27871    0.604    0.000    0.604    0.000 random.py:229(choice)

I\'m going to paste the code from the hot spots identified here.

This is the one that came with mine.

       def index_text(self): 
           index={} 
           textsize=len(self.text) 
           for n,v in enumerate(self.text): 
               if n+self.size<=textsize: 
                   seed=self.text[n:n+self.size] 
               else: 
                   seed=self.text[n:textsize] 
               if index.has_key(seed): 
                   index[seed].append(n) 
               else: 
                   index[seed]=[n] 
           return index 

The reason I ended up doing this is because my first time solving the problem I got correct results but terrible execution time so I profiled it to find out what the problem was. I was using a loop very similar to the one I\'m using above. Before I was doing this for each character, instead I cached my results here and used them on every seed look up. Every possible seed is already in the dictionary. Apparently dictionary lookups are quite fast.

This is David\'s hot spot.

    def nextAfterSeed(seed): 
       """ takes seed to Sort and find probability for next character based on source """ 
       # abstracted for onceandonlyonce principle from doSeed 
       tempvariable = sourcefile.split(seed) 
       del tempvariable[0] # first entry of split sourcefile is not a probable character 
       # OneLiner, return list of first characters in tempvariable, no blanks 
       return [item[:1] for item in tempvariable if len(item) > 0] 

I thought this was interesting and it never crossed my mind, and gives good performance on small values because it uses implied \'C\' based loops. The one I used was python only so it was very slow.

Where he loops through the file each time for each character needed in the output. This makes good sense split the file on the seed then the first character of each subsequent string is the one that is wanted. I have a feeling the string slices are slowing this one down a little I\'m not really sure.

This is Christian\'s hot spot.

       def _getMatches(self): 
           """build a list of indexes of the current seed in the text""" 
           matches = [] 
           match = self.text.find(self.seed) 
           matches.append(match) 
           while match != -1: 
               match = self.text.find(self.seed, match+1) 
               matches.append(match) 
           return matches 

I needed to look this up so I\'m putting it here for the sake of others too.

find(sub\[,start\[,end\]\]) Return the lowest index in the string where substring sub is found, such that sub is contained in the range \[start, end). Optional arguments start and end are interpreted as in slice notation. Return \|-1\| if sub is not found.

This is not so different in concept from the previous hot spot. Find the seed matches then keep their index then he passes this to the character grabber function that takes the index adds the seed length then take that character. It is fast enough because of the implied C loops also.

This is Brian's hot spot.

        def get_choices(self):
            search_point = self.orig_text.find(self.seed, 0, -1)
            choices = []
            while True:
                if search_point == -1:
                    if choices == []:
                        self.get_novel_seed
                    else:
                        break 
                else:
                    choices.append(
                                 self.orig_text[search_point + len(self.seed)])
                    search_point = self.orig_text.find(self.seed, search_point + 1, -1)
            return choices

This does not look to different from how Christian solved the problem. From the profile and comparing it to our profiles Brian's has an unreasonable number of calls to the biggest hotspot. 27k calls to this function. To figure this out we need to look at function that is the second heavy hotspot, to look at why this is so.

    def get_randomwriter_text(self):
            self.get_input()
            self.get_orig_text()
            word_count = old_word_count = 0
            self.get_novel_seed()
            while word_count < self.output_text_length:
                new_character = self.get_new_character()  # stored as used x2
                self.output_text = self.output_text + new_character
                old_word_count = word_count
                word_count = len(self.output_text.split())
                self.seed = self.seed[1:] + new_character\

I was baffled for a little while what was going on in the above code that caused all the function calls, then on the line

Word_count=len(self.output_text.split())

I noticed this would cause the output to be much longer. I changed the line in his program to not split() the string and got the correct output and a much speedier 1.77 seconds on 5 500 tom.txt. The rest of his algorithm was the same as ours just those 8 characters changed things and caused a great slow down. On the parameters 10 5000 tom.txt he got 16.5 seconds, he uses basically the same algorithm as Christian but he caches his previous results, so every time he gets a new seed he looks in the cache and if it already exists then he uses that if not he makes a new one and caches it. This causes his implementation sans .split() to be a bit faster than Christian's. Yet another metric to look at when inspecting code is lines of code.

Brian's code was 364 loc with a whole bunch of comments and doc strings. Christians Code was 128 loc with comments and spaces between functions. David's was 124 with copious comments and good spacing. Mine was 108 after I took out all the extra white

you can find the originals here [Randomwriter Clinic Source](http://www.imperialdata.net/randomwriter_clinic.zip)

Note: I did make changes to the sources in order to do the profiling and to use the timeit module.

- In the case of Brians code I hard coded the paramaters in order to get accurate results for profile and timeit

Email: base64.decodestring(\'ZmxheGVhdGVyQHlhaG9vLmNvbQ==\\n\')

\...

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
