# PyConPostMortemIrcTranscript

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    (12:58:01) slinkP!~pw@h-68-167-56-203.nycmny83.dynamic.covad.net: slinkP has changed the topic to: 
    Please familiarize yourselves with http://www.python.org/cgi-bin/moinmoin/PyConPostMortem
    (12:59:15) holdenweb: Aahz shouldn't be a long meeting (I hope)
    (12:59:33) holdenweb: SlinkP: You must tell me how to get op privileges one day :-)
    (12:59:39) holdenweb: Two minutes ...
    (12:59:54) slinkP: holdenweb: i'm not an op... i assume anyone can set topic here
    (13:00:00) slinkP: just do /topic foo
    (13:00:07) showell left the room ("Client Exiting").
    (13:00:26) holdenweb: 'K
    (13:02:19) amk_: Do we have an agenda?
    (13:03:14) holdenweb: OK, let's make a start. First, what else do we need:
    (13:03:17) holdenweb: AGENDA (PROVISIONAL)
    (13:03:17) holdenweb: 1. What Worked
    (13:03:17) holdenweb: 2. What Didn't Work
    (13:03:17) holdenweb: 3. Changes Required
    (13:03:28) holdenweb: Anyone?
    (13:04:10) slinkP: sounds reasonable to me
    (13:04:19) slinkP: maybe set a time frame for each?
    (13:04:19) ldl: ditto
    (13:04:49) holdenweb: Right. Let's try to work on each for around ten minutes, if we need that long, 
    then have a round-up and free-for-all.
    (13:05:00) holdenweb: 1. What worked?
    (13:05:16) slinkP: wired network was good... much more accessible than last year
    (13:05:36) holdenweb: Agreed. Can't do without that!
    (13:05:58) ldl: location was good, IMO
    (13:06:07) Aahz: We succeeded!  ;-)
    (13:06:09) slinkP: location was fine
    (13:06:31) altis: relevant URLs for the wiki challenged
    (13:06:33) slinkP: especially that outdoor terrace thing :-)
    (13:06:33) altis: http://www.python.org/cgi-bin/moinmoin/PyConPostMortem
    (13:06:43) holdenweb: Yeah, I just wish they had more room ...
    (13:06:47) amk_: Food seems to have worked out nicely, with a few adjustments.
    (13:06:48) altis: http://www.python.org/cgi-bin/moinmoin/PyConVenue
    (13:07:13) slinkP: yep i had no real prob with food... i was happy
    (13:07:27) briandorsey: sprints went well... network was up and everyone was working on code almost 
    immediately.
    (13:07:35) ldl: were the "what worked" items going to be put in the wiki?
    (13:07:36) slinkP: oh yeah ... sprints went great
    (13:07:50) holdenweb: briandorsey: much thanks to Michael McLay for that
    (13:07:59) Trevor: hello all...heya Kevin
    (13:08:04) amk_: ldl: maybe someone is keeping a transcript.
    (13:08:35) holdenweb: ldl: I think after the meeting we should summarise, yes. They aren't there 
    yet, not formally
    (13:08:45) slinkP: i can dump transcript into the wiki ... yes no?
    (13:09:25) holdenweb: slinkP: Summary would be better, but if you want to store it there for 
    accessibility that would be good, yeah
    (13:09:33) slinkP: holdenweb: i was thinking both
    (13:09:38) ldl: I was referring to items in pycon-organizers
    (13:09:45) holdenweb: 'k. So, what else worked well?
    (13:10:19) ldl: time... got out early enough to do something before supper
    (13:10:22) amk_: A/V worked.  The one problem I saw got fixed quickly.
    (13:10:51) slinkP: talks schedule didn't fall apart :-)
    (13:10:53) Aahz: Schedule worked well, aside from lack of Open Space
    (13:11:00) holdenweb: Yeah, A/V recovered quickly form a poor start, I thought. We could have 
    liaised better in advance, so not all their fault.
    (13:11:26) briandorsey: Lots and lots of good conversations happened.
    (13:11:32) altis: for people that weren't at the conference, the subethaedit notes people were 
    taking were great
    (13:11:53) holdenweb: We should definitely encourage more subetha, I think, it *was* good
    (13:12:21) altis: so maybe an official hosting spot next time
    (13:12:23) holdenweb: And yes, the whole point is to put people in the same space who don't normally 
    meet face to face, and everyine was happy about that.
    (13:12:40) briandorsey: (as an aside, a group of the subetha folks started coding up a 
    cross-platform version in python at the conference. ;)
    (13:12:52) holdenweb: altis: yes, definitely, plus we already have a note to ask for Creative 
    Commons clearance in advance from speakers
    (13:12:52) ldl: cool
    (13:13:23) holdenweb: briandorsey: would be nice if it weren't just a Mac thing.
    (13:13:37) holdenweb: So, anything else for "What worked" before we move on?
    (13:13:56) altis: was there any audio or video recorded? that is probably topic 3, but i would like 
    to see some of that go out live next year
    (13:14:12) Trevor: frequent list ANNCE worked, tho we can do them much better next year
    (13:14:14) holdenweb: Yes, briandorsey can update us
    (13:14:15) ldl: yeah, I'm waiting to comment there.
    (13:14:44) holdenweb: Trevor: yes, more PR would probablyhelp.
    (13:14:50) briandorsey: I got some of the audio, I'm in the process of getting CC permissions from 
    speakers and editing/converting to MP3.
    (13:15:05) holdenweb: Brian, just suimmarise the audio you've got, then we'll move on to 2.
    (13:15:12) altis: do you consider the pre-conference stuff: collection of submissions, evaluation, 
    notification, etc. a success or needs work item?
    (13:15:14) briandorsey: I've got OK's from 9 people so far, including all three keynotes.
    (13:15:22) ldl: wonderful - I know Bruce Eckels plans to release his talk
    (13:15:26) Trevor: coat check worked.  blocking access to the closet worked.
    (13:15:36) amk_: altis: good question!
    (13:15:36) Trevor: Big posters worked
    (13:15:37) holdenweb: The closet?
    (13:15:39) slinkP: briandorsey: please tell me you got the starkiller talk ... that one was 
    hysterical
    (13:15:42) briandorsey: Yup, Bruce is probably going to do his own.
    (13:15:47) briandorsey: I got the starkiller talk.
    (13:16:09) holdenweb: altis: Most of it was better than last year, but just as late :-(
    (13:16:10) briandorsey: and the schtoom talk - Anthony is going to try and sync up the slides and 
    the audio.
    (13:16:23) holdenweb: So, a mixed success on which we can build ...
    (13:16:49) slinkP: i'd say the pycon-organizers list worked as an organizing medium
    (13:16:55) ldl: maybe plan to "officially" plug into the pa system
    (13:17:03) ldl: yes to py-org
    (13:17:26) holdenweb: Right, Item 2: What didn't work.
    (13:17:29) briandorsey: ldl - plugging into the PA for next year is a great idea.
    (13:17:43) ldl: room ventilation
    (13:17:54) holdenweb: Form my PoV, py-org didn't work until fairly late on in the process.
    (13:18:04) amk_: missing submission deadlines because the software needed to be written
    (13:18:15) Aahz: Agreed on py-org, but it also failed late, too, from my POV
    (13:18:22) briandorsey: paypal. *sigh*
    (13:18:24) holdenweb: ldl: Yeah, HVAC was a problem both years. amk: You saved my ass there!
    (13:18:53) Aahz: More precisely, I'd say that concom communication was a problem
    (13:19:01) holdenweb: concom?
    (13:19:13) slinkP: having 2 websites was a big clunky pain in the arse IMHO
    (13:19:13) Aahz: Conference committee
    (13:19:21) amk_: slinkP: amen to that.
    (13:19:36) holdenweb: slinkP: yes we already have a big flag to avoid "batling web sites" next year 
    :-)
    (13:19:37) whoever: I agree.  It was hard to tell how decisions were being made, which lead to 
    indecision and confusion.
    (13:19:51) Trevor: the 2 websites was very uncoordinated and all mid-stream development
    (13:20:02) Trevor: we can use the off-season to coordinate
    (13:20:05) holdenweb: whoever: yes, and that's why this year I'm looking to devolve more specific 
    responsibilities
    (13:20:08) slinkP: Trevor: agreed
    (13:20:14) Trevor: we did not have use of pycon.org at the beginning
    (13:20:28) slinkP: personally i don't care what web platform we use as long as we get it all working 
    way in advance
    (13:20:30) holdenweb: Trevor: yes, but that won't be a problem next year
    (13:20:31) Trevor: and then all of a sudden the rules of its use started changing
    (13:20:35) whoever: The 2 web sites were an example of "concom" problems, because it's creation 
    wasn't really discussed on pycon-organizers.
    (13:21:07) Aahz: Short answer: the basic driver behind the two websites was CNRI owning python.org 
    until late.
    (13:21:12) holdenweb: whoever: my problme with pycon-organiuzers was that often I'd ask for input 
    and get nothing, so I more or less gave up for a while.
    (13:21:33) whoever: Aahz: Huh?
    (13:22:01) holdenweb: aahz: there'll be no domain problems next year anyway. WE can leave web topics 
    now, IMHO
    (13:22:03) Aahz: We couldn't create the subdomains we needed for PyCon, so we were forced to use 
    pycon.org, and things didn't get handled well.
    (13:22:18) Aahz: Right.
    (13:22:43) holdenweb: Open Space was a minor disaster this year compared to its outstanding first 
    year. I was very disappointed.
    (13:23:02) whoever: I agree, but not sure why other than using the ballroom for talks instead of 
    open space.
    (13:23:04) ldl: having some whitespace on the schedule (thing wrong)
    (13:23:08) altis: holdenweb: i think that we are going to have to start putting time bounds on 
    getting input, so whoever wants to reply will know they only have a day or week to do so and then 
    everyone forfeits their right on an opinion
    (13:23:30) holdenweb: altis: right, I'll mail c.l.py and announce after this meeting.
    (13:23:45) whoever: there's no point setting a deadline before the review forms are tallied, though.
    (13:23:46) Trevor: I would like to ask the BIG Q.  How can we grow PyCON next year?  What will 
    attract more people, and the potential 500 we are discussing on the list?
    (13:23:48) Aahz: altis was talking more about concom
    (13:24:04) holdenweb: ldl: last year there were times with no formal program items, and htat helped 
    to encourage Open Space and the rest.
    (13:24:13) altis: i'm talking about all decisions that require group input, pycon, python.org, etc.
    (13:24:19) Aahz: Last year we had three tracks
    (13:24:27) altis: this is a generic problem in our decsion making process
    (13:24:27) ldl: build and maintain milestone/deadline in PyCON2005 wiki
    (13:24:33) altis: brb
    (13:24:35) holdenweb: This year I suspect Bob didn;t have as much time to give. I saw him for the 
    first time on Wednesday morning, which was way too late.
    (13:24:42) altis left the room (quit: "http://altis.pycs.net/").
    (13:24:50) Aahz: I think advance planning is the key to larger PyCon
    (13:25:13) Trevor: ldl: i agree, a little more calendaring autmoation and task deadlines will help 
    considerably
    (13:25:16) whoever: I found the dead time in the '03 schedule just annoying.  I missed the beginning 
    of almost everything I wanted to see, because the schedule was so irregular.
    (13:25:43) holdenweb: whoever: but if we had deceant annunciator displays we coudl avoid that, 
    right?
    (13:26:02) Aahz: Regularity is one thing; complete lack of unscheduled time another.
    (13:26:10) whoever: holdenweb: I don't know what you mean.
    (13:26:21) Trevor: i believe broadening the scope of talks to incoude solicitied topics could 
    attract more people
    (13:26:39) holdenweb: whoever: we simply make sure that people can glance at a screen to see what's 
    happening now and in the future.
    (13:26:51) Aahz: Attract more speakers or attendees with solicited talks?
    (13:27:12) whoever: aahz: If I could revise this year's schedule, I'd add a lightning talks and open 
    space as indivduals sessions just like paper sessions.
    (13:27:15) altis: were there many (if any) complaints of too many interesting talks that overlapped 
    and so people were forced to miss something they really wanted to see?
    (13:27:26) whoever: Then they would only have to compete with one set of talks, instead of two.
    (13:27:35) Trevor: there were also many comments about looking for more basic info
    (13:27:39) Aahz: Less this year than last year, I think.  (complaints of overlap)
    (13:27:39) holdenweb: altis: we still have to analyze that, but early results suggest it wasn't 
    horrible.
    (13:27:41) Trevor: and I think that is our growth market
    (13:27:50) ldl: if all available later paper/audio then missing is not as big of a deal
    (13:28:05) briandorsey: and I'd also propose a few spots in the 2nd/3rd days for popularity based 
    repeats.
    (13:28:06) altis: ldl: agreed
    (13:28:14) Aahz: Yes, open space & lightning should be formally scheduled.
    (13:28:19) holdenweb: we have already recorded the "schedule Lightning Talks and BoFs" idea.
    (13:28:31) whoever: Trevor: I think identifying the growth market comes first, then seeing what we 
    can do to accommodate them.  If we same new users is the growth area, I think we'll need to work 
    harder to make sure they even know about the conf.
    (13:28:31) slinkP: Aahz: amen to that
    (13:28:48) holdenweb: briandorsey: that's a good plan, but speakers have to be prepraed to do that, 
    which some weren't this year.
    (13:28:48) whoever: Aahz: If we do that, then I don't see any need for dead time in the schedule.
    (13:28:48) ldl: repeat of popular items using web-based questionaire is a good idea
    (13:28:53) Aahz: But just the timeslots, not the contents of open space / lightning
    (13:29:11) holdenweb: aahz: right, that should be decided on-site on the day
    (13:29:34) Trevor: whoeva: new users vs. NOT experts is where I think we should land
    (13:29:41) amk_: Trevor: could subconferences be held as part of PyCon?  e.g. scipy  as subconf.
    (13:29:46) holdenweb: Anything else before we move to "Changes Required" ... or have we already done 
    that ? ;-)
    (13:29:49) Aahz: Except I think first day (or half-day) of open space should be pre-scheduled by 
    wiki starting two weeks before conference
    (13:30:18) whoever: trevor: I don't know if that's a reasonable goal.  We definitely need a 
    developers conference, where developer is broadly construed but includes experts.
    (13:30:23) holdenweb: aahz: that would be possible
    (13:30:24) Aahz: I'd suggest tracks make more sense for now than subconferences
    (13:30:44) altis: could't sub-conferences be handled in the same way as sprints?
    (13:30:48) altis: before or after
    (13:30:53) holdenweb: whoever: I also feel we definitely need a place people can come and have a 
    comfort level about NOT knowing Python, and being there to learn./
    (13:31:08) Aahz: Why can't PyCon be both?
    (13:31:15) whoever: holdenweb: agreed, but not to the detriment of the existing community.  that's 
    all I'm saying.
    (13:31:21) holdenweb: Anna Ravenscroft's talk was apparently a model of how to synthesise the two approaches :-p0
    (13:31:23) ldl: suggest that "after sprints" be paralleled with "tutorial", fee or free
    (13:31:35) Aahz: Good suggestion
    (13:31:44) Aahz: But I think tutorials need to be before
    (13:31:53) Aahz: Anyway, I need to run.  Bye!
    (13:31:54) Aahz left the room (quit: "Leaving").
    (13:32:07) holdenweb: whoever: yes, we can't afford to leave our current congregation behind
    (13:32:31) Trevor: I suggest that the py-org group think more strategic about the content and dont 
    rely 100% on topics from volunteers.  If we know there is interest in a topic, and no one 
    volounteers, then it is our responsibility to identify that domain expert to ask to do the talk
    (13:32:36) ldl: I doubt that tutorials before would be that beneficial cf. tutorials after
    (13:32:43) altis: especially since it would be nice to hit 500 next year
    (13:32:47) Trevor: PyCON needs to stay a dev conference and keep that feel
    (13:33:02) itamar: tutorials are a good way to address new users, yes
    (13:33:08) Trevor: but I think we can broaden the audience, while not diluting the benefit the 
    current group gets
    (13:33:11) ldl: Yes, have a "suit and tie" track at another venue
    (13:33:13) whoever: I think we can do a lot to solicit submissions that address a broader audience.  
    One example is that I'd like to see a full-day session on Python for application developement that 
    discusses best practices -- distutils, testing, documentation, design techniques, case studies, etc.
    (13:33:19) altis: trevor: agreed on soliciting certain people/talks/papers. i will definitely do 
    that for oscon next year if i'm still co-chair
    (13:33:23) holdenweb: Trevor: that the best approach if we can manage it ...
    (13:33:48) slinkP: whoever: that would rock
    (13:33:52) whoever: I think we should solicit people to send in submissions.
    (13:34:00) ldl: whoever: absolutely!
    (13:34:07) holdenweb: whoever: that would be a great tutorial, and I have no problem with solicited 
    talks.
    (13:34:08) Trevor: 'suit and tie' cna be part of this 'open last day' sugestion on the list, if we 
    valuie it
    (13:34:37) holdenweb: what's the general feeling on "open last day"?
    (13:34:49) whoever: I was thinking of it as a full day of talks by experts, but based on the actual 
    submissions.  So, for example, I can see Anna Ravenscroft's talk and Jim Fulton's talk fitting in 
    there naturally.
    (13:34:50) Trevor: whoever: NOW you are talking.  content that is less theoretical and more 
    practical can help us grow
    (13:35:38) ldl: holdenweb: open last day... sounds good.
    (13:35:41) whoever: how were the tutorial talks we had this year, e.g. Thomas Wouters' talks.  I 
    didn't see any of them.
    (13:35:47) altis: holdenweb: open last day? where is that described?
    (13:36:12) holdenweb: altis: search for "think about"
    (13:36:37) holdenweb: altis: "last afternoon" seems to have broadened a bit :-)
    (13:36:54) ldl: practical is good.. and if presenter were ready for a after tutorial (fee or free) 
    then good practicum
    (13:37:00) holdenweb: whoever: I missed those too, but I've seen some positive feedback about them
    (13:37:00) Trevor: the 'open last day' for suits, educators, newbies, etc needs a major PR push with 
    it to be succesful
    (13:37:27) holdenweb: Trevor: we might be able to link with FOSE next year ... ?
    (13:37:34) Trevor: if we do it, those interest group champions need to be identified and orgnize 
    talks specifically for their invited audience
    (13:37:37) whoever: so one organizational suggestion is to delegate the task of assembling the 
    content to a program chair, separate from the conference chair.
    (13:37:38) altis: were publishers and businesses represented at PyCon with tables...?
    (13:37:48) itamar: altis: no
    (13:37:49) altis: those would be obvious sponsors of practical talks
    (13:38:01) holdenweb: whoever: or even to track chairs, yes, that would be a helpful development
    (13:38:06) ldl: I see FOSE as a distraction to be avoided, unless we merely time it so that they can 
    attend
    (13:38:39) holdenweb: ldl: perhaps. We did try and organize a "Why Python" talk for FOSE delegates, 
    but it didn't come off.
    (13:38:40) Trevor: certainly the FOSE market can be targeted for a 'free python in government track 
    on the last day'
    (13:38:49) whoever: altis: they would?
    (13:38:55) altis: community conference community conference community conference... okay, mind fixed
    (13:38:57) holdenweb: Trevor: that was more what I was hoping
    (13:39:06) holdenweb: altis: ;-)
    (13:39:19) ldl: altis: good for you.. try to stay focused ;-)
    (13:40:05) slinkP: wtf is FOSE?
    (13:40:10) Trevor: LOL
    (13:40:18) ldl: I've seen too many things (Usenix, IPC to name two) devolve when the suits get too 
    close.
    (13:40:26) holdenweb: OK, we're kind of rambling on. Does anyone have issues they want to address 
    before we finish? I'll go round the meeting - wait for your monicker beofer you type ...
    (13:40:29) amk_: fose: a big computer show for gvt. www.fose.com
    (13:40:32) holdenweb: altis?
    (13:40:38) whoever: another thought on increasing attendance-- it would be interesting to do a 
    survey of python developers in general to find out the reasons people didn't come.
    (13:40:49) holdenweb: whoever: sshh!!
    (13:40:51) ldl: slinkP: FOSE is free for Federal Employees, $50 for the people that pay for it (e.g. 
    us)
    (13:41:01) holdenweb: ldl: sshh!!
    (13:41:06) holdenweb: altis?
    (13:41:17) holdenweb: 5 ... 4 ... 3 ... 2 ...
    (13:41:20) whoever: holdenweb: I'll take it to the list.  If we want to increase attendance, we need 
    to understand who those new attendees would be.
    (13:41:35) holdenweb: amk_ ?
    (13:41:37) amk_: Do we need refereed papers at all?
    (13:41:49) altis: i definitely see a need to represent python in education, government, etc. but 
    that is a separate mailing list topic and my gut is that we should probably bring python to those 
    conferences not try and have sub-PyCons for those users
    (13:41:49) itamar: the papers aren't really refereed as such
    (13:41:52) holdenweb: Were they really refereed this year?
    (13:41:57) amk_: Lots of reviewing effort; not clear there's much benefit.
    (13:42:03) holdenweb: They woulodn't be academically credible.
    (13:42:05) amk_: s/refereed/reviewed/, then.
    (13:42:05) itamar: no one reviewed the papers
    (13:42:13) itamar: we just accepted talks
    (13:42:17) whoever: I reviewed some papers, but the reviews never got sent to the authors.
    (13:42:20) Trevor: short summary: keep it to 3 days. expand the talks to 3 to 4 tracks to include 
    more practical talks for non-experts.  Target more specific sub-groups of the python community so 
    they can feel this is their get together too.
    (13:42:24) ldl: except that they more or less exist
    (13:42:27) whoever: I definitely saw talks that could have been improved by refereeing...
    (13:42:40) altis: amk: no refereed papers! pain in the ass
    (13:42:42) ldl: no to more tracks, imo
    (13:42:43) whoever: Trevor: I disagree with the notion of more tracks.
    (13:42:50) holdenweb: One idea for next year is a "How to be a PyCON Speaker" track.
    (13:43:07) ldl: or merely a session?
    (13:43:13) holdenweb: This would give advice in advance, and coach presenters before to Conference 
    opened
    (13:43:15) amk_: We did reject proposals, though, but I don't know if doing so really mattered.
    (13:43:20) Trevor: how can you expand your content base and audience interest without adding tracks?
    (13:43:39) ldl: some tracks contract
    (13:43:42) itamar: amk_: I can think of at least two that made the conference a lot better for 
    having been rejected
    (13:43:47) holdenweb: We probably need to analyze the "what would you have liked" answers for ideas
    (13:44:08) holdenweb: amk_: anythiogn else?
    (13:44:10) whoever: make better use of the time we had there.  make sure the talks we accept are all 
    excellent and address attendee interests.
    (13:44:19) amk_: holdenweb: no
    (13:44:23) slinkP: if we don't expand tracks, and we keep to 3 days, and we make talks longer, 
    that'll mean fewer talks
    (13:44:33) whoever: let's not make talks longer!
    (13:44:39) holdenweb: whoever: excellent idea, but perhaps imprcactical given our impoerfect 
    knowledge
    (13:45:00) Trevor: my thought: we arent diluting anything by adding more practical tracks alongside 
    the existing-style talks, if we attract new attendees that want the practical talks
    (13:45:14) slinkP: whoever: *shrug* some people on organizers list seemed to think it necessary  ... 
    i thought 1/2 hour was ok but there was barely any time for Q/A and changing rooms
    (13:45:15) ldl: whoever: several speakers seemed surprised by the 30 minute limit -- communicate 
    better?
    (13:45:15) ***briandorsey has to head out. Take care all! Thanks for everything!
    (13:45:15) whoever: holdenweb: perfection is impossible, but we could do better.
    (13:45:24) bkc left the room (quit: "Client Exiting").
    (13:45:28) altis: can you identify which talks were very poorly presented, poorly attended, etc.?
    (13:45:43) holdenweb: ldl/whoever: yes, better communication with speakers is a definite requirement 
    next time.
    (13:45:44) briandorsey left the room (quit: ).
    (13:45:59) Trevor: i am just suggesting we explore expanding our menu
    (13:46:03) holdenweb: altis: we have questionnaires that might give us *some * feedback
    (13:46:11) Trevor: altis: yes, we have a good feel for the talks
    (13:46:16) altis: so nobody did head counts?
    (13:46:19) whoever: holdenweb: and easy to do.  communication with speakers was almost accidental 
    this year
    (13:46:23) ldl: Trevor: I think that Zope contracted quite a bit over IPC 8
    (13:46:31) Trevor: we had a daily survey and we know what talks filled what rooms
    (13:46:35) altis: ok
    (13:46:36) holdenweb: altis: great, make sure THAT goes on the Wiki
    (13:47:07) holdenweb: headcounts should definitely be a chair task
    (13:47:17) Trevor: final head counts is a good point done by the session chair
    (13:47:22) holdenweb: itamar: any closing thoughts?
    (13:47:45) holdenweb: 5 ... 4 ...
    (13:47:59) holdenweb: ... 1 ... 0
    (13:48:09) holdenweb: ldl: what else would you like to say?
    (13:48:29) ldl: It would be good to get permissions to publish before
    (13:48:43) holdenweb: [thinks: wow, I thought he'd NEVER shut up ;-)]
    (13:48:45) ldl: the conference, so that we can video/audio record  --
    (13:48:48) altis: make it part of the notification/acceptance email
    (13:49:15) Trevor: session chairs should be responsible for maiing sure people can hear, repeat 
    questions, etc.  IOW, if the speaker isnt following the guidelines the chair needs to help
    (13:49:18) holdenweb: ldl: yup, we have already got that down, I think, but it was a slipup this 
    year
    (13:49:48) ldl: done
    (13:49:50) holdenweb: Trevor: again I have been capturing the advice to speakers/chairs, and will be 
    sending it out in advance next year.
    (13:50:04) Trevor: i will give leeway for first time speakers getting nervous and forgetting the 
    audience, so we need to help nicely
    (13:50:11) holdenweb: rholbert: you've been quiet, any final points?
    (13:50:40) rholbert: just lurking, but agree, some speakers were talking to the slides...
    (13:50:40) holdenweb: ... 3 ... 2 ...
    (13:50:58) holdenweb: rholbert: thanks, yes, we need to give better support to new speakers.
    (13:51:06) rholbert: agreed!
    (13:51:17) holdenweb: [nothing wrong with lurking, BTW]
    (13:51:26) rholbert: overall, good conference.
    (13:51:40) holdenweb: thanks. slinkP: Anythign else?
    (13:51:50) rholbert: next year, i hope to be more involved, but first time, just wanted to get a 
    feel for it.
    (13:51:53) slinkP: nope... going back to work :-)
    (13:52:12) holdenweb: slinkP: can you make sure you put the transcript somewhere accessible?
    (13:52:25) holdenweb: Trevor: final points?
    (13:52:32) altis: yes beers all around for a great job and major success as the biggest Python 
    conference ever!
    (13:52:39) slinkP: holdenweb: i'll put it in the wiki, linked from the post-mortem page
    (13:52:45) Trevor: beer!
    (13:52:48) altis: later
    (13:52:49) slinkP: woohoo!
    (13:52:49) Trevor: we forgot beer
    (13:52:56) slinkP: pycon rocked
    (13:52:59) altis left the room (quit: "http://altis.pycs.net/").
    (13:53:11) holdenweb: altis: yes, the beer wasn't a great feature of this PyCON. Next year maybe ...
    (13:53:30) holdenweb: whoever: last, but not least ... ?
    (13:53:54) Trevor: we need to more narrowly identify the interest groups and see where our biggest 
    potential lies, and then figure out how to attract them
    (13:54:35) holdenweb: Trevor: hopefully the surveys will help us do that?
    (13:54:46) whoever: I'd love to add a webcast, but that's expensive.  On the practical side, I'd 
    just say that if we do as well in '04 as in '05, I'll be happy.
    (13:54:58) Trevor: yes, to a degree, but only from the people that attended
    (13:55:14) Trevor: that challenge is figuring out what the people would say that didnt attend
    (13:55:34) whoever: Trevor: A survey on python.org might help for that.
    (13:55:42) holdenweb: whoever: thanks. A great note on which to end. Thank you all for your input, 
    I'll try to make sure it all goes into next year's plan. Anyobody want to be vice chair? ...
    (13:56:04) Trevor: whoever: that could work and show us as being very proactive if we do it 
    early-enuff to matter
    (13:56:05) ***holdenweb sees everyone suddenly leave the channel :-)
    (13:56:17) ldl: if I end up in DC area by then, possibly (poor you ;-)
    (13:57:04) holdenweb: ptyhon.org survey V good idea. Q1: did you attend PCDC2005? Yes: stop there. 
    No: ... real questions!
    (13:57:31) ldl: holdenweb: did you mean 2004?
    (13:57:37) holdenweb: Maybe we could recruit Shane McChesney and Nooro top help with that?
    (13:57:58) holdenweb: ldl: yup. another of those damned tpyos :-)
    (13:58:04) ldl: holdenweb: maybe that's where Guido misplaced the time machine ;-)
    (13:58:09) Trevor: is shange still using ASP for his surveys?
    (13:58:18) holdenweb: Trevor: yes, deo we care?
    (13:59:12) ldl: holdenweb: only "ideologically"
    (13:59:19) Trevor: i do. been trying to get him to write a ptyhon library to generate forms.  ;)
    (13:59:28) holdenweb: Right, everyone. My luinchtime's about over. Thanks for all your help!
    (13:59:54) ldl: when is the next #pycon?
    (14:00:20) holdenweb: ldl: good question. How about two weeks after this one?
    (14:00:42) slinkP: Trevor: web forms? arent't there a bunch of those?
    (14:00:59) Trevor: not if encode was a hot talk
    (14:01:08) ldl: holdenweb: how about a py-org announce the day before???
    (14:01:24) Trevor: evidently we dont do webform generation well in python
    (14:02:05) holdenweb: ldl: indeedy. Maybe a few days before that a 1-day reminder?
    (14:02:42) ldl: holdenweb: Helps me!
    (14:04:41) ldl: anything else... seems like the "popcorn" is done.
    (14:04:46) slinkP: if we're done, i'll save the transcript now
    (14:04:55) whoever: sounds good.  i've got to go.
    (14:04:59) Trevor: mmm beer and popcorn

------------------------------------------------------------------------

[CategoryPyCon](CategoryPyCon)
