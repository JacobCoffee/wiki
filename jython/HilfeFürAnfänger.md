# HilfeFürAnfänger

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## WikiWikiWeb 

Ein [WikiWikiWeb](WikiWikiWeb) ist eine Hypertext-Umgebung für gemeinschaftliches Zusammenarbeiten, mit Betonung auf einfachen Zugriff auf und einfaches Ändern von Informationen.

Durch einen Klick auf den Verweis \"Edit\" können Sie jede Seite selbst verändern. Je nach Gestaltung der Benutzeroberfläche (engl. *theme*) finden sie diesen Verweis oben, links oder auch am unteren Ende der Seite. Aneinander gefügte, vorne groß geschriebene Worte bilden einen sog. [WikiName](WikiName)n, der automatisch einen Verweis auf eine andere Seite bildet. Ein Klick auf den Seitentitel sucht alle Seiten, die auf die aktuelle Seite verweisen, also deren [WikiName](WikiName)n enthalten. Seiten, die noch nicht existieren, werden mit einem Fragezeichen abgebildet (oder auch in einer anderen Form dargestellt, üblicherweise fett und rot). Folgen Sie einfach einem solchen Verweis und Sie können eine Definition hinzufügen, also die Seite anlegen. Das ist auch ein Weg, um neue Seiten anzulegen: fügen Sie einen neuen [WikiName](WikiName)n auf eine existierende Seite hinzu, speichern Sie Ihre Änderung, klicken Sie auf Ihren neuen Verweis und erzeugen Sie die Seite (mehr Details siehe [HilfeZurSeitenErzeugung](HilfeZurSeitenErzeugung)).

Sie können den [WikiSandkasten](WikiSandkasten) gerne ändern, wie es Ihnen beliebt. Halten Sie sich aber bitte mit Änderungen anderer Seiten etwas zurück, bis Sie sich mit der Funktionsweise eines Wikis vertraut gemacht haben.

Um mehr darüber zu erfahren, was ein [WikiWikiWeb](http://c2.com/cgi/wiki?WikiWikiWeb "Wiki") ist, lesen Sie [WhyWikiWorks](http://c2.com/cgi/wiki?WhyWikiWorks "Wiki") und [WikiNature](http://c2.com/cgi/wiki?WikiNature "Wiki") (englisch). Des weiteren lesen Sie bitte auch [WikiWikiWebFaq](http://c2.com/cgi/wiki?WikiWikiWebFaq "Wiki") und [WikiInEinerMinute](http://c2.com/cgi/wiki?WikiInEinerMinute "Wiki"). Dieses Wiki ist auch ein Teil des [InterWiki](InterWiki)-Verbunds, was bedeutet, dass Sie leicht auf eine Vielzahl von Informationen verweisen können, die auf anderen öffentlichen Wikis verfügbar sind.

Gute Ausgangspunkte für eine Wiki-Erkundung sind:

- [AktuelleÄnderungen](./Aktuelle(c384)nderungen.html): damit sehen Sie, was in letzter Zeit geändert wurde

- [SeiteFinden](SeiteFinden): durchsuchen Sie die Datenbank auf verschiedene Weisen

- [TitelIndex](TitelIndex): eine Liste aller Seiten im Wiki

- [WortIndex](WortIndex): eine Liste aller Worte, die Teil eines Seitentitels sind (und daher eine Liste aller Konzepte im Wiki)

- [WegWeiser](./WegWeiser.html): eine Seite, die zu den unterschiedlichen Indizes des Wikis führt

- [WikiSandkasten](WikiSandkasten): diese Seite dürfen Sie nach Herzenslust für eigene Änderungen und Experimente benutzen

Für weitere Hilfe siehe die Seiten [HilfeInhalt](HilfeInhalt) und [HilfeIndex](HilfeIndex).

## WikiNamen 

Ein [WikiName](WikiName) ist ein Wort, zusammengesetzt aus vorne groß geschriebenen Worten.

[WikiName](WikiName)n werden automatisch zu Verweisen (Hyperlinks) auf die Seite, die so heißt, wie der [WikiName](WikiName). Was genau als Groß- bzw. Kleinbuchstabe betrachtet wird, wird durch die Konfiguration festgelegt - die Standard-Konfiguration funktioniert für utf-8-Zeichen.

Wenn Sie auf den Seitentitel (z.B. HilfeFürAnfänger auf dieser Seite) klicken, wird Ihnen eine Liste aller Seiten angezeigt, die auf die aktuelle Seite verweisen - und das funktioniert sogar auf noch nicht definierten Seiten.

Ein Fragezeichen vor einem Link (oder auch ein Link, der fett und rot abgebildet ist) bedeutet, dass eine Seite noch nicht definiert wurde. Sie können dann auf das Fragezeichen klicken und die Seite anlegen (z.B.: [SoEineSeiteGibtEsNicht](./SoEineSeiteGibtEsNicht.html)). Wenn Sie auf einen solchen Link klicken, bekommen Sie eine Standardseite, die Sie dann editieren können. Erst beim Speichern dieser Seite wird die Seite dann wirklich angelegt. Eine Liste von noch nicht erzeugten Seiten, auf die aber von anderen Seiten verwiesen wird, befindet sich auf [GesuchteSeiten](GesuchteSeiten).

Um einen [WikiName](WikiName)n nicht als solchen gelten zu lassen (ihn zu \"escapen\"), z.B. wenn man WikiName schreiben will, ohne einen Link zu generieren, kann man eine leere Fettschrift-Markierung verwenden (also eine Folge von sechs einfachen Anführungszeichen) wie hier: `Wiki''''''Name`. Alternativ können Sie die kürzere Sequenz \"``` `` ```\" (zwei inverse Hochkommata, engl. *backticks*) verwenden, d.h. ``` Wiki``Name ```, oder, je nach Konfiguration, auch ein vorangestelltes Ausrufungszeichen, z.B. `!WikiName`.

Lesen Sie [HilfeZumEditieren](HilfeZumEditieren), um weiteres über Wiki-Notation zu lernen.

## Siehe auch 

- [WikiKurs](WikiKurs): Eine strukturierte Einführung in Wikis
