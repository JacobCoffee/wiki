# BrianvandenBroek

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Welcome to my page 

I\'m not a IT or programming professional, and am only a hobbyist programmer. Python is proving to be a great source of \"other things to do\" when I\'m not feeling like working on my thesis which should be finished *any day now*. (I\'m a PhD student in Philosophy.)

The most valuable Python resource for beginner\'s that I know is the [PythonTutorList](../archive/PythonTutorList).

I\'ve recently been trying to start a public project as an off-shoot of, or supplement to, the [PythonTutorList](../archive/PythonTutorList). The idea, called the Tutor Code Clinic until someone comes up with something better, is for interested folks to pick a smallish project (such as those found at [http://nifty.stanford.edu](http://nifty.stanford.edu)) write up code for it, and then exchange the code and give each other critiques and comments. It seems worth doing as separate from Tutor as the possible length of code and sustained focus on one task seem to me to run the risk of getting in the way of Tutor\'s mission. A number of people expressed interest both on the Tutor list and by writing me directly.

Originally, I thought to put up a dedicated wiki page for it. But, until I see if it comes off and how successfully, that seems premature. Knowing I\'d want a wiki page here anyway, I started my wiki homepage and I think it is best for now to use this space. If you\'ve come here to participate in planning for the first Code Clinic, there is a section for that below. Please, feel free to contribute. (As in, don\'t think, \"Well, its his homepage, so I better not edit it.\")

# The Tutor Code Clinic 

Glad you are interested! I\'ve split this into subsections to try to give some direction. But I\'m not a czar, so, feel free to grab the wheel and steer in different directions. I do think it would be best though if people signed their contributions. Crunching first name and last name together like BrianvandenBroek will make a wiki link, so, if you don\'t want that, space as normal.

Right now, the idea is in its nascent stages. I regret that I choose mid-December as the time to try to get this up and going, but there you have it.

The main questions to address are:

1.  Choice of coding task
2.  Time frame until we start sharing code.
3.  Communication
4.  Other issues.

## Choice of task 

To keep a clear focus, I\'d suggest that the first task at least should be drawn from [http://nifty.stanford.edu](http://nifty.stanford.edu). There are other similar sites, and I will put links here if we get momentum.

I\'m open to any task. The point for me is the exchange, rather than the actual task worked on. I like [http://nifty.stanford.edu/2003/randomwriter/](http://nifty.stanford.edu/2003/randomwriter/) \-- it is a fun idea, and fairly small and simple. But any will do. Suggestions? Votes? \-- BrianvandenBroek

I Second [RandomWriter](./RandomWriter.html) it looks the most interesting of the ones on that page. Particuarly for the sharing of code because it will be interesting to see different approaches. Should we try and have something like phase 1 evaluation done by January 4th? The Link to the Adventures of Tom Sawyer is [http://www.gutenberg.org/dirs/7/74/74.txt](http://www.gutenberg.org/dirs/7/74/74.txt), this way we can all use the same text file to test against. This is from Project Gutenberg. \-- [ChadCrabtree](ChadCrabtree)

Hey Chad, thanks for the contribution! How about this? We give it 2 more days to see if anyone else speaks up. If not, I will post the tasks and time frame as your paragraph suggests to [PythonTutorList](../archive/PythonTutorList) and invite any one interested to join us. \-- BrianvandenBroek

I am in favor of the project and the time frame that Chad proposed. I have my first level code ready (it seems to work at least\...). Where will we post the code once the 4th rolls around? \-- [ChristianWyglendowski](ChristianWyglendowski)

OK, it seems like it is just the three of us that are interested. Rather than fussing with a place to post, how about we just email between ourselves? Less bother, plus it prevents an assignment from having a googleable answer up on the web for the plagiarists of the world to submit as their own work. I\'m a half-hour of polishing from being ready to send what I have. Christian seems similarily situated. So, Chad, when you\'re ready, we can start reading each others efforts. I also suggest that we just do it, without announcing. A number of people expressed interest and then faded-out. No harm, and I get that life can be a barrier. But the fade-out rate makes we want to just get on with it. What would you guys say about just doing this, and seeing how it goes? If it seems worth repeating, we can pick another one with a timeframe and post to the [PythonTutorList](../archive/PythonTutorList) to invite others to join then. \-- BrianvandenBroek

Just wanted to pipe in that I\'m ready to share my code. My biggest learning curve was this; `string.split(sep)` WILL give blanks in it\'s list from time to time AND `item[:1]` will NOT filter them out \... Oh well. \-- [DavidBroadwell](DavidBroadwell)

I\'m off for a few days in a couple of hours; I\'m ready to share by the 31st. \-- BrianvandenBroek

Ok. I just sat down and did this, I finally had the time and gumption do to so. [http://www.imperialdata.net/randomwriter.txt](http://www.imperialdata.net/randomwriter.txt). I got it done in about 5-6 hrs. Mostly I spent time getting the performance up. I look forward to hearing from you guys. If you like I can set up an anonymous ftp site to share the code, just email me. [chad.crabtree@imperialdata.net](mailto:chad.crabtree@imperialdata.net) \-- [ChadCrabtree](ChadCrabtree)

I\'m ready, too. Do you think an ftp is needed, Chad? Others? I\'d thought just to email, but if people would rather that way, I can go with the flow. \-- ??

Well I updated my analysis and looked it over. I\'m very sorry about the bad writing on the first one I have included Brian\'s effort and a commentary. Check it out on my page. \-- [ChadCrabtree](ChadCrabtree)

I see a use for classes that I hadn\'t before, that will having me useing them every time. I always write multiple versions of things, with classness I can keep it in the same library. But I have more reading to do, Also, See communication notes. \-- [DavidBroadwell](DavidBroadwell)

I made a subclass to implement a caching/indexing design like Chad did. It certainly is faster for large output values. What would be really cool would be to implement different \"engines\" that would be loaded depending on output size. That way a simple non-caching engine could handle small outputs while the caching version could deal with the large outputs. Anyhow, my subclass is on my wiki page. \-- [ChristianWyglendowski](ChristianWyglendowski)

## Time Frame 

The Nifty Assignments are meant to be doable for an undergrad with a full course load in 1 or 2 weeks. To keep momentum, I think a similar time frame would be good. But, given the holiday season (I\'m writing December 19th), and some other constraints I have between the 25th and New Year\'s, either we start pretty well right now, or aim to share code early in the year. \-- BrianvandenBroek

## Communication 

It would be easier with a dedicated mailing list. I will soon ask my university to set me up a listserve. But I\'m not sure they will go for it. Last summer, when I taught a course, the computing services department went for that, but I couldn\'t, even as a course prof, get allocated any web-space. So, we will see. Maybe a yahoo group? \<blech!\>

For now, people can put their emails up here (be sure to obscure them from the spambots!) or send me an email by writing to the gmail.com account with the words between Brian and Broek just as it appears in my [WikiName](WikiName). \-- BrianvandenBroek

On the issue of [MailingList](./MailingList.html) and \~maybe\~ [WebSpace](./WebSpace.html). My web page is a celebration of lack of content and my mail server mostly idling except for being used as a IM server. In the interest of thumbing our collective noses at yahoo, what would we want the mailing list to be called? \-- [DavidBroadwell](DavidBroadwell)

I would be willing to setup a \"community site\" using [drupal](http://www.drupal.org) or [plone](http://www.plone.org) on my server. I would lean towards drupal since it is so easy, but then it is based on PHP and this is a python group ![:-)](/wiki/europython/img/smile.png ":-)") Thoughts? \-- [ChristianWyglendowski](ChristianWyglendowski)

## Other Issues 

Make a proper and dedicated wiki page? Other things? \-- BrianvandenBroek

# Links I like 

# Leave a Comment 

Please deface this space.

\...

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
