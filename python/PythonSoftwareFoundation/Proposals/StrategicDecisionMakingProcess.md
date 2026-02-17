# PythonSoftwareFoundation/Proposals/StrategicDecisionMakingProcess

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PSF Strategic Decision Making Process 

**Proposal editor:** Alyssa Coghlan

**Proposal status:** Deferred

This proposal has been deferred indefinitely.

# (FINAL DRAFT presented for PSF Board resolution) 

PSF Board resolution for adopting these guidelines:

- RESOLVED, that the Strategic Decision Making Process proposal put forward at [https://wiki.python.org/moin/PythonSoftwareFoundation/Proposals/StrategicDecisionMakingProcess](https://wiki.python.org/moin/PythonSoftwareFoundation/Proposals/StrategicDecisionMakingProcess) be adopted as the Python Software Foundation\'s approach to making significant strategic decisions in cases where neither confidentiality nor an urgent response are required.

Board members familiar with the [Python Enhancement Proposal process](https://www.python.org/dev/peps/pep-0001/) used by groups such as the CPython core development team and the Python Packaging Authority to resolve significant design decisions should not find any surprises in the philosophy behind these proposed guidelines, although the exact mechanics involved are quite different. Elements of Red Hat\'s internal \"Open Decision Making Framework\" and the Fedora change approval process have also influenced the specific design proposed.

The \"[psf-discuss@python.org](mailto:psf-discuss@python.org)\" list mentioned in the proposal will be a new list fulfilling a similar role for Python Software Foundation community management discussions that python-dev fills for Python technical discussions.

## Approval process for these guidelines 

The final draft of these guidelines is currently before the Board for formal ratification through the Board resolution process.

## Implementation of these guidelines 

Implementation of this proposal consists firstly of taking the policy documented in this proposal, editing out this preamble and the references to deferred features, and publishing the result at [PythonSoftwareFoundation/BoardPolicies/StrategicDecisionMakingProcess](./PythonSoftwareFoundation(2f)BoardPolicies(2f)StrategicDecisionMakingProcess.html).

Secondly, it involves the creation of the psf-discuss mailing list where at least the PSF Board, and optionally other interested PSF members, will publicly discuss submitted proposals.

## Significant changes from earlier discussion draft 

The earlier draft proposed a more complex proposal lifecycle that was reflected in the URL of the proposals, but actually moving this proposal through that chain indicated how tedious it was going to be to use. As a result, the proposal states indicated through the URL have been removed, with the proposal status now being tracked within the body of the proposal and in the list of proposals at [PythonSoftwareFoundation/Proposals](./PythonSoftwareFoundation(2f)Proposals.html). This is much closer to the way the Python Enhancement Proposal Process works (at some point in the future, a [MoinMoin](MoinMoin) wiki macro could potentially be used to automate generation of the categorised list of proposals).

In a similar vein of simplification, rather than building the notion of Active and Retired policies into the process itself, this specific proposal instead states that the proposal is to adopt this decision making process as a Board policy, and publish it at a particular page in the public wiki.

Consideration of the future of the psf-members list has also been moved out of this proposal, and will be handled as a separate Board resolution (linked to the creation of a separate psf-community list for general communications and collaboration amongst PSF members, distinct from the more formal psf-discuss list covered in this proposal)

## Out of scope items 

The following items are specifically out of scope for this discussion:

- Investing in relevant enhancements to [MoinMoin](MoinMoin), or changing to a different collaborative editing technology entirely. [MoinMoin](MoinMoin)\'s existing capabilities are entirely sufficient for this proposal, and discussing switching to something else would be a distraction from the core objective of establishing the PSF\'s equivalent of PEP 1.

- Defining how to republish the details of at least active policies on the main python.org site. That\'s a separate entirely technical discussion related to the capabilities of the python.org service to consume content defined elsewhere and republish it as part of the site. See [this RFE](https://github.com/python/pythondotorg/issues/608) for more details.

- Any **Deferred feature** listed throughout the body of the proposal. These notes are included for discussion purposes to clarify that addressing certain limitations of the current proposal is a task being left until later in order to prioritise getting a usable initial version of the process in place as soon as possible.

One technical enhancement potentially worth considering in a future revision to these guidelines is configuring wiki.python.org to allow the use of DISQUS powered comment threads on pages: [https://moinmo.in/MacroMarket/DisqusThread](https://moinmo.in/MacroMarket/DisqusThread)

That would allow proposal editors to opt-in on a proposal-by-proposal base to moderating a public (rather than members-only) discussion thread for that specific proposal.

# (FINAL DRAFT presented for PSF Board resolution) 

# PSF Strategic Decision Making Process 

The primary mechanism for strategic decision making in the PSF is through resolutions of the PSF Board. Members of the PSF Board of Directors are elected annually in accordance with the [PSF Bylaws](https://www.python.org/psf/bylaws/), and bear the ultimate responsibility for determining *how* the PSF pursues its [mission](https://www.python.org/psf/mission/) to:

- *\... promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.*

However, some proposed clarifications of or changes to the way the PSF pursues its strategic priorities are of sufficient import that they will benefit from a period of open discussion amongst the PSF membership prior to presentation for a Board resolution.

Similarly, new Working Group charters (as described in the Bylaws) will likely benefit from a period of collaborative discussion on the details of the charter prior to their presentation to the Board.

Just as the Python Enhancement Proposal process defines an approach to be used to propose significant technical changes to the Python language definition and other key interoperability standards, this Strategic Decision Making Process policy defines a process for proposing PSF organizational and policy changes. The approved version of this policy is published at [PythonSoftwareFoundation/BoardPolicies/StrategicDecisionMakingProcess](./PythonSoftwareFoundation(2f)BoardPolicies(2f)StrategicDecisionMakingProcess.html).

## Python Software Foundation Public Discussion Mailing List 

Collaborative discussions of proposals amongst PSF Members take place on the publicly archived \"[psf-discuss@python.org](mailto:psf-discuss@python.org)\" mailing list.

Anyone in the world that wishes to do so is free to read these discussions, but active participation requires first registering as a [PSF Member](https://www.python.org/accounts/login/) on python.org, including agreeing to abide by the Foundation\'s [Code of Conduct](https://www.python.org/psf/codeofconduct/), and choosing to subscribe to the psf-discuss mailing list, including agreeing to abide by the list\'s specific Code of Conduct. Persistent failure to abide by the Code of Conduct in collaborative environments provided by the Foundation may result in suspension or permanent removal from those environments.

**Deferred feature:** For a variety of reasons, not all Python Software Foundation Members will be equally comfortable with posting to a publicly archived discussion list. For the benefit of these members, it may be appropriate to create a core-mentorship style closed archive list aimed at newcomers to PSF deliberations. However, rather than creating such a list pre-emptively, we can wait and see how the environments on the psf-community and psf-discuss lists evolve, and determine at a later date whether or not to create a separate \"psf-mentorship\" list.

## Non-binding polls of PSF Voting Members 

At their discretion, the PSF Board may choose to include non-binding polls in ballots issued to PSF members. This may be appropriate in situations where a policy decision with no obviously correct answer needs to be made, and the Board is unable to find a clear reasoned consensus. In these cases, the collective opinion of the broader PSF membership is likely to provide an additional valuable data point that individual Directors may take into account when voting on any associated Board resolutions.

**Deferred feature:** These non-binding polls will initially be sent out solely through the formal PSF [voting infrastructure](http://vote.python.org). While it is likely desirable to also eventually make use of a simpler consensus assessment mechanism akin to [Loomio](https://www.loomio.org/) within the context of the main PSF infrastructure in order to improve discoverability for new members, that specific proposal is being omitted from this initial iteration as it is far from clear how best to pursue providing such a service ([one possibility](https://fedorahosted.org/hyperkitty/ticket/89) would be to integrate it into HyperKitty, the recommended mail archiver/web gateway for the next generation Mailman 3 mailing list service).

## Formal Proposals 

### Proposals for Discussion 

Any PSF Member (including Basic Members) may use the [Python wiki](https://wiki.python.org) to submit a proposal for discussion with the full PSF membership. Such proposals should be filed under the [PythonSoftwareFoundation/Proposals](./PythonSoftwareFoundation(2f)Proposals.html) section of the wiki. For example:

- [PythonSoftwareFoundation/Proposals/StrategicDecisionMakingProcess](./PythonSoftwareFoundation(2f)Proposals(2f)StrategicDecisionMakingProcess.html)

Proposals that are open for membership discussion should have a designated editor (or editors) listed at the top of the page and a header indicating that the proposal is a draft being discussed with the broader PSF membership. It is expected that in most cases the initial author(s) of a proposal will also be the designated editor(s). Significant changes to a proposal under discussion should only be made by the designated editors, although other PSF Members should feel free to make minor corrections (such as fixing typos and broken links) directly. If in doubt regarding the appropriateness of an edit, it\'s best to suggest it to the editors on the psf-members mailing list rather than making the change directly.

The proposal editors may choose to withdraw their proposal, in which case it will be marked as Resolved/Withdrawn in the header and the link moved to the corresponding section of the [PythonSoftwareFoundation/Proposals/](./PythonSoftwareFoundation(2f)Proposals(2f).html) page.

**Deferred feature:** There is currently no automatic link between registering as a PSF Member and gaining write access to the Python wiki, and addressing that limitation will require some significant enhancements to the PSF\'s identity management infrastructure. In the meantime refer to [FrontPage#use](FrontPage#use) to request write access if you wish to submit a proposal.

### Proposals for Resolution 

When the designated editor(s) consider it appropriate, they may submit their proposal for consideration by the PSF Board. They do this by changing the header of their proposal to indicate that it has been submitted to the Board together with emailing the psf-discuss list to request final Board consideration of the proposal.

Proposals submitted for resolution will be resolved either directly by a Board resolution, or, at the Board\'s discretion, by a full binding vote of eligible PSF Voting Members.

If the Board accept a proposal, it will be marked in its header as Accepted, the link moved to the corresponding section of the [PythonSoftwareFoundation/Proposals/](./PythonSoftwareFoundation(2f)Proposals(2f).html) page, and the acceptance communicated explicitly on the psf-discuss mailing list.

If the Board reject a proposal, it will be marked in its header as Resolved/Rejected, the link moved to the corresponding section of the [PythonSoftwareFoundation/Proposals/](./PythonSoftwareFoundation(2f)Proposals(2f).html) page, and the rejection communicated explicitly on the psf-discuss mailing list.

### Accepted Proposals 

The consequences of acceptance of a proposal will vary based on the specific proposal. For example, implementing a proposal to establish a new PSF Working Group will include at least publishing the new Working Group charter on the main python.org website, as well as establishing a mailing list or other agreed channel for discussion..

Once an accepted proposal has been implemented, it will be marked in its header as Implemented, and the link moved to the corresponding section of the [PythonSoftwareFoundation/Proposals/](./PythonSoftwareFoundation(2f)Proposals(2f).html) page.
