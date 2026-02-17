# JepGuidelines

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- *JEP: JepGuidelines*

- *Title: JEP Guidelines*

- *Version: 1*

- *Last-Modified: 20050205*

- *Author: [BillDehora](BillDehora)*

- *Status: Draft*

- *Type: Informational*

- *Created: 20050205*

------------------------------------------------------------------------

### Contents 

- What is a JEP?
- Kinds of JEPs
- JEP Work Flow
- What belongs in a successful JEP?
- JEP Formats and Templates
- JEP Header Preamble
- Reporting JEP Bugs, or Submitting JEP Updates
- Transferring JEP Ownership
- References and Footnotes
- Copyright

### What is a JEP? 

JEP stands for Jython Enhancement Proposal. JEPs are strongly based on Python Enhancement Proposals (PEP) (indeed much of the content here is lifted from PEP 1).

A JEP is a design document providing information to the Jython community, or describing a new feature for Jython. The JEP should provide a concise technical specification of the feature and a rationale for the feature.

JEPs are the primary mechanisms for proposing new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Jython. The JEP author is responsible for building consensus within the community and documenting dissenting opinions.

### Kinds of JEPs 

There are two kinds of JEPs.

- A Standards Track JEP, or SJEP, describes a new feature or implementation for Jython.
- An Informational JEP, or IJEP, describes a Jython design issue, or provides general guidelines or information to the Jython community, but does not propose a new feature. Informational JEPs do not necessarily represent a Jython community consensus or recommendation, so users and implementors are free to ignore Informational JEPs or follow their advice.

### JEP Work Flow 

The JEP process begins with a new idea for Jython. It is highly recommended that a single JEP contain a single key proposal or new idea. The more focussed the JEP, the more successful it tends to be. The community reserves the right to reject JEP proposals if they appear too unfocussed or too broad.

Each JEP must have a champion \-- someone who writes the JEP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea. The JEP champion (a.k.a. Author) should first attempt to ascertain whether the idea is JEP-able. Posting to the jython-dev mailing list is recommended. Small enhancements or patches often don\'t need a JEP and can be injected into the Jython development work flow with a patch submission or feature request.

The JEP champion then creates the JEP with a proposed title and a rough, but fleshed out, draft of the JEP on the Jython Wiki. This draft must be written in JEP style as described below.

If the community approves, the JEP will be assigned a wiki page, label it as Standards Track or Informational, give it status \"Draft\". The community will not unreasonably deny a JEP. Reasons for denying JEP status include duplication of effort, being technically unsound, not providing proper motivation or addressing backwards compatibility, or not in keeping with the Jython philosophy.

If a pre-JEP is rejected, the author may elect to take the pre-JEP to the jython-dev list to help flesh it out, gain feedback and consensus from the community at large, and improve the JEP for re-submission.

The author of the JEP is then responsible for posting the JEP to the community fora, and marshaling community support for it. As updates are necessary, the JEP author can edit the JEP on the wiki.

Standards Track JEPs consists of two parts, a design document and a reference implementation. The JEP should be reviewed and accepted before a reference implementation is begun, unless a reference implementation will aid people in studying the JEP. Standards Track JEPs must include an implementation \-- in the form of code, patch, or URL to same \-- before it can be considered Final.

JEP authors are responsible for collecting community feedback on a JEP before submitting it for review. A JEP that has not been discussed on jython-dev will not be accepted. However, wherever possible, long open-ended discussions on public mailing lists should be avoided. Strategies to keep the discussions efficient include, setting up a separate forum for the topic, having the JEP author accept private comments in the early design phases, etc. JEP authors should use their discretion here.

Once the authors have completed a JEP, they must inform the community that it is ready for review. JEPs are reviewed by the BDFL and his chosen consultants, who may accept or reject a JEP or send it back to the author(s) for revision. For a JEP that is pre-determined to be acceptable (e.g., it is an obvious win as-is and/or its implementation has already been checked in) the community may also initiate a JEP review, first notifying the JEP author(s) and giving them a chance to make revisions.

For a JEP to be accepted it must meet certain minimum criteria. It must be a clear and complete description of the proposed enhancement. The enhancement must represent a net improvement. The proposed implementation, if applicable, must be solid and must not complicate the interpreter unduly.

Once a JEP has been accepted, the reference implementation must be completed. When the reference implementation is complete and accepted by the community, the status will be changed to \"Final\".

A JEP can also be assigned status \"Deferred\". The JEP author or editor can assign the JEP this status when no progress is being made on the JEP. Once a JEP is deferred, the JEP editor can re-assign it to draft status.

A JEP can also be \"Rejected\". Perhaps after all is said and done it was not a good idea. It is still important to have a record of this fact.

JEPs can also be replaced by a different JEP, rendering the original obsolete. This is intended for Informational JEPs, where version 2 of an API can replace version 1.

JEP work flow is as follows:

      Draft -> Accepted -> Final -> Replaced
       ^
       +----> Rejected
       v
     Deferred

Some Informational JEPs may also have a status of \"Active\" if they are never meant to be completed. E.g. JEP 1 (this JEP).

### What belongs in a successful JEP? 

Each JEP should have the following parts:

1.  Preamble \-- RFC 822 style headers containing meta-data about the JEP, including the JEP [WikiPage](./WikiPage.html), a short descriptive title (limited to a maximum of 44 characters), the names, and optionally the contact info for each author, etc.

2.  Abstract \-- a short (\~200 word) description of the technical issue being addressed.

3.  Copyright/public domain \-- Each JEP must either be explicitly labelled as placed in the public domain (see this JEP as an example) or licensed under the Open Publication License \[8\].

4.  Specification \-- The technical specification should describe the syntax and semantics of any new language feature. The specification should be detailed enough to allow competing, interoperable implementations for any of the current Jython platforms (CJython, Jython, Jython .NET).

5.  Motivation \-- The motivation is critical for JEPs that want to change the Jython language. It should clearly explain why the existing language specification is inadequate to address the problem that the JEP solves. JEP submissions without sufficient motivation may be rejected outright.

6.  Rationale \-- The rationale fleshes out the specification by describing what motivated the design and why particular design decisions were made. It should describe alternate designs that were considered and related work, e.g. how the feature is supported in other languages. The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.

7.  Backwards Compatibility \-- All JEPs that introduce backwards incompatibilities must include a section describing these incompatibilities and their severity. The JEP must explain how the author proposes to deal with these incompatibilities. JEP submissions without a sufficient backwards compatibility treatise may be rejected outright.

8.  Reference Implementation \-- The reference implementation must be completed before any JEP is given status \"Final\", but it need not be completed before the JEP is accepted. It is better to finish the specification and rationale first and reach consensus on it before writing code.

The final implementation must include test code and documentation appropriate for either the Jython language reference or the standard library reference.

### JEP Formats and Templates 

Each JEP must begin with an RFC 822 alike header preamble. The headers must appear in the following order. Headers marked with \"?\" are optional and are described below. All other headers are required.

      JEP: <jep wiki page>
      Title: <jep title>
      Version: <version string>
      Last-Modified: <date string>
      Author: <list of authors' real names and optionally, email addrs>
      ?Discussions-To: <email address>
      Status: <Draft | Active | Accepted | Deferred | Rejected | Final | Replaced>
      Type: <Informational | Standards Track>
      ?Requires: <jep numbers>
      Created: <date created on, in yyyymmdd format>
      ?Jython-Version: <version number>
      Post-History: <dates of postings to python-list and python-dev>
     ?Replaces: <jep wiki page>
     ?Replaced-By: <jep number>

The Author header lists the names, and optionally the email addresses of all the authors/owners of the JEP. The format of the Author header value must be

- Random J. User \<[address@dom.ain](mailto:address@dom.ain)\>

if the email address is included, and just

- Random J. User

if the address is not given. For historical reasons the format \"[address@dom.ain](mailto:address@dom.ain) (Random J. User)\" may appear in a JEP, however new JEPs must use the mandated format above, and it is acceptable to change to this format when JEPs are updated.

If there are multiple authors, each should be on a separate line following RFC 2822 continuation line conventions. Note that personal email addresses in JEPs will be obscured as a defense against spam harvesters.

While a JEP is in private discussions (usually during the initial Draft phase), a Discussions-To header will indicate the mailing list or URL where the JEP is being discussed. No Discussions-To header is necessary if the JEP is being discussed privately with the author, or on the python-list or python-dev email mailing lists. Note that email addresses in the Discussions-To header will not be obscured.

The Type header specifies the type of JEP: Informational or Standards Track.

The format of a JEP is specified with a Content-Type header. The acceptable values are \"text/plain\" for plaintext JEPs (see JEP 9 \[3\]) and \"text/x-rst\" for reStructuredText JEPs (see JEP 12 \[4\]). Plaintext (\"text/plain\") is the default if no Content-Type header is present.

The Created header records the date that the JEP was created, while Post-History is used to record the dates of when new versions of the JEP are posted to python-list and/or python-dev. Both headers should be in yyyymmdd format, e.g. 20050205.

Standards Track JEPs must have a Jython-Version header which indicates the version of Jython that the feature will be released with. Informational JEPs do not need a Jython-Version header.

JEPs may have a Requires header, indicating the JEP numbers that this JEP depends on.

JEPs may also have a Replaced-By header indicating that a JEP has been rendered obsolete by a later document; the value is the [WikiPage](./WikiPage.html) of the JEP that replaces the current document. The newer JEP must have a Replaces header containing the [WikiPage](./WikiPage.html) of the JEP that it rendered obsolete. Reporting JEP Bugs, or Submitting JEP Updates

How you report a bug, or submit a JEP update depends on several factors, such as the maturity of the JEP, the preferences of the JEP author, and the nature of your comments. For the early draft stages of the JEP, it\'s probably best to send your comments and changes directly to the JEP author. For more mature, or finished JEPs you may want to submit corrections to the Jython issue list or better yet as a patch so that your changes don\'t get lost.

When in doubt about where to send your changes, please check first on jython-dev.

### Transferring JEP Ownership 

It occasionally becomes necessary to transfer ownership of JEPs to a new champion. In general, we\'d like to retain the original author as a co-author of the transferred JEP, but that\'s really up to the original author. A good reason to transfer ownership is because the original author no longer has the time or interest in updating it or following through with the JEP process, or has fallen off the face of the \'net (i.e. is unreachable or not responding to email). A bad reason to transfer ownership is because you don\'t agree with the direction of the JEP. We try to build consensus around a JEP, but if that\'s not possible, you can always submit a competing JEP.

If you are interested in assuming ownership of a JEP, send a message asking to take over, addressed to the original author. If the original author doesn\'t respond to email in a timely manner, the community can make a decision.

### Copyright 

This document has been placed in the public domain.

------------------------------------------------------------------------

[CategoryJep](CategoryJep)
