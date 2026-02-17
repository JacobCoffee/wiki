# SummerOfCode/Expectations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Summary

This page covers, in detail, the expectations for Google Summer of Code students in regards to communication. This is useful for PSF projects which haven\'t codified their expectations\--they can point to this document and use it as is.

The Google Summer of Code coding period is very short. On top of that, many students haven\'t done a lot of real-world development/engineering work previously; one of the primary purposes of the program is to introduce students to F/OSS and real-world development scenarios. On top of that, most mentors and students are in different locations\--so face-to-face time is difficult. Because of this, it\'s vitally important to the success of the GSoC project for all expectations to be specified before students begin coding. This should be the first step in a long series of frequent communication between student and mentor(s).

This document walks through various expectations for students and mentors, as well as addressing various ways to communicate effectively.
:::

::: 
### 40 hour work week

Students are expected to work at least 40 hours a week on their GSoC project. This is essentially a full-time job.

The benefits for the GSoC project are huge:

- the chance to become part of a project community over the long term\--this can lead to involvement with other projects, social network, good friends, valuable resources, \...
- the chance to work with real developers on a real project
- the end result of the student\'s project can be used for resume material that is available for all future employers to see

The final point is an important one for a beginning developer. Employers greatly appreciate having a referenceable body of work when looking at potential employees. Your code says more about your abilities than any amount of algorithms on a whiteboard can.

And of course, the program will provide you stipend and a really cool t-shirt.
:::

::: 
### Self-motivation and steady schedule

The student is expected to be self-motivated. The mentor may push the student to excel, but if the student is not self-motivated to work, then the student probably won\'t get much out of participating.

The student should schedule time to work on the project each day and keep to a regular schedule. It\'s not acceptable to fiddle around for days on end and then pull an all-nighter just before deadlines. It will show in your code.
:::

::: 
### Frequent communication with mentor

Frequent communication with your mentor is a **must**. Your mentor should have a good idea of:

- what you\'re currently working on
- how far you\'ve gotten
- how you\'re implementing it
- what you plan on working on next
- what issues have come up
- what you did to get around them
- what\'s blocking you if you\'re stuck

The mentor is one of the most valuable resources for GSoC projects. The mentor is expected to be both a solid developer and a solid engineer. The mentor likely has worked on the project for long enough to know the history of decisions, how things are architected, the other people involved, the process for doing things, and all other cultural lore that will help the student be most successful.

Before the GSoC project has started, the mentor and student should iron out answers to the following questions:

1.  What is the communication schedule? Daily? Every two days? Mondays, Wednesdays, Fridays?
2.  What is the best medium to use for regular, scheduled communication? Email? IRC? Instant messenger? VOIP? Telephone call? Face-to-face?
3.  What is the best medium to use for non-scheduled communication? Email? Instant messenger?

DO:

- **keep your mentor up to date as much as possible**

  This forces you to be more organized and it gives your mentor a chance to help you out if you\'re having trouble.

- **let your mentor know what your schedule is**

  Are you going on vacation, moving, writing papers for class? If your mentor doesn\'t know where you\'ll be or to expect a lag in your productivity, your mentor can\'t help you course correct or plan accordingly.

AVOID:

- **going for more than a week without communicating with your mentor**

  The project timeline doesn\'t allow for unplanned gaps in communication.
:::

::: 
### Guidelines for mentors

One key responsibility for mentors is to help GSoC students to connect with the project development community. Working on a project for the summer and only producing one giant patch at the end is a recipe for disappointment. It also means that the student\'s contributions are heavily dependent on the mentor\'s availability.

First and foremost, encourage students to communicate using the regular project channels. If the project has a mentorship list (e.g. [core-mentorship@python.org](mailto:core-mentorship@python.org) for CPython), suggest they sign up and communicate with them there rather than through private email. For design discussions, again, try to use the appropriate project list (e.g. [python-ideas@python.org](mailto:python-ideas@python.org) for CPython) rather than private email. This helps other contributors be aware of what is going on with the GSoC project, and perhaps offer suggestions and advice.

Secondly, try to help the student to break up their work into smaller increments that can be submitted as individual patches. While this isn\'t always possible, smaller patches are generally easier to get reviewed, and submitting some early patches can help the student to become more comfortable with the project\'s development processes.
:::

::: 
### Version control

Students should be using version control for their project.

DO:

- **commit-early/commit-often**

  This allows issues to be caught quickly and prevents the dreaded one-massive-commit-before-deadline.

- **use quality commit messages**

  Bad examples:

      Fixed a bug.

      Tweaks.

  Good examples:

      Fixed a memory leak where the thingamajig wasn't getting freed
      after the parent doohicky was freed.

      Fixed bug #902 by changing the comparison used for duplicate
      removal.

      Implemented Joe's good idea about rendering in a separate
      buffer and then swapping the buffer in after rendering is complete.

      Improved HTML by simplifying tables.

- **refer to specific bug numbers, links, and issues as much as possible**

  The history in version control is frequently the best timeline log of what happened, why, and who did it.

AVOID:

- **checking in multiple non-related changes in one big commit**

  If something is bad about one of the changes and someone needs to roll it back, it\'s more difficult to do so.

- **checking in changes that haven\'t been tested**
:::

::::: 
### Communication with project

Most F/OSS projects have mailing lists for project members and the community and/or have IRC channels to communicate. These communication channels allow the student to keep in touch with the other project members and are an incredibly valuable resource. Other members of the project may be better versed in various parts of the project, they may provide a fallback if the mentor isn\'t available, and they may be a good sounding board for figuring out the specific behavior for features. You are assigned a mentor, but the whole community is there to help you learn. Make use of all the resources at your disposal.

Shyness is a common problem for students who are new to open source development. At the beginning of the project, the student is encouraged to send a \"Hello! I\'m \... and I\'m working on a GSoC project on \... and here\'s a link to the proposal.\" email to project mailing lists and encouraged to log in and say \"hi\" on IRC. Break the ice early\--it makes the rest of the project easier. If you don\'t know where you announce yourself, ask your mentor.

::: 
#### Project mailing lists

Mailing lists are a great way to work out feature specifications and expected behavior.

Often mailing lists are archived and the archives are a rich source of information regarding prior discussions, decisions, and technical errata.

DO:

- **search through the archives for answers before asking on the list**

- **be courteous at all times**

- **be specific**

  Cite data, references, and use links wherever possible when discussing technical things.

- **be patient**

  Don\'t expect an answer within minutes or hours; people often read their mailing-list messages once per day.

- **be helpful**

  Helping other people when you know the answer makes things easier on your mentors and demonstrates your understanding of the project. Many mentors have told me their best students have been those who help others, so it\'s a great way to make a good impression!

AVOID:

- **being rude**

  Since most mailing lists are archived or recorded, it\'s likely anything you say will be available for everyone to see forever; exercise good manners in all aspects of life.

- **saying things with all capital letters and excessive punctuation**

  This is perceived as shouting

- **getting into heated arguments**

  If someone insults you, it\'s best to ignore it.
:::

::: 
#### IRC

Most F/OSS projects have an [IRC](#irc) channel and some have more than one. People from the project and its community \"hang out\" on these channels and talk about various things. Some projects have regularly scheduled meetings to cover the status of the project, how development is going, status of major blocking bugs, map out future plans, \...

If the project has an IRC channel, it\'s a good idea to hang out there. This allows the student to interact with the community and also a forum for working out problems and ideas in real time.

DO:

- **hang out on the project IRC channels when you\'re working on the project**

- **take time to interact with people who are on the IRC channel**

  This builds community and it\'s easier to get help from people who are familiar with you than people who aren\'t.

- **be helpful**

  Folk asking questions on IRC are often looking for a quick answer: if you happen to know one, or can help ask questions that would allow them to debug, helping others is a great way to get to know the project better.

AVOID:

- **saying things with all capital letters and excessive punctuation**

  This is perceived as shouting.

- **poor grammar**

  It makes it harder for other people to understand what you\'re trying to say.

- **being rude**

  We\'re all real people with real feelings and if you\'re rude it\'s likely people will interact with you and help you less; also it\'s not uncommon for IRC history to be recorded and archived for all to see forever.

  See:

  - [http://www.linuxchix.org/irc-basics.html](http://www.linuxchix.org/irc-basics.html)
  - [http://en.wikipedia.org/wiki/Internet_Relay_Chat](http://en.wikipedia.org/wiki/Internet_Relay_Chat)
:::
:::::

::: 
### Design documents

It\'s a good idea for the student to maintain design documents during the course of the GSoC project. These design documents should cover:

1.  the project plan, with additional detail to flesh out the original program application
2.  deviations from the project plan and how and why the original design plan changed
3.  any issues that could not be worked out or overcome
4.  possible future directions
5.  any resources used or relevant specifications

The student and mentor should work out what design documents should be maintained during the course of the GSoC.

One thing to note is that the student shouldn\'t spend all his/her time doing design documents. It\'s important to keep track of the design, but it\'s also important to get some code done. The mentor should be able to help the student strike a balance between these two goals.
:::
