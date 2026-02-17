# ZwjAndZwnjAsIdentifiers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Inroduction 

Python 3 Supports Non-ASCII Identifiers as per [PEP 3131](http://www.python.org/dev/peps/pep-3131/). But this support is incomplete for certain languages where special characters such as ZWJ, ZWNJ are used extensively. Example for such languages are Malayalam, Kannada, Sinhala, Farsi etc.

## Unicode standard on Using ZWJ/ZWNJ etc in Identifiers 

ZWJ and ZWNJ are format control characters and unicode defines the usage of these characters in identifiers in [TR31 in section 2.3 Layout and Format Control Characters](http://unicode.org/reports/tr31/#Layout_and_Format_Control_Characters)

Unicode recommends allowing usage of ZWJ/ZWNJ or \"the Join_Control characters\" in Identifiers limited to 3 contexts.

- Allow ZWNJ in breaking a cursive connection : That is, in the context based on the Joining_Type property, consisting of:
  - A Left-Joining or Dual-Joining character, followed by zero or more Transparent characters, followed by a ZWNJ, followed by zero or more Transparent characters, followed by a Right-Joining or Dual-Joining character
  - This corresponds to the following regular expression (in Perl-style syntax): /\$LJ \$T\* ZWNJ \$T\* \$RJ/
    - where:
      - \$T = \[:Joining_Type=Transparent:\] \$RJ = \[ \[:Joining_Type=Dual_Joining:\]\[:Joining_Type=Right_Joining:\] \] \$LJ = \[ \[:Joining_Type=Dual_Joining:\]\[:Joining_Type=Left_Joining:\] \]
- Allow ZWNJ in a conjunct context. That is, a sequence of the form:
  - A Letter, followed by a Virama, followed by a ZWNJ
  - This corresponds to the following regular expression (in Perl-style syntax): /\$L \$V ZWNJ/
    - where:
      - \$L = \[:General_Category=Letter:\] \$V = \[:Canonical_Combining_Class=Virama:\]
- Allow ZWJ in a conjunct context. That is, a sequence of the form:
  - A Letter, followed by a Virama, followed by a ZWJ
  - This corresponds to the following regular expression (in Perl-style syntax): /\$L \$V ZWJ/ where:
    - \$L= \[:General_Category=Letter:\] \$V = \[:Canonical_Combining_Class=Virama:\]

## Affected Languages 

- Malayalam
- Kannada
- Bengali
- Languages that use Devanagari Script (Hindi, Marathi..)
- Telugu
- Farsi
- Sinhala
- Arabi
- Khmer

## References 

- [http://bugs.python.org/issue5358](http://bugs.python.org/issue5358) \-- Rejected issue about control characters

- [http://www.python.org/dev/peps/pep-3131/](http://www.python.org/dev/peps/pep-3131/)

- [http://unicode.org/review/pr-96.html](http://unicode.org/review/pr-96.html)

- [http://unicode.org/reports/tr31/#Layout_and_Format_Control_Characters](http://unicode.org/reports/tr31/#Layout_and_Format_Control_Characters)

- [http://www.unicode.org/reports/tr36/](http://www.unicode.org/reports/tr36/)

- [Suggestions from /r/Python community](http://www.reddit.com/r/Python/comments/dgf1q/how_to_approach_a_complex_issue_where_python_core/)
