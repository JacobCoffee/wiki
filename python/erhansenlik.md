# erhansenlik

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    # -*- coding: cp1254 -*-
    #random number generation
    import random
    f=open("ran.dat","wr")
    n=int(raw_input("kaç tane rasgele sayı istersiniz\n"))
    for i in range(n):
        x=random.random()
        y=str(x)
        z=str(i)
        print x
        f.write(y),f.write("\n")
        if i == n-1 :
            print x
            f.close()
    import Numeric
    import Gnuplot,Gnuplot.funcutils
    g=Gnuplot.Gnuplot(debug=1)
    g('set grid')
    g.plot("'ran.dat' with linespoints")
    g('set terminal png')
    g('set output "random.png"')
    g.plot("'ran.dat' with linespoints")
