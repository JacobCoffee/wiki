# SummerOfCode/PythonLibraries/SimpleNetworkingForPygame

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Simple Networking For Pygame 

Write a simple network library which integrates with the pygame event queue.

## Basic requirements: 

- Seamless reconnection
- Support TCP and UDP
- use select based non blocking IO
- network library is iterated manually (so we use our own event loops)

## Potential API: 

- connect(uri, onConnection, onLostConnection)
- send(conn, data)
- recv(conn, num_bytes)
- listen(uri, onConnection, onLostConnection)
- poll()

## Things not to worry about: 

- Object serialization

## NOTES, api part 2? 

I think I like the url idea. We could not worry about connections at all by using urls. Optional carring about connections could be implmented.

Two or three example games should be implemented to test the API. Something turnbased. Something with lots of action. Something with lots of connections (eg \> 100 players).

UDP and [ENet](http://enet.cubik.org/) are interesting things to consider for the api. UDP is connectionless.

All bits of data could be strings. Serialisation should be done outside of it\... however perhaps we can add a safe basic serialisation so that people don\'t use pickle.

The event queue api could event be used for some of it.

    #pygame.network.send(data, channel, lossy)
    pygame.network.send("hello network.", CHANNEL_CHAT, 0)

    for e in pygame.event.get():
       if e.type == NETWORK:
           if e.what == NETWORK_DATA_IN:
               print e.channel
               print e.data
               print e.sequenceid
               print e.peer
               if e.channel == CHANNEL_CHAT:
                   # we write the incomming text to our chat window.
                   chatwindow.write_text(e.peer, e.data)

## COMMENT 

The pygame queue integrated networking library is a great idea.

I would suggest supporting client-to-client (peer-to-peer) networking, and adding functionality to find other networked machines running the same application.

Using \'connection-less\' http and urls introduced some limitations: How does the server initiate contact with the client (assuming it keeps track of clients)? It could use http, but firewalls on many workstations/play-stations/LANs block incoming http requests.

Creating and maintaining connections would make the library more generally useful, I think, than using independent one-transaction connections like http. It would allow asynchronous notifications both ways, and would allow peer-to-peer networking.

[A very rough proposal on simple networking in python/pygame](./(5b)http(3a2f2f)pitchersduel(2e)iuplog(2e)com(2f)default(2e)asp(3f)item(3d)89521.html)\]

dkeeney

## Proposal 

I\'m interested in taking on this project, and I\'ve started to write up my ideas on my website. Please take a look and let me know what you think.

[First draft of my proposal](./(5b)http(3a2f2f)www(2e)mumstudents(2e)org(2f7e)bda(2f)soc(2f)NetworkingForPygame(2e)html.html)\]

Bryce Allen
