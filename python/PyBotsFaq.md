# PyBotsFaq

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Question 

Does a project have to already be using buildbot to use this community buildbot? I\'m still more than a bit fuzzy on how the whole thing is supposed to work. Suppose I decided to help out project Foo, an application written in Python. Does project Foo have to already have drunk the buildbot Kool Aid or can I take that task on, assuming they already have some sort of unit test framework?

### Answer 

No, you don\'t need to drink any buildbot Kool Aid at all ![:-)](/wiki/europython/img/smile.png ":-)")

The idea is this: let\'s say you work on project Foo, or decide to help project Foo. You just need to figure out how to run project Foo\'s unit tests from the command line. Once you have a shell script or python script that does that, my [instructions](http://agiletesting.blogspot.com/2006/08/setting-up-pybots-buildslave.html) show you how to set up a buildslave that runs that script every time a checkin is made into Python trunk, using the newly built Python binary. This way, both project Foo\'s developers and the Python core developers will know if things suddenly start breaking in project Foo because of new/modified code in Python trunk.

### Question 

I\'ve downloaded buildbot and made a buildbot.tac. I\'ve also made a python-tool directory and an empty run_tests.py file. Now what? From the [instructions](http://agiletesting.blogspot.com/2006/08/setting-up-pybots-buildslave.html), it\'s not entirely clear to me what I should do next. What packages should I be testing? Can I keep those separated from my \"normal\" Python install? Some more help would be appreciated.

### Answer 

Your run_tests.py script is supposed to check out the latest source code for that project (or the latest tar.gz and unpack it), then run the automated test suite that the project provides. If the project doesn\'t have an automated unit test suite (or functional tests), then it\'s not a good candidate for inclusion in the pybots. The main thing we\'re achieving here is that those automated tests will be run via a newly-built python binary. The binary will be built on your buildslave machine via commands that will be sent from the master to the slave. You don\'t need to do anything special on your slave for that. The new binary will be installed in /tmp/python-buildbot/local/bin/python, so we\'ll run your run_tests.py script via:

    /tmp/python-buildbot/local/bin/python run_tests.py

### Question 

I have several projects that I\'d like to test, but I don\'t want to configure a buildslave for each project \-- instead, I\'d like to run the tests as separate build steps on a single buildslave. Is this possible?

### Answer 

Yes, it is.

If you want to test project_A and project_B on your buildslave, all you need to do is change your run_tests.py script so that it accepts an extra argument from the command line. That argument will be \"project_A\" for the build step involving project_A, and \"project_B\" for the build step involving project_B.

For example, Sanghyeon Seo (who was the initiator of the multiple-step feature) wanted to run tests for both docutils and roundup on the same buildslave. His run_tests.py script is prepared to run the docutils tests if it receives \"docutils\" as the first argument on the command line, and run the roundup tests if \"roundup\" is received.

### Question 

I\'d like to be able to run the \'prepare\' script (the one that installs the pre-requisites for the package I want to test) as a separate build step in my buildslave. How do I do this?

### Answer 

The way this works is that the buildmaster will send the command \"run_tests.py prepare\" to your buildslave. You run_tests.py script will have to be able to interpret the \'prepare\' command line argument and launch the appropriate pre-requisite installation script.

Thanks to Manuzhai for asking for this feature ![:-)](/wiki/europython/img/smile.png ":-)")

### Question 

What would be the procedure for releasing a new version of project Foo to the pybots system?

### Answer 

The way pybots is running the Twisted unit tests is: the Twisted buildslave checks out the latest Twisted code from the Twisted svn repository, then it uses the newly built python binary to run them. It\'s detailed in these [instructions](http://agiletesting.blogspot.com/2006/08/setting-up-pybots-buildslave.html).

If you prefer to test a released package against the latest python binary, we can do that too. The pybots buildslave just needs to know where to get the package from, then it can unpack it and run its automated tests. Basically, anything you can do from the command line, you can also run within a buildslave.

### Question 

How do you get the various buildslaves to update the run_tests.py and prepare_packages.sh files or are these pushed to the slaves by the buildmaster?

### Answer 

The only thing that the master knows about is the name of the script that will run the automated tests on each buildslave. The content of the script is totally up to the owner of the buildslave, so any updates happen on a slave-by-slave basis.

The master doesn\'t push any scripts to the slaves, it only sends them commands to run certain scripts. So you can customize your run_tests.py script to do whatever you need. The prepare_packages.sh script is an example of a customization: I needed to install the prerequisite packages for Twisted using the newly-built python binary. You might not need this.

### Question 

We\'d be interested in getting project Foo into the pybots test builds and would also contribute a buildbot if we can get some idea of the security implications this would have.

### Answer 

Buildbot is based on the idea is that the buildmaster machine sends commands to the buildslave, which then executes them and reports back to the master. One security implication is the authentication between master and slave. This is done via a slave name and password. The slave name can be gleaned from the buildbot HTML status page, but the password of course is secret. So you would be protected against somebody posing as a master and trying to send you commands.

The other security implication is that there is a \"Force build\" button on the Web interface, which by default can be pressed by anybody. This can be disabled easily, or it can be configured so it requires authentication.

### Question 

OK, but I am still a little worried about the possibility of using the build machine for purposes such as e.g. sending out spam mail. After all, the buildbot system is per definition a bot net ![:-)](/wiki/europython/img/smile.png ":-)")

Is there some level of control as to what gets executed on the build slaves?

### Answer 

The build slaves only run the commands that are specified as build steps in the buildmaster configuration file. Everything is controlled on the buildmaster. The buildslave will not run any other commands, so there is no danger of somebody using your buildslave to run random commands.

### Question 

I don\'t have a project Foo right now. Do you know of a couple candidates?

### Answer 

Maybe pick one of your favorite Python packages, and take it from there\.....Anything at all really would be very well received into the pybots project ![:-)](/wiki/europython/img/smile.png ":-)") I\'d really like to get some momentum going, so the more people support the project, the better chance it will actually get somewhere\....

One suggestion though: how about running the automated tests for your favorite Web framework? Django, or [TurboGears](TurboGears) for example. In the case of TG, it would actually be very interesting to run the tests for the individual packages that make up TG\....And maybe it will encourage the Web framework developers to donate more buildbots for other platforms\...
