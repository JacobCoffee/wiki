# StructureAnnotation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

StructureAnnotation presentation technologies (see [DataRepresentation](DataRepresentation)) marks regions of content in a Web page (or other resource to be presented) with indications that such regions represent or \"map onto\" particular data structures or parts of data structures. Consequently, the content is transformed using a combination of this mapping and the underlying data, and in the purest form of StructureAnnotation, no explicit programmatic transformations are employed (unlike in [PythonInWebPage](../archive/PythonInWebPage) systems) - the data structures appear to do all the work.

A fictional example of this concept could be provided as follows:

    <table annotation:element="items">
      <tr annotation:element="item">
        <th>Name</th>
        <td>{name}</td>
      </tr>
    </table>

This would work on a data structure described by the following XML extract:

    <items>
      <item name="Ape"/>
      <item name="Baboon"/>
      <item name="Chimpanzee"/>
    </items>

Many StructureAnnotation template systems provide support for additional features such as condition testing, and temporary variables, making them more of a hybrid of [PythonInWebPage](../archive/PythonInWebPage) and StructureAnnotation.

Some example systems are

- [ZopePageTemplates](../web/ZopePageTemplates)

- Cocoon, I guess, which is Java, but has good design stuff to rip off ![;)](/wiki/europython/img/smile4.png%20";)")
