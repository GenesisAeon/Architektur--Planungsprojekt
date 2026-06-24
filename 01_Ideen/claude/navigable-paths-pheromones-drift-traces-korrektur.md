# Korrektur: Cartography/Drift/Traces durch genesis-scope-README bestätigt; Pheromones offene Designidee statt Diskursbegriff

**Status:** idea · **Epistemic Status:** derived · **Autor:** Claude
(Korrektur einer eigenen Statusentscheidung — siehe
`adr/adr-003-ai-as-maintainer.md`)

## Problem

Der vorherige Eintrag (vormals `status: archived` in `archive/`, jetzt
hierher verschoben und korrigiert) stufte Pheromones/Drift/Traces als
reine Genesis-Diskursterminologie ein, weil sie in `ECOSYSTEM_MAP.yaml`
(nur Roadmap-Domänenbeschreibungen, kein Code-Einblick) nicht auffindbar
waren. Johann hat im Chat (2026-06-24) das echte `genesis-scope`-README
(github.com/GenesisAeon/genesis-scope, Package P39) eingebracht. Daraus
ergibt sich: die Archivierung war voreilig, gestützt auf eine zu
schwache Quelle (Roadmap-Zusammenfassung statt tatsächliche
Paket-Dokumentation).

## Korrektur

Eintrag von `archive/` zurück nach `01_Ideen/` verschoben, Begriffe neu
bewertet anhand des tatsächlichen READMEs:

- **Cartography**: bestätigt — eigenes Modul `cartography.py`
  (`DEFAULT_MAP`, typed nodes/edges, `compare_maps`,
  `compare_perspectives`, `attractors`).
- **Drift**: bestätigt — eigenes Modul `drift_model.py` mit expliziter
  Formel `dD/dt = -kappa * (D - D*)`, CLI-Kommando `scope drift`, sowie
  Drift-Erkennung zwischen Map-Snapshots (`compare_maps`).
- **Traces**: bestätigt — CLI-Kommando `scope trace <start> <end>` und
  `DEFAULT_MAP.trace("crep", "agent_coordination")` als expliziter Pfad
  durch den Concept Space.
- **Pheromones**: **nicht** im README als eigener Begriff/Code gefunden.
  Johanns Präzisierung im Chat: gemeint ist eine geplante Technik
  (Analogie zu Ameisen-Pheromonen), um Wege durch latente semantische
  Räume zu markieren und zu bewerten — bisher nur Bestandteil der
  Monorepo-/Scope-*Planung*, noch kein bestätigter Code. Nächstliegender,
  aber nicht identischer bestehender Mechanismus: "semantic anchors
  (Sigillin)" (`semantic_anchor.py`), die Drift zwischen Sessions
  reduzieren — das ist Anti-Drift-Verankerung, nicht Pfad-Markierung
  durch wiederholte Traversierung. Pheromones bleibt daher eine eigene,
  noch unimplementierte Designidee, keine reine Diskursmetapher und auch
  keine bereits bestehende Funktion.

## Erwartetes Ergebnis

- `ADR-002`-Begriffszuordnungstabelle, Zeile "Navigable Paths":
  Cartography/Drift/Traces gelten als durch das `genesis-scope`-README
  bestätigt (`epistemic_status: derived`, README-Ebene, kein direkter
  Quellcode-Zugriff/Tests durch dieses Repo selbst durchgeführt).
- Pheromones bleibt offene Idee für das spätere Genesis-Core-Monorepo
  bzw. für `genesis-scope` selbst: ein expliziter
  Pfad-Bewertungsmechanismus (z.B. Gewichtung von Edges nach
  Traversierungshäufigkeit, analog zu Ameisenpheromon-Verstärkung), der
  sich von den bestehenden Sigillin-Ankern unterscheidet.

## Nächster Schritt

`02_Plaene/adr002-begriffszuordnung-verifikationsplan.md` erneut
korrigieren: Cartography/Drift/Traces als README-bestätigt vermerken,
Pheromones als offene Idee für `genesis-scope` referenzieren statt
archiviert.

## Betrachtete Alternativen

- Nur den Fehler in einer neuen Idee dokumentieren, archivierten Eintrag
  unverändert in `archive/` stehen lassen — verworfen: Regel 2 verlangt,
  dass der Ordner zum Status passt; ein nicht mehr archivierter Begriff
  darf nicht in `archive/` verbleiben.
- Den ursprünglichen Eintrag komplett löschen statt verschieben/
  korrigieren — verworfen: widerspricht Regel 11 (Verwerfen ist kein
  Löschen) im Geiste — die Korrektur soll im Diff sichtbar bleiben, nicht
  spurlos verschwinden.
