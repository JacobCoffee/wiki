# Semplici Programmi versione Italiana

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Inserire una descrizione per [SimplePrograms](SimplePrograms) = Semplici Programmi versione Italiana.

Questa pagina dovrebbe aiutare i neofiti italiani, mediante la propria lingua madre, ad imparare il linguaggio di programmazione **Python**. Zio google nella sua infinita bontà, quando effettua una traduzione oltre a tradurre l\'inglese, traduce anche il codice dei programmi. Se ciò può aiutare noi Italiani a comprendere meglio ciò che deve fare il programma, e mi riferisco in particolare modo ai commenti, ci mette in crisi perché la traduzione anche delle istruzioni python rendono ineseguibile il programma stesso. Se poi si utilizza un altro browse che non fa la traduzione istantanea, per chi ha problemi con l\'inglese, ha l\'onere di tradursi i commenti. Quindi, mi permetto di tradurre in lingua italiana la pagina wiki [SimplePrograms](SimplePrograms). Qualcuno potrà osservare che ho tentato di modificarla, non lo nego, volevo attuare il mio intento di aiutare i miei connazionali, ma poi mi sono reso conto che avrei fatto un torto a tutti quelli che non conosco l\'italiano. Ho quindi rimesso le cose a posto per cui ora esistono due pagine il cui contenuto è pressoché simile ma del tutto identiche nel codice salvo i commenti. Quest\'ultimi sono rimasti nella versione originale in inglese. Ma se un italiano consulterà quella pagina e cioè \[[SimplePrograms](SimplePrograms)\] usando Zio google la troverà tradotta in Italiano. Se invece consulterà la pagina [SempliciProgrammi](./SempliciProgrammi.html) versione Italiana con altri browse diversi da Zio google la leggerà tutta in un Italiano chiaro e semplice.

Bene ora bando alle chiacchiere e cominciamo!

Ecco alcuni semplici programmi esempio. Non esitate a contribuire, ma, per favore, attenetevi a quanto detto dall\'autore a fondo pagina.

Per Questi esempi ho supposto che si stia usando la versione v 2.6 o successive di Python. Posso assicurare che funzionano, basta semplicemente fare copia / incolla del codice in un file (chiamato per esempio test.py ) e poi mandare in esecuzione con python test.py.

- 

------------------------------------------------------------------------

1 linea: Codice

:::: 
::: 
``` 
   1 print 'Ciao, MONDO!'
   2      ---->> uscita sullo schermo    Ciao, MONDO!
```
:::
::::

- 

------------------------------------------------------------------------

2 linee: Input e assegnazione

:::: 
::: 
``` 
   1 name = raw_input('Ciao, come ti chiami?\n')
   2 print 'Mi chiamo , %s.' % name
   3     ---->> uscita sullo schermo    MI chiamo  [ tuo nome ]
```
:::
::::

------------------------------------------------------------------------

3 linee: Ciclo For , Funzione interna enumerate , nuovo stile di formattazione

:::: 
::: 
``` 
   1 amici = ['gianni', 'patrizia', 'sergio', 'michele']
   2 for i, nome in enumerate(amici):
   3     print "all'indice  {indice} corrisponde il nome {nome}".format(indice=i, nome=nome)
```
:::
::::

- 

------------------------------------------------------------------------

4 linee: Fibonacci, assegnazione di una tuple

:::: 
::: 
``` 
   1 genitori, bambini = (1, 1)
   2 while bambini < 100:
   3     print 'Questa generazione ha  {0} bambini'.format(bambini)
   4     genitori, bambini = (bambini, genitori + bambini)
```
:::
::::

- 

------------------------------------------------------------------------

5 lines: Functions

:::: 
::: 
``` 
def greet(name):
    print 'Hello', name
greet('Jack')
greet('Jill')
greet('Bob')
```
:::
::::

- 

------------------------------------------------------------------------

6 lines: Import, regular expressions

:::: 
::: 
``` 
import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'
```
:::
::::

- 

------------------------------------------------------------------------

7 lines: Dictionaries, generator expressions

:::: 
::: 
``` 
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill
```
:::
::::

- 

------------------------------------------------------------------------

8 lines: Command line arguments, exception handling

:::: 
::: 
``` 
#!/usr/bin/env python
# This program adds up integers in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print 'sum =', total
except ValueError:
    print 'Please supply integer arguments'
```
:::
::::

- 

------------------------------------------------------------------------

9 lines: Opening files

:::: 
::: 
``` 
# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print '    ------' + file_name

    with open(file_name) as f:
        for line in f:
            print '    ' + line.rstrip()

    print
```
:::
::::

- 

------------------------------------------------------------------------

10 lines: Time, conditionals, from..import, for..else

:::: 
::: 
``` 
from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
```
:::
::::
