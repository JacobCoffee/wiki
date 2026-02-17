# StructuredText/MarkUp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Structured text is text that uses indentation and simple symbology to indicate the structure of a document. For the next generation of structured text, see [ReStructuredText](http://moinmo.in/ReStructuredText "MoinMoin") and [here](http://dev.zope.org/Members/jim/StructuredTextWiki/StructuredTextNG).

A structured string consists of a sequence of paragraphs separated by one or more blank lines. Each paragraph has a level which is defined as the minimum indentation of the paragraph. A paragraph is a sub-paragraph of another paragraph if the other paragraph is the last preceding paragraph that has a lower level.

Special symbology is used to indicate special constructs:

- A single-line paragraph whose immediately succeeding paragraphs are lower level is treated as a header.

- A paragraph that begins with a \'-\', \'\*\', or \'o\' is treated as an unordered list (bullet) element.

- A paragraph that begins with a sequence of digits followed by a white-space character is treated as an ordered list element.

- A paragraph that begins with a sequence of sequences, where each sequence is a sequence of digits or a sequence of letters followed by a period, is treated as an ordered list element.

- A paragraph with a first line that contains some text, followed by some white-space and \'\--\' is treated as a descriptive list element. The leading text is treated as the element title.

- Sub-paragraphs of a paragraph that ends in the word \'example\' or the word \'examples\', or \'::\' is treated as example code and is output as is.

- Text enclosed single quotes (with white-space to the left of the first quote and whitespace or puctuation to the right of the second quote) is treated as example code.

- Text surrounded by \'\*\' characters (with white-space to the left of the first \'\*\' and whitespace or puctuation to the right of the second \'\*\') is emphasized.

- Text surrounded by \'\*\*\' characters (with white-space to the left of the first \'\*\*\' and whitespace or puctuation to the right of the second \'\*\*\') is made strong.

- Text surrounded by \'\_\' underscore characters (with whitespace to the left and whitespace or punctuation to the right) is made underlined.

- Text encloded by double quotes followed by a colon, a URL, and concluded by punctuation plus white space, \*or\* just white space, is treated as a hyper link. For example:

  - \"Zope\":[http://www.zope.org/](http://www.zope.org/) is \...

  Is interpreted as \'\<a href=\"[http://www.zope.org/\"\>Zope\</a\>](http://www.zope.org/%22%3EZope%3C/a%3E) is \....\'

  **Note:** This works for relative as well as absolute URLs.

- Text enclosed by double quotes followed by a comma, one or more spaces, an absolute URL and concluded by punctuation plus white space, or just white space, is treated as a hyper link. For example:

  - \"mail me\", [mailto:amos@digicool.com](mailto:amos@digicool.com).

  Is interpreted as \'\<a href=\"[mailto:amos@digicool.com\"\>mail](mailto:amos@digicool.com%22%3Email) me\</a\>.\'

- Text enclosed in brackets which consists only of letters, digits, underscores and dashes is treated as hyper links within the document. For example:

  - As demonstrated by Smith \[12\] this technique is quite effective.

  Is interpreted as \'\... by Smith \<a href=\"#12\"\>\[12\]\</a\> this \...\'. Together with the next rule this allows easy coding of references or end notes.

- Text enclosed in brackets which is preceded by the start of a line, two periods and a space is treated as a named link. For example:

  - . \[12\] \"Effective Techniques\" Smith, Joe \...

  Is interpreted as \'\<a name=\"12\"\>\[12\]\</a\> \"Effective Techniques\" \...\'. Together with the previous rule this allows easy coding of references or end notes.

- A paragraph that has blocks of text enclosed in \'\|\|\' is treated as a table. The text blocks correspond to table cells and table rows are denoted by newlines. By default the cells are center aligned. A cell can span more than one column by preceding a block of text with an equivalent number of cell separators \'\|\|\'. Newlines and \'\|\' cannot be a part of the cell text. For example:

  - |||| **Ingredients** ||
        || *Name* || *Amount* ||
        ||Spam||10||
        ||Eggs||3||

  renders like this:

  - ::: {}
    +:----------:+:----------:+
    | \*\*Ingredients\*\*     |
    +------------+------------+
    | \*Name\*   | \*Amount\* |
    +------------+------------+
    | Spam       | 10         |
    +------------+------------+
    | Eggs       | 3          |
    +------------+------------+
    :::
