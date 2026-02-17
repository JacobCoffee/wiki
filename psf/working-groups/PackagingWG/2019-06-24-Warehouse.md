# PackagingWG/2019-06-24-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# API key design - design decisions 

Monday, June 24th

- Participants: Will, Donald, Ernest
- Note-taker: Sumana

[GitHub issue](https://github.com/pypa/warehouse/issues/994)

conversation from last week:

- Donald: \..... simple bearer token vs macaroon, because I \*think\*, given the existing PoCs it's probably less work to just start off with macaroons off the bat and the only real downside to them is their length. But I'd love to get your thoughts on that.

- Will: Paul Kehrer and I discussed this a bit. My concern was that Macaroons would be too big of a lift for what's scoped in the SoW, but the existing work changes that a bit.

Will wanted to start with non-macaroons approach for complexity\..... but earlier PR + Donald\'s work makes him less worried about that

but constraint modeling \.... features might creep in that aren\'t in SoW scope

many nice-to-have things are avail with Macaroons

Donald:

happy personally if, in the 1st cut\....

if Macaroons work is too much for current contract, ok with going simpler! Not trying to scope creep

given current work \-- getting macaroons across finish line should be not more work than doing fresh work

existing PR \.... make them better than simple API keys

separate out from defining caveat lang, Macaroons don\'t have it, just raw string

have infra around validating them, etc. \.... makes them longer \-- extra validation complexity

if it\'s possible to start adding caveats in this SOW, that\'s great, if too much, that\'s fine too. We can build upon that in the future easily. (a bit of a bikeshedding thing \.... minimal engineering effort, mostly deciding what we want, what shape it takes \-- bikeshedding)

Will: was pleasantly surprised to read PRs. Macaroons, simplified, initial implementation, fine

Ernest:

1\) hey Donald: E would like Macaroons

2\) we\'re limited time/scope. less worried about how we implement, more about amount UX/UI work required for macaroons. UX questions (caveats reduce complexity) \.... we should target - not necessarily API keys/tokens. Call them \"upload tokens\" \-- \"this implements a stand-in for your password when uploading via legacy upload URL, is specified to a specific project.\" Say no to passwords when 2FA is enabled, start automating uploads, strict UX/UI scope to this to make sure we keep making progress in new milestone. Lots of issues coming in. And translations/i18n.

So keep narrow scope - Upload Tokens - keep barrier between these things & what API tokens MIGHT be in the future when we have a new API!

D:

if we use macaroons as new API key, UX concerns are the same

need a way to create, delete, list token(s)

E:

and when last used

Not worried about implementation specifically. But push THIS thing over the finish line specifically.

Personally preferentially - if he were doing the work - not implement as macaroons, so there\'s a blast radius around that code

not sharing that code \.... delete legacy, \[not backwards compat\]

start saying no to passwords for accounts that have 2FA enabled

D:

concern about doing a stepping-stone measure \-- we have 2 things that are like API keys in packaging \-- people are already confused by \# of options

watch out for confusion

E: comment - acceptance criteria - caveats

[https://github.com/pypa/warehouse/issues/994#issuecomment-503624890](https://github.com/pypa/warehouse/issues/994#issuecomment-503624890)

this needs to Just Work with existing client tools with no changes

D: would modify this \... would not REQUIRE client modifications to function. but clients could be modified to use advanced featrues\..... add caveats, expirations dates \-- clients could modulate token, good for 15 min before putting it on the wire, etc. \-- enhances the feature

E:

other than that, no concerns.

those 3 requirements are important to support future work: support current implementation, quick, and doesn\'t make us tear our hair out

W:

someday you will switch off passwords on upload API

E:

yes - we\'ll announce, manage that. See who is using 2FA and send them all an email: \"that changes on this date. api keys available - go get them!\"

W:

that rollout will happen, and a 2ndary rollout when refined API scheme is released in the future

Unless we transparently roll over old keys to the new scheme/endpoint

S:

feel unsure when will new API happen

D:

new \.... tied into Pyramid authz/authn

new API implementation of tokens would automatically work

the PR in question let you choose which routes the token could be used for, limit the blast radius as Ernest said

other than initial rollout \... macaroons are more futureproof \.... no question about \"keys we add more, do they start working for those routes\" \.... \[? did I get that right?\]

question for any API key - does it get new scopes as site adds new scopes?

(w & d - talking about whitelisting routes, using caveat language)

Pyramid has permissions in authz framework - can be plugged into that

Donald did sketch out some ideas for what caveat language would look like \-- implementation detail for 99% of people, sort of bikeshedding \-- caveat language won\'t be a massive amount of work, and most people won\'t care what shape it takes

you can definitely add a simple thing like a JSON dict with a permissions key that takes an array

W: that sounds fine

D:

can make it smaller with serialization

other than tests, 90% of the work is done on that PR I think, now just the second 90% ![:-)](/wiki/europython/img/smile.png ":-)")

if all that is deemed too much for scope of work on this, I\'m fine \.... but if we can make it macaroons, that reduces future churn & reimplementation

W:

I have a proposal for how we can do this

I start rebasing your PR, get it into a working state with uploads

we eval how much time it will take to implement caveat lang, otherwise, just whitelist this route & move on to next task (i18n) & put a moratorium on adding new routes to authn policy

so, easy upgrade path for caveats

plus functional upload-only API key

D:

worst-case scenario

bake version \# into macaroon ID \# (which we probably should (anyway)). then, if we get caveat lang wrong, just increment version \#

W:

sounds good to me!

E:

I trust you both!

we are near the end of milestone 1 funding, so, let\'s be careful with that

\[Will & Ernest & Sumana discussing invoices\]
