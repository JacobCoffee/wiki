# ManutenereLeEccezioni

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Manutenere le Eccezioni 

Un semplice modo per manutenere le eccezioni è usare il blocco \"try-except\" \--\> \"prova all\'innfuoridi\"

:::: 
::: 
``` 
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError:
   5   print "divide by zero"
```
:::
::::

Se volete esaminare l\'eccezione dal codice,guardate qua:

:::: 
::: 
``` 
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError, e:
   5   z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
   6 print z # output: "integer division or modulo by zero"
```
:::
::::

## Prendiamo il controllo generale del codice 

Talvolta,potete prendere \"all\" tutti gli errori che è possibile generare, ma di solito non è possibile.Nella mag- gior parte dei casi,quanto specificate tanto è possibile ([CatchWhatYouCanHandle](http://c2.com/cgi/wiki?CatchWhatYouCanHandle "Wiki")). Nel primo caso, se stavate usando una clausola eccezione incontrata e l\'utente ha premuto Ctrl-C,generando una [KeyboardInterrupt](./KeyboardInterrupt.html) (interruzione da tastiera),non desiderate che il programma emetta il messaggio \"divide by zero\"\--\> (divisione per zero.)

Tuttavia,ci sono alcune situazioni in cui è meglio prendere *all* tutti gli errori

Per esempio, supponiamo che scriviate un modulo per un servizio web. Vorrete che le informazioni inerenti gli errori sia riportate in una pagina web, e il server continui a girare,se tutto ciò è possibile.Ma voi non avete idea che tipo di errori dovete mettere nbel vs codice.

In una situazio9ne di questo tipo,il codice potrebbe essere simile a questo:

:::: 
::: 
``` 
   1 import sys
   2 try:
   3   untrusted.execute()
   4 except: # catch *all* exceptions
   5   e = sys.exc_info()[1]
   6   write_to_page( "<p>Error: %s</p>" % e )
```
:::
::::

[MoinMoin](MoinMoin) software è un buon esempio su dove in generale catturare gli errori. Se scrivte MoinMoin macro estensione,e diamo avvio ad un errore,Moin*Moin prepareà un dettagliato rapporto circa l\'errore e la catena di eventi che conduce a lui. Il software Python deve essere abilitato a catturare tutti gli errori, e li spedisce poi alla pagina web.*

## Ricerca di Nomi Specifici di Eccezioni 

Eccezioni Standard che possono essere emesse sono dettaglaite in questo sito:

- [http://python.org/doc/lib/module-exceptions.html](http://python.org/doc/lib/module-exceptions.html)

Osservate la Classe documentazione per trovare che eccezioni una data classe può emeyttere.

# Vedi Anche 

Su questa [WritingExceptionClasses](WritingExceptionClasses), [TracebackModule](./TracebackModule.html).

Per idde generali(non specificate in Python) circa le eccezioni,consulatre [ExceptionPatterns](http://c2.com/cgi/wiki?ExceptionPatterns "Wiki").

# Per scrivere sull\'argomento\...\.... 

- Dammi un esempio di IOError, e interpretiamo il codice di errore
- Dammi un esempio di eccezioni multiple. Manteniamo le eccezioni multiple in linea
- Mostra come usare \"else\" e \"finalità\"
- Mostra come continuare con un \"rialzo\"

# Domande 

## Manutenzione generale degli errori 

Nella sezione \"manutenzione generale degli errori\", si è detto che per la cattura degli errori userete questo codice:

:::: 
::: 
``` 
   1 import sys
   2 try:
   3   untrusted.execute()
   4 except: # catch *all* exceptions
   5   e = sys.exc_info()[1]
   6   write_to_page( "<p>Error: %s</p>" % e )
```
:::
::::

Tuttavia in origine era:

:::: 
::: 
``` 
   1 try:
   2   untrusted.execute()
   3 except Exception, e:
   4   write_to_page( "<p>Error: %s</p>" % str(e) )
```
:::
::::

Alcune indicano che \"except\" catturano piu di un semplice \"except Exception, e.\"

Perchè è questo il caso??.Qual è la differenza? *\--[LionKimbro](LionKimbro).*

Per ora ( nella ver. 2.3) l\'eccezionempm ha ereditato da Exception. Allora pianifichiamo \'except:\' catturiamo tutte le eccezioni,non solo quelle di sistema. \-- [MikeRovner](MikeRovner) 2004-01-19 05:49:19

## Prendiamo utili Informazioni da una eccezione 

Cosi si pò avere qualcosa di simile:

:::: 
::: 
``` 
   1 (a,b,c) = d
```
:::
::::

\... e Python soffia indietro

    ValueError: unpack list of wrong size

\.... e cosi,naturalmente chiederete, \"bene che, cosa \'era\' in `d`?\"
