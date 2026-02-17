# PdbImprovments

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page point issues related to [Python Debugger](http://docs.python.org/lib/module-pdb.html) that will led to(hopefully) better Python debugging environment:

- bugfixes/functionality improvments in bug/patch tracker

- write pdb\'s unit_tests *\[rocky: the [extended python debugger](http://bashdb.sourceforge.net/pydb) does in fact has such unit tests. Because lots of tests are needed, a diff output file mechanism was added on top of the standard unit test mechanism.\]*

- look at other debuggers(Python/non-Python) and see if we can learn something from it. (I\'m sure we can;) *\[rocky: pydb mentioned above tries to follow gdb\'s command set.\]*

- pdb\'s design issues (Could someone add more information about it?)

You are welcome to add your pdb\'s wishes below.

------------------------------------------------------------------------

It would be great if pdb\'s environment were like the Python interactive shell - for example, you would be able to run multiline blocks, in the context of the running program.

Here\'s an example:

- {{{(Pdb) for x in \[1,2,3\]:

\*\*\* [SyntaxError](./SyntaxError.html): unexpected EOF while parsing (\<stdin\>, line 1) (Pdb) print \"\"\"A multi- \*\*\* [SyntaxError](./SyntaxError.html): EOF while scanning triple-quoted string (\<stdin\>, line 1)}}}

*\[rocky: Both pdb (and pydb) inherit from the Cmd class which handles user interaction. Add this improvement to the Cmd class and virtually no change needs to be done to either pdb or pydb.\]*

Something that\'s really needed is the possibility to stop another Python process in the middle and work from there - gdb has this possibility, and a few times I\'ve tried to use it to find what my Python processes were doing, but it wasn\'t easy and most of the times I wasn\'t able to understand what they were really doing.

*\[rocky: I\'m not sure that this can be done without changing the python interpreter or without arranging for the possibility previously. A step along the way to accomplish this might be to extend pdb to allow another process to control it, but the python program would have had to been started in a way that allows for this. Nir Aides in winpdb allows for control by remote execution for which this is a special case where the process lives on the same machine.\]*

Running pdb from another code - many times I want to go back again and again to a specific situation, and I turn out to many times do a specific procedure to get there, like setting a breakpoint, hitting it three times, setting another breakpoint, and so on. If there was a way to run all these commands from a Python function, all this would be much simpler - I would write a code to do it, and give me control after the procedure is done.

*\[rocky: to a limited extent this exists. pdb allows for a script file to get run before starting the debugger. I think it reads .pdbrc. The [extended python debugger](http://bashdb.sourceforge.net/pydb) may also be of use here. It uses .pydbrc rather than .pdbrc. But there is a \"source\" command that can run debugger commands at any time, not just on start up. Also there is a \"restart\" command which remembers debugger settings like breakpoints\]*

It seems to me that the basic interface should be an instance which controls an execution, which can be given commands such as:

- Set breakpoint
- Continue until reaching a breakpoint
- Execute code in the debugged context
- Evaluate an expression in the debugged context

Such an interface would be easily wrapped by an interactive user interface similiar to that of today.

*\[rocky: I\'m not sure what the above means; bdb does the things listed above, while pdb or pydb is there to add the interactive user interface via Cmd.\]*

Noam Raphael

------------------------------------------------------------------------

a couple of observations about pdb\'s source code:

- pdb.py/bdb.py interaction seems to be very convoluted: it really feels that getting rid of bdb.py would simplify things a lot

*\[rocky: sorry but I disagree here. bdb is there to handles just the debugging aspect, while pdb builds on this and adds the user interaction and command interface.\]*

\[ilya: well, my biggest problem with pdb/bdb pair is that the modules just *feel* too intertwined.. All too often doing anything in pdb.py requires touching or understanding of internals of bdb\...

*rocky: perhaps, but I think to some extent that\'s the nature of the beast. Suppose I have have this minitaur object which is half human and half horse. Any time you want to change the minitaur behavior you may find you are really have to understand either the horse or the human objects. In the case of pdb, the split is probably more 80% Bdb and 20% Cmd. And yes, the analogy isn\'t all that good. There are way more horses out there than minitaurs, while you\'ll rarely see a bdb thing without pdb/pydb.*

there are several minor annoyances: like bdb printing to stdout, *rocky: yes it should be fixed. In pydb it is done by subclassing all those routines that print to stdout. Better of course would be to fix bdb.* or keeping bp list as Class variables, etc. But these are probably fixable\... (but then again it would be much easier to fix them if there was no risk of breaking code relying on current bdb behaviour). *rocky: you are more than welcome to suggest changes to pydb or pdb for that matter, but making changes to pydb I think the changes will have a shorter time to market.* \]

- runtime documentation of pdb.py is spread over 2 places (pdb.doc and pdb.py itself) with a lot of duplication (of course there are std lib docs too). My feeling is that pdb.doc should go.

*\[rocky: I agree that pdb.doc should go. In fact pdb.doc also duplicates a lot of the on-line help of various commands via doc strings that the Cmd class introspects and will show you via its help mechanism. In pydb I have extended the documentation and that is self sufficient.\]*

Ilya (isandler)

------------------------------------------------------------------------

One handy thing that gdb has that pdb and pydb don\'t appear to have is watchpoints.

In gdb, watchpoints cause a break whenever the value of an expression changes (watch) or when the value of a variable is used (rwatch).

I think watchpoints could be implemented in pdb/pydb using one of two approaches:

- \(1\) using a callback whenever the value of a watched object is modified, or when a watched variable is rebound. (2) adding a conditional breakpoint on every statement where the watched object could be modified or the watched variable could be rebound.

Does this sound like a useful feature? Any suggestions?

Ed Groth

*rocky: Adding watchpoints is a good thing. A good way to make sure it gets done is to dig in and make a patch. Although I can\'t speak for pdb, but I can assure folks that if the code is reasonably written and follows gdb\'s lingo, it would be added to pydb.*

*With respect to approach (1) versus (2). Perl has this \"tie\" mechanism that allows interception of assignment commands variables at the Perl level efficiently. Unless there\'s something equivalent (and I doubt it), I don\'t see how this could be done short of changing the interpreter (which might be a good thing). Using approach (2) could be done within the existing pdb/pydb by adding more code to the \"user_line\" routine. But downside of approach (2) is that when there are watchpoints, the execution of the code will slow down even more. In fact I think this may already be a criticism of pdb/pydb.*
