# Concurrency/99Bottles

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# 99 Concurrent Bottles of Beer

    99 bottles of beer on the wall, 99 bottles of beer.
    Take one down, pass it around,
    Take one down, pass it around,
    97 bottles of beer on the wall, 97 bottles of beer
    98 bottles of beer on the wall, 98 bottles of beer

The purpose of this page is to show solutions to common concurrent problems in different styles/toolkits. Inspired by [99 Bottles of Beer](http://99-bottles-of-beer.net/). It is not intended to demonstrate high-performance code, but rather to give potential users a sense of what typical code using the various libraries looks like.

These example are interesting, in that they provide an idea of clarity, how much boiler plate code is needed, how message passing looks, and how to yield to the operating system.

Include a brief description if you add to this page. Please make sure your source is well commented - concurrency is hard!

## The Problem 

Implement

    #!/bin/sh
    tail -f /var/log/system.log |grep pants

in concurrent Python. On unix, you can send syslog messages via `logger`{.backtick}; filenames may vary.

## Errata 

Solutions using readline() will exhibit bugs if less than a full line is flushed to disk. If your input file is syslog, this shouldn\'t be a problem however.

Glyph makes the very valid point that these examples are in fact serial programs (ie, they don\'t do more than one thing at a time). A better example would be following multiple files simultaneously.

## Solutions 

### Generator 

Generators implement a \"pull-style\" approach to concurrency.

:::: 
::: 
``` 
   1 import time
   2 import re
   3 
   4 def follow(fname):
   5     f = file(fname)
   6     f.seek(0,2) # go to the end
   7     while True:
   8         l = f.readline()
   9         if not l: # no data
  10             time.sleep(.1)
  11         else:
  12             yield l
  13 
  14 def grep(lines, pattern):
  15     regex = re.compile(pattern)
  16     for l in lines:
  17         if regex.match(l):
  18             yield l
  19 
  20 def printer(lines):
  21     for l in lines:
  22         print l.strip()
  23 
  24 f = follow('/var/log/system.log')
  25 g = grep(f, ".*pants.*")
  26 p = printer(g)
  27 
  28 for i in p:
  29     pass
```
:::
::::

### Coroutines 

The inversion of the generator example above, coroutines use a \"push-style\" approach to concurrency:

:::: 
::: 
``` 
   1 import time
   2 import re
   3 from functools import wraps
   4 
   5 
   6 def coroutine(func):
   7     @wraps(func)
   8     def thing(*args, **kwargs):
   9         gen = func(*args, **kwargs)
  10         gen.next() # advance to the first yield
  11         return gen
  12     return thing
  13 
  14 @coroutine
  15 def follow(fname, next):
  16     f = file(fname)
  17     f.seek(0,2) # go to the end
  18     while True:
  19         l = f.readline()
  20         if not l: # no data
  21             time.sleep(.1)
  22         else:
  23             next.send(l)
  24 
  25 @coroutine
  26 def grep(pattern, next):
  27     regex = re.compile(pattern)
  28     while True:
  29         l = yield
  30         if regex.match(l):
  31             next.send(l)
  32 
  33 @coroutine
  34 def printer():
  35     while True:
  36         l = yield
  37         print l.strip()
  38 
  39 
  40 p = printer()
  41 g = grep('.*pants.*', p)
  42 f = follow('/var/log/system.log', g)
```
:::
::::

### Greenlets 

Greenlets are similar to coroutines.

:::: 
::: 
``` 
   1 import greenlet
   2 import time
   3 import re
   4 
   5 def follow(fname, next):
   6     # setup
   7     f = file(fname)
   8     f.seek(0,2) # go to the end
   9     # do stuff
  10     while True:
  11         l = f.readline()
  12         if not l: # no data
  13             time.sleep(.1)
  14         else:
  15             next.switch(l)
  16 
  17 def grep(pattern, next):
  18     # setup
  19     regex = re.compile(pattern)
  20 
  21     def do_stuff(l):
  22         parent = greenlet.getcurrent().parent
  23         while True:
  24             if regex.match(l):
  25                 l = next.switch(l)
  26             else:
  27                 l = parent.switch() # subtle!
  28 
  29     return do_stuff
  30 
  31 def printer(l):
  32     # no setup
  33     parent = greenlet.getcurrent().parent
  34     # do stuff
  35     while True:
  36         print l.strip()
  37         l = parent.switch()
  38 
  39 p = greenlet.greenlet(printer)
  40 g = greenlet.greenlet(grep(".*pants.*", p))
  41 follow("/var/log/system.log", g)
```
:::
::::

### Gevent 

[Gevent](http://www.gevent.org) builds user-level threads on top of greenlets.

:::: 
::: 
``` 
   1 import re
   2 import gevent
   3 from gevent.queue import Queue
   4 
   5 def follow(fname, dest):
   6     # setup
   7     f = file(fname)
   8     f.seek(0,2) # go to the end
   9     # do stuff
  10     while True:
  11         l = f.readline()
  12         if not l: # no data
  13             gevent.sleep(.1)
  14         else:
  15             dest.put(l)
  16 
  17 def grep(pattern, source, dest):
  18     # setup
  19     regex = re.compile(pattern)
  20 
  21     def do_stuff():
  22         while True:
  23             l = source.get()
  24             if regex.match(l):
  25                 dest.put(l)
  26 
  27     return do_stuff
  28 
  29 def printer(source):
  30     while True:
  31         line = source.get()
  32         print line.strip()
  33 
  34 source_queue = Queue()
  35 filtered_queue = Queue()
  36 
  37 p = gevent.spawn(printer, filtered_queue)
  38 g = gevent.spawn(grep(".*pants.*", source_queue, filtered_queue))
  39 follow("/var/log/system.log", source_queue)
```
:::
::::

### Kamaelia 

:::: 
::: 
``` 
   1 import time
   2 import re
   3 
   4 import Axon
   5 from Kamaelia.Chassis.Pipeline import Pipeline
   6 
   7 # threaded due to the time.sleep() call
   8 # No yield since a threaded component
   9 class Follow(Axon.ThreadedComponent.threadedcomponent):
  10     def __init__(self, fname, **argv):
  11         self.fname = fname
  12         super(Follow,self).__init__(**argv)
  13     def main(self):
  14         f = file(self.fname)
  15         f.seek(0,2) # go to the end
  16         while not self.dataReady("control"):
  17             l = f.readline()
  18             if not l: # no data
  19                 time.sleep(.1)
  20             else:
  21                 self.send(l, "outbox")
  22 
  23         self.send(self.recv("control"), "signal")
  24 
  25 class Grep(Axon.Component.component):
  26     # Default pattern, override in constructor with pattern="some pattern"
  27     # See below
  28     pattern = "."
  29     def main(self):
  30         regex = re.compile(self.pattern)
  31         while not self.dataReady("control"):
  32            for l in self.Inbox("inbox"):
  33                if regex.match(l):
  34                    self.send(l, "outbox")
  35            self.pause()
  36            yield 1
  37         self.send(self.recv("control"), "signal")
  38 
  39 class Printer(Axon.Component.component):
  40     def main(self):
  41         while not self.dataReady("control"):
  42             for l in self.Inbox("inbox"):
  43                 print l.strip()
  44             self.pause()
  45             yield 1
  46         self.send(self.recv("control"), "signal")
  47 
  48 Pipeline(
  49     Follow('/var/log/system.log'),
  50     Grep(".*pants.*"),
  51     Printer(),
  52 ).run()
```
:::
::::

### Twisted 

:::: 
::: 
``` 
   1 from twisted.protocols.basic import LineReceiver
   2 from twisted.python import log
   3 
   4 SLOW_INTERVAL = 1.0
   5 FAST_INTERVAL = 0.001
   6 SEEK_END = 2
   7 BLOCKSIZE = 8192
   8 
   9 class TailTransport(object):
  10   def __init__(self, fileobj, protocol):
  11       self.fileobj = fileobj
  12       self.protocol = protocol
  13       self.disconnecting = False
  14 
  15   def start(self, clock):
  16       self.clock = clock
  17       self.fileobj.seek(0, SEEK_END)
  18       self.protocol.makeConnection(self)
  19       self.tick()
  20 
  21   def tick(self):
  22       anyData = self.fileobj.read(BLOCKSIZE)
  23       try:
  24           self.protocol.dataReceived(anyData)
  25       except:
  26           log.err()
  27       if anyData:
  28           interval = FAST_INTERVAL
  29       else:
  30           interval = SLOW_INTERVAL
  31       self.clock.callLater(interval, self.tick)
  32 
  33 class Grep(LineReceiver):
  34   delimiter = '\n'
  35   def __init__(self, term):
  36       self.term = term
  37 
  38   def lineReceived(self, line):
  39       if self.term in line:
  40           print line.rstrip("\n")
  41 
  42 def main():
  43   from twisted.internet import reactor
  44   TailTransport(file("/var/log/syslog", "rb"),
  45                 Grep("pants")).start(reactor)
  46   reactor.run()
  47 
  48 main()
```
:::
::::

### Fibra 

:::: 
::: 
``` 
   1 import fibra
   2 import re
   3 
   4 def tail(f, output):
   5     f.seek(0,2)
   6     while True:
   7         line = f.readline()
   8         yield output.push(line) if line else 0.1 #push line, or sleep.
   9 
  10 def grep(pattern, input, output):
  11     regex = re.compile(pattern)
  12     while True:
  13         line = yield input.pop()
  14         if regex.match(line):
  15             yield output.push(line) 
  16 
  17 def printer(input):
  18     while True:
  19         line = yield input.pop()
  20         print line.strip()
  21     
  22 schedule = fibra.schedule()
  23 schedule.install(tail(open("/var/log/syslog.log","r"), fibra.Tube("T2G")))
  24 schedule.install(grep(".*pants.*", fibra.Tube("T2G"), fibra.Tube("G2P")))
  25 schedule.install(printer(fibra.Tube("G2P")))
  26 schedule.run()
```
:::
::::

### Stackless 

:::: 
::: 
``` 
   1 import stackless
   2 import time
   3 import re
   4 
   5 @stackless.tasklet
   6 def tail(f, output):
   7     f.seek(0,2)
   8     while True:
   9         line = f.readline()
  10         if line:
  11             output.send(line)
  12         else:
  13             time.sleep(0.1)
  14 
  15 @stackless.tasklet
  16 def grep(pattern, input, output):
  17     regex = re.compile(pattern)
  18     while True:
  19         line = input.receive()
  20         if regex.match(line):
  21             output.send(line)
  22 
  23 @stackless.tasklet
  24 def printer(input):
  25     while True:
  26         line = input.receive()
  27         print line.strip()
  28 
  29 T2G = stackless.channel()
  30 G2P = stackless.channel()
  31 tail(open("/var/log/syslog.log","r"), T2G)
  32 grep(".*pants.*", T2G, G2P)
  33 printer(G2P)
  34 stackless.run()
```
:::
::::

### circuits

:::: 
::: 
``` 
   1 import sys
   2 
   3 from circuits.io import File
   4 from circuits import Component
   5 from circuits.net.protocols import LP
   6 
   7 class Tail(Component):
   8 
   9     def init(self, filename):
  10         (File(filename, "r", autoclose=False) + LP()).register(self).seek(0, 2)
  11 
  12 class Grep(Component):
  13 
  14     def init(self, pattern):
  15         self.pattern = pattern
  16 
  17     def line(self, line):
  18         if self.pattern in line:
  19             print line
  20 
  21 (Tail(sys.argv[1]) + Grep(sys.argv[2])).run()
```
:::
::::

### pprocess

This example needs pprocess 0.5. The activity functions are similar to the generator (and other) solutions, and the differences lie in the use of the `multigrep`{.backtick} function, which is invoked to provide `grep`{.backtick} functionality for each pattern in a separate process, and in the way the `multigrep`{.backtick} function itself follows several files using the `multifollow`{.backtick} callable (the `follow`{.backtick} function invoked in a separate process). A channel is used in the `follow`{.backtick} function to communicate new lines which are then consumed via a queue in the `grep`{.backtick} function, which in turn communicates matching lines via a channel which are then consumed by the `printer`{.backtick} function.

:::: 
::: 
``` 
   1 import pprocess
   2 import time
   3 import re
   4 
   5 def follow(ch, fname):
   6     f = file(fname)
   7     f.seek(0,2) # go to the end
   8     while True:
   9         l = f.readline()
  10         if not l: # no data
  11             time.sleep(.1)
  12         else:
  13             ch.send(l)
  14 
  15 def grep(ch, lines, pattern):
  16     regex = re.compile(pattern)
  17     for l in lines:
  18         if regex.match(l):
  19             ch.send(l)
  20 
  21 def printer(lines):
  22     for l in lines:
  23         print l.strip()
  24 
  25 def multigrep(ch, pattern):
  26     queue = pprocess.Queue(continuous=1)
  27     multifollow = queue.manage(follow)
  28 
  29     # Launch concurrent following activities.
  30     multifollow('/var/log/system.log')
  31     multifollow('/var/log/other.log')
  32     multifollow('/var/log/another.log')
  33 
  34     # Handle incoming lines using the specified pattern.
  35     grep(ch, queue, pattern)
  36 
  37 # Permit multiple simultaneous grep activities.
  38 queue = pprocess.Queue(continuous=1)
  39 multigrep = queue.manage(multigrep)
  40 
  41 # Launch concurrent grep activities.
  42 multigrep(".*pants.*")
  43 multigrep(".*trousers.*")
  44 multigrep(".*shorts.*")
  45 
  46 # Print incoming lines.
  47 p = printer(queue)
```
:::
::::

### pypes

Here is a simple example based on the pypes framework. It should look similar to the Stackless example above. Pypes abstracts away the semantics of tasklets and channels and provides a model for looser coupling. This makes connecting components at runtime easier which is necessary since at the point in which the component is created, it has no idea what other components it might be interacting with.

:::: 
::: 
``` 
   1 # load the pypes framework
   2 from pkg_resources import require
   3 require('pypes')
   4 
   5 import re
   6 import time
   7 
   8 from pypes.pipeline import Dataflow
   9 from pypes.component import Component
  10 
  11 class Tail(Component):
  12     __metatype__ = 'ADAPTER'
  13 
  14     def __init__(self, fp):
  15         Component.__init__(self)
  16         self.fp = fp
  17 
  18     def run(self):
  19         self.fp.seek(0,2)
  20         while True:    
  21             self.receive('in')
  22             line = self.fp.readline()
  23             if line:
  24                 self.send('out', line.strip())
  25             else:
  26                 self.yield_ctrl()
  27 
  28 class Grep(Component):
  29     __metatype__ = 'TRANSFORMER'
  30 
  31     def __init__(self, pattern):
  32         Component.__init__(self)
  33         self.regex = re.compile(pattern)
  34 
  35     def run(self):
  36         while True:
  37             for line in self.receive_all('in'):
  38                 if self.regex.match(line):
  39                     self.send('out', line)
  40             self.yield_ctrl()
  41 
  42 class Printer(Component):
  43     __metatype__ = 'PUBLISHER'
  44 
  45     def __init__(self):
  46         Component.__init__(self)
  47 
  48     def run(self):
  49         while True:
  50             for data in self.receive_all('in'):
  51                 print data
  52             self.yield_ctrl()
  53 
  54 tail    = Tail(open('/var/log/system.log', 'r'))
  55 grep    = Grep('.*pants.*')
  56 printer = Printer()
  57 
  58 pipe = Dataflow({
  59     tail: {grep:('out','in')}, 
  60     grep: {printer:('out', 'in')}
  61 })
  62 
  63 while True:
  64     pipe.send(None)
  65     time.sleep(0.1)
```
:::
::::
