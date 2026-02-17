# StruktureradText

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

StruktureradText är text som använder indrag och enkla symboler för att beskriva dokumentets strukture. För att läsa om nästa generations strukturerad text, se [ReStructuredText](http://moinmo.in/ReStructuredText "MoinMoin") och [here](http://dev.zope.org/Members/jim/StructuredTextWiki/StructuredTextNG).

En strukturerad sträng består av en sekvens av paragrafer åtsklijda av en eller flera blankrader. Varje stycke har en nivå som är definierad av det minsta indraget i stycket. En stycke är inuti ett annat stycke om det omkringliggande stycker har en lägre indragsnivå.

Speciell symbolik används för att beskriva speciella konstruktioner:

- Ett enradsstycke som kommer direkt efter ett stycke med lägre indragsnivå behandlas som en rubrik.

- Ett stycke som börjar med \'-\', \'\*\', or \'o\' behandlas som en oordnad punktlista.

- Ett stycke som börjar med en sekvens av siffror, följt av mellanslag behanldas som en numrerad lista.

- Ett stycke som börjar med en sekvens av sekvenser, där varje sekvens är en sekvens av siffror eller en sekvens av bokstäver följt av en punkt, behandlas som ett numrerat listelement.

- Ett stycke vars första rad innehåller någon text, följt av mellanslag och \'\--\' behanldas som ett beskrivande listelement. Den initiala texten tas som rubrik.

- Delstycken av ett stycke som slutar med ordet \'exempel\' eller med \'::\' behandlas som exempelkod och visas som det är.

- Texts som är innanför enkla citationstecken (med mellanslag till vänster om det första citationstecknet och mellanslag eller interpunkteringstecken till höger om det avslutande citationstecknet) behandlas som exempelkod.

- Text som står mellan två \'\*\'-tecken (med mellanslag före det första \'\*\' och mellanslag eller interpunkteringstecken efter den andra \'\*\') blir betonad.

- Text som står mellan två \'\*\*\'-tecken (med mellanslag före det första \'\*\*\' och mellanslag eller interpunktionstecken efter den andra \'\*\*\') visas förstärkt.

- Text som står mellan två \'\_\'-tecken (med mellanslag före det första \'\_\' och mellanslag eller interpunktionstecken efter den andra \'\_\') visas understruken.

- Text som står mellan dubbla citationstecken följt av ett kolon, eller en `URL`{.backtick}eller som avslutas med interpunktionstecken följt av mellanslag, behandlas som en hyperlänk. Till exempel:

  - \"Zope\":[http://www.zope.org/](http://www.zope.org/) är \...

  Tolkas som \'\<a href=\"[http://www.zope.org/\"\>Zope\</a\>](http://www.zope.org/%22%3EZope%3C/a%3E) är \....\'

  **Observera:** Detta fungerar för relativa såväl som för absoluta `URL`{.backtick}:er.

- Text som står mellan dubbla citationstecken följt av ett comma, en eller flera blanktecken, en absolut URL och avslutas med interpunktionstecken och ett mellanslag, eller bara mellanslag, ses som en hyperlänk. Exempel:

  - \"maila mig\", [mailto:amos@digicool.com](mailto:amos@digicool.com).

  Ses som \'\<a href=\"[mailto:amos@digicool.com\"\>maila](mailto:amos@digicool.com%22%3Emaila) mig\</a\>.\'

- Text som står mellan hakparentser och som består av endast bokstäver, siffror, understryckningstecken och bindestreck ses som en hyperlänk i dokumentet. Exempel:

  - Som demonstrerats av Smith \[12\] är den här tekniken ganska effektiv.

  Ses som \'\... av Smith \<a href=\"#12\"\>\[12\]\</a\> är \...\'. Tillsammans med nästa regel gör det enkelt att göra referenser och slutreferenser.

- Text som står innanför hakparenteser och som står först på raden och följs av två punter och ett mellanrum behandlas som en namngiven länk. Exempel:

  - . \[12\] \"Effective Techniques\" Smith, Joe \...

  Behandlas som \'\<a name=\"12\"\>\[12\]\</a\> \"Effective Techniques\" \...\'. Tillsammans med föregående regerl gör detta det enkelt att skriva referenser och slutreferenser

- Ett stycke som har block av text mellan \'\|\|\' behanlas som en tabel. Textblocken som korresponderar till tabelellens celler och rader är avdelade med radslut. Om inte annat anges så är texten i cellerna centrerad. En cell kan gå över mer än en kolumn genom att sätta det ekvivalenta antalet med cellseparatorer \'\|\|\' före. Radmatningar och \'­\|\' kan inte vara del av celltexten. Exempel:

  - |||| **Ingredienser** ||
        || *Namn* || *Antal* ||
        ||Morötter||10||
        ||Ägg||3||

  visas som följer:

  - ::: {}
    +:----------:+:----------:+
    | \*\*Ingredienser\*\*    |
    +------------+------------+
    | \*Namn\*   | \*Antal\*  |
    +------------+------------+
    | Morötter   | 10         |
    +------------+------------+
    | Ägg        | 3          |
    +------------+------------+
    :::
