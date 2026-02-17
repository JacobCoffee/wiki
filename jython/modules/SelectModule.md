# SelectModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# New Select Module 

## Introduction 

There is now select support in the [jython distribution](http://www.jython.org/Project/download.html), as of version 2.2rc1.

The new module presents an API which is as close as possible to the [cpython select module](http://www.python.org/doc/lib/module-select.html), Jython supports both the

1.  select.select function

2.  [select.poll objects](http://www.python.org/doc/lib/poll-objects.html).

When using the select module, you should be guided by the cpython documentation: any deviation from the behaviour described in that documentation, except for the the considerations mentioned below, should be considered a bug and [reported](http://www.jython.org/bugs) as such.

If you are starting a new project, it is recommended that you use select.poll objects, because

1.  Poll objects are the most efficient mechanism to multiplex sockets on jython, being fairly much a direct mapping to [java.nio.channel.Selector objects](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Selector.html).

2.  The select.select function is implemented using a poll object, which means that sockets are de/registered every single time, which is slightly less efficient.

## Usage notes 

### Always close poll objects 

When a socket has been registered with a select.poll object, it remains registered until explicitly deregistered. This has the following implications

1.  Sockets cannot be placed in blocking mode while they are still registered with poll objects
2.  The reference from the poll object to the socket might interfere with garbage collection

Therefore, it is recommended that you always explicitly close poll objects, using an idiom such as

    def my_polling_func(sockets):
        poll_object = select.poll()
        try:
            for s in sockets:
                poll_object.register(s)
        finally:
            poll_object.close()

Closing a poll object cancels all registrations of sockets.

## Differences between cpython and jython 

Due to fundamental differences in the behaviour of java and C on various platforms, there are differences between the cpython and jython select modules which are not possible to code around. Those differences will be listed here.

### Only sockets can be multiplexed, not files or any other IO channel 

The design of the cpython non-blocking API is derived from the UNIX C api, which deals with [FILE DESCRIPTORS](http://en.wikipedia.org/wiki/File_descriptor). Since file descriptors can describe any type of I/O channel on unix OSes, cpython can deal with selecting and polling on multiple channel types, such non-blocking files, pipes and named-pipes, fifos, etc.

The java model for selecting on channels is much more restrictive. There is a java abstract class, [SelectableChannel](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html), which other channel classes must subclass if they are to be multiplexed. On 1.4 JVMs, only the following classes subclass [SelectableChannel](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html).

- [Socket channels](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SocketChannel.html)

- Pipe [source](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Pipe.SourceChannel.html) and [sink](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Pipe.SinkChannel.html) channels

Specifically, [FileChannel\'s](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/FileChannel.html) **do not subclass** [SelectableChannel](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html), and thus it is not possible to include files in non-blocking multiplex operations on Java platforms. If you attempt to carry out a select operation on a file in jython, you will get a **[TypeError](./TypeError.html)**, like so

    >>> from select import select
    >>> import os
    >>> fp = os.open("test.txt")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: open() takes at least 2 arguments (1 given)
    >>> fp = os.open("test.txt", os.O_WRONLY|os.O_CREAT)
    >>> select([fp], [], [])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\jython\Lib\select.py", line 176, in native_select
        pobj.register(fd, POLLIN)
      File "C:\jython\Lib\select.py", line 95, in register
        channel = _getselectable(socket_object)
      File "C:\jython\Lib\select.py", line 95, in register
        channel = _getselectable(socket_object)
      File "C:\jython\Lib\select.py", line 56, in _getselectable
        raise TypeError("Object '%s' is not watchable" % selectable_object,
    TypeError: ("Object 'org.python.core.io.FileIO@c4afc4' is not watchable", 39)

Of the two channel types listed above, these modules only support socket channels. This is because it was necessary to rewrite all of the socket creation calls to return [SelectableChannels](./SelectableChannels.html). To do so for Pipes, which are used for communication with sub-processes, it would be necessary to rewrite the jython sub-process creation modules, i.e. popen, etc, to create [SelectableChannels](./SelectableChannels.html). Although it should be reasonably straightforward to implement this, I have no plans to do this work.

### Only sockets in non-blocking mode can be multiplexed 

On cpython, when a socket is passed to select.select or select.poll, it can either be in blocking or non-blocking mode.

However, [java will only permit multiplex operations on sockets that are in non-blocking mode](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html#register(java.nio.channels.Selector,%20int)). Because jython must respect this java restriction, any attempt in jython to pass a socket in blocking mode to either select.select or select.poll().register will fail with an exception.

To summarise

1.  You must set a socket in non-blocking mode before passing it to the select function or registering it with a poll object

2.  Any attempt to register a blocking socket for multiplex will raise a select.error exception, with an error code of errno.ESOCKISBLOCKING

3.  If a socket is currently registered with a select.poll object, an attempt to change it to blocking mode will give rise to the same exception.

4.  A socket can only be placed in blocking mode if it is **not** registered with a select.poll object.

This issue could be problematic if you want to use a cpython module which relies on select. Such cpython modules do not set their sockets in non-blocking mode before passing them to select.select. In order to support such cpython modules, the following workaround is available.

#### The cpython-compatible select function 

A special version of the select function is provided, to provide cpython compatible select functionality. This function works by

1.  Recording the blocking mode of all sockets that are passed to the function
2.  Setting non-blocking mode on all sockets
3.  Calling the normal jython select.select function (which requires non-blocking sockets)
4.  Restoring the previously-saved blocking mode for all sockets
5.  Returning the results of the wrapped select function

This function should only be used when you are working with code that has been written for cpython select, i.e. when the code is passing blocking-sockets to the select function.

#### How to enable cpython compatible select processing 

Here is a code sample which shows how to use the cpython-compatible select function as a replacement for the standard jython select function

    from select import cpython_compatible_select as select

    # Make use of the select function here

#### WARNING! 

1.  If using the cpython_compatible_select function, you must be aware that the function will modify the blocking mode of your sockets for the duration of the call. If you are carrying out socket operations on that socket in another thread, then those socket operations may fail or raise exceptions.

2.  This function will still not cover all possible uses of select.select by cpython modules. If a cpython module tries to multiplex the **sys.stdin** or **sys.stdout** streams, then registration of the channels will fail, because the InputStream and OutputStream representing sys.stdin and sys.stdout are **not** SelectableChannels.

## Known Issues 

### Receiving urgent data can cause select to lie (Windows implementation) 

Bug 1773955 describes the scenario. It is caused by a bug in the Sun Java implementation and there is no known Jython fix. A partial workaround is to call setOOBInline(True) on the jsocket within the Jython socket. This will cause the urgent data to be merged into the regular stream and will keep from confusing select() however you will have to ignore the urgent data at the application level.

**Addendum**: Support for socket options has been checked into the repo at [revision 4494](http://fisheye3.atlassian.com/changelog/jython/?cs=4494). See [NewSocketModule](NewSocketModule) for more details on the options available.

With the new support, you don\'t need to call the java API on the underlying socket; you can set the OOBINLINE flag using python syntax, like this

    mysock.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)

But there is still no workaround for the lack of support for TCP Urgent Data on java.
