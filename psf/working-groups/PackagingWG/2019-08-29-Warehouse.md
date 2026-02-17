# PackagingWG/2019-08-29-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Prioritize Warehouse & OTF work 

Meeting on Thursday, 29 August 2019

Attendees:

- Sumana
- William
- Ernest
- Nicole

## What can we actually finish by September 30th? And within remaining budget? 

**Imperative: Up to date Invoices to close month**

In scope?

- [https://github.com/pypa/warehouse/issues/6441](https://github.com/pypa/warehouse/issues/6441) Expose \'user\' scoped API tokens in project security history?

  - Yes

- What else? Update API token help and instructional documentation to reflect findings of user testing. Need to open ticket. See [https://gist.github.com/nlhkabu/3a571933dab1db807000658ecab27d87](https://gist.github.com/nlhkabu/3a571933dab1db807000658ecab27d87)

  - Yes

### Stopping work on security milestone 

Outside of OTF-scoped work: ToB intern will be working on security items (API tokens, events)

Sumana\'s OK with leaving this as beta and concentrating on accessibility and localisation.

Sumana to announce WebAuthn & API tokens to Announce mailing list

### Accessibility 

[https://github.com/pypa/warehouse/milestone/15](https://github.com/pypa/warehouse/milestone/15)

- All but 1 css/design issues complete \\o/
- 11 remaining issues - mostly small adjustments to HTML and JS, excluding a refactor of our tooltip component, which may be larger

We are confident we will complete this in Sept

### Localization: how far can we get? 

[https://github.com/pypa/warehouse/milestone/14](https://github.com/pypa/warehouse/milestone/14) milestone

Individual tasks we need to do: [https://github.com/pypa/warehouse/issues/1453#issuecomment-500156827](https://github.com/pypa/warehouse/issues/1453#issuecomment-500156827)

- Will we be getting tooling for i18n?

- Work in progress l10n skeleton: [https://github.com/pypa/warehouse/pull/6535](https://github.com/pypa/warehouse/pull/6535)

  - Which access tokens will we need for \... ?

- Platform options: Transifex and Weblate
  - Ernest likes Weblate

- If we are not done with localizing strings by 30 September, then let\'s start planning to tell the community that in advance, and to solicit people to complete translation.
  - Estimate 16 hours remain on localizing template strings (Nicole)
  - View/form strings (??)
    - Will to handle localizing these
    - Idea: ask in the Pyramid IRC channels

- 99% of design issues covered by accessibility work. Only need to add language switcher (#6455)

- Localizing JavaScript:

  - Will to look into this. pyBabel may be able to handle this.

When can we start recruiting translators? mid-September?

Suggestion: once we are set up with many localized messages on the translation platform, reach out to French community

## Invoices 

Let\'s aim to submit invoices on 1 September

## To Do 

\* Ernest to reach out to Weblate
