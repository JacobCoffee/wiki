# DistributeSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

In order to continue the effort started in distutils-ML. We are organizing a distutils PEP sprint with people that works differently to deliver Python applications.

- using virtualenv
- using zc.buildout/setuptools
- using scons
- using the debian packaging system
- using the fedora packaging system

If you want to join, please do !

- Where: remote sprint, #distutils on freenode
- When (proposed date) :
  - Thursday, 2 oct. 9 a.m. CEST

  - Friday, 3 oct. 9 a.m. CEST

  - Saturday, 4 oct. 9 a.m. CEST

  - [http://timeanddate.com/worldclock/meeting.html](http://timeanddate.com/worldclock/meeting.html)

# Participants 

name / skills / desired date

- Tarek Ziadé / zc.buildout, some distutils and setuptools internals / Any of the three dates

- Toshio Kuratomi / Fedora Packaging, some paver, setuptools consumer / Thursday, Friday but none of the times ![:-(](/wiki/europython/img/sad.png ":-(") 7:00AM my time == 4:00PM CEST == 14:00 UTC. I could meet from that point on? Alternately, I could be online at 5:00UTC until I fall asleep.

# Tasks that will be covered 

- make a synthesis of all the threads that have discussed distutils previously

- work on the Python Metadata definition (PEP 345, see [http://www.python.org/dev/peps/pep-0345](http://www.python.org/dev/peps/pep-0345)) and see if some improvments could be done in it.

- work on a proposal to see how these metadata could be defined in the package, besides setup.py, and let external tools read them.

- work on a proposal to structure the content of packages

- list the problems in compilation matters and work on a proposal to improve it

# Desired output 

We would like to come up with enough material to write a meta-PEP and a series of PEP. These PEPs will then be submitted in the distutils-SIG mailing list for further discussions.
