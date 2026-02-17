# WikiKurs/15 Tabellen

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiKurs(2f)15(20)Tabellen.html?action=print&media=projection) [\^](WikiKurs) [\|\<](./WikiKurs(2f)01(20)Was(20)ist(20)ein(20)MoinMoin(2d)Wiki(3f).html) [\<\<](./WikiKurs(2f)14(20)Text(2d)Stil.html) Slide 14 of 27 [\>\>](./WikiKurs(2f)16(20)Wiki(2d)interne(20)Links.html) [\>\|](./WikiKurs(2f)52(20)Struktur(20)im(20)Wiki.html)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tabellen 

## Einfachste Tabelle 

     || eins || zwei || drei ||
     || vier || fünf || sechs ||

- ::: {}
    ------ ------ -------
    eins   zwei   drei
    vier   fünf   sechs
    ------ ------ -------
  :::

## Allgemeines Tabellen-Layout 

     ||||||<tablewidth="80%">'''Kopfzeile'''||
     ||Zelle 1||Zelle 2||Zelle 3||
     ||<rowspan=2> Zeilen-übergreifend||||<bgcolor="#AAAAFF"> 2 Spalten übergreifend||
     ||<rowbgcolor="#FFFFAA">Zelle 2||Zelle 3||

- ::: {}
  +:-------------------:+:-----------:+:-----------:+
  | **Kopfzeile**                                   |
  +---------------------+-------------+-------------+
  | Zelle 1             | Zelle 2     | Zelle 3     |
  +---------------------+-------------+-------------+
  | Zeilen-übergreifend | 2 Spalten übergreifend    |
  |                     +-------------+-------------+
  |                     | Zelle 2     | Zelle 3     |
  +---------------------+-------------+-------------+
  :::

## Zellenbreite 

     || schmal ||<:99%> breit ||

- ::: {}
    -------- -------
    schmal    breit
    -------- -------
  :::

## Übergreifende Zeilen und Spalten 

     ||<|2> 2 Zeilen || Zeile 1 ||
     || Zeile 2 ||
     ||<-2> Zeile 3, 2 Spalten übergreifend ||

- ::: {}
  +:----------------:+-----------------:+
  | 2 Zeilen         | Zeile 1          |
  |                  +------------------+
  |                  | Zeile 2          |
  +------------------+------------------+
  | Zeile 3, 2 Spalten übergreifend     |
  +-------------------------------------+
  :::

## Ausrichtung 

     ||<(50%> links ||<^|3> oben ||<v|3> unten ||
     ||<:> mittig ||
     ||<)> rechts ||

- ::: {}
  +:-------+:----:+:-----:+
  | links  | oben | unten |
  +--------+      |       |
  | mittig |      |       |
  +--------+      |       |
  | rechts |      |       |
  +--------+------+-------+
  :::

## Farben 

     ||<#FF0000> rot ||<#00FF00> grün ||<#0000FF> blau ||

- ::: {}
    ----- ------ ------
    rot   grün   blau
    ----- ------ ------
  :::
