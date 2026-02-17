# CommentBasedSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Comment-based syntax typically uses XML-like comments or special preprocessed comment-like elements to either annotate parts of a Web page (see [StructureAnnotation](StructureAnnotation)) or to introduce program code into the document (see [PythonInWebPage](PythonInWebPage)).

See [PythonInWebPage](PythonInWebPage) for an example using JSP-like syntax. Here is a [StructureAnnotation](StructureAnnotation) version using HTML-like syntax:

    <table>
      <!-- loop:item in items -->
        <tr>
          <th>Name</th>
          <td><!-- expr:item.name --></td>
        </tr>
      <!-- loop:end -->
    </table>

One potential advantage of comment-based syntax is that HTML-aware tools can ignore the comments, should the syntax have been chosen correctly.
