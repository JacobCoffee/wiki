# PackagingWG/2020-11-11-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Nov 11th, 2020

Participants:

- Georgia Bullen
- Pradyun Gedam
- Bernard Tyers
- Sumana Harihareswara

Agenda:

- status and blockers
  - Georgia: we\'re working our way through analysis of diff. surveys, the \"buy a feature\"
    - we have pulled together a meeting to swap notes re: workshops for FLOSS developers to plan
    - no known blockers
    - prediction: high likelihood of submission today
  - Nicole: pushed out documentation survey and is doing interviews on that
    - no known blockers
  - Bernard: no real blockers. Working on the report
    - pip backtracking message PR - probably finished [https://github.com/pypa/pip/pull/9040](https://github.com/pypa/pip/pull/9040)

      - TODO: Sumana to re-review

    - about to start: trying to get in touch with package manager maintainers, so, is changing approach to \"pip in pckg mngr ecosystem\" and will talk to users instead
      - TODO: Sumana to ping William Woodruff and ask him for an hour of Bernard\'s time
      - TODO: Sumana to ping people who run package managers that interact/interoperate/conflict with pip stuff
        - aptitude (Debian/Ubuntu)

        - (ana)conda - done 17 Nov

        - brew/homebrew - done 17 Nov

        - dnf (Fedora)

        - pacman \[used in Manjaro Linux distro\] ([https://wiki.archlinux.org/index.php/pacman](https://wiki.archlinux.org/index.php/pacman))

          - TODO: Sumana to ping Santiago from Arch - done 17 Nov
      - There are some other package managers where we could learn from their experience/UX/functionality
        - I\'ve not spoken to them but: cargo (from research people have mentioned it\'s nice)

        - ruby, bundler ([https://bundler.io/](https://bundler.io/))
- invoices
  - Gedam has been requested to do so
- issues that need followup
  - [https://github.com/pypa/pip/issues/9011](https://github.com/pypa/pip/issues/9011)

    - depends on resolvelib (Carry all incompatibilities during backtracking \-- #60)
    - next: Pradyun will do some test writing

  - [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785)

    - New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together
    - next: Pradyun to do deep investigative dive
- pip 20.3 release
  - Release blockers/things we need to do first \[basically all Pradyun\]: (PG: wheeeeeeee)
    - 7744 \-- small, needs implementation.
    - 9011 \-- needs a test.
    - 9040 \-- needs re-review and merge.
    - 8785 \-- needs a deeper dive.
    - 8495 \-- needs implementation.
  - people offer help - what would be most effective is some virtual coworking time
    - Bernard is free to do this all Thurs, plus Fri morning
    - TODO: This time tomorrow would be ideal!
