# PloneOrgMigration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**When**: Saturday and Sunday before [EuroPython](EuroPython) (June 25th-26th 2005) - the dates are now confirmed.

**Sprint leader**: [AlexanderLimi](AlexanderLimi)

**Remote Sprinting via IRC is also encouraged!**

Before the Plone 2.1 release we should have plone.org running on the new release, to show off the fantastic new features.

The plone.org site is extremely old and crufty, and suffers from a lot of problems from back in the early days. It has been migrated from early pre-releases of Plone 0.8 and 0.9, and is not in good shape.

The best approach is to create a clean Plone 2.1 instance of plone.org and move all the content over, leaving plone.org in a read-only state during the migration.

We will perform the migration on a backup instance to figure out the steps involved, and then do the migration properly when everything is verified to work. We will **document** and **script** the process to the fullest extent possible.

There is some crufty old software running on plone.org that needs special care:

- **CMFCollector** - this is very old and about to die from the amount of issues we have in it. At the very minimum, we need to look at converting it to a BTree-based structure - \$DEITY knows why it wasn\'t in the first place. ![:)](/wiki/europython/img/smile.png ":)")

- **CMFWorkspaces** - another old piece of software that nearly works. ![;)](/wiki/europython/img/smile4.png ";)") We need to evaluate whether we need this software anymore. My guess is no - since we have [ConstrainTypes](./ConstrainTypes.html) in the new 2.1 release, but this is something that we need to reach a decision on.

- **ZWiki** - ideally we should get rid of all wiki pages and turn them into normal documents. ZWiki doesn\'t work very well in Plone, and it\'s become a burden to support it. Also, it makes sense to reduce the number of external dependencies. The only Wiki feature we use is the link markup, and that can be replaced with products like Wicked later on.

In addition, we need to make sure that all the user setting and configuration makes it over to the new site.

It\'s not very glamorous work, but it\'s necessary - and it will pay back immensely in a fast and usable plone.org that doesn\'t suck maintenance time.

**Location**

Where, oh where?

**Add your name below if you plan to participate**

(indicate whether you\'ll actually be at [EuroPython](EuroPython), or remote sprinting)

- Alexander Limi (at [EuroPython](EuroPython))

- Martin Aspeli (at [EuroPython](EuroPython))

- Alan Runyan (at Enfold Houston Office)

- [ReinoutVanRees](ReinoutVanRees) (at [EuroPython](EuroPython))

- Ivo van der Wijk (at [EuroPython](EuroPython))
