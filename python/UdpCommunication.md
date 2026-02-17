# UdpCommunication

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# UDP Communication 

See also [SoapOverUdp](./SoapOverUdp.html), [TcpCommunication](TcpCommunication)

## Sending 

Here\'s simple code to post a note by UDP in Python 3:

:::: 
::: 
``` 
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 MESSAGE = b"Hello, World!"
   6 
   7 print("UDP target IP: %s" % UDP_IP)
   8 print("UDP target port: %s" % UDP_PORT)
   9 print("message: %s" % MESSAGE)
  10 
  11 sock = socket.socket(socket.AF_INET, # Internet
  12                      socket.SOCK_DGRAM) # UDP
  13 sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
```
:::
::::

## Receiving 

Here\'s simple code to receive UDP messages in Python 3:

:::: 
::: 
``` 
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 
   6 sock = socket.socket(socket.AF_INET, # Internet
   7                      socket.SOCK_DGRAM) # UDP
   8 sock.bind((UDP_IP, UDP_PORT))
   9 
  10 while True:
  11     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  12     print("received message: %s" % data)
```
:::
::::

## Using UDP for e.g. File Transfers 

If considering extending this example for e.g. file transfers, keep in mind that UDP is not reliable. So you\'ll have to handle packets getting lost and packets arriving out of order. In effect, to get something reliable you\'ll need to implement something similar to TCP on top of UDP, and you might want to consider using TCP instead.

That being said, sometimes you *need* to use UDP, e.g. for [UDP hole punching](http://en.wikipedia.org/wiki/UDP_hole_punching). In that case, consider [TFTP](http://en.wikipedia.org/wiki/TFTP) [for python](https://www.google.com/search?q=python+tftp) or [UDT](http://udt.sourceforge.net/) [for python](https://www.google.com/search?q=python+udt)

## Multicasting? 

The *official* example of multicast can be found at /usr/share/doc/python2.3/examples/Demo/sockets/mcast.py (at least on Debian Sarge, after `apt-get install python-examples`{.backtick}). It worked on my machine, but I have yet to try it running on different machines. \-- \-- 200.138.245.121 2006-08-09 03:20:30

I\'ve been googling for some time now, and *still* have yet to find a *working* example of Python multicast listening.

(The example below has been updated to work \-- Steven Spencer 2005-04-14 13:19:00)

(I\'ve replaced it with one that works. \-- Asgeir S. Nilsen 2005-05-09 19:25:00)

(I\'ve corrected the mreq according to the comment below \-- Sebastian Setzer 2006-01-25 14:28:00)

(I added an \"=\" to the \"4sl\" struct packing. Both the old version and the new version work on my 32-bit machine, but the Python documentation for the struct module suggests that \"l\" would be 64 bits on an LP64 or LPI64 platform without it, so I thought it would be prudent to add. \-- Kragen Sitaker 2010-04-28 07:03:00)

:::: 
::: 
``` 
   1 import socket
   2 import struct
   3 
   4 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
   5 sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   6 sock.bind(('', 4242))
   7 # wrong: mreq = struct.pack("sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
   8 mreq = struct.pack("=4sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
   9 
  10 sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
  11 
  12 while True:
  13   print(sock.recv(10240))
```
:::
::::

The mreq packing is based on [some code that I found,](http://www.senux.com/linux/network/multicast/) *that does not work.* On my computer, at least.

Sending to multicast groups is just fine; Here\'s some functional text:

:::: 
::: 
``` 
   1 import socket
   2 
   3 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
   4 sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
   5 sock.sendto(b"robot", ("239.192.0.100", 1000))
```
:::
::::

(You might want to reconsider the IP_MULTICAST_TTL setting here \-- the recommended value for local-network multicasts is \< 32, whilst a value \> 32 indicates multicasts which should traverse onto the Internet \-- Asgeir S. Nilsen)

*Note the above example is missing a bind() call. This will work OK if there is a multicast route setup in the IP routing table {i.e. os.system(\'route add 224.51.105.104 eth0\')} But without a bind() nor route, the kernel will not determine which network interface to send the data on, and will return an error. There may be other ways for the \"socket to network interface\" mapping to be defined, but I forget what they are. (Chris David)*

The above multicasting examples do not work on my computer, but I was able to fix them using code from [http://sourceforge.net/projects/pyzeroconf](http://sourceforge.net/projects/pyzeroconf). Try these examples:

:::: 
::: 
``` 
   1 # UDP multicast examples, Hugo Vincent, 2005-05-14.
   2 import socket
   3 
   4 def send(data, port=50000, addr='239.192.1.100'):
   5         """send(data[, port[, addr]]) - multicasts a UDP datagram."""
   6         # Create the socket
   7         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   8         # Make the socket multicast-aware, and set TTL.
   9         s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20) # Change TTL (=20) to suit
  10         # Send the data
  11         s.sendto(data, (addr, port))
  12 
  13 def recv(port=50000, addr="239.192.1.100", buf_size=1024):
  14         """recv([port[, addr[,buf_size]]]) - waits for a datagram and returns the data."""
  15 
  16         # Create the socket
  17         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  18 
  19         # Set some options to make it multicast-friendly
  20         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  21         try:
  22                 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
  23         except AttributeError:
  24                 pass # Some systems don't support SO_REUSEPORT
  25         s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
  26         s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
  27 
  28         # Bind to the port
  29         s.bind(('', port))
  30 
  31         # Set some more multicast options
  32         intf = socket.gethostbyname(socket.gethostname())
  33         s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(intf))
  34         s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton(intf))
  35 
  36         # Receive the data, then unregister multicast receive membership, then close the port
  37         data, sender_addr = s.recvfrom(buf_size)
  38         s.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton('0.0.0.0'))
  39         s.close()
  40         return data
```
:::
::::

At this point, I\'m beginning to think: \"Python multicast simply *does not work.*\"

- Are you running on Windows 2000/XP (pre-SP2)/Server 2003 with more than one network adapter? If so, the problem is Windows, not Python. The original code works for me on Windows 2000 (1 network adapter), but fails under XP Pro (pre-SP2, 3 adapters though 2 are disabled). Microsoft has a [support page](http://support.microsoft.com/default.aspx?scid=kb;en-us;827536) on the issue. The problem appears to be in the receiver: with both machines running the receiver, the Win2K machine sees packets sent from both machines, while the receiver on XP sees messages sent from the Win2K machine only. This, despite specifying the local IP address of the appropriate adapter in the second part of the mreq structure in the IP_ADD_MEMBERSHIP call. \-- [VinaySajip](VinaySajip) *Hm, that\'s interesting. No, I\'m not running on Windows; I\'m running on FC3. That said, I hadn\'t considered the machine as a possible problem. What I\'ll do is this: I\'ll run this on my* home *FC3 computer, and on my* home *Redhat 9 computer, and see if I can get it to work on one of them.* \-- [LionKimbro](LionKimbro) 2005-01-20 02:07:18 *The new version still doesn\'t work for me. I mean, it* does *work for local traffic: the host talking with itself. But as soon as I get to another link-local computer, and do the same over again, it doesn\'t work. I\'ve replaced 127.0.0.1 with the actual IP address of the computer, and I\'ve shut down the firewall (service iptables stop). No dice. This is all on my FC3 host, again.* \-- [LionKimbro](LionKimbro) 2005-04-14 17:27:42 *When implementing multicast, it\'s important to understand the requirements of [IGMP](ftp://ftp.rfc-editor.org/in-notes/rfc3376.txt), especially when working in a switched network. IGMP describes how routers should exchange membership information, but does not describe how layer 2 switches should handle this. Many switches have a feature called IGMP snooping, where the switch snoops for IGMP traffic, thereby gaining knowledge of which switch ports belong to a multicast group. Cheap switches typically either does not handle this or handles it wrongly.* \-- Asgeir S. Nilsen 2005-05-09 19:39:00 *The first version, I tested side-by-side equivalent C code. The C code worked, the Python code did not. Thus, I ruled out special router, switch, hub issues. However, the second version, I just ran the Python code. I did not test vis-a-vis C code. Sol, I will have to try it vis-a-vis C code, again, to be sure.* \-- [LionKimbro](LionKimbro) 2005-05-09 22:56:26

It\'s too bad we don\'t have anything as simple as this:

:::: 
::: 
``` 
   1 import UDP
   2 
   3 sock = UDP.MulticastListener("239.192.0.100", 1000)  # Listen on port 1000
   4 print sock.recv(100)
```
:::
::::

:::: 
::: 
``` 
   1 import UDP
   2 
   3 UDP.send("Hello, world!", "239.192.0.100", 1000)
```
:::
::::

\...or something like that.

\-- [LionKimbro](LionKimbro) 2005-01-19 19:54:19

You could do something like this:

:::: 
::: 
``` 
   1 class McastSocket(socket.socket):
   2   def __init__(self, local_port, reuse=False):
   3     socket.socket.__init__(self, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
   4     if(reuse):
   5       self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   6       if hasattr(socket, "SO_REUSEPORT"):
   7         self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
   8     self.bind(('', local_port))
   9   def mcast_add(self, addr, iface):
  10     sock.setsockopt(
  11         socket.IPPROTO_IP,
  12         socket.IP_ADD_MEMBERSHIP,
  13         socket.inet_aton(mcast_addr) + socket.inet_aton(mcast_iface))
```
:::
::::

Then to listen to multicast events locally:

:::: 
::: 
``` 
   1 sock = McastSocket(local_port=12345, reuse=1)
   2 sock.mcast_add('239.192.9.9', '127.0.0.1')
```
:::
::::

The perl IO::Socket::Multicast class doesn\'t look much different from this.

\-- [PaulBrannan](./PaulBrannan.html)

I was able to get the above example to work fine on a linux platform, with one small change. I had to put a \"4sl\" in the pack statement for creating mreq. It seems as if when I didn\'t have a 4, the pack statement was just using the first octet (somehow dropping the other octets), so I could only create the multi-cast \"listener\" on a 234.0.0.0 ip. After some debugging, I put the 4 in front of the \"s\", which forced it to get all 4 octets from the inet_aton, and everything worked fine. Hope this helps.

\-- JIRWIN

\...Which is exactly what the pack statement is expected to do, according to the manual:

- *For the \"s\" format character, the count is interpreted as the size of the string, \... For packing, the string is truncated or padded with null bytes as appropriate to make it fit.*

=UPDATE:= Definitive UDP multicasting example code can be found in [PyZeroConf](./PyZeroConf.html) at [http://sourceforge.net/projects/pyzeroconf](http://sourceforge.net/projects/pyzeroconf)

------------------------------------------------------------------------

How can it be definitive, if you have to download a whole project in order to read simply how to do multicasting in Python?

------------------------------------------------------------------------

\* [How to Write New Components for Kamaelia](http://kamaelia.sourceforge.net/cgi-bin/blog/blog.cgi?rm=viewpost&nodeid=1113495151) has example code for doing multicast send and receipt at the top.

------------------------------------------------------------------------

Perhaps this is what you are looking for: [http://www.doughellmann.com/PyMOTW/socket/multicast.html](http://www.doughellmann.com/PyMOTW/socket/multicast.html)

\-- cswank

------------------------------------------------------------------------
