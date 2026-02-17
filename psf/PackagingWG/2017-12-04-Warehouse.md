# PackagingWG/2017-12-04-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Warehouse kickoff meeting, 12-04-2017
      -------------------------------------
      Attending:

      * Nicole Harris
      * Donald Stufft
      * Mark Mangoba
      * Ernest W. Durbin III
      * Sumana Harihareswara
      * Eric Holscher
      * Dustin Ingram
      * Laura Hampton


      1. Introductions

       - Ernest - 30 hours/wk. Particularly working on infrastructure & automation for getting Warehouse deployed, implementing metrics, and adding monitoring, and additionally contributing to features on project. Also will be doing some community support - working on tickets, issues, etc. for Warehouse/PyPI & contributors.

       - Dustin - 30 hours/wk. Shipping features in Warehouse, infrastructure dev, community stuff as well.

       - Donald - 2 days/week (Wednesdays and Thursdays), largely coordinating and working on features for Warehouse. Amazon gives him 40% of his time to work on PyPI, pip, and related packaging work.

       - Nicole - about 10 hours/week. Responsible for UX and UI and HTML/CSS of any new features, plus cleaning up any existing interfaces we have in Warehouse. Also intending to work on the fundraising aspect of the PyPI relaunch.

       - Mark Mangoba (PSF IT manager) works from 7-11am every day on PSF. Mainly this group's PSF liaison, helping with contracts, community reporting, and anything else we need from PSF.

       - Eric: wearing 2 hats. PSF board member hat - helped get grant, and wants to make sure PyPI is sustainable. Read the Docs hat - not specifically funded to dedicate time to this project via the grant, but happy to help, especially with pythonhosted translation & docs, and be a resource for sustainability conversation. Available across the week.

       - Sumana - approximately 10-15 hours per week, with more as needed. Project manager, working to break blockers for others, make sure other people know what expectations are of them & what to do next, and do stuff that needs doing, eg., testing, release management, product management/prioritization, meeting-running, communication.

       - Laura - several hours per week, assisting Sumana with project management

      2. Planned next steps

       - On Wednesday, Ernest, Donald, Dustin and Sumana triage existing bugs and figure out milestones to parallelize work. (See the second item in Issues/Blockages below.)

       - Nicole is considering doing some user tests on the UI to qualify the UI, to pick up problems that currently exist.

      3. Tabled Activities

       - Our original vision for this grant included funding for us to do sponsorship outreach; the current grant-funded project does not include this position. We have money to build a mechanism into PyPI/Warehouse, but we do not have money for someone to do outreach/marketing/execution. Maybe this is an after-grant concern. A TODO for Sumana: in approximately 2 weeks (e.g., on December 18th), discuss this with Eric, so he can perhaps champion this issue within PSF to get resoources or otherwise help us work towards getting someone's time to work on sponsorship outreach for PyPI sustainability.

      4. Issues / Blockages

       - Nicole mentioned potentially needing help with JavaScript [per https://github.com/pypa/warehouse/issues/1297 ], regarding form validation, password complexity validation, and so on, and suggested we want to tag JS work in issues in the GitHub repo. Dustin, Donald, and Ernest reassured that they can handle helping with JavaScript issues probably to the extent necessary.

       - It would be useful to have some smaller feature-based milestones to use to organize our activity, especially to help parallelize people's work. The basic division for parallelization is probably (a) user based interactions (being able to reset your password, manage your projects and releases through Warehouse) and infrastructure (infrastructure and deployment on new hosting).

         Our APIs work, but aren't robust enough for the amount of traffic that would flow through once we redirect pypi.python.org. And we can split up things we need in order for pip install to work (for users) and things we need for the UI to be redirected (features for maintainers). The UI side is where the bulk of the work is less done, primarily UI flows around management and similar tasks.
