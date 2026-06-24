# Cartography/Pheromones/Drift/Traces nicht als eigene Pakete in `ECOSYSTEM_MAP.yaml` auffindbar

**Status:** idea · **Epistemic Status:** derived · **Autor:** Claude

## Problem

`02_Plaene/adr002-begriffszuordnung-verifikationsplan.md` fordert als
ersten konkreten Schritt, die Begriffe *Cartography*, *Pheromones*,
*Drift* und *Traces* (Mission-Begriff "Navigable Paths" aus ADR-002) in
`ECOSYSTEM_MAP.yaml` zu suchen, um zu klären, ob es sich um eigene
Pakete, Teilmodule bestehender Pakete oder reine Genesis-Diskurs-
Terminologie handelt.

## Vorschlag

Durchsuchung von `ECOSYSTEM_MAP.yaml` (48 Pakete) durchgeführt:

```
grep -in -E "cartograph|pheromon|drift|trace" ECOSYSTEM_MAP.yaml
```

**Befund:** *Pheromones*, *Drift* und *Traces* kommen in der gesamten
Datei überhaupt nicht vor — kein `package_id`, kein `domain`-Text, kein
`hinweis`-Feld erwähnt sie. *Cartography* taucht genau einmal auf, nicht
als eigenes Paket, sondern als Teil der `domain`-Beschreibung von
`genesis-scope` (P39): *"semantic cartography / human-AI navigation
layer"*. Das deckt sich mit dem bereits identifizierten Zusammenhang zu
"Semantic Maps" (`genesis-scope-blindtest`), ist aber kein
eigenständiger Beleg für "Navigable Paths" als Cartography/Pheromones/
Drift/Traces.

## Erwartetes Ergebnis

- Klarheit, dass die Recherche in `ECOSYSTEM_MAP.yaml` allein die vier
  Begriffe nicht eigenständig verifizieren kann — Cartography ist nur
  indirekt (als Teil von genesis-scope) belegt, die anderen drei gar
  nicht.
- Explizite Entscheidungsgrundlage für den Maintainer: entweder
  (a) Pheromones/Drift/Traces sind unklassifizierte Konzepte aus dem
  ursprünglichen Genesis-Diskurs ohne aktuelle Code-Entsprechung in den
  48 Paketen und sollten gemäß Regel 9 nach `archive/` verschoben
  werden, oder (b) sie sind Teilmodule innerhalb eines bestehenden
  Pakets, das aus der Roadmap-Domänenbeschreibung allein nicht erkennbar
  ist und direkten Code-Zugriff zur Klärung braucht.

## Nächster Schritt

Maintainer (Johann) entscheidet anhand der Quellgenese
(Unified-Mandala-Diskurs), ob Pheromones/Drift/Traces echte, noch
unklassifizierte Code-Konzepte sind oder reine Diskurs-Metaphern. Falls
Letzteres: eigener `archive/`-Eintrag mit Begründung gemäß Regel 9/11.
Falls Ersteres: welches Paket sie enthält, damit `ECOSYSTEM_MAP.yaml`
entsprechend ergänzt werden kann.

## Betrachtete Alternativen

- Die Begriffe stillschweigend als durch "semantic cartography"
  (genesis-scope) abgedeckt betrachten und die Zeile im
  Verifikationsplan als erledigt markieren — verworfen, das wäre eine
  unbelegte Verallgemeinerung (Regel 5).
- Ohne weitere Prüfung direkt nach `archive/` verschieben — verworfen,
  das ist eine inhaltliche Einordnungsentscheidung (Regel 9), die dem
  Maintainer vorbehalten ist.
