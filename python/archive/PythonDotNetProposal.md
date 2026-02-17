# PythonDotNetProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Let\'s use this page to construct a concrete proposal to submit to the PSF Board. The Board is meeting on Monday, April 10, 2006, at 17:00 UTC.

IRC discussions: irc.freenode.net #starship

Proposal champion: [David Goodger](mailto:goodger@python.org).

As David Ascher wrote,

> Speaking personally, I think that the PSF board is happy to consider helping the starship, but we need a specific proposal, not a long dialogue. If someone comes to us saying: \"we want to do X, it will cost Y, we need Z from the PSF\", then we can talk about it. But we need someone to lead, coordinate, synthesize and argue the point.

And Martin von Löwis wrote,

> Somebody needs to take charge. The PSF board can provide funding that is necessary (assuming it can agree to the requested budget); it can also select between a number of presented alternatives if nobody else feels like deciding. However, the PSF *cannot* /run/ the starship.

::: 
### Uses of Starship.python.net

- Starship is or has been used to distrubute several important Python packages, including Mark Hammond\'s Win32 extensions, and as a staging area where preview builds of wxPython are made available for testing.
- Starship hosts a plethora of smaller projects, scripts, and snippets.
- Starship hosts a bevy of Pythonista\'s home pages.
- Testbed with several versions of Python installed.
- A mailing list for communication among the crew is hosted on starship.
- Various community mailing lists.
:::

::: 
### The Present

Starship.python.net is a machine hosted by Stefan Drees in a datacenter in Germany. It\'s costing him 149 EUR per month. Over the last three months the used bandwidth was between 50 GB/month and 70 GB/month. So expecting 2,5 GB/day is not to far from reality. (caveat: future usage depends on future users)
:::

::: 
### Future Scenarios

1.  Keep the current server in the current datacenter.

      ------- -----------------------------------------------------------------------
      Pros:   No work to do, except for collecting the money.
      Cons:   Expensive (149 EUR/month) minus the part contributed by Stefan Drees.
      ------- -----------------------------------------------------------------------

2.  Get a cheaper (but much better!) dedicated server in the current datacenter.

    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Details:               | 69 EUR/month will get us a CPU AMD Athlon 64 3000+, 1 GB RAM, 2 x 80 GB hard disc (RAID1), 80 GB ftp-based backup space, unlimited traffic via 100 Mbit/s, GeoTrust Inc. SSL certificate, with an additional Cisco-based firewall. |
    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Questions and proposed answers/alternatives:                                                                                                                                                                                                                |
    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                        | - How will we pay for it? PSF or individuals                                                                                                                                                                                       |
    |                        | - Who will receive payment? Stefan Drees as partial refund.                                                                                                                                                                        |
    |                        | - Who is responsible for paying the bills? Stefan Drees, like before.                                                                                                                                                              |
    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Pros:                  | No unknowns.                                                                                                                                                                                                                       |
    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Cons:                  | Payment logistics (see Questions above).                                                                                                                                                                                           |
    +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    A \"show of hands\" survey on the crew member\'s list showed that many members would be willing to pay for the starship\'s upkeep, certainly enough to cover the monthly cost.

3.  Host with XS4ALL on a python.org machine, such as MacTeagle.

    +------------+---------------------------------------------+
    | Questions: | - Is XS4ALL *willing* to host the starship? |
    |            | - Is there a machine available?             |
    +------------+---------------------------------------------+
    | Pros:      | Potentially free.                           |
    +------------+---------------------------------------------+
    | Cons:      | Unknowns (see questions above).             |
    +------------+---------------------------------------------+

4.  Host elsewhere.

    - [http://python-hosting.com](http://python-hosting.com)
      +------------+-----------------------------------------------------------------------------------------------------------------+
      | Questions: | - Are they willing to host the starship?                                                                        |
      |            | - At what cost?                                                                                                 |
      |            | - With what functionality? (We\'d need more than the \"free Trac & SVN\" they provide to open-source projects.) |
      +------------+-----------------------------------------------------------------------------------------------------------------+
      | Pros:      | Potentially free.                                                                                               |
      +------------+-----------------------------------------------------------------------------------------------------------------+
      | Cons:      | Unknowns (see questions above).                                                                                 |
      +------------+-----------------------------------------------------------------------------------------------------------------+
    - Alternatives?
:::

::: 
### Future Membership

- Free or fee?
- Open to all PSF members?
- Open to others? Under what criteria?
:::

::: 
### Python.net Administrators

- [Stefan Drees](mailto:stefan@drees.name)
- Greg Ward greg-starship at gerg dot ca
- [Jim Tittsler](mailto:jwt@python.net)
- Tom Bryan tbryan at python dot net
- [Michael Hudson](MichaelHudson)

Are all willing to administer the future ship like they have administered the current.
:::
