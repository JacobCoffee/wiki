# ThreadProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Stopping Threads Fermare un Processo 

I\'d like to start this page off with a question. How do you kill one thread from within another? Here\'s some code that shows the problem:

- Vorrei iniziare questa pagina con una domanda. Come posso terminare un processo dall\'interno di un altro?

Ecco il codice che mostra come risolvere il problema:

:::: 
::: 
``` 
   1 import threading
   2 import time
   3 
   4 class Worker(threading.Thread):
   5   def __init__(self, eventChannel, eventHandler):
   6     self.eventChannel = eventChannel
   7     self.eventHandler = eventHandler
   8     self.stopFlag = 0
   9 
  10   def shutdown(self):
  11     self.stopFlag = 1
  12 
  13   def run(self):
  14     self.stopFlag = 0
  15     while not self.stopFlag:
  16       event = self.eventChannel.waitEvent() # blocking call
  17       self.eventHandler.dispatchEvent(event)
  18 
  19 
  20 eventChannel = EventChannel()
  21 eventHandler = EventHandler()
  22 worker = Worker(eventChannel, eventHandler)
  23 worker.start()
  24 time.sleep(20)
  25 worker.shutdown()
```
:::
::::

The problem here is that `EventChannel.waitEvent()` is a blocking operation. So if no event ever arrives, then our worker thread never stops. *(`EventChannel` and `EventHandler` are classes I\'ve invented for this example)*

Il costrutto o funzione `EventChannel.waitEvent()` è un blocco operativo. Così se un evento mai arriva, il nostro lavoro non fermerà mai il processo. Attenzione!!! Le (`EventChannel` and `EventHandler` sono classi da me inventate per questo esempio.

## Suggestions Suggerimento 

- Make the `shutdown()` method put some harmless event on the event channel:

- Realiziamo il metodo `shutdown()` e spingiamo un innocuo evento nel channel event:

<!-- -->

      def shutdown(self):
        self.stopFlag = 1
        self.eventChannel.push_event(NullEvent())

- Or use a Queue to pass data. Handle errors in the handler (e.g. print them to the console), keep the thread alive.
- Oppure usiamo una coda per passare i dati. Manovrare gli errori con il manipolatore( es. stampa da console),mantiene vivo il processo.

:::: 
::: 
``` 
   1 import Queue, threading, traceback
   2 
   3 class StopMarker:
   4     """This is used as an individual stopper item."""
   5     
   6 class Worker(threading.Thread):
   7     """Get items from a queue and call the handler with the item.
   8     Errors in the handler are printed to stderr, the thread
   9     continues to run.
  10     An individual stop marker is used, so you can pass everyting
  11     as item (including None).
  12     """
  13     
  14     def __init__(self, handler):
  15         """Initialize Thread object and worker."""
  16         threading.Thread.__init__(self)
  17         self.running = 1
  18         self.handler = handler
  19         self.queue   = Queue.Queue()
  20         self.stopper = StopMarker()
  21     
  22     def run(self):
  23         """Worker loop. Errors in the handler are printed to
  24         stderr and the thread continues with the next item."""
  25         while self.running:
  26             try:
  27                 item = self.queue.get()
  28                 if item is self.stopper:
  29                     break
  30                 else:
  31                     self.handler(item)
  32             except:
  33                 traceback.print_exc()
  34     
  35     def stop(self):
  36         """Stop the worker thread and wait until it terminates.
  37         (Waits until last item is processed)"""
  38         self.queue.put(self.stopper)    #stopper item, then...
  39         self.join()                     #wait until the thread has shutdown
  40 
  41     def put(self, item):
  42         """Put an item in the queue to be processed by the handler."""
  43         self.queue.put(item)
  44 
  45 if __name__ == '__main__':
  46     def printer(item):
  47         print "printer(%r)" % item
  48     
  49     w = Worker(printer)
  50     w.start()
  51     for i in range(10):
  52         w.put(i)
  53     w.stop()
```
:::
::::

= Call to C function blocks all threads! !La chiamata ad una funzione C blocca tutti i processi=

I have a C module that does database queries. Those queries go off to an SQL server to be processed. I would like to use my query function within threads and to have it work like `time.sleep()`, that is, block the current thread until it finishes but allow other threads to continue operation. I haven\'t seen this issue addressed in any of the books I have.

Ho un modulo C che pone delle interrogazioni ad un Databases. Queste queries pongo a fermo un server SQL per essere processate. Voglio usare le mie funzioni querry all\'interno dei processi e avere il lavoro come `time.sleep()`, se stesse in pausa, blocco il corrente processo finchè questo non ha finito, ma permetto ad altri processi di continuare le loro operazioni. Non vedo questa asserzione pubblicata in nessuno dei libri che possiedo.

- *This can\'t be handled in Python code. The author of the database module should use Py_BEGIN_ALLOW_THREADS and Py_END_ALLOW_THREADS around blocking calls to permit other threads to run.*

\" Ciò può essere attuato con il codice python. L\'autore del D.B.

# Resources 

- \[[http://starship.python.net/crew/aahz/OSCON2001/index.html](http://starship.python.net/crew/aahz/OSCON2001/index.html) Aahz OSCON 2001 presentation

- Italian version of this page: Processo Programma
