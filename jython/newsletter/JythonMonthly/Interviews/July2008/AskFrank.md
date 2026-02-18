# JythonMonthly/Interviews/July2008/AskFrank

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Ask Frank! 

Welcome to the Ask Frank question form for July 2008!

I\'ve been in touch with [Frank Wierzbicki](http://fwierzbicki.blogspot.com/) of Sun Microsystems. In case you aren\'t aware, Frank is one of the top Jython developers, and [earlier this year](http://fwierzbicki.blogspot.com/2008/02/jythons-future-looking-sunny.html) Sun Microsystems hired him to work on Jython full time!

Thanks to everyone for your participation\...this is a great opportunity for the Jython community. Special thanks to Frank Wierzbicki for his time!

Josh Juneau

[Gather Event Planning](http://www.gathereventplanning.com) [juneau001@gmail.com](mailto:juneau001@gmail.com)

### Questions for Frank 

I\'ll start it off with the question we all want to ask:

1\) *You\'ve been with Sun for just over three months now, how is Jython development at Sun been going so far?*

***Sun has been great. They genuinely want me to just do more of what I had been doing. They really want to see Jython succeed. I\'ve also been helping with some [NetBeans](./NetBeans.html) work \-- mainly helping them use the antlr parser that I wrote for Jython in [NetBeans](./NetBeans.html).***

2\) *To me it seems from the Python side, Jython is considered irrelevant. Is there any effort to get Jython more into a cooperative effort with Python development? (marvin greenberg, public dot marvin on gmail dot com)*

***Python and Jython have been cooperating from the very beginning. It has been more difficult lately since Jython has been lagging version-wise (we\'re at version 2.2 while Python is at 2.5) but once we catch up this will become better. If you look at the CPython sources you can see lots of places that have Jython specific areas, and CPython has been making great progress lately in making sure that there is always a pure Python version of standard libraries (this makes it easier for other implementations like Jython). This will become more common I think, once we have caught up.***

------------------------------------------------------------------------

- Here\'s my 2 cents worth:

3\) *Building on question 2, IDE/Editor support, there is a fair amount of Python support in IDE\'s but with the exception of Eclipse with [PyDev](./PyDev.html) is there any true Jython support (ie Python with Java)*

***I don\'t personally spend much time using IDEs (which btw is a situation I should remedy \-- for some reason IDEs have never \"fit my brain\" \-- but I have seen developers that I respect use them to great advantage - I \*do\* use them for refactoring in Java) but other Jython developers tell me that Eclipse does allow breakpoints, etc to work between Jython and Java projects. Also, given the JRuby support that I\'ve seen in [NetBeans](./NetBeans.html), I expect the same from that project once the Jython/Python support appears \-- see nbpython project for more: [https://nbpython.dev.java.net/](https://nbpython.dev.java.net/).***

4\) *A while back there was talk about scripting languages being able share object at the JVM level, for example, Jython using JRuby objects. Is there any news in that regard?*

***Nothing concrete yet. We can actually do that in a limited way now, by using each languages support of creating a Java interface, and using the Java integration of these languages (so from Jython you can implement a Java interface, then from JRuby you could call that interface). This is clunky though, and we would like to do better. A cool project looking into this is Attila Szegedi\'s metaobject protocol (MOP) project: [http://dynalang.sourceforge.net/](http://dynalang.sourceforge.net/)***

5\) *With you working at Sun now, obviously they have gained in stature but where does Sun see JVM based scripting languages, like Jython fitting into the over all picture with future JVM and Java versions.*

***Sun is very interested in making the JVM a rich environment for many languages. Certainly in the past the JVM was developed as a Java-only kind of place. This is no longer the case. There is some really interesting work going on to make the JVM a really great environment for languages like Jython. For more see the Da Vinci Machine project (also called the multi-language VM or mlvm \-- in my opinion \"Da Vinci Machine\" is a way cooler name): [http://openjdk.java.net/projects/mlvm/](http://openjdk.java.net/projects/mlvm/)***

5.5) *(not related to q5, just days later ![:)](/wiki/modernized/img/smile.png%20":)") ) Would the results of Java profiling tools like findbugs, Jprofiler or myKit be helpful or more importantly useful to you or one of the members of the development team?*

***Certainly \-- some of the Jython devs, particularly Nicholas Riley are using profiling tools already. Nicholas is using [YourKit](./YourKit.html) ([http://www.yourkit.com/java/profiler/index.jsp](http://www.yourkit.com/java/profiler/index.jsp)).***

Thanks Frank and Josh.\
Greg.

------------------------------------------------------------------------

- 6\) *In which type of applications or which type of uses is Jython more fit / successful*

***At present (say for Jython 2.2) I would say the best fit for Jython is any project where you want to drive Java frameworks or libraries using Python. In the future, I think we will start to have a great story with respect to going the other way (that is using a framework like Django that needs to call into Java api\'s). Furthermore, I think Jython will become attractive for its deployment options even for Python projects that have no need to integrate with Java. To take one example, I think being able to deploy a full Django app as a self-contained war file onto a J2EE app server will become a compelling option.***

7\) *When do you think jython will reach 3.0. What are the most difficult things to implement in going from python 2.5 to 3.0?*

***I don\'t think I\'m ready to make any predictions about Jython 3.0 \-- at the moment my plan is to start work on 2.6 immediately after 2.5 is out. My hope is that we can get 2.6 out long before CPython 2.7 comes out, putting Jython in a position to develop the 2.x series concurrently with CPython. When CPython releases a production 3.0, I expect we will start an experimental 3.0 branch for Jython \-- but I have no idea how long it will take to get to a production 3.0 for Jython.***

8\) *Which part of jython are you working more? Why?*

***My personal coding time is probably at least 50% parser work. Probably it is becuase the code is changing quickly and has a certain goofiness to it (it is my first large scale Antlr project and some of the learning curve still shows) so no one else really wants to touch it yet. I am working hard to make it clearer. Probably the next most common place for me to work is in the compiler \-- this is where work is needed to get the 2.5 language level feature implemented.***

9\) *Sun as some developers working in JRuby and now you are working in Jython. Do you work together in some type of \"open source java dynamic languages\" lab or is your work uncoordinated?*

**\'There is no physical \"language lab\". I am in North Carolina and the JRuby guys are located in Minnesota. But there has been collaboration (For example, we are directly using their work for a Jython posix layer: see [https://svn.codehaus.org/jruby-contrib/trunk/jna-posix/](https://svn.codehaus.org/jruby-contrib/trunk/jna-posix/)). I expect there will be much more collaboration in the future. The JRuby folks have pre-explored many of the trails that Jython needs to follow.**

10\) Have you heard of Fortress? From a language point of view what do you consider more revolutionary in it? AFAIK it has currently only an interpreter and being so it is kinda-dynamic. Do you think we\'ll have a JFortress?

**I have heard of Fortress \-- but I haven\'t actually given it a look. I\'m still deciding on a language to dable in this year \-- Fortress is a possibility since I want to look into a functional language.**

Thanks in advance,

Luis Sergio Oliveira

------------------------------------------------------------------------

- 11\) On the current jython website, the roadmap says that the current codebase of Jython 2.2 \"is extremely brittle\". Is it possible for you to walk us through some of the (major) refactoring that have been done to the codebase of Jython 2.5?

**I can\'t really give this question the attention it really deserves, but I can give some brief examples. \"Extremely brittle\" might have been better stated as \"really hard for newcomers to read\". We have replaced the Javacc parser with an Antlr parser \-- and Antlr has \*much\* better documentation compared to Javacc. We have refactored the compiler to use ASM, which is a very common choice for bytecode generation. We have reduced the amount of custom code generation for new-style classes and replace it with annotations, which should be much more familiar to Java programmers. We have reformatted lots of code to better fit a Java style.**

12\) Is it possible to do optional static type declaration in Jython? It will not be compliant to CPython, but I would like to know if it is at least technically feasible since Jython is running on JVM.

**We will be looking into adding decorators that will allow Jython to automatically express Java methods something like the support that jythonc used to give. Jim Baker has been talking with Jemery Seik about his work in gradual typing \-- so this may be something to watch.**

Thanks,

Anthony Kong

------------------------------------------------------------------------

- 13)What would be the first steps for someone that wants to help with developing Jython itself?

**Where to start? Are there lightweight tasks? Which skills are really needed? Etc. The first thing would be to try compiling Jython on your local system and see how it works. See [http://wiki.python.org/jython/JythonDeveloperGuide](http://wiki.python.org/jython/JythonDeveloperGuide) for more. Next you might want to see if there is a particular Python module that you want to use or that isn\'t working \-- and take a look at why it isn\'t working (and give us a bug report or try to fix it!)**

thx, Berco Beute

------------------------------------------------------------------------

- 14\) Do you plan on releasing any milestones in the development of jython2.5?

**Timely question ![:)](/wiki/modernized/img/smile.png%20":)") \-- see [http://fwierzbicki.blogspot.com/2008/07/jython-25-alpha-released.html](http://fwierzbicki.blogspot.com/2008/07/jython-25-alpha-released.html) for the alpha announcement.**

Thanks, Allan Davis

------------------------------------------------------------------------

- Sorry, more questions\...

15\) What is your take on GIL given your experience with Jython development? Is GIL, in CPython world, a bottleneck to performance? (There are already a lot of discussions around this topic. It is hard to tell which is fact, opinion or just myth. I\'d like to see if u may provide a different angle to this topic)

**I suspect the average user of Python is not affected by the GIL in current environments. However, highly multithreaded environments and the massively multicore machines that are coming, are quite likely to get a performance advantage from GIL-less Pythons (with Jython, of course, being one of those GIL-less Pythons).**

16\) Do you have any kind of possible arrangement of tests/benchmark in mind such that, by comparing cpython and jython, we can find out the performance gain that is a result of removal of GIL?

**We have some ideas in this area, but nothing concrete to point at just yet.**

Cheers, Anthony

------------------------------------------------------------------------

- 17\) I\'m a non-Java programmer who\'s into Jython programming. It seems that Jython is geared more towards the Java developers; for example, creating stand-alone jar applications is only practical if you already know Java. Are there any attempts to \"not alienate\" (for lack of a better term) people like me? I\'m sure Jython would love to have a much wider audience.

**The main thrust of 2.5 work has been to get to a modern version of Python that is better able to run typical Python programs that we see heavily used (like Django, [TurboGears](./TurboGears.html), and Pylons). In the course of this work we have improved support for more standard Python practices like the use of setuptools. Our first target is to make Jython a really good implementation of Python. Hopefully that will help\...**

- Submitted by astigmatik
- 
