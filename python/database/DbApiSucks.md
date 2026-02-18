# DbApiSucks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

What sucks about the [DbApi](./DbApi.html)

It totally misuses the cursor concept.

A cursor is a set of database rows you iterate over. It can be clientside or server-side.

In the [DbApi](./DbApi.html), you first create a cursor object, then execute a statement on it, then fetch the results.

The normal way of using cursors with the DB-API is to reuse the cursor objects and fire new statements with them, and fetch new results.

This is totally misguided in my opinion.

A much better API should look similar to:

    cx = dbapimodule.connect()
    cx.execute("insert into tablename(val) values (?)", ('foo',))

    for row in cx.executeReader("select val from tablename"):
        print row

    row = cx.executeRow("select max(val) from tablename")

etc.

executing statements logically belongs in the connection object, not in the cursor object.

(Alas, then you could only loop over a single set of results at a time. I think the current cursor concept makes sense. -skip)

Enough ranting for now, more will come some day. Maybe somebody can clean this up and add a few thoughts ![:)](/wiki/europython/img/smile.png%20":)")

\-\--

The \"execute\" method, or whatever it\'s called, could then return an iterator. In that case there is no problem with loop over different sets of results. The current cursor concept does make \*some\* sense, but it\'s awkward and pre-iterators.
