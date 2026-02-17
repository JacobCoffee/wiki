# WikiKurs/20 Dynamische Inhalte

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiKurs(2f)20(20)Dynamische(20)Inhalte.html?action=print&media=projection) [\^](WikiKurs) [\|\<](./WikiKurs(2f)01(20)Was(20)ist(20)ein(20)MoinMoin(2d)Wiki(3f).html) [\<\<](./WikiKurs(2f)19(20)Symbole.html) Slide 19 of 27 [\>\>](./WikiKurs(2f)21(20)Makros.html) [\>\|](./WikiKurs(2f)52(20)Struktur(20)im(20)Wiki.html)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![(!)](/wiki/europython/img/idea.png "(!)") *Die folgenden vier Kapitel behandeln fortgeschrittene Details. Wenn Sie das nicht interessiert, können Sie sie auch einfach [überspringen](./WikiKurs(2f)30(20)Der(20)grafische(20)Editor.html).*

# Dynamische Inhalte 

[MoinMoin](MoinMoin) ist sehr modular aufgebaut und durch Plugins in seinen Funktionen erweiterbar. Makros, Parser, Aktionen usw. können entweder eingebaut, mitgeliefert oder als Plugin selbst installiert werden.

## Makros 

Ein Makro wird als Wiki-Markup eingegeben und verarbeitet einige wenige Parameter und erzeugt daraus eine Ausgabe, die im Content-Bereich angezeigt wird.

## Parser 

Ein Parser wird als Wiki-Markup eingegeben und verarbeitet einige wenige Parameter und einen i.d.R. mehrzeiligen Block von Textdaten und erzeugt daraus eine Ausgabe, die im Content-Bereich angezeigt wird.

## Aktion 

Eine Aktion wird meist aus dem Menü aufgerufen (oder durch ein Macro) und erzeugt eine komplette HTML-Seite selbst.
