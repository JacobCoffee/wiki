# AdvocacyWritingTasks/Sprinting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This will be an article demystifying Development Sprints. We hope to publish it in a major journal in time to contribute to the PyCon 2008 publicity effort and to encourage first-time sprinters to take part.

Interview participants:

- **CD** is Catherine Devlin: never sprinted; interviewer
- **BC** is Brett Cannon: Python core sprint coach/participant
- **JB** is Jim Baker: Jython sprint co-coach/participant and first-time PyCon sprinter
- **JS** is Johnny Stovall: Professor of computer science and PyCon sprint participant then coach

**Begin interview**

*Open-source development often involves far-flung groups of developers working in different regions and countries. Increasingly, however, many projects find that their progress is enhanced by hosting occasional \"sprints\", which gather their developer communities into one place for short bursts of intense, face-to-face cooperation.*

*Despite their increasing popularity, sprints are still unfamiliar to many developers, who don\'t know enough about them to decide whether they should take part. We speak with veteran and rookie sprinters to get a better idea of what the sprinting experience is like for the individual participant.*

CD: Brett, Jim, and Johnny, can you start by telling us a little about your backgrounds?

JB: I\'ve been all over the place: academia, IT consulting, software development, software startups, and recently open source as a community - and not just a place to get generously-licensed quality software. As a result of asking some questions, I found myself leading the Boulder Python Users Group (FrontRangePythoneers), which lead into sprinting. What prompted that was that the Arlington Python User Group was sprinting, that looked quite interesting, and that eventually lead to our first sprint on Django. We have had several since then (BoulderSprint). The last was participating in the world-wide Django sprint. Our goal remains the same: everyone who walks in learns the project, and we get some usable contribution out of that day.

Finally, 12 years ago a friend suggested I use [Python](http://www.python.org). About 4 years ago, I finally heeded his advice. It became increasingly clear to me that writing software is many things. It includes not only communicating to the computer, it\'s also about communicating that intent to other developers. Python excels in combining code clarity with code conciseness. If you think about that, these are virtues especially valuable in a peer activity like sprinting.

My background more formally is over 15 years of industry experience, with roles including CTO, Chief Scientist, and Enterprise Architect. I have co-founded two startups in the business intelligence space, including one that raised \$10M in VC financing. I was also a software engineer on a business intelligence product when I first got out of school (not that we called it that marketing term back then, it was a multidimensional array database, with its own language not so different from [Matlab](http://en.wikipedia.org/wiki/MATLAB) or [NumPy](http://numpy.scipy.org/)). I\'m a graduate of Harvard (A.B.) and Brown (Sc.M.), both in Computer Science, and I also qualified for the Ph.D. at Brown. I\'m what you\'d call an ABD - all but dissertation.

BC: Currently, I am attending the University of British Columbia where I am working towards my Ph.D. in computer science (hopefully only two or so years left). I am researching some Java-related security stuff after trying for over a year to come up with a thesis topic that could involve Python. Previously I got my masters in computer science at California Polytechnic State University, San Luis Obispo (Cal Poly SLO for short). And before that I got my bachelors in philosophy at UC Berkeley. Basically I have been in school for a long time. =)

My involvement in Python started with me getting a pure Python implementation of time.strptime() accepted into the standard library in the summer of 2002 after I graduated with my bachelors. I enjoyed learning about Python and being on the python-dev mailing list so much that I started writing the Python-Dev Summaries that August and continued to do so until [PyCon](http://us.pycon.org) 2005. Got my commit privileges for Python the month after PyCon 2003 when Guido got tired of checking in patches for me. And as of PyCon 2006 I have been on the board of directors for the [Python Software Foundation](http://www.python.org/psf/). Python is basically what I do with my free time.

In terms of PyCon and sprinting, I have attended every PyCon since its inception. I have also sprinted on Python\'s core at every PyCon and been the coach for the core sprint in some capacity at every PyCon since 2004.

JS: I started programming by plugging wires into a card sorting machine in \'74. From Algol to XML and beyond, I have always tried to use and teach the very best. This is why I prefer Python. I liken Pycon to a high speed mini graduate education. At the Ph.D. level, we do not teach computer science techniques because they change so fast and because it takes all of our time to teach all of the fundamentals. Many of the talks at Pycon, at least the ones I give, are like that. But Sprints are the best time to share as much as possible the many rich techniques in Python. Python is so rich here that I doubt than any person has discovered all of this wealth.

CD: Wow. Meanwhile, I\'m a complete rookie - I\'m planning to attend a sprint for the very first time at [PyCon](http://us.pycon.org) 2008. Help me understand what to expect - what will it look like, what will I do?

BC: It looks like a bunch of programmers sitting at long tables, hunched over laptops with the occasional food break, having fun just programming; not much of a sight, I know, but it is fun when you are a part of it. =)

In terms of what you will do varies from sprint team to sprint team. Some spend the first half of the first day giving people an introduction to the project for those that have no experience with the code base. Others just have you start coding the instant you sit down. But in general you find your group, introduce yourself, and ask how you can help.

Then the sprint coach or group suggest something (unless you come with an idea of what you want to work on, which is great and encouraged). Some teams come in with a list of things they need done, varying based on difficulty, required experience, etc. For the core sprint, for instance, this has varied from having people rewrite tests to use unittest or doctest instead of an old-style test that is really archaic to writing the new string interpolation implementation for Python 3.0. The knowledge for this stuff ranges from just knowing how to program in Python to understanding C extensions. Pretty much anyone at any skill level can help.

You just need to come motivated. At least in the core sprint the core developers come with a list of stuff they want to try to accomplish, so they won\'t be hovering over you constantly asking if you need help. That being said, everyone in the sprint is quite happy to answer questions when asked! It\'s rather cool to be working on a bug and having the person who wrote that part of Python actually sitting at the table meander over to you, plop down next to you, and discuss the bug and the possible fix.

JB: The [Jython](http://www.jython.org) sprint shared many of these qualities. But it had some fundamental differences, due to the succession challenges we have seen in Jython development. It was not too long ago that the project had been given up by many (including myself), as yet another dying open source project - despite its fairly wide adoption in enterprise apps.

So our sprinting was a bit different. Often, we were trying to figure out how to wrangle a brilliant codebase that had not been touched in many places for probably 8 years. (This not legacy code where you say, I could write this so much better myself in my sleep or whatever, although a good deal is dated.) So there was not only a lot of trying out of code, there was a significant amount of discussion going on. The sprint also was an opportunity to expand the ranks of developers. And the whole time, Charlie Groves did a good job of staying on focus for bug fixes for the 2.2 release he was leading.

So while successful sprinting is going to look more or less the same as an intense peer activity, the dynamics of the underlying project are going to be significant factors as well.

CD: Working with top coders, revitalizing a whole project - it sounds exciting, but kind of intimidating, too. Jim, was it hard to decide to jump in and join a sprint?

JB: Yes. There\'s a significant time commitment to spending an extra 3 or 4 days sprinting at PyCon. I had signed up for - but didn\'t go to PyCon 2005, because of other commitments. At the 2006 event, I first heard about this craziness called sprinting, and it sounded intriguing, but I didn\'t know where to start.

But then there was the various articles, such as [Steve Holden\'s](http://www.onlamp.com/pub/a/python/2006/10/19/running-a-sprint.html), and various announcements out there. The fact that PyPy facilitated its collaboration by sprinting I found fascinating. On the Jython front, I was not certain about jumping in as a co-coach, because my own Jython dev experience was at that time quite limited. But the nature of the open source community is that someone has got to step in, and that person might in fact be you or me. Would the Jython sprint had happened if I hadn\'t started organizing that sprint, because it seemed like a good idea? I don\'t know the answer to that counterfactual ;)\... But in general, I think the vitality of an open source project is often seen in how willing it is to welcome new people in the fold. Python in general - and Jython in specific - has shown just an amazing friendliness.

And looking back on it, asking was it worth it to jump in and spend that time? Absolutely. This experience transformed my relationship to this open source community. So now I\'m a committer on Jython, we had a successful Google Summer of Code project with a working 2.5 compiler, and I\'m even going to be a reader of that student\'s thesis (a continuation of the GSoC project). By working so intensely with other dedicated people, sprinting enables a quick immersion into a project. Also, one cannot discount how important face-to-face is; sprinting goes beyond a meeting by interacting with artifacts that software developers truly respect.

BC: While I can\'t speak directly for the Jython sprint, I do remember my first time sprinting back at PyCon 2003. I was extremely intimidated! Here I was, really traveling for the first time on my own (all the other instances someone I knew was meeting me at the airport), attending a conference for the first time. But before the conference even began, I needed to walk into a room full of people who I not only knew by email only, but idolized as these great programmers who had developed the Python programming language. Definitely had the small-fish-in-big-pond feeling!

But my fears were for naught. Everyone was extremely friendly, both people I had communicated with on top of people I had never met before. I got to pair-program on developing a new opcode with Thomas Wouters who I had never met before until that sprint.

And I think it is key to remember that people are just genuinely nice in the Python \[community\]. You should not feel intimidated about sprinting. It\'s basically sitting around for hours on end with really friendly people, programming on fun stuff.

CD: Finally, I\'d like to ask a little more about what benefits sprinting has brought to you as individuals. Jim, you mentioned it drawing you quickly into a big role in the community. How else has it changed all of you?

BC: For me, it has led to making many more friends and acquaintances within the Python community. While you are at the conference you run into people and chat, but it is usually just in the hallway, maybe dinner if you manage to arrange it. But at the sprints, everyone is just sitting in the same room, chatting about who knows what throughout the day. You tend to grab all of your meals together as well, leading to more chances to getting to know the folks sitting around you. The camaraderie you tend to gain during the sprints make it as much fun as the conference itself, if not more so.

Plus my abilities as a programmer improves. If you happen to do any pair programming or working on the same thing as another person there you learn a great deal from them. I know for me I have picked up a thing or two from Guido about the language itself as talking to him in person makes it easy for him to explain his thinking behind something.

JB: I have to echo Brett\'s experience, I certainly learned a lot, as well as made some enduring connections. To be sure, those of us in the Jython sprint did not have the luxury of working side-by-side with the people who wrote much of the code. But at least we worked side-by-side, sharing the occasional discovery while endlessly tossing out ideas on how to improve things. (Most of which were very bad and fortunately have since been buried!)

As a side note, having the sprint at the end of PyCon makes a lot of sense because you\'ve been stimulated with ideas floating around, talking to people, finding out what needs to be done at a BoF (Bird of a Feather session), not to mention being in a new environment.

CD: Johnny what you like to say in closing.

JS: Hour per hour, I believe Sprinting will help most people learn more than the same amount of time spent on college assignments. College is a marathon. You can go faster in a sprint if you will just take off. I have had graduate classes with over 200 students. The system will not allow me to give as much personal attention as I have given to the 3 sprints which I coached. No one is a professor or a student in a sprint. Everyone is teaching others their best ideas. Everyone is learning as much as possible, especially those who are contributing the most.

**end interview**

References

Sprints at PyCon 2008: [http://us.pycon.org/2008/sprints/projects/](http://us.pycon.org/2008/sprints/projects/)

\[[http://www.onlamp.com/pub/a/python/2006/10/19/running-a-sprint.html](http://www.onlamp.com/pub/a/python/2006/10/19/running-a-sprint.html) \"Running a Sprint\"\] by Steve Holden
