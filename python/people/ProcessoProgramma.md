# ProcessoProgramma

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*\[note: Ho raccolto il nome di questa pagina da un dizionario su internet . Come tale \[,questa pagina,\]può contenere degli errori, di grammatica o di altro genere. Se tu conosci L\' Italiano meglio di me, ti prego di rinominare questa pagina (anche a ritroso,se del caso).\]*

Titolerei questo programmino = Blocco dei processi = tengo a precisare una cosa: Al fine di poter usare le lettere accentate che nell\' orignale del linguaggio inglese non sono riconosciute, e quindi nemmeno nei commenti all\'interno del codice, e se lo facessi senza la giusta indicazione il parser segnalerebbe un errore, devo scrivere subito dopo la prima riga, che a tutti è nota e cioè #! /usr/bin/python , questa indicazione: **\# -\*- coding: utf-8 -\*-** . In tal modo posso tranquillamente usare nei commenti le lettere accentate che si usano nel linguaggio classico Italiano. Aggiungo ancora un messaggio per l\'autore di questa pagina **mi congratulo per la sua conoscenza dell\'Italiano** e vorrei prendere contatto con lui per dialogare su python e tutto quanto concerne questo fantastico linguaggio di programmazione. Può scrivermi qui [vonkes@gmail.com](mailto:vonkes@gmail.com) se vuole. Non entro nel merito del programma che segue ma mi permetterò ,eventualmente, di migliorare quei commenti che, forse, possono risultare poco chiari. Spero di non suscitare i risentimenti dell\'autore.

**Da questo punto in avanti è tutta opera dell\'autore**

Inizio questa pagina facendo una domanda. Come si può fermare un processo dall\'interno di un altro?

    # -*- coding: utf-8 -*-     #   vedi la intestazione di A.CHESSA
    #!python
    import threading
    import time

    class Worker(threading.Thread):
      def __init__(self, eventChannel, eventHandler):
        self.eventChannel = eventChannel
        self.eventHandler = eventHandler
        self.stopFlag = 0

      def shutdown(self):
        self.stopFlag = 1

      def run(self):
        self.stopFlag = 0
        while not self.stopFlag:
          event = self.eventChannel.waitEvent()  # blocking call  chiamata del blocco
          self.eventHandler.dispatchEvent(event)


    eventChannel = EventChannel()
    eventHandler = EventHandler()
    worker = Worker(eventChannel, eventHandler)
    worker.start()
    time.sleep(20)
    worker.shutdown()

Il problema è che `EventChannel.waitEvent()` è una operazione di blocco. Così se l\'evento non si verifica, allora il nostro lavoro non si fermerà mai. *(`EventChannel` e `EventHandler` sono classi che io ho inventato per questo esempio)*

## Suggerimenti 

- Utilizzando il metodo `shutdown()` si spingono alcuni innocui eventi nell\'evento channel

<!-- -->

      def shutdown(self):
        self.stopFlag = 1
        self.eventChannel.push_event(NullEvent())

- oppure usando Queue passiamo dei dati . Manipolare gli errori con il manipolatore ( e.g. stampa \[print\] poi alla console), mantiene vivo il processo

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-     #   vedi la intestazione di A.CHESSA
   2 import Queue, threading, traceback
   3 
   4 class StopMarker:
   5     """This is used as an individual stopper item.
   6         Uso questo [StopMarker] come un bloccatore individuale
   7     """
   8     
   9 class Worker(threading.Thread):
  10     """Get items from a queue and call the handler with the item.
  11     Errors in the handler are printed to stderr, the thread
  12     continues to run. 
  13         Prende gli articoli da queue e chiama il gestore degli errori con detto articolo.
  14         Gli Errori vengono poi stampati nel stderr dal gestore, il processo continua.  
  15     An individual stop marker is used, so you can pass everyting
  16     as item (including None).
  17     Un singolo marcatore stop è usato ,così pote passere qualunque cosa come articolo
  18     (incluso None).
  19     """
  20     
  21     def __init__(self, handler):
  22         """Initialize Thread object and worker.
  23             Inizializzo l'oggetto e il worker [il lavoratore] 
  24         """
  25         threading.Thread.__init__(self)
  26         self.running = 1
  27         self.handler = handler
  28         self.queue   = Queue.Queue()
  29         self.stopper = StopMarker()
  30     
  31     def run(self):
  32         """Worker loop. Errors in the handler are printed to
  33         stderr and the thread continues with the next item.
  34             Worke cicla. Gli errori sono stampati dal gestore nel stderr 
  35         ed il processo continua con l'articolo successivo.
  36        """
  37         while self.running:
  38             try:
  39                 item = self.queue.get()
  40                 if item is self.stopper:
  41                     break
  42                 else:
  43                     self.handler(item)
  44             except:
  45                 traceback.print_exc()
  46     
  47     def stop(self):
  48         """Stop the worker thread and wait until it terminates.
  49         (Waits until last item is processed)
  50            Ferma il compito del lavoratore e aspetta finchè lui ha terminato
  51         (aspetta fino a che l'ultimo articolo viene processato
  52         """
  53         self.queue.put(self.stopper)    #stopper  item, then...  ferma l'articolo,........  
  54         self.join()                     #wait until the thread has shutdown aspetta finchè il compito è
  55                                            #completato
  56 
  57     def put(self, item):
  58         """Put an item in the queue to be processed by the handler.
  59             Spinge un articolo nella coda e poi lo fa processare dal gestore
  60         """
  61         self.queue.put(item)
  62 
  63 if __name__ == '__main__':
  64     def printer(item):
  65         print "printer(%r)" % item
  66     
  67     w = Worker(printer)
  68     w.start()
  69     for i in range(10):
  70         w.put(i)
  71     w.stop()
```
:::
::::

# Chiamata ad una Funzione \"C\" che blocca tutti i processi 

Ho un modulo in \"c\" che pone delle interrogazioni al D.B. Queste interrogazioni pongono ad off il server SQLper essere processato.Posso usare delle mie funzioni di interrogazione dentro i processi per avere un lavoro come questo `time.sleep()`,blocco il corrente processo finchè lui termina ma permette agli altri processi di continuare le operazioni. Non ho visto questi indirizzamenti in nessuno dei libri che possiedo.

# Risorse 

- [Aahz OSCON 2001 presentatione](http://starship.python.net/crew/aahz/OSCON2001/index.html)
