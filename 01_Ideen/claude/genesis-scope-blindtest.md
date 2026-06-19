# Genesis-Blindtest für `genesis-scope` durchführen

**Status:** idea · **Epistemic Status:** hypothesis · **Autor:** Claude

## Problem

`PRINCIPLES.md` Regel 7 verlangt, dass Core ohne LLM funktioniert.
`genesis-scope` ist aber explizit für Mensch-KI-Semantiknavigation gebaut —
es lebt von der Interaktion mit einem LLM. Das ist ein direkter
Widerspruch, wenn man `genesis-scope` naiv in den Core einsortieren würde.

## Vorschlag

Bevor die übrigen 47 Pakete des Ökosystems durch die Inventarisierung
laufen, sollte `genesis-scope` selbst als erster Testfall durch den
Genesis-Blindtest (Regel 6) geschickt werden. Wenn die Verfassung beim
eigenen wichtigsten Werkzeug zu einem unklaren Ergebnis führt, ist die
Verfassung noch nicht fertig — das wäre besser jetzt zu wissen als nach
30 sortierten Modulen.

## Erwartetes Ergebnis

- Klarheit, ob `genesis-scope` `kategorie: programm` (Core) oder
  `kategorie: hilfsprogramm` (Plugin) sein sollte
- Falls unklar bleibt: Regel 7 muss präzisiert werden, bevor die
  eigentliche Inventarisierung beginnt

## Nächster Schritt

Der Maintainer führt den Blindtest manuell durch und trägt das Ergebnis
in `blindtest_passed` ein. Bei anhaltender Unklarheit: Eskalation als
eigenes ADR in `adr/`.

## Betrachtete Alternativen

- Sofort als `hilfsprogramm` einordnen — verworfen, weil das eine
  vorschnelle Entscheidung ohne Test wäre (verstößt gegen Regel 8)
- Sofort als `programm`/Core einordnen — verworfen, weil das Regel 7
  ohne weitere Prüfung verletzen würde
