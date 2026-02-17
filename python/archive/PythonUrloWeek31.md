# PythonUrloWeek31

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    [python-urlo;)] Newsletter di notizie e links sul Python [08 Aug 2003]
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Questa newsletter e' la decima della serie ed e' stata scritta da Nicola Paolucci in collaborazione con Luca Simonetti.

    Tutte le newsletter sono archiviate all'indirizzo http://www.python.it/python-urlo/.

    Attenzione, questa newsletter e' stata scritta usando reStructuredText_ che trovate all'indirizzo http://docutils.sf.net/rst.html . Tutta la strana punteggiatura in questo testo e' probabilmente markup per rST_; potete ignorarla senza problemi.

    .. _rST:
    .. _reStructuredText: http://docutils.sf.net/rst.html

    .. contents::

    ================================
    Citazione della Settimana (QOTW)
    ================================

    ::

        [about significant whitespace, dynamic typing, interpreted:]
        What's more, these are three of Python's greatest *strengths*. We
        resist all attempts to change these, and we (at least I) avoid other
        languages because they do not supply these features."
                                    -- Gary Herron

    ===========
    Discussioni
    ===========

    Le discussioni altamente interessanti su comp.lang.python e python-dev si sprecano, riporto solo brevissimi frammenti che mi sono preso la briga di segnare questa settimana:

    Fredrik Lundh mostra `come decomprimere una stringa gzippata`__ (per esempio ottenuta da un server HTTP che supporta la compressione).

    __ http://groups.google.com/groups?threadm=mailman.1059589546.1179.python-list@python.org

    Raymond Hettinger rende nota `una nuova pagina nella doucumentazione`__ del Python a proposito dell'unit testing. Mostra come eseguire i test direttamente invece che dalla riga di comando.

    __ http://groups.google.com/groups?threadm=w3DWa.2211$W%3.861@nwrdny01.gnilink.net


    =====================
    Notizie e link sparsi
    =====================

    `Presentazione di Chandler`__ e della sua roadmap all'ultima OSCON.

    __ http://www.osafoundation.org/presos/OSAFatOSCon2003.pdf

    `Come mandare Trackbacks`__ in Python. Le Trackback sono usate ultimamente per creare link istantanei tra weblogs.

    __ http://roughingit.wari.org/python/tutor/sendingtrackback

    `Programmazione dichiarativa e mini linguaggi`__ di David Mertz.

    __ http://www.onlamp.com/pub/a/python/2003/07/31/declarative_python.html

    Tutorial su `Networking con Twisted`__ presentato a OSCON 2003. Se avete problemi a capire la maniera "Twisted" di fare le cose ve lo consiglio caldamente ! Anche se sono slide concise spiega molto bene alcuni concetti chiave del framework.

    __ http://itamarst.org/writings/OSCON03/twisted_internet-0.html

    E un'altro `Tutorial su Twisted`__ di poco precedente.

    __ http://itamarst.org/writings/pycon03/twisted_internet-00.html

    Fredrik Lundh da una `panoramica dei nuovi moduli della libreria standard`__ in Python 2.3

    __  http://effbot.org/zone/librarybook-py23.htm

    Conoscete la `PythonPhilosophy`__ ? Provate allora a fare:  ">>>import this" con Python 2.1.2 o successivo

    __ http://www.python.org/cgi-bin/moinmoin/PythonPhilosophy

    Ancora `Fredrik Lundh descrive il modulo bz2`__ per la compressione bzip2 (nuovo in Python 2.3)

    __ http://online.effbot.org/2003_08_01_archive.htm#librarybook-bz2-module

    Walter de Jong: un `modulo python-ipc`__ per l'utilizzo dei meccanismi di interprocessing communication sotto Linux(shared memory, semafori e code di messaggi).

    __ http://www.heiho.net/python-ipc/

    Carl Free Jr ci illustra il suo modulo `Simple Universally Unique ID (UUID or GUID)`__ .

    __ http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/213761

    ==============================================
    Notizie dal vecchio mondo della carta stampata
    ==============================================

    In questa sezione troverete quando possibile riferimenti ad articoli riguardanti Python usciti sulle riviste tecniche italiane e non(Se avete segnalazioni in proposito inviatele all'indirizzo indicato in calce alla nostra newsletter):

    * Questo mese nel numero 92 di Inter.Net compare un dossier dal titolo "Python e i suoi fratelli". E' una interessante comparazione tra Python ed i suoi diretti "concorrenti" Perl, PhP e Java. 

    =======
    Annunci
    =======

    `Annunciato Jython 2.2 alpha 0`__. E' una notizia di rilevo perche' lo sviluppo di Jython si era un po' seduto ultimamente ed e' bello vedere che lo sviluppo sia ripreso. La richiesta di Guido di aiutare il progetto sembra avere dato frutti. Non mi azzarderei ad usare questa versione ancora, a meno che non vogliate contribuire al progetto.

    __ http://jython.sourceforge.net/

    Rilasciata la release 0.7 di `PyTables`__ una pacchetto molto interessante per l'elaborazione e l'analisi di grandi quantità di dati (usato per applicazioni di meteorologia, oceanografia, astronomia, etc.) 
    Al riguardo è anche disponibile una presentazione del modulo fatta a `EuroPython2003`__ all'indirizzo http://www.europython.org/sessions/talks/slidespapers .

    __ http://www.python.org/pypi?:action=display&name=PyTables&version=0.7
    __ http://www.europython.org/

    Una compagnia di San Diego cerca `programmatori Python per sviluppare due giochi massivamente multigiocatore`__.

    __ http://groups.google.com/groups?selm=mailman.1060307942.15812.clpa-moderators%40python.org

    `Anobind 0.5.0`__ e' una libreria per il Python/XML data binding, in sostanza un'API per l'XML molto Pythonica.

    __ http://uche.ogbuji.net/tech/4Suite/anobind

    ------------------------------------------------------

    Tutto quello di cui hai bisogno e' probabilmente a uno o due click
    di distanza dalle pagine seguenti:

       Il `Sito del linguaggio Python`__ e' il tradizionale centro di
       Pythonia.
       
    __ http://www.python.org

       Nota bene specialmente le FAQ__
       
    __ http://www.python.org/doc/FAQ.html

       Il `Sito italiano del linguaggio Python`__  e' il punto di partenza
       per i Pythonisti di lingua italiana.
       
    __ http://www.python.it
       
       E rispettivamente le `FAQ in italiano`__.
       
    __ http://www.python.it/faq/index.html

       Un complemento alla newsletter che state leggendo e' il
       `daily python url`__ aggiornato costantemente da PythonWare.
       
    __ http://www.pythonware.com/daily

       Mygale__ e' un webcrawler specializzato nel raccogliere
       articoli relativi a Python.
       Anche se e' cosmeticamente simile a `Daily Python-URL`__
       i due sono completamente differenti quanto a tecnologia e
       generalmente anche nei risultati.
       
    __ http://www.awaretek.com/nowak/mygale.html
    __ http://www.pythonware.com/daily

       comp.lang.python.announce__ e' dove viene annunciato nuovo
       software per il Python. Ricordatevi di leggere questo newsgroup
       almeno settimanalmente.
       
    __ http://groups.google.com/groups?oi=djq&as_ugroup=comp.lang.python.announce
       
       Brett Cannon continua la meravigliosa tradizione di scrivere
       `riassunti settimanali`__ dell'attivita' della mailing list python-dev.
       
    __ http://www.python.org/dev/summary/

       Il `Python Package Index`__ cataloga i pacchetti.
       
    __ http://www.python.org/pypi/

       `Vaults of Parnassus`__ ambiziosamente raccoglie collegamenti ad
       ogni sorta di risorse per il Python.
       
    __ http://www.vex.net/~x/parnassus/

       `Python FAQTS`__

    __ http://python.faqts.com/

       Gli archivi della newsletter `Python-URL!`__ .
       
    __ http://www.ddj.com/topics/pythonurl/

       Gli archivi di questa newsletter si trovano all'indirizzo
       http://www.python.it/python-urlo

       Suggerimenti/correzioni per il numero della settimana prossima
       sono sempre benvenuti. Possono essere indirizzati a python-urlo[chiocciola]python.it

       Questa newsletter e' stata realizzata con e reST_.

    .. _reST: http://docutils.sourceforge.net/rst.html 
