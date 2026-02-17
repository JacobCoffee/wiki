# WikiKurs/16 Wiki-interne Links

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiKurs(2f)16(20)Wiki(2d)interne(20)Links.html?action=print&media=projection) [\^](WikiKurs) [\|\<](./WikiKurs(2f)01(20)Was(20)ist(20)ein(20)MoinMoin(2d)Wiki(3f).html) [\<\<](./WikiKurs(2f)15(20)Tabellen.html) Slide 15 of 27 [\>\>](./WikiKurs(2f)17(20)Externe(20)Links.html) [\>\|](./WikiKurs(2f)52(20)Struktur(20)im(20)Wiki.html)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Wiki-interne Links 

Eine der wichtigsten Funktionen im Wiki ist das Verlinken auf andere Wiki-Seiten - deshalb geht dies auch sehr einfach.

## WikiNamen (\"CamelCase\") 

Wenn man WorteZusammenschreibt wie z.B. bei VornameNachname oder [CamelCase](CamelCase) oder [MoinMoin](MoinMoin), so dass in einem Wort mindestens 2 Wechsel Großbuchstabe-Kleinbuchstabe(n) vorkommen, so verlinkt [MoinMoin](MoinMoin) dieses Wort automatisch zu der gleichnamigen Seite.

Dies geht sehr einfach, es ist kein Wiki-Markup notwendig. Aber die ungewöhnliche Schreibweise ist nicht jedermanns Sache, daher gibt es eine weitere Alternative, die sog. \"free links\".

### Eingabe 

    CamelCase !CamelCaseAberNichtVerlinkt

### Anzeige 

[CamelCase](CamelCase) CamelCaseAberNichtVerlinkt

## Freie Links 

Möchte man Seiten verlinken, die nicht [CamelCase](CamelCase) sind oder wenn man einfach kein [CamelCase](CamelCase) mag, kann man wie folgt verlinken:

### Eingabe 

    Ein [[freier Link]] und [[andere Seite|eine andere Seite]].

### Anzeige 

Ein [freier Link](./freier(20)Link.html) und [eine andere Seite](./andere(20)Seite.html).

# Rückwärtsverfolgung von Links 

Wenn man auf den Seitennamen im Navigationsbereich klickt, sucht das Wiki nach Seiten, die auf diesen Seitennamen verlinken.

Dies wird z.B. für sogenannte Wiki-Badges (Wiki-Sticker) verwendet. Man schreibt einfach irgendwo hin:

[ToDo](./ToDo.html): Kunden XY zurückrufen wegen \...

[ToDo](./ToDo.html) ist [CamelCase](CamelCase) und verlinkt daher auf eine gleichnamige Seite, was nicht weiter aufregend ist. ![:)](/wiki/modernized/img/smile.png ":)")

Man kann aber auf der Seite [ToDo](./ToDo.html) einfach auf den Seitennamen klicken und siehe da, man findet alle Seiten, auf denen es noch irgendetwas \"zu tun\" gibt! ![(!)](/wiki/modernized/img/idea.png "(!)")
