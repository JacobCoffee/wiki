# ElementBasedSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Element-based syntax typically uses XML-like elements to either annotate parts of a Web page (see [StructureAnnotation](StructureAnnotation)) or to introduce program code into the document (see [PythonInWebPage](PythonInWebPage)). For example:

    <table>
      <python-block>
      for item in items:
        </python-block>
        <tr>
          <th>Name</th>
          <td><python-expr>item.name</python-expr></td>
        </tr>
        <python-block>
        # End of for loop.
      </python-block>
    </table>

One stated advantage of element-based syntax is that the document can be manipulated more easily with XML tools. Arguably, the use of [PythonInWebPage](PythonInWebPage) techniques can complicate matters because the content of the program code elements requires additional parsing and analysis.
