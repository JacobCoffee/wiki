# PythonInWebPage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PythonInWebPage presentation systems (see [DataRepresentation](DataRepresentation)) encourages the use of Python source code embedded in the content of a Web page (or other resource to be presented) such that the execution of the code causes the surrounding content to be transformed in some way. A classic, simplified example of this concept using JSP syntax might look like this:

    <table>
      <%
      for item in items:
        %>
        <tr>
          <th>Name</th>
          <td><%= item.name %></td>
        </tr>
        <%
      %>
    </table>

or like this ([PythMl](http://adullact.net/projects/pythml/) syntax)

    <table>
    for item in items:
      <tr>
      <th>Name</th>
      <td>`item.name`</td>
      </tr>
    </table>

Note that Python\'s need for indentation raises issues with how code blocks are to be delimited, especially in content which may itself be indented according to a different scheme, hence the use of an empty code block after the body of the loop in the above example.

Comparable technologies include: ASP (Active Server Pages), JSP ([JavaServer](./JavaServer.html) Pages), PHP.
