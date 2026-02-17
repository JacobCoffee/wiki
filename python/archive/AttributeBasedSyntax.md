# AttributeBasedSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Attribute-based syntax typically uses XML-like attributes to either annotate parts of a Web page (see [StructureAnnotation](StructureAnnotation)) or to introduce program code into the document (see [PythonInWebPage](PythonInWebPage)).

See [StructureAnnotation](StructureAnnotation) for an example.

One stated advantage of attribute-based syntax is that the document can still be manipulated using XML tools and typically be edited using HTML-aware tools. However, not all HTML editors allow the use of arbitrary XML attributes on HTML elements, and the (mis/re)use of permissible HTML attributes may be required. For example:

    <table id="annotation:items">
      <tr id="annotation:item">
        <th>Name</th>
        <td>{name}</td>
      </tr>
    </table>

Attribute-based syntax is arguably unsuitable for true [PythonInWebPage](PythonInWebPage) systems, since attributes do not lend themselves to the storage of potentially large pieces of Python code, and indentation could be a major problem. However, programmatic features can be introduced into the attribute values using a restricted subset of Python code - see Zope Page Templates for an example of this kind of thing in action.
