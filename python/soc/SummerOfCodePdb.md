# SummerOfCodePdb

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Improving the Python debugger 

Student: Matthew J Fleming

Mentor: Rocky Bernstein

Repository: [http://svn.python.org/projects/sandbox/trunk/pdb](http://svn.python.org/projects/sandbox/trunk/pdb)

Many people have voiced their concern that the Python debugger could be improved in a number of ways. This project aims to incorporate these suggestions into an improved version of Pdb. These improvements are to allow,

- debugging from another process
- debugging remotely
- debugging a threaded application

The class that overrides Pdb and provides our enhancements is \'MPdb\'.

#### None of the information below is set in stone and may change based on mine or Rocky\'s ideas and public feedback as we feel it is better to make some of the decisions (communication mechansim) open to change in the future or at least being able to make a decision later rather than sooner. 

The design of these improvements has been of great importance and we have specifically concentrated on allowing future programmers to easily add to our work. For example, up until recently in the Python trunk, to get a Pdb session to send program output to some place other than stdout one had to override all of the methods in Pdb that used a \'print\' statement. However, now, the version of Pdb in the trunk allows a programmer to specify both a stdin and a stdout stream. We will follow this example. The advantage of our design is that it is easily extensible and it aims to follow the gdb way to doing things.

## Debugging communication techniques and ideas 

We have discussed various communication mechanisms including sockets and serial communication. For debugging from another process it became clear (after looking at other debuggers) that most people choose to go with a \'socket-based\' approach. The advantages of using this approach is that it is a tried and tested method that many debuggers use. One alternative to the socket approach is to use xmlrpc which allows the passing around of requests in a structured format, which may come in most handy when the debugger server is sending information to a debugger console. For instance, if someone were to write an IDE for MPdb, it would be trivial when using xmlrpc to allow the debugging server class to return a tagged message to the console which would indicate,

- Where in the source we currently were
- The state of some configuration variable on the server side

It became clear that the method of communication that is available to a programmer when debugging an application will change between projects. An embedded devices programmer working with python may not necessarily have access to a network card and thus, no access to network sockets. However, they may have access to a serial port on the embedded device and whilst this project may not provide code to allow communication over a serial line, it should be easy for a programmer to subclass MPdb and write one themselves, without having to undo or \'work around\' any of the features or specifications or MPdb.
