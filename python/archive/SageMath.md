# SageMath

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# SageMath 

SageMath or Sage is an open source implementation of mathematics and scientific software based on Python. On this page I am using SageMath as a general term for several different but closely related things:

## SageMath General 

Generically SageMath is Python plus a lot of math and science extensions plus some SageMath specific extensions. What does it do? Since it is Python, it does most of what Python does, and of course there are extensions. Some of the extensions are math/science extensions so it does what [NumPy](./NimPy.html), Mathplot\.... do\....( for a list of modules included see: [http://www.sagemath.org/links-components.html](http://www.sagemath.org/links-components.html) )

And it does all sorts of math, both numeric and symbolic. This includes:

- Algebra
- Limits
- Taylor Series
- Graphing
- and on and on

SageMath really wants to run in Linux with a some sort of interface to Python ( something like iPython is good because SageMath is designed to be useful in an interactive mode ) so some of the installation methods are simply a intall on a Linux box using the usual facilities that one uses with Python. I cannot really say much more because I have not done these types of installs or used it in this kind of environment. Perhaps someone more familiar with this can update this wiki. To find more information go to: [http://www.sagemath.org/index.html](http://www.sagemath.org/index.html) or you may also find [https://help.ubuntu.com/community/SAGE](https://help.ubuntu.com/community/SAGE) useful. The is also a bootable flash drive version ( also not tried by me ) see: [http://wiki.sagemath.org/SageLiveUSB](http://wiki.sagemath.org/SageLiveUSB)

## SageMath Notebook 

In this version the user uses a web browser to access \"Worksheets\". A worksheet is a series of cells each of which contains some Python code. Each cell can be executed seperately with the output appearing below the cell. Worksheets can be saved, opened, downloaded, etc.. Technically the notebook has a web server component which runs either on a seperate machine from the client, or on the same machine.

There are some free public servers for running the notebook, for example see [http://www.sagenb.org/](http://www.sagenb.org/) or you can set up your own server. Generally you need to register to get an account.

Setting up your own server can be a bit of a task. On windows, however, there is a simple method: your install a virtual machine, then install an image of a linux notebook server. It is quite easy. See: [http://www.sagemath.org/download-windows.html](http://www.sagemath.org/download-windows.html)

## SageMath Cloud 

This version is similiar to the SageMath Notebook but runs on a beefed up server and offers beefed up services which I will describe later. It is currently in beta release, seems pretty functional.

Work with Sage, or run Python, R, GAP, M2 and more in the Cloud. See: [https://cloud.sagemath.com/](https://cloud.sagemath.com/)

## Single Cell 

A publically availble, no logon site [http://sagecell.sagemath.org/](http://sagecell.sagemath.org/) offers one cell of SageMath computation. [http://sagecell.sagemath.org/](http://sagecell.sagemath.org/)

You can type in one cell and then evauate, say :

plot( x\^2, x, 0, 10 )

or

equ = sin( x) == 1/2

print equ.solve( x )

[http://www.sagemath.org/eval.html](http://www.sagemath.org/eval.html) has a cell with a simple way of giving you examples.

In running on the web there are some limitations relative to running on your own machine. I am not entirely clear on how extensive they are but seem to stem from the fact that since SageMath is server based you do not have as full control over the server as you do over a machine sitting on your lap.

## Other Links 

- Master link to the head of the river: [http://www.sagemath.org/](http://www.sagemath.org/)

- It has its own wiki: [http://wiki.sagemath.org/](http://wiki.sagemath.org/)

- Wikipedia has a good write up: [http://en.wikipedia.org/wiki/Sage\_(mathematics_software](http://en.wikipedia.org/wiki/Sage_(mathematics_software))
