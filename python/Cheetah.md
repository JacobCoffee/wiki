# Cheetah

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A templating framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.cheetahtemplate.org/](http://www.cheetahtemplate.org/)

### Sample 

    <table>
       #for $client in $clients
          <tr>
             <td>$client.surname, $client.firstname</td>
             <td><a href="mailto:$client.email">$client.email</a></td>
          </tr>
       #end for
    </table>

### Deployment Platforms 

Templates are compiled to Python modules, with a Pythonic interface. The generated template module can also be used as a stand-alone program (which prints the text of the generated page), useful for instance to create a static HTML site. Templates are true Python objects, supporting inheritance and user-defined methods.

### InTheirOwnWords 

Cheetah is a Python-powered template engine and code generator. It can be used standalone or combined with other tools and frameworks. Web development is its principle use, but Cheetah is very flexible and is also being used to generate C++ game code, Java, SQL, form emails and even Python code.

Cheetah has a large and active user community. Products built with Cheetah are used by most of the Fortune 500. One prominent new user is reddit.com, a startup funded by Paul Graham.

"I\'m enamored with Cheetah" -Sam Ruby, senior member of IBM\'s Emerging Technologies Group & director of Apache Software Foundation

"Give Cheetah a try. You won\'t regret it. \... Cheetah is a truly powerful system. \... Cheetah is a serious contender for the \'best of breed\' Python templating." -Alex Martelli, Google uber techie, core Python developer & author of several popular Python books
