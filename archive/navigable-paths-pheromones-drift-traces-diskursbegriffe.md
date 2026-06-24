# Pheromones/Drift/Traces als Entsprechung für "Navigable Paths" (ADR-002) archiviert

**Status:** archived · **Epistemic Status:** hypothesis · **Autor:** Claude
(Statusentscheidung selbst, nicht nur Vorschlag — siehe
`adr/adr-003-ai-as-maintainer.md`)

## Problem

ADR-002s Begriffszuordnungstabelle vermutet "Pheromones, Drift, Traces"
(zusammen mit Cartography) als Entsprechung für den Mission-Begriff
"Navigable Paths". Der Befund in
`01_Ideen/claude/cartography-pheromones-drift-ecosystem-map-befund`
zeigt: Pheromones/Drift/Traces kommen in `ECOSYSTEM_MAP.yaml` (48
Pakete, aus der v1.0.0-Sprint-Roadmap abgeleitet) überhaupt nicht vor.

## Entscheidung

Diese drei Begriffe werden als reine Genesis-/Unified-Mandala-
Diskursterminologie ohne aktuelle Code-Entsprechung eingestuft und nach
`archive/` verschoben (Regel 9, Regel 11). Begründung für diesen Schritt
statt weiterem Liegenlassen als offene Idee:

1. Die Roadmap deckt explizit alle 48 Pakete des Ökosystems ab — eine
   vollständige Abwesenheit in dieser Quelle ist ein stärkeres Signal
   als eine einzelne fehlende Datei.
2. **"Cartography" selbst ist NICHT betroffen** — es hat über die
   `domain`-Beschreibung von `genesis-scope` (P39) eine tatsächliche,
   wenn auch indirekte Entsprechung. Nur Pheromones/Drift/Traces werden
   hier archiviert; Cartography bleibt Teil der offenen
   Semantic-Maps/`genesis-scope`-Linie.

## Erwartetes Ergebnis

- `02_Plaene/adr002-begriffszuordnung-verifikationsplan.md`, Zeile
  "Navigable Paths", kann von "noch zu klären" auf "Cartography
  bestätigt (via genesis-scope), Pheromones/Drift/Traces als
  Diskursbegriffe archiviert" präzisiert werden.
- Diese Entscheidung ist **vollständig revidierbar**: falls später Code
  in einem der 48 Pakete auftaucht, der Pheromones/Drift/Traces
  tatsächlich implementiert, kann der Eintrag per Git-Revert oder neuem
  Trylayer-Eintrag korrigiert werden — `archive/` löscht nichts
  (Regel 11).

## Nächster Schritt

`02_Plaene/adr002-begriffszuordnung-verifikationsplan.md` auf diesen
Archiv-Eintrag verweisen lassen. Falls Johann anderer Einschätzung ist
(z.B. weil ihm aus der Unified-Mandala-Historie eine konkrete
Code-Entsprechung bekannt ist, die in der Roadmap-Zusammenfassung nur
nicht auftaucht): Revert per Git, Korrektur als neuer Trylayer-Eintrag.

## Betrachtete Alternativen

- Status `idea`/`hypothesis` unverändert belassen, bis Code-Zugriff auf
  die 48 Pakete besteht — verworfen unter ADR-003: die vorhandene
  Evidenz reicht für eine begründete, jederzeit revidierbare Einordnung;
  ständiges Offenlassen ohne neue Evidenz in Aussicht wäre kein
  Fortschritt.
- Auch Cartography mitarchivieren — verworfen: Cartography hat einen
  konkreten, wenn auch indirekten Beleg und gehört weiter zur offenen
  Semantic-Maps-Linie.
