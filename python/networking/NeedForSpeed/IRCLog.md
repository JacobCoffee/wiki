# NeedForSpeed/IRCLog

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    2006-05-22 05:10:40>  *** nfsbot has joined #nfs
    2006-05-22 05:10:40>  *** nfsbot has joined #nfs
    2006-05-22 05:11:08>  <jafo> Hello nfsbot.
    2006-05-22 05:12:00>  <jafo> Ok, does anyone want the IRC logs on the web live as they are happening, or can I just wait until we're done and publish then?
    2006-05-22 05:13:41>  *** blais has joined #nfs
    2006-05-22 05:14:20>  <rjones> whatever :)
    2006-05-22 05:15:31>  *** dalke has joined #nfs
    2006-05-22 05:15:44>  <jafo> dalke: Hey there.
    2006-05-22 05:19:42>  <effbot> anyone here?
    2006-05-22 05:19:59>  <effbot> have everyone found anything to do, or ...
    2006-05-22 05:23:09>  <jafo> I'm just building my task list now.
    2006-05-22 05:26:33>  *** jbenedik has quit IRC
    2006-05-22 05:39:00>  *** jbenedik has joined #nfs
    2006-05-22 05:41:53>  *** ymmit has quit IRC
    2006-05-22 05:41:59>  <jafo> Is anyone working on trying to convert to 64-bit ints on 32-bit platforms and see how it impacts pybench?
    2006-05-22 05:45:35>  <jafo> holdenweb_: I still think we need to have a group discussion on the slow-down from 2.4 to 2.5 that you saw.
    2006-05-22 05:48:34>  *** blais has quit IRC
    2006-05-22 05:56:51>  *** holdenweb_ has quit IRC
    2006-05-22 06:03:40>  *** jbenedik_ has joined #nfs
    2006-05-22 06:06:36>  *** runarp has joined #nfs
    2006-05-22 06:07:00>  *** kristjan_ has joined #nfs
    2006-05-22 06:07:13>  *** ymmit has joined #nfs
    2006-05-22 06:07:35>  *** sholden__ has joined #nfs
    2006-05-22 06:08:22>  *** etrepum_ has joined #nfs
    2006-05-22 06:09:45>  *** holdenweb_ has joined #NFS
    2006-05-22 06:11:54>  *** jbenedik_ has quit IRC
    2006-05-22 06:15:44>  *** gbrandl has quit IRC
    2006-05-22 06:15:49>  *** jbenedik has quit IRC
    2006-05-22 06:15:52>  *** rjones has quit IRC
    2006-05-22 06:15:52>  *** grunar has quit IRC
    2006-05-22 06:16:05>  *** etrepum has quit IRC
    2006-05-22 06:16:08>  *** gbrandl has joined #nfs
    2006-05-22 06:16:14>  *** sholden_ has quit IRC
    2006-05-22 06:16:18>  *** sholden has quit IRC
    2006-05-22 06:16:22>  *** dalke has quit IRC
    2006-05-22 06:16:39>  *** kristjan has quit IRC
    2006-05-22 06:16:47>  *** sholden has joined #nfs
    2006-05-22 06:20:17>  *** effbot has quit IRC
    2006-05-22 06:21:32>  *** uncletimmy has joined #nfs
    2006-05-22 06:21:43>  *** effbot has joined #nfs
    2006-05-22 06:21:56>  <effbot> I've posted my slowdown results here:
    2006-05-22 06:21:57>  <effbot> http://wiki.python.org/moin/NeedForSpeed/Goals/Slowdown#preview
    2006-05-22 06:22:26>  <effbot> The big ones seem to be import and try/except.
    2006-05-22 06:22:28>  <jafo> effbot: I'm just running tests now.
    2006-05-22 06:25:17>  *** jack_diederich has joined #nfs
    2006-05-22 06:27:08>  <holdenweb_> anyone using svn tortoise can show me how to set up authentication?
    2006-05-22 06:32:15>  *** ymmit has quit IRC
    2006-05-22 06:40:30>  *** etrepum has joined #nfs
    2006-05-22 06:40:52>  *** gbr_ has joined #nfs
    2006-05-22 06:41:25>  *** kristjan has joined #nfs
    2006-05-22 06:42:10>  *** holdenweb has joined #NFS
    2006-05-22 06:45:36>  *** runarp has quit IRC
    2006-05-22 06:55:56>  *** uncletimmy has quit IRC
    2006-05-22 06:58:36>  *** jack_diederich has quit IRC
    2006-05-22 06:58:39>  *** etrepum_ has quit IRC
    2006-05-22 06:58:43>  *** sholden_ has joined #nfs
    2006-05-22 06:58:58>  *** sholden__ has quit IRC
    2006-05-22 06:58:58>  *** jack_diederich has joined #nfs
    2006-05-22 06:59:00>  *** sholden has quit IRC
    2006-05-22 06:59:11>  *** kristjan_ has quit IRC
    2006-05-22 06:59:20>  *** sholden has joined #nfs
    2006-05-22 06:59:42>  *** effbot has quit IRC
    2006-05-22 07:00:24>  *** gbrandl has quit IRC
    2006-05-22 07:01:36>  *** holdenweb_ has quit IRC
    2006-05-22 07:39:38>  *** effbot has joined #nfs
    2006-05-22 07:44:50>  *** grunar has joined #nfs
    2006-05-22 07:56:08>  *** runarp has joined #nfs
    2006-05-22 08:00:10>  *** rxe has joined #nfs
    2006-05-22 08:01:14>  <effbot> I have gobby running on 192.168.0.103 port 6522 if anyone wants to try.
    2006-05-22 08:11:05>  <holdenweb> effbot: gobby 0.3 or 0.4?
    2006-05-22 08:14:54>  *** grunar has quit IRC
    2006-05-22 08:20:08>  <effbot> gobby 0.4
    2006-05-22 08:36:52>  <holdenweb> so i discovered when I ran 0.3 :_)
    2006-05-22 08:43:48>  *** kristjan_ has joined #nfs
    2006-05-22 08:47:06>  *** ymmit has joined #nfs
    2006-05-22 08:51:15>  <holdenweb> effbot: how come I get an "overhead" column on my pybench output where you have a "diff *)" column?
    2006-05-22 09:02:49>  *** kristjan has quit IRC
    2006-05-22 09:13:36>  *** jbenedik has joined #nfs
    2006-05-22 09:17:59>  *** blais has joined #nfs
    2006-05-22 09:19:35>  *** ymmit has quit IRC
    2006-05-22 09:23:37>  *** ymmit has joined #nfs
    2006-05-22 09:24:11>  <jafo> I'm going to take a look at switching ints to 64 bits on 32-bit platforms.
    2006-05-22 09:42:40>  *** blais has quit IRC
    2006-05-22 09:42:51>  *** blais has joined #nfs
    2006-05-22 09:46:49>  *** b-_-d has joined #nfs
    2006-05-22 09:47:04>  <b-_-d> anyone use nfs? how do i get locking?
    2006-05-22 09:54:15>  <jafo> b-_-d: See the channel topic.
    2006-05-22 09:58:57>  *** kristjan_ has quit IRC
    2006-05-22 10:06:51>  <jafo> How does Python decide to do the up-convert from int to long?  I've converted all the types, I think, to "long long", but 1<<32 is going to L.
    2006-05-22 10:12:02>  *** doctorwells has joined #nfs
    2006-05-22 10:13:09>  <ymmit> jafo:  for 1<<32, see intobject.c's int_lshift.
    2006-05-22 10:13:20>  <jafo> Thanks.
    2006-05-22 10:13:57>  <ymmit> You're probably see that the platform LONG_BIT is #define'd as 32, so left shift figures it _needs_ a Python long.
    2006-05-22 10:14:35>  <b-_-d> channel name is deciving 
    2006-05-22 10:14:59>  <b-_-d> #Python would work
    2006-05-22 10:15:10>  *** b-_-d has left #nfs
    2006-05-22 10:15:11>  <jafo> b-_-d: No, it wouldn't.
    2006-05-22 10:30:48>  <jbenedik> doctorwells: you at keys?
    2006-05-22 10:31:57>  <doctorwells> yup
    2006-05-22 10:34:21>  *** uncletimmy has joined #nfs
    2006-05-22 10:39:37>  *** ymmit has quit IRC
    2006-05-22 10:41:05>  <jbenedik> i'm working on psyco dicts right now
    2006-05-22 10:44:14>  <doctorwells> cool, what part?  virtualized keys(), values() and items() ?
    2006-05-22 10:44:37>  <jbenedik> we'll see how much - ideally yes
    2006-05-22 10:44:40>  <jbenedik> faster iteration
    2006-05-22 10:44:44>  <jbenedik> virtualized access
    2006-05-22 10:46:11>  <jafo> Ok, this is extremely weird.  I converted the int stuff to long long on 32-bit platforms, and I'm getting:
    2006-05-22 10:46:13>  <jafo> Average round time:    4081.70 ms             -100.00%
    2006-05-22 10:46:26>  <jafo> The -100.00% is consistent.
    2006-05-22 10:47:02>  <doctorwells> sounds a lot faster
    2006-05-22 10:48:08>  <jafo> But the original is: Average round time:    4037.00 ms
    2006-05-22 10:48:25>  <jafo> Oh, wait, obviously there's a problem in my conversion to long long...
    2006-05-22 10:48:34>  <rxe> doctorwells: joining the sprint remotely?  :-)
    2006-05-22 10:48:44>  <doctorwells> sumthin' like that
    2006-05-22 10:50:19>  <jafo> So, it looks like on pybench the difference is 1.11% slow-down by going to long long.
    2006-05-22 10:51:03>  <jafo> So, do we want to suck it up, or give it a pass?  Anyone?
    2006-05-22 10:51:26>  <jbenedik> What kind of speedup do you get when you overflow?  any?
    2006-05-22 10:51:40>  <doctorwells> does pybench do anything with ints in the 32 - 64 bit range?
    2006-05-22 10:51:53>  <jafo> Don't know and don't know.
    2006-05-22 10:55:17>  <jafo> Looks like 1<<35 is around 34% faster.
    2006-05-22 11:13:24>  *** runarp has quit IRC
    2006-05-22 11:13:24>  *** jafo has quit IRC
    2006-05-22 11:13:30>  *** runarp has joined #nfs
    2006-05-22 11:13:30>  *** jafo has joined #nfs
    2006-05-22 11:37:12>  *** kristjan has joined #nfs
    2006-05-22 11:49:22>  <kristjan> CS:EIP Symbol + Offset Thread ID       Samples Total % CPU0    32 bit  64 bit
    2006-05-22 11:49:22>  <kristjan> 0x1e00f070     PyEval_EvalFrameEx              12839   49.94   12839   12839   0
    2006-05-22 11:49:22>  <kristjan> 0x1e01aa80     lookdict_string         738     2.87    738     738     0
    2006-05-22 11:49:22>  <kristjan> 0x1e00ea20     call_function           526     2.05    526     526     0
    2006-05-22 11:49:22>  <kristjan> 0x1e033560     rangeiter_next          338     1.31    338     338     0
    2006-05-22 11:49:24>  <kristjan> 0x1e0135d0     tupledealloc            333     1.3     333     333     0
    2006-05-22 11:49:26>  <kristjan> 0x1e0120d0     PyObject_GenericGetAttr         269     1.05    269     269     0
    2006-05-22 11:49:30>  <kristjan> 0x1e015320     list_dealloc            259     1.01    259     259     0
    2006-05-22 11:49:40>  <kristjan> profile data, functions over one %
    2006-05-22 11:59:19>  *** jbenedik has quit IRC
    2006-05-22 12:09:53>  <runarp> is anyone else looking at the longpatch?
    2006-05-22 12:17:31>  *** jbenedik has joined #nfs
    2006-05-22 12:28:30>  *** holdenweb has left #nfs
    2006-05-22 12:31:12>  <jafo> Room 332 now has wireless in it, essid=tummy, feel free to use it if you can get it.
    2006-05-22 12:37:30>  *** Klipsch has joined #nfs
    2006-05-22 12:41:34>  *** uncletimmy has left #nfs
    2006-05-22 12:41:55>  *** effbot has quit IRC
    2006-05-22 12:44:53>  *** kristjan has quit IRC
    2006-05-22 12:49:10>  <Klipsch> is there a way to mount and ignore all hidden files like .hidden
    2006-05-22 12:56:15>  *** sholden_ has quit IRC
    2006-05-22 12:56:18>  *** sholden has quit IRC
    2006-05-22 12:57:29>  *** etrepum has quit IRC
    2006-05-22 13:13:31>  <gbrandl> Klipsch: this is not a Network File System channel
    2006-05-22 13:17:43>  <Klipsch> oh
    2006-05-22 13:18:06>  *** Klipsch has left #nfs
    2006-05-22 13:22:24>  *** jack_diederich has quit IRC
    2006-05-22 13:23:26>  *** jbenedik has quit IRC
    2006-05-22 13:27:05>  *** rxe has quit IRC
    2006-05-22 13:38:04>  *** blais has quit IRC
    2006-05-22 13:38:46>  *** gbrandl has quit IRC
    2006-05-22 13:43:34>  *** runarp has quit IRC
    2006-05-22 15:54:39>  *** grunar has joined #nfs
    2006-05-22 16:15:16>  *** doctorwells has left #nfs
    2006-05-22 16:22:17>  *** blais has joined #nfs
    2006-05-22 16:55:05>  *** blais has quit IRC
    2006-05-22 17:00:52>  <jafo> Hey folks.  Anyone up for hacking in the lobby for a bit more?
    2006-05-22 17:16:13>  *** efm has joined #nfs
    2006-05-22 17:16:34>  <efm> SteveH: don't forget the Big Visible Charts for measuring progress
    2006-05-22 17:29:10>  <jafo> holdenweb is absent until around 3am your time.
    2006-05-22 17:29:19>  <jafo> Sounds like people would like to say hi though.
    2006-05-22 17:29:34>  <jafo> And, of course, nfsbot is logging this.
    2006-05-22 17:30:17>  <jafo> So far, 'we've had fewer people asking about network filsystems than I expected.
    2006-05-22 17:35:42>  <efm> hi All sprinters from warm and sunny Colorado!
    2006-05-22 18:05:57>  *** efm has quit IRC
    2006-05-22 18:32:28>  *** runarp has joined #nfs
    2006-05-22 18:32:40>  *** grunar has quit IRC
    2006-05-22 18:44:03>  *** grunar has joined #nfs
    2006-05-22 18:55:18>  *** efm has joined #nfs
    2006-05-22 18:57:45>  *** runarp has quit IRC
    2006-05-22 19:08:37>  *** grunar has quit IRC
    2006-05-22 19:11:58>  *** grunar has joined #nfs
    2006-05-22 20:23:54>  *** grunar has quit IRC
    2006-05-23 02:07:12>  *** grunar has joined #nfs
    2006-05-23 02:13:03>  *** jack_diederich has joined #nfs
    2006-05-23 02:37:23>  *** grunar has quit IRC
    2006-05-23 02:59:07>  *** TomasOsmena has joined #nfs
    2006-05-23 02:59:12>  <TomasOsmena> hi all anybody here know what is the tool to print the ip of connected nfs client from our nfs server?
    2006-05-23 02:59:24>  <jafo> TomasOsmena: See the topic.
    2006-05-23 03:00:20>  <TomasOsmena> sorry
    2006-05-23 03:00:24>  <jafo> No problem.
    2006-05-23 03:00:56>  <TomasOsmena> any help which channel my question belongs to?
    2006-05-23 03:02:26>  <jafo> Don't know, sorry.
    2006-05-23 03:05:51>  *** grunar has joined #nfs
    2006-05-23 03:06:23>  *** ymmit has joined #nfs
    2006-05-23 03:08:49>  *** TomasOsmena has left #nfs
    2006-05-23 03:10:12>  <jack_diederich> my jotlive username is "jackdied"
    2006-05-23 03:10:18>  *** holdenweb has joined #NFS
    2006-05-23 03:11:09>  *** gbrandl has joined #nfs
    2006-05-23 03:13:25>  *** effbot has joined #nfs
    2006-05-23 03:20:49>  *** jbenedik has joined #nfs
    2006-05-23 03:21:21>  *** ccpRichard2 has joined #nfs
    2006-05-23 03:22:30>  *** etrepum has joined #nfs
    2006-05-23 03:23:04>  *** blais has joined #nfs
    2006-05-23 03:23:32>  <etrepum> jafo: jotlive user name is etrepum
    2006-05-23 03:23:48>  <jafo> done
    2006-05-23 03:25:31>  <grunar> my jotlive is  runar
    2006-05-23 03:26:08>  <jafo> Done.
    2006-05-23 03:29:38>  <gbrandl> jafo: my name's gbrandl
    2006-05-23 03:30:02>  <jafo> Done.
    2006-05-23 03:32:51>  <ccpRichard2> jafo: mine is richardtew
    2006-05-23 03:33:10>  <jafo> Done.
    2006-05-23 03:44:30>  *** ymmit has quit IRC
    2006-05-23 03:45:19>  <etrepum> the nnorwitz "speed up function calls" patch is http://python.org/sf/1479611
    2006-05-23 03:52:31>  <blais> jafo: add me "blais"
    2006-05-23 03:52:34>  <blais> to that jot thing
    2006-05-23 03:52:36>  <blais> ja
    2006-05-23 03:52:48>  <jbenedik> jafo: invite mrjbq7
    2006-05-23 03:54:32>  *** rxe has joined #nfs
    2006-05-23 04:18:50>  <etrepum> What's the PyMember type for Py_ssize_t? Do we need to add one?
    2006-05-23 04:19:04>  <etrepum> T_LONGLONG?
    2006-05-23 04:20:59>  <gbrandl> etrepum: no, there isn't one yet. I actually wrote to python-dev about it, and Martin (vL) said he'd like to see a use case ;)
    2006-05-23 04:22:27>  <etrepum> well my use case is that I have fields that count things, and it seems like it would make sense to use the appropriate Python type for counting things
    2006-05-23 04:22:54>  <etrepum> I guess I'll just use int
    2006-05-23 04:22:56>  <gbrandl> I'd say just add it in your branch
    2006-05-23 04:23:13>  <etrepum> I'm developing this as an extension module, not a branch of Python
    2006-05-23 04:23:37>  <etrepum> I don't need to recompile Python to add an API to an extension :)
    2006-05-23 04:25:58>  *** ccpRichard2 has quit IRC
    2006-05-23 04:31:04>  <gbrandl> etrepum: FWIW, the thread is at http://mail.python.org/pipermail/python-dev/2006-May/064996.html
    2006-05-23 04:38:38>  *** runarp has joined #nfs
    2006-05-23 04:38:38>  *** grunar has quit IRC
    2006-05-23 04:39:46>  * jafo stabs jotlive in the face over the Internet.
    2006-05-23 04:44:50>  *** effbot has quit IRC
    2006-05-23 04:46:35>  <etrepum> http://docs.python.org/api/api.html
    2006-05-23 04:57:54>  *** ccpRichard2 has joined #nfs
    2006-05-23 04:58:49>  <jafo> runarp: So, on the string offset idea.  Adding string offsets to a function seems like the camels nose under the tent, if you know the expression.  It seems like there are a lot of places it would be nice to have that.  I wonder if it might be possible to do something like have a string sub-class that is a StringOffset(s, start, length) sort of thing, that would be light a light weight wrapper on top of string, which some functions would be specialized to 
    2006-05-23 04:58:49>  <jafo> handle.
    2006-05-23 04:59:52>  <jafo> In the case of functions that don't understand it, the class could look like a regular string and provide a slice.  For functions that do understand it, they could bypass the slicing.
    2006-05-23 04:59:56>  <jafo> Thoughts?
    2006-05-23 05:16:44>  *** ymmit has joined #nfs
    2006-05-23 05:32:16>  <ccpRichard2> jafo: Can you add KristjanJonsson please :)
    2006-05-23 05:32:47>  <jafo> Done.
    2006-05-23 05:34:05>  *** kristjan has joined #nfs
    2006-05-23 05:46:38>  <jafo> runarp: It sounds like the bute buffer stuff we're talking about out here would prevent the issues I was trying to solve above.  Martin has more information.
    2006-05-23 06:50:26>  *** jbenedik has quit IRC
    2006-05-23 06:55:21>  *** blais has quit IRC
    2006-05-23 06:56:37>  *** ymmit has quit IRC
    2006-05-23 06:57:11>  *** gbrandl has quit IRC
    2006-05-23 06:58:20>  *** kristjan_ has joined #nfs
    2006-05-23 06:58:52>  *** holdenweb_ has joined #NFS
    2006-05-23 06:59:03>  *** jbenedik has joined #nfs
    2006-05-23 07:01:17>  *** etrepum_ has joined #nfs
    2006-05-23 07:03:56>  *** grunar has joined #nfs
    2006-05-23 07:09:36>  *** thingie56 has joined #nfs
    2006-05-23 07:14:42>  *** runarp has quit IRC
    2006-05-23 07:14:58>  *** jack_diederich has quit IRC
    2006-05-23 07:15:05>  *** rxe has quit IRC
    2006-05-23 07:15:27>  *** ccpRichard2 has quit IRC
    2006-05-23 07:15:32>  *** holdenweb has quit IRC
    2006-05-23 07:15:33>  *** etrepum has quit IRC
    2006-05-23 07:16:51>  *** etrepum has joined #nfs
    2006-05-23 07:16:58>  *** ccpRichard2 has joined #nfs
    2006-05-23 07:17:09>  *** holdenweb has joined #NFS
    2006-05-23 07:20:16>  *** kristjan has quit IRC
    2006-05-23 07:20:21>  *** runarp has joined #nfs
    2006-05-23 07:23:39>  *** jbenedik_ has joined #nfs
    2006-05-23 07:33:20>  *** kristjan_ has quit IRC
    2006-05-23 07:34:08>  *** jbenedik has quit IRC
    2006-05-23 07:34:11>  *** holdenweb_ has quit IRC
    2006-05-23 07:34:15>  *** thingie56 has quit IRC
    2006-05-23 07:34:40>  *** grunar has quit IRC
    2006-05-23 07:36:19>  *** jack_diederich has joined #nfs
    2006-05-23 07:42:10>  *** grunar has joined #nfs
    2006-05-23 07:42:53>  *** etrepum_ has quit IRC
    2006-05-23 07:43:41>  *** holdenweb_ has joined #NFS
    2006-05-23 07:46:05>  *** gbrandl has joined #nfs
    2006-05-23 07:51:27>  *** ccpRichard2 has quit IRC
    2006-05-23 07:53:13>  *** holdenweb has quit IRC
    2006-05-23 07:56:34>  *** blais has joined #nfs
    2006-05-23 07:59:51>  *** holdenweb_ has quit IRC
    2006-05-23 08:01:01>  *** runarp has quit IRC
    2006-05-23 08:23:02>  *** ymmit has joined #nfs
    2006-05-23 08:24:05>  *** jbenedik_ has quit IRC
    2006-05-23 08:31:07>  *** jbenedik has joined #nfs
    2006-05-23 08:41:52>  *** amk_ has joined #nfs
    2006-05-23 08:43:28>  *** ccpRichard2 has joined #nfs
    2006-05-23 08:54:16>  *** synic has joined #nfs
    2006-05-23 08:54:19>  *** synic has left #nfs
    2006-05-23 09:16:06>  *** kristjan has joined #nfs
    2006-05-23 09:19:20>  *** ymmit has quit IRC
    2006-05-23 09:23:35>  *** ymmit has joined #nfs
    2006-05-23 09:35:39>  *** amk_ has quit IRC
    2006-05-23 09:45:36>  <kristjan> on windows, you want GetProcessTimes() or GetThreadTimes()
    2006-05-23 09:46:07>  <kristjan> http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dllproc/base/getprocesstimes.asp
    2006-05-23 09:48:29>  *** jbenedik has quit IRC
    2006-05-23 09:49:56>  <kristjan> works on NT
    2006-05-23 10:09:21>  *** unkatimmy has joined #nfs
    2006-05-23 10:14:47>  *** ymmit has quit IRC
    2006-05-23 10:27:59>  <blais> some pics here:
    2006-05-23 10:28:00>  <blais> http://furius.ca/tmp/nfs1/html/dirindex.html
    2006-05-23 10:44:23>  *** grunar has quit IRC
    2006-05-23 10:47:59>  <etrepum> http://python.org/sf/1493701 - struct module performance enhancements
    2006-05-23 10:52:33>  *** bcannon has joined #nfs
    2006-05-23 10:52:54>  <bcannon> Morning folks.
    2006-05-23 10:53:40>  <bcannon> Actually, I just realized it's 3:00 over there so I bet no one is even logged in.  =)
    2006-05-23 10:54:44>  <bcannon> OK, when you guys start to sprint again, shoot me an email and I will try to pop back on to answer questions about possibilities as to why the addition of new-style classes for exceptions could have added a performance hit.
    2006-05-23 10:55:14>  <bcannon> This is Brett in case people don't recognize the IRC nick.  =)
    2006-05-23 10:55:17>  *** bcannon has quit IRC
    2006-05-23 11:02:12>  <blais> hey brett, wazzup
    2006-05-23 11:07:22>  <kristjan> sprinting is well and truly underway
    2006-05-23 11:07:46>  *** bcannon has joined #nfs
    2006-05-23 11:07:51>  <jafo> Hey there.
    2006-05-23 11:08:11>  <bcannon> I just realized my math was off because I subtracted instead of added 7 hours.  =)
    2006-05-23 11:08:15>  <jafo> Still kind of scratching our heads as to where the performance change is.
    2006-05-23 11:08:32>  <jafo> guin:msglog$ TZ=GMT date
    2006-05-23 11:08:32>  <jafo> Tue May 23 17:08:27 GMT 2006
    2006-05-23 11:08:50>  <jafo> I don't do math when I check the time here.
    2006-05-23 11:08:54>  <bcannon> So a possibility is the PyException_* macros that are used to verify that an object is acceptable as a macro.
    2006-05-23 11:09:40>  <bcannon> Those are at several key points in the code path and they do several checks so there are more 'if' checks and have more memory accesses.
    2006-05-23 11:09:58>  <bcannon> I don't think object creation is done in a stupid way so I don't think it is from object creation, but it is a possibility.
    2006-05-23 11:10:39>  <bcannon> Otherwise I can't think of any specific points where the differences were huge.
    2006-05-23 11:10:41>  <jafo> Ok, a few things.
    2006-05-23 11:10:56>  <bcannon> Unless checking for string exceptions for possible warnings is just ridiculously costly.
    2006-05-23 11:11:02>  <jafo> We seem to still be seeing performance issues, even if we've already created the object.
    2006-05-23 11:11:10>  <bcannon> OK.
    2006-05-23 11:11:24>  <jafo> We're looking at the macros now, and it seems like they would be getting called for both new and old style objects.
    2006-05-23 11:11:47>  <bcannon> So this is a performance hit in 2.5 for both new-style and classi?
    2006-05-23 11:11:54>  <bcannon> I thought this was a 2.4 -> 2.5 issue.
    2006-05-23 11:12:10>  <jafo> Kind of.
    2006-05-23 11:12:28>  <jafo> In 2.5, old style classes if thrown as an exception show no performance drop from 2.4.3.
    2006-05-23 11:12:34>  <bcannon> OK
    2006-05-23 11:12:43>  <jafo> New style classes show like a 100% drop.
    2006-05-23 11:13:46>  <bcannon> Unfortunately I am at work and just discovered svn is not installed so I can't check the code out and look.
    2006-05-23 11:14:03>  <jafo> Ok.
    2006-05-23 11:14:15>  <jafo> There is, of course: http://svn.python.org/view?rev=42711&view=rev
    2006-05-23 11:14:31>  <bcannon> Going from memory, the differences in terms of code path is that obviously that new-style exceptions are new-style classes (but you mostly showed that is not needed).
    2006-05-23 11:14:33>  <jafo> We can dig into the macros and see if it seems that that is it.
    2006-05-23 11:15:12>  <bcannon> I remember there is a place where divergence happens in the code path based on type; give me a minute to try to find it.
    2006-05-23 11:15:30>  <jafo> Based on old or new style classes you mean?
    2006-05-23 11:15:33>  <jafo> We haven't seen that.
    2006-05-23 11:16:09>  <bcannon> Yeah, I think there is one spot; but my memory could be foggy since I had spent the previous day at the sprints fixing a bitch of a bug to track down and so my brain was frazzled.
    2006-05-23 11:16:24>  <jafo> Ah.
    2006-05-23 11:20:13>  <jafo> Thanks for popping in.  I'm trying dikeing out some of the macros for our limited tests and seeing if that has an impact.
    2006-05-23 11:20:34>  <bcannon> OK, what I was remembering is that block change in errors.c
    2006-05-23 11:20:52>  <jafo> haven't looked in errors.c
    2006-05-23 11:24:09>  <bcannon> When benchmarking, is it purely in raising an exception, or are you also viewing the exception in any way to trigger the __repr__ or __unicode__ methods?
    2006-05-23 11:24:28>  <jafo> Purely raising the exception.
    2006-05-23 11:24:30>  <bcannon> OK
    2006-05-23 11:24:37>  <jafo> try: raise ValueError
    2006-05-23 11:24:40>  <jafo> except: pass
    2006-05-23 11:25:26>  <bcannon> And no difference if you ``raise ValueError()`` or catching the specific exception?
    2006-05-23 11:25:53>  <jafo> Have only tried "raise ValueError, 5".
    2006-05-23 11:26:05>  <jafo> I can try the except ValueError in a few.
    2006-05-23 11:26:09>  *** grunar has joined #nfs
    2006-05-23 11:26:39>  <bcannon> Actually, try it so that the object creation is outside of the timing code and raise the instance.
    2006-05-23 11:26:43>  <jafo> Ok, if I change PyExceptionClass_Check to "1", pybench doesn't show any impact.
    2006-05-23 11:26:55>  <bcannon> OK
    2006-05-23 11:28:38>  <jafo> Trying outside of the timing code.
    2006-05-23 11:28:50>  *** jbenedik has joined #nfs
    2006-05-23 11:30:09>  <jafo> It's looking like by moving it out of the loop it's faster than 2.4.3 by an amazing amount.
    2006-05-23 11:30:18>  <jafo> 50%.
    2006-05-23 11:30:19>  <bcannon> =)
    2006-05-23 11:30:29>  <jafo> I guess it's not that amazing, but yeah, faster.
    2006-05-23 11:30:31>  <bcannon> So it is new-style instantiation.
    2006-05-23 11:30:46>  <jafo> Wait a moment.
    2006-05-23 11:30:46>  <bcannon> Or at least a good chunk of it.
    2006-05-23 11:30:49>  <bcannon> OK
    2006-05-23 11:31:01>  <jafo> I need to re-run the baseline.
    2006-05-23 11:31:07>  <bcannon> ok
    2006-05-23 11:32:55>  <jafo> Ok.  With the exception outside the timing loop, it's the same speed on 2.4.3 and 2.5a2.
    2006-05-23 11:33:02>  <jafo> So, yeah, instance creation.
    2006-05-23 11:33:05>  <bcannon> Figures.
    2006-05-23 11:33:14>  <jafo> I guess there's nothing that can be done there.
    2006-05-23 11:33:20>  <bcannon> =)
    2006-05-23 11:33:31>  <bcannon> Can always work your voodoo on instance creation.  =)
    2006-05-23 11:34:01>  <jafo> What makes you think I have voodoo?
    2006-05-23 11:34:13>  <bcannon> Or perhaps there is a better way to define the class than how it is currently.
    2006-05-23 11:34:41>  <jafo> I don't honestly know.
    2006-05-23 11:35:15>  <bcannon> Could possibly be better to define the class all in C with a proper struct instead of using a PyMethodDef for the magic methods.
    2006-05-23 11:35:26>  <bcannon> That should help take out some overhead.
    2006-05-23 11:35:52>  *** ccpRichard2 has quit IRC
    2006-05-23 11:35:54>  <bcannon> Assuming that doesn't break code somewhere for some odd reason.
    2006-05-23 11:36:24>  <bcannon> But basically that is the best I can think of.  Might not be bad in terms of cleanup of the code anyway.
    2006-05-23 11:36:38>  <bcannon> Planning to do that at some point.
    2006-05-23 11:36:53>  <bcannon> But it might be a few years.  =)
    2006-05-23 11:37:08>  <jafo> Are you talking about for the BaseException class?
    2006-05-23 11:37:13>  <bcannon> Yep.
    2006-05-23 11:37:32>  <jafo> Ok, I can try that.
    2006-05-23 11:37:38>  <bcannon> OK, cool.
    2006-05-23 11:37:44>  <jafo> Thanks for the help.
    2006-05-23 11:37:51>  <bcannon> No problem.  Glad I could help.
    2006-05-23 11:38:06>  <bcannon> Everything going well over there?
    2006-05-23 11:44:27>  <blais> (c-add-style
    2006-05-23 11:44:27>  <blais>  "python-new"
    2006-05-23 11:44:27>  <blais>  '((indent-tabs-mode . nil)
    2006-05-23 11:44:27>  <blais>   (fill-column      . 78)
    2006-05-23 11:44:27>  <blais>   (c-basic-offset   . 4)
    2006-05-23 11:44:28>  <blais>   (c-offsets-alist  . ((substatement-open . 0)
    2006-05-23 11:44:30>  <blais>                        (inextern-lang . 0)
    2006-05-23 11:44:32>  <blais>                        (arglist-intro . +)
    2006-05-23 11:44:34>  <blais>                        (knr-argdecl-intro . +)))
    2006-05-23 11:44:36>  <blais>   (c-hanging-braces-alist . ((brace-list-open)
    2006-05-23 11:44:38>  <blais>                              (brace-list-intro)
    2006-05-23 11:44:42>  <blais>                              (brace-list-close)
    2006-05-23 11:44:44>  <blais>                              (brace-entry-open)
    2006-05-23 11:44:46>  <blais>                              (substatement-open after)
    2006-05-23 11:44:48>  <blais>                              (block-close . c-snug-do-while)))
    2006-05-23 11:44:50>  <blais>   (c-block-comment-prefix . ""))
    2006-05-23 11:44:52>  <blais>  )
    2006-05-23 11:44:54>  <blais> (add-to-list 'c-default-style '(c-mode . "python-new"))
    2006-05-23 11:45:29>  <bcannon> And then Martin scares me away with Emacs Lisp.  =)
    2006-05-23 11:45:43>  <bcannon> Well all, continue the great work.
    2006-05-23 11:45:54>  *** bcannon has quit IRC
    2006-05-23 11:47:42>  *** unkatimmy has quit IRC
    2006-05-23 12:30:51>  *** kristjan has quit IRC
    2006-05-23 12:32:53>  *** grunar has quit IRC
    2006-05-23 12:46:24>  *** jbenedik has quit IRC
    2006-05-23 13:02:58>  *** stakkars has joined #nfs
    2006-05-23 13:03:33>  <stakkars> hola
    2006-05-23 13:03:41>  <jafo> j0
    2006-05-23 13:04:33>  <jafo> WTF are you?
    2006-05-23 13:05:23>  <stakkars> I'm downstairs, locked in a somewhat hairy problem.
    2006-05-23 13:05:32>  <stakkars> this way should be faster to get out
    2006-05-23 13:05:56>  <jafo> Mmm.  Hair.
    2006-05-23 13:05:58>  <stakkars> amazing that I have IRC, here
    2006-05-23 13:07:00>  <stakkars> WTF == Who or where?  "who" == 'chris'
    2006-05-23 13:07:11>  <jafo> What The F**k
    2006-05-23 13:07:43>  <stakkars> Mr. Stackless, of course
    2006-05-23 13:07:59>  <jafo> Sorry, I meant Where.
    2006-05-23 13:08:02>  <jafo> Got distracted.
    2006-05-23 13:08:09>  <stakkars> oki :-)
    2006-05-23 13:08:23>  <jafo> [13:02:58] --> stakkars (n=tismer@213.213.135.203) has joined #nfs
    2006-05-23 13:08:26>  <jafo> I got the whom.
    2006-05-23 13:08:55>  <stakkars> if somebody is asking, I will show up, of course
    2006-05-23 13:09:21>  <jafo> I was just wondering because I didn't think I saw you up here, and you were online...
    2006-05-23 13:09:44>  <stakkars> amazing, that tiny HUB
    2006-05-23 13:11:06>  <jafo> You are associated with the NFS APs, not the lobby one?
    2006-05-23 13:12:26>  <stakkars> no idea. I'm connected to needforspeed
    2006-05-23 13:13:14>  * stakkars going back into deep thought mode
    2006-05-23 13:16:57>  *** jack_diederich has left #nfs
    2006-05-23 13:32:59>  *** grunar has joined #nfs
    2006-05-23 13:51:55>  *** etrepum has quit IRC
    2006-05-23 14:02:27>  *** grunar has quit IRC
    2006-05-23 14:10:05>  *** stakkars has quit IRC
    2006-05-23 14:13:50>  *** blais has quit IRC
    2006-05-23 14:18:20>  *** gbrandl has quit IRC
    2006-05-23 14:42:20>  *** gecjr has joined #nfs
    2006-05-23 14:42:29>  *** gecjr has left #nfs
    2006-05-23 16:45:34>  *** efm has quit IRC
    2006-05-23 17:53:09>  *** efm has joined #nfs
    2006-05-23 19:20:42>  *** efm has quit IRC
    2006-05-23 20:14:47>  *** efm has joined #nfs
    2006-05-23 20:27:54>  *** Syron has joined #nfs
    2006-05-23 20:28:15>  <Syron> I know this isn't the network filesystems channel but do you know what channel that is?
    2006-05-23 20:31:59>  <efm> Syron: Finally, there is a public IRC channel #linux-nfs on the server irc.oftc.net, which may be used for discussing Linux NFS development, testing, and related topics.
    2006-05-23 20:35:54>  <Syron> thanks, the channel list was a bit long. :)
    2006-05-23 20:36:36>  *** Syron has left #nfs
    2006-05-23 21:44:01>  *** bthornton has joined #nfs
    2006-05-23 21:44:10>  *** bthornton has left #nfs
    2006-05-23 22:04:44>  *** efm has quit IRC
    2006-05-23 22:32:10>  *** efm has joined #nfs
    2006-05-24 02:20:17>  <jafo> j0 par-tay ppl.
    2006-05-24 03:12:38>  *** grunar has joined #nfs
    2006-05-24 03:16:48>  *** gbrandl has joined #nfs
    2006-05-24 03:19:02>  *** runarp has joined #nfs
    2006-05-24 03:27:21>  *** etrepum has joined #nfs
    2006-05-24 03:29:51>  *** ccpRichard2 has joined #nfs
    2006-05-24 03:37:50>  *** grunar has quit IRC
    2006-05-24 03:53:08>  *** blais has joined #nfs
    2006-05-24 04:02:14>  *** stakkars has joined #nfs
    2006-05-24 04:22:53>  *** jbenedik has joined #nfs
    2006-05-24 04:23:45>  *** runarp has quit IRC
    2006-05-24 04:25:49>  *** etrepum has quit IRC
    2006-05-24 04:37:58>  *** mwh has joined #nfs
    2006-05-24 04:39:39>  <mwh> ok, so my recent mail to python-dev is wrong :)
    2006-05-24 04:40:07>  <jafo> mwh: If you were using Outlook you could send a retraction.  :-)
    2006-05-24 04:40:21>  <jafo> Like the hotel did to us when we were at PyCon...
    2006-05-24 04:40:47>  *** etrepum has joined #nfs
    2006-05-24 04:41:06>  <jafo> <Reply All> "Wait till those suckers see what we're going to charge them next year."  <Send>  "Oh, wait..."
    2006-05-24 04:41:25>  <mwh> oops
    2006-05-24 04:42:09>  <stakkars> mike, do you have the rights to create a codespead account for John?
    2006-05-24 04:42:27>  *** rxe has joined #nfs
    2006-05-24 04:42:29>  <mwh> yes
    2006-05-24 04:42:32>  *** jack_diederich has joined #nfs
    2006-05-24 04:42:41>  <stakkars> we would like to work on a psyco branch and need to share for debugging
    2006-05-24 04:42:50>  <stakkars> that would be great!
    2006-05-24 04:42:54>  <mwh> who is john?
    2006-05-24 04:43:09>  <stakkars> John Benediktsson from EWT LLC
    2006-05-24 04:43:19>  <mwh> ah, jbenedik ?
    2006-05-24 04:43:23>  <stakkars> jup
    2006-05-24 04:43:40>  <stakkars> alternatively I could use my account, but well
    2006-05-24 04:47:29>  *** jack_diederich has quit IRC
    2006-05-24 04:48:38>  *** jack_diederich has joined #nfs
    2006-05-24 04:52:29>  *** stakkars has quit IRC
    2006-05-24 04:53:32>  *** stakkars has joined #nfs
    2006-05-24 04:54:50>  <stakkars> thanks, Mike!
    2006-05-24 04:55:53>  *** blais has joined #nfs
    2006-05-24 04:56:17>  <blais> hey
    2006-05-24 04:56:18>  <blais> more pics
    2006-05-24 04:56:20>  <blais> http://furius.ca/tmp/nfs2/html/dirindex.html
    2006-05-24 04:56:49>  *** hpk has joined #nfs
    2006-05-24 04:57:23>  <jafo> I put up Steve's picture of unkatimmy from yesterday at http://www.tummy.com/journals/
    2006-05-24 04:57:36>  <jafo> Of course, more photos at jafo.ca
    2006-05-24 05:02:58>  <mwh> jafo: i'm not seeing anything like the slowdown you report with new-style exceptions
    2006-05-24 05:03:25>  <mwh> i'm seeing about 20%
    2006-05-24 05:04:01>  <mwh> and the time in all cases seems to be dominated by building the exception
    2006-05-24 05:04:51>  <jafo> Hrmm.
    2006-05-24 05:04:55>  <jafo> What platform?
    2006-05-24 05:04:59>  <mwh> os x
    2006-05-24 05:05:06>  <jafo> Sorry, we were also trying to figure out lunch plans.
    2006-05-24 05:05:12>  <mwh> fair enough
    2006-05-24 05:05:41>  <jafo> Are you using the pybench from trunk?
    2006-05-24 05:05:49>  <mwh> i'm using timeit
    2006-05-24 05:06:01>  <jafo> Hmm.  Can you get me your test?
    2006-05-24 05:06:24>  <mwh> http://pastebin.de/6937
    2006-05-24 05:06:37>  <mwh> then just
    2006-05-24 05:06:39>  <mwh> ./python.exe -m timeit -s 'import t' 't.main()'
    2006-05-24 05:07:57>  *** grunar has joined #nfs
    2006-05-24 05:08:18>  <jafo> zsh: no such file or directory: ./python.exe
    2006-05-24 05:08:44>  <mwh> it's freshly built from svn head
    2006-05-24 05:08:58>  <mwh> comparing vs python2.4
    2006-05-24 05:09:09>  <jafo> Nah, just giving you shit.
    2006-05-24 05:09:35>  <mwh> i generally assume a brain on behalf of my readers :)
    2006-05-24 05:10:05>  <jafo> So you expect them not to be running on a platform that has .exe extensions in other words?  ;-)
    2006-05-24 05:10:26>  <mwh> oh don't even start
    2006-05-24 05:11:16>  <jafo> :-)
    2006-05-24 05:18:45>  <jafo> guin:Python-2.4.3$ python -m timeit -s 'import t' 't.main()'     
    2006-05-24 05:18:45>  <jafo> 10 loops, best of 3: 37.9 msec per loop
    2006-05-24 05:19:52>  <jafo> guin:python-trunk$ python -m timeit -s 'import t' 't.main()'
    2006-05-24 05:19:53>  <jafo> 10 loops, best of 3: 37.9 msec per loop
    2006-05-24 05:20:00>  <jafo> And these are best of like a dozen runs.
    2006-05-24 05:20:08>  <mwh> your machine is faster than mine!
    2006-05-24 05:20:30>  <mwh> pybench stikes again
    2006-05-24 05:20:37>  <mwh>       ^r
    2006-05-24 05:20:39>  <jafo> I don't know...
    2006-05-24 05:39:22>  <gbrandl> etrepum: I assigned a struct bug to you, perhaps you can look into it
    2006-05-24 05:40:07>  <etrepum> gbrandl: as long as it is reproducible on 32-bit.. I don't have any 64 bit machines
    2006-05-24 05:44:31>  *** ericvrp-lunch has joined #nfs
    2006-05-24 05:47:03>  <jafo> mwh: What about Fredrik's results?
    2006-05-24 05:47:41>  <jafo> That was done in 2.5a2, I'm told.
    2006-05-24 05:48:30>  <mwh> yikes
    2006-05-24 05:48:48>  *** jbenedik has quit IRC
    2006-05-24 05:51:39>  *** rxe has quit IRC
    2006-05-24 05:52:49>  <gbrandl> etrepum: was there some mention of 64-bit in it? I don't really recall...
    2006-05-24 05:53:05>  <etrepum> gbrandl: I don't know, I still don't know which bug it is
    2006-05-24 05:53:13>  <gbrandl> oh
    2006-05-24 05:53:17>  <gbrandl> 1229380
    2006-05-24 05:53:31>  <etrepum> gbrandl: but I know there are bugs in 64-bit because the int size is different and the struct module works on C types 
    2006-05-24 05:53:39>  <gbrandl> isn't it on the list in "My SF"?
    2006-05-24 05:54:41>  <etrepum> gbrandl: ah, yeah, I see it now. They moved that stuff around since I've last used it
    2006-05-24 05:55:25>  <gbrandl> they don't seem to employ any usability experts
    2006-05-24 06:02:14>  *** rxe has joined #nfs
    2006-05-24 06:31:07>  <jafo> mwh: Ok, Tim solved the mystery of why it was the same.  I was running "python" instead of "./python".  I'm absolutely seeing a difference on Linux, Tim is seeing a difference on Windows.
    2006-05-24 06:37:14>  *** grunar has quit IRC
    2006-05-24 07:08:12>  *** grunar has joined #nfs
    2006-05-24 07:26:40>  *** ericvrp has left #nfs
    2006-05-24 07:32:41>  <blais> emacs users
    2006-05-24 07:32:47>  <blais> if you edit document strings
    2006-05-24 07:32:51>  <blais> you will liek this
    2006-05-24 07:32:54>  <blais> (kjust wrote it)
    2006-05-24 07:32:59>  <blais> ;; For fixing up multi-line strings embedded in C code.
    2006-05-24 07:33:00>  <blais> (defun c-multiline-string-fixup (beg end)
    2006-05-24 07:33:00>  <blais>   (interactive "r")
    2006-05-24 07:33:00>  <blais>   (let ((mbeg (set-marker (make-marker) beg))
    2006-05-24 07:33:00>  <blais>   (mend (set-marker (make-marker) end)))
    2006-05-24 07:33:00>  <blais>     ;; Remove the current postfixes.
    2006-05-24 07:33:02>  <blais>     (goto-char mbeg)
    2006-05-24 07:33:04>  <blais>     (while (< (point) mend)
    2006-05-24 07:33:06>  <blais>       (when (re-search-forward "\\\\n\\\\" (line-end-position) t)
    2006-05-24 07:33:09>  <blais>   (goto-char (match-beginning 0))
    2006-05-24 07:33:10>  <blais>   (delete-char 3))
    2006-05-24 07:33:12>  <blais>       (forward-line 1))
    2006-05-24 07:33:14>  <blais>     ;; Add the postfixes back in.
    2006-05-24 07:33:16>  <blais>     (goto-char mbeg)
    2006-05-24 07:33:18>  <blais>     (while (< (point) mend)
    2006-05-24 07:33:20>  <blais>       (end-of-line)
    2006-05-24 07:33:24>  <blais>       (insert "\\n\\")
    2006-05-24 07:33:26>  <blais>       (forward-line 1))
    2006-05-24 07:33:28>  <blais>     ;; Clear markers.
    2006-05-24 07:33:30>  <blais>     (dolist (x (list mbeg mend)) (set-marker x nil))
    2006-05-24 07:33:32>  <blais>   ))
    2006-05-24 07:33:34>  <blais> in c code
    2006-05-24 07:33:36>  <blais> will adjust the \n\ markers at the end of strings for ya
    2006-05-24 07:35:45>  <jafo> blais: The jotlive.com page has a link to pastebin.de, you should use that for that sort of thing.
    2006-05-24 07:35:46>  <gbrandl> jack_diederich: try out str(Decimal(222222222222222222222222222222222222222222222222222))
    2006-05-24 07:36:45>  <blais> here, even better, this versoin you can remove the \n\ first, then edit, then have them put back
    2006-05-24 07:36:51>  <blais> (defun c-multiline-string-fixup (beg end)
    2006-05-24 07:36:51>  <blais>   "Replace or remove (with prefix arg) trailing \n\ chars within the region.
    2006-05-24 07:36:51>  <blais> This is useful for editing multi-line strings in C."
    2006-05-24 07:36:51>  <blais>   (interactive "r")
    2006-05-24 07:36:55>  <blais>   (let ((mbeg (set-marker (make-marker) beg))
    2006-05-24 07:36:55>  <blais>   (mend (set-marker (make-marker) end)))
    2006-05-24 07:36:56>  <blais>     ;; Remove the current postfixes.
    2006-05-24 07:36:58>  <blais>     (goto-char mbeg)
    2006-05-24 07:37:00>  <blais>     (while (< (point) mend)
    2006-05-24 07:37:02>  <blais>       (when (re-search-forward "\\\\n\\\\" (line-end-position) t)
    2006-05-24 07:37:04>  <blais>   (goto-char (match-beginning 0))
    2006-05-24 07:37:06>  <blais>   (delete-char 3))
    2006-05-24 07:37:08>  <blais>       (forward-line 1))
    2006-05-24 07:37:10>  <blais>     (unless current-prefix-arg
    2006-05-24 07:37:12>  <blais>       ;; Add the postfixes back in.
    2006-05-24 07:37:14>  <blais>       (goto-char mbeg)
    2006-05-24 07:37:16>  <blais>       (while (< (point) mend)
    2006-05-24 07:37:18>  <blais>   (end-of-line)
    2006-05-24 07:37:20>  <blais>   (insert "\\n\\")
    2006-05-24 07:37:24>  <blais>   (forward-line 1)))
    2006-05-24 07:37:26>  <blais>     ;; Clear markers.
    2006-05-24 07:37:28>  <blais>     (dolist (x (list mbeg mend)) (set-marker x nil))
    2006-05-24 07:37:30>  <blais>   ))
    2006-05-24 07:37:32>  <blais> (define-key c-mode-map [(control c)(\\)] 'c-multiline-string-fixup)
    2006-05-24 07:37:34>  <blais> enjoy
    2006-05-24 07:41:00>  <mwh> blais: pastebin.de
    2006-05-24 07:51:53>  <jafo> Calling Mr. Blivious.  Mr. Martin O. Blivious.
    2006-05-24 07:56:14>  *** jbenedik has joined #nfs
    2006-05-24 08:27:49>  *** etrepum has quit IRC
    2006-05-24 08:30:24>  *** etrepum has joined #nfs
    2006-05-24 08:54:57>  *** ccpRichard2 has quit IRC
    2006-05-24 08:57:11>  *** jbenedik has quit IRC
    2006-05-24 08:59:34>  *** jbenedik has joined #nfs
    2006-05-24 09:04:50>  *** etrepum has left #nfs
    2006-05-24 09:08:55>  *** jbenedik has quit IRC
    2006-05-24 09:28:49>  *** jbenedik has joined #nfs
    2006-05-24 09:29:37>  *** runarp has joined #nfs
    2006-05-24 09:38:52>  *** blais_ has joined #nfs
    2006-05-24 09:39:10>  *** gbr_ has joined #nfs
    2006-05-24 09:39:49>  *** gbrandl has quit IRC
    2006-05-24 09:40:16>  *** rxe has quit IRC
    2006-05-24 09:40:32>  *** grunar has quit IRC
    2006-05-24 09:40:33>  *** stakkars has quit IRC
    2006-05-24 09:40:34>  *** blais has quit IRC
    2006-05-24 09:41:16>  *** jack_diederich has quit IRC
    2006-05-24 09:42:51>  *** etrepum_ has joined #nfs
    2006-05-24 10:01:07>  *** jbenedik has quit IRC
    2006-05-24 10:11:33>  <gbrandl> blais_: do you want to copyright your next code file to me?
    2006-05-24 10:12:12>  *** jbenedik has joined #nfs
    2006-05-24 10:21:23>  *** Stargazers has joined #nfs
    2006-05-24 10:21:30>  *** Stargazers has left #nfs
    2006-05-24 10:23:23>  <blais_> huh?
    2006-05-24 10:28:08>  *** tiny has joined #nfs
    2006-05-24 10:28:15>  *** tiny has left #nfs
    2006-05-24 10:32:48>  *** Yhg1s has joined #nfs
    2006-05-24 10:33:01>  <Yhg1s> heh, getting a lot of NFS questions here, I guess? ;)
    2006-05-24 10:37:40>  <gbrandl> blais_: you copyrighted your test file to Greg P. Smith ;)
    2006-05-24 10:46:18>  <etrepum> Is it likely to break anything if I return int instead of long from struct when they're small enough to fit?
    2006-05-24 10:47:05>  <etrepum> creating and working with long is awfully slow
    2006-05-24 10:56:53>  <Yhg1s> etrepum: no, it shouldn't.
    2006-05-24 10:57:17>  <Yhg1s> (assuming we're talking about Python ints and longs; C ints and longs should be automatically converted, and not slow anyway)
    2006-05-24 11:03:43>  <etrepum> C ints and longs are the same thing on most architectures...
    2006-05-24 11:04:06>  <blais_> brnadl: you can see how much I care abouw copyrights
    2006-05-24 11:08:13>  *** stakkars has joined #nfs
    2006-05-24 11:15:31>  <Yhg1s> etrepum: yes (except for me, as I mostly have em64t machines), hence 'not slow'
    2006-05-24 11:46:50>  *** bcannon has joined #nfs
    2006-05-24 11:47:05>  <bcannon> exit
    2006-05-24 11:47:07>  *** bcannon has quit IRC
    2006-05-24 12:01:58>  *** gbrandl has quit IRC
    2006-05-24 12:02:16>  *** jbenedik has quit IRC
    2006-05-24 12:02:25>  *** etrepum has quit IRC
    2006-05-24 12:02:36>  *** runarp has quit IRC
    2006-05-24 12:02:58>  *** stakkars has quit IRC
    2006-05-24 12:06:02>  *** blais_ has quit IRC
    2006-05-24 12:20:13>  *** blais has joined #nfs
    2006-05-24 12:23:03>  *** gbrandl has joined #nfs
    2006-05-24 12:26:42>  *** jbenedik has joined #nfs
    2006-05-24 12:44:46>  *** stakkars has joined #nfs
    2006-05-24 13:37:31>  *** jbenedik has quit IRC
    2006-05-24 13:39:16>  *** gbrandl has quit IRC
    2006-05-24 13:41:00>  *** blais has quit IRC
    2006-05-24 13:55:34>  *** stakkars has quit IRC
    2006-05-24 18:31:37>  *** efm has quit IRC
    2006-05-24 19:28:50>  *** ferringb has joined #nfs
    2006-05-24 21:16:46>  *** efm has joined #nfs
    2006-05-25 01:51:34>  <jafo> j0
    2006-05-25 01:59:07>  *** hpk has quit IRC
    2006-05-25 02:24:22>  *** rjones has joined #nfs
    2006-05-25 02:55:34>  *** rjones has quit IRC
    2006-05-25 02:56:05>  *** The_Ball has joined #nfs
    2006-05-25 02:56:31>  <The_Ball> is there a network filesystem channel?
    2006-05-25 03:02:22>  <ferringb> not here ;)
    2006-05-25 03:10:51>  <jafo> The_Ball: Yeah, no idea.  Sorry.
    2006-05-25 03:11:34>  <jafo> When we set up the channel on Sunday, it didn't exist for at least the previous day.
    2006-05-25 03:12:18>  <The_Ball> i see
    2006-05-25 03:12:49>  *** The_Ball has left #nfs
    2006-05-25 04:32:46>  <Yhg1s> jafo: will you sprinters be doing any sightseeing in iceland? I can highly recommend it, it's an extremely beautiful island (although my favourite spots are more than 7 hours drive away from reykjavik ;P)
    2006-05-25 06:21:46>  <ccpRichard> They went out to the Blue Lagoon this morning
    2006-05-25 07:41:46>  *** jack_diederich has joined #nfs
    2006-05-25 07:43:52>  <jafo> Yhg1s: We ewnt to a viking dinner last night, and a today we just got back from the Blue Lagoon.
    2006-05-25 07:48:11>  *** grunar has joined #nfs
    2006-05-25 07:48:57>  *** gbrandl has joined #nfs
    2006-05-25 07:57:00>  *** jbenedik has joined #nfs
    2006-05-25 08:04:59>  *** stakkars has joined #nfs
    2006-05-25 08:05:23>  *** mwh has quit IRC
    2006-05-25 08:11:43>  *** blais has joined #nfs
    2006-05-25 08:15:30>  *** etrepum has joined #nfs
    2006-05-25 08:19:55>  *** pico has joined #nfs
    2006-05-25 08:20:13>  *** pico has left #nfs
    2006-05-25 08:32:01>  <blais> t
    2006-05-25 08:32:07>  <jack_diederich> est
    2006-05-25 08:35:03>  <blais> http://furius.ca/tmp/nfs3/html/dirindex.html
    2006-05-25 08:35:04>  <blais> new pics
    2006-05-25 08:35:07>  <blais> from the lagoon
    2006-05-25 08:35:09>  <blais> and last nite
    2006-05-25 08:35:13>  <blais> enjoy
    2006-05-25 08:38:37>  <efm> thanks blais
    2006-05-25 08:43:45>  <blais> hey evelyn wazzup, sitting here next to jafo
    2006-05-25 08:45:46>  <jafo> Hi, efm.
    2006-05-25 08:46:05>  <efm> just getting up. It's another beautiful day in Colorado. Kitties are wonderful.
    2006-05-25 08:46:29>  <efm> Looks like you're having a great time. I've wanted to visit the Blue Lagoon for many years. I hear it's great.
    2006-05-25 08:46:41>  <efm> hi jafo
    2006-05-25 09:10:46>  <Yhg1s> the blue lagoon is nice, but not as nice as the parts of Iceland that aren't as close to Reykjavik :)
    2006-05-25 09:11:15>  <Yhg1s> warmer than Jokulsarlon though.
    2006-05-25 09:11:46>  <Yhg1s> (sorry, Jökulsárlón)
    2006-05-25 09:14:59>  *** rxe has joined #nfs
    2006-05-25 09:18:36>  <jafo> Yeah, but, you know, we're working.  This was just a morning trip.
    2006-05-25 09:20:48>  <Yhg1s> good thing I'm not there, I don't know if I'd been able to resist the temptation to keep driving :)
    2006-05-25 09:21:36>  <jafo> :-)
    2006-05-25 09:27:43>  *** ymmit has joined #nfs
    2006-05-25 10:20:08>  *** jbenedik has quit IRC
    2006-05-25 10:29:39>  *** jbenedik has joined #nfs
    2006-05-25 10:55:55>  *** uncletimmy has joined #nfs
    2006-05-25 11:01:41>  *** ymmit has quit IRC
    2006-05-25 11:18:23>  *** uncletimmy has left #nfs
    2006-05-25 11:27:00>  *** jack_diederich has quit IRC
    2006-05-25 11:30:11>  *** jbenedik has quit IRC
    2006-05-25 11:35:51>  *** jbenedik has joined #nfs
    2006-05-25 11:49:17>  *** jack_diederich has joined #nfs
    2006-05-25 11:49:35>  *** grunar has quit IRC
    2006-05-25 11:54:28>  *** jbenedik has quit IRC
    2006-05-25 11:59:45>  *** jbenedik has joined #nfs
    2006-05-25 12:02:05>  *** uncletimmy has joined #nfs
    2006-05-25 12:03:37>  *** etrepum has quit IRC
    2006-05-25 12:13:35>  *** holdenweb has joined #nfs
    2006-05-25 12:16:18>  *** rjones has joined #nfs
    2006-05-25 12:16:35>  <jafo> :w
    2006-05-25 12:16:39>  <jafo> Ugh.  Sorry.
    2006-05-25 12:29:34>  <holdenweb> ls
    2006-05-25 12:57:52>  *** jbenedik has quit IRC
    2006-05-25 13:01:05>  *** tuv has joined #nfs
    2006-05-25 13:01:22>  *** tuv has left #nfs
    2006-05-25 13:04:05>  *** uncletimmy has quit IRC
    2006-05-25 13:17:05>  *** krang has joined #nfs
    2006-05-25 13:17:38>  <krang> hey hey, anyone got a URL for a good tutorial on automounting home directories with NFS+LDAP?
    2006-05-25 13:18:13>  <krang> I don't seem to be able to find one
    2006-05-25 13:18:33>  <efm> krang: you'll want to try #linux-nfs on irc.oftc.net
    2006-05-25 13:19:02>  <krang> efm: cheers
    2006-05-25 13:19:35>  <krang> which *is* the best network for general linuxry?
    2006-05-25 13:19:36>  *** grunar has joined #nfs
    2006-05-25 13:20:03>  *** rjones has quit IRC
    2006-05-25 13:20:30>  <efm> It depends krang.  I hang out on the channel for my local linux users group, and then use other networks for specific questions
    2006-05-25 13:21:14>  *** jamwt has joined #nfs
    2006-05-25 13:21:27>  <krang> I'm basically trying to get my sysadmin skills together, and have lots of questions.
    2006-05-25 13:21:39>  <krang> where's best for that?
    2006-05-25 13:21:45>  <efm> then I'd suggest hooking up with people locally. 
    2006-05-25 13:22:13>  <krang> lol, I'm in rural Canada and had to shoot internet 5km with a wireless link. I think I'm SOL on that count :-)
    2006-05-25 13:22:42>  <efm> krang you can follow me to community.tummy.com 6667 #hackingsociety
    2006-05-25 13:22:46>  <krang> regardless, is there a directory for local groups somewhere?
    2006-05-25 13:22:59>  <krang> cheers dude
    2006-05-25 13:24:23>  <efm> krang: correction irc.community.tummy.com 6667 #hackingsociety
    2006-05-25 13:24:32>  <krang> gotcha
    2006-05-25 13:24:54>  *** etrepum has joined #nfs
    2006-05-25 13:27:44>  *** uncletimmy has joined #nfs
    2006-05-25 13:30:46>  *** blais has quit IRC
    2006-05-25 13:31:44>  *** stakkars has quit IRC
    2006-05-25 13:36:56>  <jafo> I know this music.
    2006-05-25 13:37:53>  <jafo> krang/efm: Please take the discussion elsewhere.  See the topic.
    2006-05-25 13:38:36>  <efm> yes jafo
    2006-05-25 13:39:27>  <krang> jafo: soz dude
    2006-05-25 13:39:45>  *** holdenweb has quit IRC
    2006-05-25 13:40:16>  <krang> back onto the topic, have any of you fine people seen a good tutorial on how to use NFS/LDAP for automounting home dirs?
    2006-05-25 13:40:32>  <efm> krang: you are on the wrong channel
    2006-05-25 13:40:47>  <jafo> krang: This is not the correct place to ask that.
    2006-05-25 13:41:02>  <krang> oh crap, i have to start reading topics
    2006-05-25 13:41:05>  <krang> sorry!
    2006-05-25 13:41:18>  <jafo> Thanks.
    2006-05-25 13:41:29>  *** krang has left #nfs
    2006-05-25 13:52:20>  *** grunar has quit IRC
    2006-05-25 14:21:17>  *** etrepum_ has joined #nfs
    2006-05-25 14:24:10>  *** uncletimmy has quit IRC
    2006-05-25 14:27:22>  *** gbrandl has quit IRC
    2006-05-25 14:29:13>  *** etrepum has quit IRC
    2006-05-25 14:29:18>  *** gbrandl has joined #nfs
    2006-05-25 14:30:14>  *** rxe has quit IRC
    2006-05-25 14:31:04>  *** jack_diederich has quit IRC
    2006-05-25 14:35:48>  *** holdenweb has joined #nfs
    2006-05-25 14:42:44>  <jafo> svn+ssh://pythondev@svn.python.org/python/trunk/
    2006-05-25 14:56:34>  *** stakkars has joined #nfs
    2006-05-25 15:01:29>  *** blais has joined #nfs
    2006-05-25 15:05:35>  *** jbenedik has joined #nfs
    2006-05-25 15:12:26>  <etrepum> that strange little test_float regression is fixed
    2006-05-25 15:14:17>  *** jbenedik has quit IRC
    2006-05-25 15:15:53>  *** jbenedik has joined #nfs
    2006-05-25 15:42:26>  *** jbenedik has quit IRC
    2006-05-25 15:51:00>  *** ferringb has left #nfs
    2006-05-25 15:52:25>  *** jbenedik has joined #nfs
    2006-05-25 15:54:34>  <gbrandl>  * mwh is tempted to reply to /F on python-dev with "are you drunk?"
    2006-05-25 16:26:53>  <etrepum> uh.. wtf.. check timemodule.c
    2006-05-25 16:26:59>  <etrepum>  46261 tim.peters #if defined(MS_WINDOWS) && !defined(__BORLANDC__)
    2006-05-25 16:26:59>  <etrepum>  15913     fdrake /* Win32 has better clock replacement
    2006-05-25 16:26:59>  <etrepum>   7713      guido #undef HAVE_CLOCK /* We have our own version down below */
    2006-05-25 16:26:59>  <etrepum>  46261 tim.peters #endif /* MS_WINDOWS && !defined(__BORLANDC__) */
    2006-05-25 16:27:14>  <etrepum> the comment isn't closed... so #undef HAVE_CLOCK never happens
    2006-05-25 16:27:17>  <etrepum> that can't be intentional can it?
    2006-05-25 16:54:52>  *** jbenedik has quit IRC
    2006-05-25 17:10:43>  *** etrepum has quit IRC
    2006-05-25 17:27:18>  *** holdenweb has quit IRC
    2006-05-25 18:20:07>  *** stakkars has quit IRC
    2006-05-25 18:30:37>  *** gbrandl has quit IRC
    2006-05-25 20:07:23>  *** blais has quit IRC
    2006-05-26 02:51:20>  *** holdenweb has joined #nfs
    2006-05-26 02:52:38>  *** grunar has joined #nfs
    2006-05-26 03:16:51>  *** stakkars has joined #nfs
    2006-05-26 03:21:08>  *** jack_diederich has joined #nfs
    2006-05-26 03:30:04>  <holdenweb> Nice benchmarks on .../Successes, John!
    2006-05-26 03:31:33>  *** grunar has quit IRC
    2006-05-26 03:40:06>  *** jbenedik has joined #nfs
    2006-05-26 03:40:59>  *** runarp has joined #nfs
    2006-05-26 03:54:24>  *** etrepum has joined #nfs
    2006-05-26 03:54:37>  <etrepum> runarp: http://groups.google.com/group/comp.lang.python/browse_thread/thread/58602fc81c2df1c8/19a6705e220c7569?lnk=raot#19a6705e220c7569
    2006-05-26 04:25:58>  *** rxe has joined #nfs
    2006-05-26 04:36:06>  *** blais has joined #nfs
    2006-05-26 04:45:55>  *** stakkars has quit IRC
    2006-05-26 04:46:07>  *** stakkars has joined #nfs
    2006-05-26 04:51:49>  *** jbenedik has quit IRC
    2006-05-26 04:53:33>  *** jbenedik has joined #nfs
    2006-05-26 05:19:01>  *** kristjan has joined #NFS
    2006-05-26 05:26:37>  *** kristjan_ has joined #NFS
    2006-05-26 06:27:39>  *** blais has quit IRC
    2006-05-26 06:28:54>  *** blais has joined #nfs
    2006-05-26 07:05:29>  *** amk_ has joined #nfs
    2006-05-26 07:16:34>  <amk_> Martin and Bob: test_struct.py now does things like 's = struct.Struct(fmt)'.
    2006-05-26 07:16:42>  <amk_> Is the intention that the Struct class is now part of the public interface?
    2006-05-26 07:25:53>  *** etrepum has quit IRC
    2006-05-26 07:27:38>  <jafo> That's crazy talk!
    2006-05-26 07:33:02>  *** etrepum has joined #nfs
    2006-05-26 07:34:01>  <etrepum> amk_: yes, it's public API. There's a doc patch, but it needs to be revised.
    2006-05-26 07:39:06>  <amk_> OK; I'll mention it in the what's-new, then.  Thanks!
    2006-05-26 07:53:40>  <amk_> Will you also be adding a pack_to() module-level function?
    2006-05-26 07:54:50>  <etrepum> I suppose we should for symmetry
    2006-05-26 07:55:19>  <etrepum> but it's not going to be commonly useful, there are very few objects that implement the write buffer protocol
    2006-05-26 07:57:28>  <etrepum> is there an IRC bot that announces python commits?
    2006-05-26 08:00:47>  <jafo> There's one that criticizes python commits...
    2006-05-26 08:02:00>  <etrepum> true
    2006-05-26 08:09:46>  <holdenweb> pybench wasn't distributed with 2.4, right?
    2006-05-26 08:12:11>  <amk_> Steve: correct.
    2006-05-26 08:20:31>  *** jbenedik has quit IRC
    2006-05-26 08:26:13>  *** jbenedik has joined #nfs
    2006-05-26 08:27:03>  *** etrepum has quit IRC
    2006-05-26 09:01:49>  <blais> john / bob: http://furius.ca/nfs/ewt/results/r1.txt
    2006-05-26 09:01:53>  <blais> some new results
    2006-05-26 09:01:59>  <blais> profiling
    2006-05-26 09:02:07>  <blais> a single funcall per message makes it slower...
    2006-05-26 09:02:10>  <blais> (python funcal)
    2006-05-26 09:02:36>  <blais> so we go from 28s to 22s with the hot bufferola
    2006-05-26 09:04:22>  <jafo> "You just spent a week saving 6 seconds, tell our viewers how you fee."
    2006-05-26 09:04:31>  <blais> hehe
    2006-05-26 09:05:01>  <blais> well that's on a 10MB file rather than a 5G
    2006-05-26 09:05:24>  <jafo> "You're WAY above our viewers heads."
    2006-05-26 09:09:29>  *** etrepum has joined #nfs
    2006-05-26 09:11:57>  <blais> etrepum
    2006-05-26 09:12:08>  <blais> john / bob: http://furius.ca/nfs/ewt/results/r1.txt
    2006-05-26 09:15:30>  <blais> jafo: here's how i fee, or whatever you mean, http://furius.ca/nfs/ewt/blobxxx.py
    2006-05-26 09:16:37>  <etrepum> blais: excellent
    2006-05-26 09:16:56>  <etrepum> blais: is hotbuf on the trunk?
    2006-05-26 09:17:02>  <jafo> blais: Excellent.
    2006-05-26 09:17:25>  <blais> hotbuf in /sandbox/trunk/hotbuf
    2006-05-26 09:17:28>  <blais> the example isn't though
    2006-05-26 09:17:44>  <blais> johnny: can I add your blobxxx.py in the python sandbox?  
    2006-05-26 09:19:15>  <blais> jafo: no, not excellent, on a larger buffer hotbuf is about the same
    2006-05-26 09:19:23>  <blais> will run oprofile
    2006-05-26 09:23:53>  *** jbenedik has quit IRC
    2006-05-26 09:26:36>  *** jbenedik has joined #nfs
    2006-05-26 09:26:40>  <etrepum> sandbox/trunk/hotbuffer
    2006-05-26 09:26:50>  <blais> ohnny: can I add your blobxxx.py in the python sandbox?  
    2006-05-26 09:27:08>  <blais> svn+ssh://pythondev@svn.python.org/sandbox/trunk/hotbuffer
    2006-05-26 09:27:37>  <blais> sorry about that, i just moved it before (it's now an extension module)
    2006-05-26 09:31:13>  *** efm has quit IRC
    2006-05-26 09:44:50>  <jafo> I noticed yesterday that when I went down the stairs there was this huge rush of air up.  Now I'm sitting by the door to the door by the elevators.  It's clear that the doors being open up here is sucking the air out of the rest of the hotel.
    2006-05-26 09:45:17>  <jafo> Hopefully, the rest of the guests can live in a perfect vacuum.
    2006-05-26 09:52:06>  *** blais has quit IRC
    2006-05-26 09:53:51>  <jafo> holdenweb: Scotty, where's that new trunk pybench?
    2006-05-26 09:55:17>  *** blais has joined #nfs
    2006-05-26 09:58:33>  <holdenweb> slight problem with the dilithium crystal, cap'n
    2006-05-26 09:59:05>  <holdenweb> ah cannae hold them together and they'll no process ther options. come help me debug!
    2006-05-26 10:26:22>  <etrepum> blais: I committed the unpack implementation to hotbuf and added some tests for the pack and unpack methods of hotbuf
    2006-05-26 10:28:19>  <holdenweb> trunk pybench now checked in
    2006-05-26 10:32:48>  <jafo> Yay!
    2006-05-26 11:08:20>  *** efm has joined #nfs
    2006-05-26 11:19:34>  <blais> etrepum: your tab setting is at 5
    2006-05-26 11:19:52>  <etrepum> no it's not
    2006-05-26 11:21:32>  <etrepum> I love the C API docs
    2006-05-26 11:21:32>  <etrepum> XXX blah, blah.
    2006-05-26 11:26:21>  <blais> dang
    2006-05-26 11:26:25>  <blais> it's still slowr
    2006-05-26 11:26:40>  <blais> i made restore() take an arg for advancing
    2006-05-26 11:27:04>  <blais> bob: it's merged BTW in case you're coding your descrpitor thingy
    2006-05-26 11:27:14>  <blais> (I mean committed)
    2006-05-26 11:28:49>  <blais> jbenedik: can I merge your ewt blobxxx.py into the python sandbox?  would you me rather not?  it could serve as a use case 
    2006-05-26 11:28:55>  <blais> (for slowing down your programs, that is ;-))
    2006-05-26 11:29:44>  <jbenedik> heh, it is an internal api and i think i'd prefer not right now.  if you want to generate some test message structures (for exercising netstring parsing and struct), thats fine
    2006-05-26 11:30:10>  <blais> noworries
    2006-05-26 11:31:58>  <blais> bob: it's still the dict lookups from getattr that kill it
    2006-05-26 11:34:28>  <blais> whoa
    2006-05-26 11:34:37>  <blais> caching the methods before the loop results in a big improvment
    2006-05-26 11:37:41>  <etrepum> blais: what is mark_position and mark_limit?
    2006-05-26 11:37:54>  <blais> the saved position and limit
    2006-05-26 11:38:24>  <jafo> You mean the marked position and limit.
    2006-05-26 11:38:27>  <etrepum> blais: should those even be exposed? should it be a 2-tuple instead?
    2006-05-26 11:40:16>  *** runarp has quit IRC
    2006-05-26 11:47:19>  <etrepum> blais: ok I rewrote the tp_members as tp_getset.. so buf.position = n should work
    2006-05-26 11:47:38>  <etrepum> blais: currently untested, I'm going to run through the code and look for ssize_t errors first.. there were some
    2006-05-26 11:54:28>  <blais> bobby: just commit when it's neat
    2006-05-26 11:54:53>  <blais> pos+limit: I suppose I don't need to expose them indeed
    2006-05-26 11:55:45>  *** stakkars has quit IRC
    2006-05-26 11:59:26>  *** kristjan_ has quit IRC
    2006-05-26 11:59:26>  *** kristjan has quit IRC
    2006-05-26 12:01:33>  <blais> bob: your changes don't help the latest version, I don't set members anymore, just function calls (cached)
    2006-05-26 12:01:38>  <blais> there are still too many funcalls
    2006-05-26 12:02:02>  <blais> maybe I should implement some iteration protocol that works with the kind of length + msg format that EWT has
    2006-05-26 12:19:51>  *** runarp has joined #nfs
    2006-05-26 12:27:47>  *** blais has quit IRC
    2006-05-26 13:12:10>  *** rower has joined #nfs
    2006-05-26 13:12:26>  *** rower has left #nfs
    2006-05-26 13:13:51>  *** rower has joined #nfs
    2006-05-26 13:19:56>  *** holdenweb has quit IRC
    2006-05-26 13:43:45>  <amk_>  /leave #nfs
    2006-05-26 13:43:51>  *** amk_ has left #nfs
    2006-05-26 13:43:51>  <jafo> Toodles
    2006-05-26 14:21:25>  *** jack_diederich has left #nfs
    2006-05-26 14:25:40>  *** rxe has left #nfs
    2006-05-26 14:33:39>  *** etrepum has quit IRC
    2006-05-26 14:33:57>  *** jbenedik has quit IRC
    2006-05-26 14:54:42>  *** runarp has quit IRC
    2006-05-26 17:00:50>  *** efm has quit IRC
    2006-05-27 03:41:57>  *** jack_diederich has joined #nfs
    2006-05-27 03:52:37>  *** stakkars has joined #nfs
    2006-05-27 03:56:25>  *** holdenweb has joined #NFS
    2006-05-27 04:01:21>  *** runarp has joined #nfs
    2006-05-27 04:03:12>  *** runarp_ has joined #nfs
    2006-05-27 04:18:48>  *** jbenedik has joined #nfs
    2006-05-27 04:21:04>  *** runarp has quit IRC
    2006-05-27 04:59:25>  *** etrepum has joined #nfs
    2006-05-27 06:55:10>  <etrepum>     s = s[:length - 1]
    2006-05-27 06:55:11>  <etrepum>     return s + '\x00' * (length - len(s))
    2006-05-27 07:00:30>  *** jbenedik has quit IRC
    2006-05-27 07:10:36>  *** runarp_ has quit IRC
    2006-05-27 07:20:31>  *** etrepum_ has joined #nfs
    2006-05-27 07:20:47>  *** etrepum has quit IRC
    2006-05-27 07:35:45>  *** stakkars has quit IRC
    2006-05-27 07:36:10>  *** stakkars has joined #nfs
    2006-05-27 07:49:40>  *** runarp has joined #nfs
    2006-05-27 08:26:29>  *** holdenweb_ has joined #NFS
    2006-05-27 08:29:44>  *** jbenedik has joined #nfs
    2006-05-27 08:35:26>  *** holdenweb has quit IRC
    2006-05-27 08:45:17>  <etrepum> cc: Info: ../Objects/exceptions.c, line 384: Extraneous semicolon. (extrasemi)
    2006-05-27 08:45:24>  <etrepum> cc: Warning: ../Modules/posixmodule.c, line 5451: In this statement, the referenced type of the pointer value "&status" is "int", which is not compatible with "union wait". (ptrmismatch)
    2006-05-27 09:10:55>  <etrepum> Program received signal SIGFPE, Arithmetic exception.
    2006-05-27 09:10:55>  <etrepum> 0x0000000160418568 in bu_double (p=0x12049d29c "", f=0x0) at /house/etrepum/src/python-46462/Modules/_struct.c:219
    2006-05-27 09:10:56>  <etrepum> 219             if (x == -1.0 && PyErr_Occurred())
    2006-05-27 09:46:31>  *** mwh has joined #nfs
    2006-05-27 09:48:11>  *** jbenedik has quit IRC
    2006-05-27 09:49:14>  *** jbenedik has joined #nfs
    2006-05-27 09:51:15>  <mwh> etrepum: re bug 1496032
    2006-05-27 09:51:27>  <mwh> i take it freebsd alpha starts up with fpu traps enabled?
    2006-05-27 09:51:52>  <etrepum> I have no idea, first time I've touched one
    2006-05-27 09:52:18>  <mwh> i see
    2006-05-27 09:52:28>  <mwh> do you have an account on one then?
    2006-05-27 10:02:27>  <etrepum> yeah I got a HP testdrive account so I could fix my damn regressions
    2006-05-27 10:02:39>  <etrepum> I couldn't find another way to get quick access to a 64-bit platform
    2006-05-27 10:02:40>  <mwh> oh right
    2006-05-27 10:02:46>  <mwh> i had one of them once
    2006-05-27 10:04:20>  <mwh> i wonder if my password still works
    2006-05-27 10:07:13>  <mwh> huh, apparently
    2006-05-27 10:09:01>  <mwh> or not
    2006-05-27 10:11:59>  * mwh hunts for the 'reset password' button
    2006-05-27 10:14:40>  <etrepum> SIGFPE looks fun
    2006-05-27 10:15:55>  <mwh> i can tell you about it on darwin/ppc :)
    2006-05-27 10:18:48>  <mwh> etrepum: look at Modules/main.c
    2006-05-27 10:19:01>  <mwh> maybe printf the result of fpgetmask?
    2006-05-27 10:23:41>  <etrepum> FreeBSD td149.testdrive.hp.com 6.0-RELEASE FreeBSD 6.0-RELEASE #0: Thu Nov  3 01:10:43 UTC 2005     root@ds10.freebie.xs4all.nl:/usr/obj/usr/src/sys/GENERIC  alpha
    2006-05-27 10:23:41>  <etrepum> fpgetmask() = 0
    2006-05-27 10:24:29>  <mwh> bleh
    2006-05-27 10:25:05>  <etrepum> 0x000000016025a568 in bu_double (p=0x1203be14c "", f=0x0) at /house/etrepum/src/python-46462/Modules/_struct.c:219
    2006-05-27 10:25:06>  <etrepum> 219             if (x == -1.0 && PyErr_Occurred())
    2006-05-27 10:25:06>  <etrepum> (gdb) p/x fpgetmask()
    2006-05-27 10:25:06>  <etrepum> $1 = 0x0
    2006-05-27 10:25:06>  <mwh> what happens if you type 1/1e-310 interactively?
    2006-05-27 10:25:27>  <etrepum> >>> 1/1e-310
    2006-05-27 10:25:27>  <etrepum> Floating exception (core dumped)
    2006-05-27 10:25:38>  <mwh> right
    2006-05-27 10:25:42>  <etrepum> Program received signal SIGFPE, Arithmetic exception.
    2006-05-27 10:25:42>  <etrepum> 0x000000012005c28c in _Py_HashDouble (v=5.5511151231257827e-17) at ../Objects/object.c:995
    2006-05-27 10:25:42>  <etrepum> 995             if (fractpart == 0.0) {
    2006-05-27 10:25:47>  <mwh> so fpgetmask() is lying, it would seem...
    2006-05-27 10:25:51>  <etrepum> sweet
    2006-05-27 10:26:05>  <mwh> gdb too, if it really thinks it crashed on that line...
    2006-05-27 10:26:19>  <etrepum> well it wasn't a debug build
    2006-05-27 10:26:49>  <mwh> oh right
    2006-05-27 10:27:03>  <etrepum> does --with-pydebug imply -O0 ?
    2006-05-27 10:27:07>  <mwh> that line is _PyHash_Double though, very odd
    2006-05-27 10:27:09>  <mwh> yes it does
    2006-05-27 10:27:47>  <etrepum> why would it be hashing a double to do division?
    2006-05-27 10:28:21>  <mwh> i doubt it is
    2006-05-27 10:29:01>  <etrepum> 1e-310 by itself dumps core
    2006-05-27 10:29:16>  <mwh> urk
    2006-05-27 10:29:40>  <mwh> it's a denorm, i guess Underflow is getting signalled
    2006-05-27 10:29:45>  <etrepum> core dump at the same place with gdb --args ./python -c '1e-310'
    2006-05-27 10:30:11>  <etrepum> IEEEtastic
    2006-05-27 10:30:19>  <mwh> what does the stack look like?
    2006-05-27 10:30:32>  <mwh> ieee mandates starting up in non-stop mode, not their fault here :)
    2006-05-27 10:31:13>  <etrepum> oh! it's in the compiler
    2006-05-27 10:31:24>  <mwh> ah haha
    2006-05-27 10:31:29>  <etrepum> http://rafb.net/paste/results/GdojeP93.html
    2006-05-27 10:31:30>  <mwh> yes, for co_consts
    2006-05-27 10:31:32>  <etrepum> yup
    2006-05-27 10:31:41>  <mwh> try 1e-308/20 then :)
    2006-05-27 10:31:51>  <mwh> i think 1e-308 should be normalized
    2006-05-27 10:32:19>  <etrepum> 1e-308 dumps
    2006-05-27 10:32:32>  *** jbenedik has quit IRC
    2006-05-27 10:32:45>  *** jack_diederich has left #nfs
    2006-05-27 10:32:47>  <mwh> odd
    2006-05-27 10:32:49>  <etrepum> 1e-307 doesn't dump
    2006-05-27 10:32:56>  <mwh> oh right
    2006-05-27 10:33:03>  <mwh> 1e-307/1e10 ?
    2006-05-27 10:33:14>  <etrepum> >>> 1e-307/1e10
    2006-05-27 10:33:15>  <etrepum> 0.0
    2006-05-27 10:33:18>  *** jbenedik has joined #nfs
    2006-05-27 10:33:33>  <mwh> huh
    2006-05-27 10:33:39>  <etrepum> >>> 1e-307/1e-307
    2006-05-27 10:33:39>  <etrepum> 1.0
    2006-05-27 10:33:39>  <etrepum> >>> 1e-307/1e-306
    2006-05-27 10:33:39>  <etrepum> 0.099999999999999992
    2006-05-27 10:33:42>  <mwh> >>> 1e-307/1e10
    2006-05-27 10:33:42>  <mwh> 1.0000002306925374e-317
    2006-05-27 10:33:54>  <etrepum> >>> 1e-307/1e1000
    2006-05-27 10:33:55>  <etrepum> Floating exception (core dumped)
    2006-05-27 10:34:05>  <mwh> maybe it would be better to not try to pretend the alpha does ieee arithmetic
    2006-05-27 10:34:15>  <mwh> etrepum: i bet 1e1000 on its own will do that
    2006-05-27 10:34:16>  <etrepum> haha
    2006-05-27 10:34:37>  <mwh> are you compiling with -mieee ?
    2006-05-27 10:34:48>  <mwh> i forget if that's relevant any more
    2006-05-27 10:35:31>  <etrepum> I didn't specify anything special
    2006-05-27 10:36:09>  <etrepum> and I don't see anything special in the compile..
    2006-05-27 10:36:09>  <etrepum> gcc -pthread -fPIC -fno-strict-aliasing -g -Wall -Wstrict-prototypes -I. -I/house/etrepum/src/python-46462/./Include -I../Include -I. -I/usr/local/include -I/house/etrepum/src/python-46462/Include -I/house/etrepum/src/python-46462/_freebsd_debug -c /house/etrepum/src/python-46462/Modules/_struct.c -o build/temp.freebsd-6.0-RELEASE-alpha-2.5/house/etrepum/src/python-46462/Modules/_struct.o
    2006-05-27 10:36:16>  <mwh> harum
    2006-05-27 10:36:30>  <mwh> googling is suggesting kernel bugs...
    2006-05-27 10:37:52>  <mwh> how long do builds take on this machine?
    2006-05-27 10:37:55>  <etrepum> a while
    2006-05-27 10:38:04>  <etrepum> like 30 min maybe
    2006-05-27 10:38:16>  <mwh> cause i think adding -mieee to CFLAGS might help after all
    2006-05-27 10:38:18>  <mwh> http://ftp4.de.freebsd.org/pub/FreeBSD/gnats/gnats/alpha/36327
    2006-05-27 10:38:25>  <mwh> that's from 2002 though
    2006-05-27 10:38:49>  *** jbenedik has quit IRC
    2006-05-27 10:39:02>  <mwh> hum
    2006-05-27 10:39:06>  <mwh> oh i don't know
    2006-05-27 10:39:15>  <mwh> who actually cares about freebsd/alpha? :)
    2006-05-27 10:40:17>  <etrepum> I don't
    2006-05-27 10:40:43>  <mwh> me neither
    2006-05-27 10:40:57>  <mwh> i'll stop worrying about it then, i think
    2006-05-27 10:48:08>  *** runarp has quit IRC
    2006-05-27 10:51:41>  *** holdenweb_ has left #nfs
    2006-05-27 10:52:00>  <etrepum> there's probably some compiler flags that'll make it work
    2006-05-27 10:52:20>  <etrepum> apparently alpha just doesn't do denorm stuff and you have to deal with it in software
    2006-05-27 10:53:00>  *** etrepum has quit IRC
    2006-05-27 11:16:21>  *** stakkars has quit IRC
    2006-05-27 11:42:35>  *** ruied has joined #nfs
    2006-05-27 11:42:39>  *** ruied has left #nfs
    2006-05-27 12:46:18>  *** ccpRichard has quit IRC
    2006-05-27 15:55:54>  <mwh> so something caused a LOT of leaks...
    2006-05-27 15:56:15>  <mwh> i'm guessing it's exception related...
    2006-05-27 16:41:09>  <Yhg1s> mwh: not trivially reproduced, though.
    2006-05-27 16:41:24>  <Yhg1s> simple exception tossing doesn't reproduce it, but running the same simple test through doctest does.
    2006-05-27 16:54:40>  <mwh> i found that test.test_support.check_syntax reliably leaks 5 references
    2006-05-27 16:55:23>  <mwh> as does compile('1=1', '', 'exec') in fact
    2006-05-27 16:58:24>  <mwh> it's leaking a tuple containing two Nones a string and an int, i think
    2006-05-27 17:00:19>  <mwh> oh well, i guess sean and richard know what they changed...
    2006-05-27 20:29:24>  *** mwh_ has joined #nfs
    2006-05-27 20:40:09>  *** mwh has quit IRC
    2006-05-28 02:58:05>  *** mwh has quit IRC
    2006-05-28 03:04:18>  <jafo> NfS article I wrote is up on lwn.net
    2006-05-28 05:57:38>  *** xorAxAx has joined #nfs
    2006-05-28 07:50:45>  *** mwh has joined #nfs
    2006-05-28 18:36:14>  *** JZA has joined #nfs
    2006-05-28 18:36:21>  <JZA> hi anyone help me share some folders
    2006-05-28 18:37:39>  <JZA> anyone here
    2006-05-28 23:46:46>  *** JZA has left #nfs
    2006-05-29 02:25:38>  *** runarp has joined #nfs
    2006-05-29 02:28:39>  <runarp> made it back to LA.  Thanks everyone for a great sprint.
    2006-05-29 02:48:39>  *** stakkars has joined #nfs
    2006-05-29 03:00:41>  *** runarp has quit IRC
    2006-05-29 03:24:21>  *** stakkars has left #nfs
    2006-05-29 09:43:11>  *** stakkars has joined #nfs
    2006-05-29 09:43:34>  <stakkars> hi! this thing is going to be long-lived?
    2006-05-29 09:49:18>  <mwh> i would guess not
    2006-05-29 09:49:26>  <mwh> i'm just a loiterer :)
    2006-05-29 10:18:49>  *** runarp has joined #nfs
    2006-05-29 10:20:19>  *** runarp has left #nfs
    2006-05-29 21:26:57>  *** goffa has joined #nfs
    2006-05-29 21:27:20>  *** goffa has left #nfs
    2006-05-30 01:43:37>  <jafo> Well, nfsbot and I are going to vacate the channel.  Thanks for a great time everyone.
