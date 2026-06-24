# Genesis-Blindtest für `genesis-scope` durchgeführt: technisch lauffähig, semantisch leer

**Status:** idea · **Epistemic Status:** measured · **Autor:** Claude

## Problem

`PRINCIPLES.md` Regel 7 verlangt, dass Core ohne LLM funktioniert.
`genesis-scope` ist aber explizit für Mensch-KI-Semantiknavigation gebaut.
Es war unklar, ob es Core oder Plugin (Hilfsprogramm) ist — und ob der
Genesis-Blindtest (Regel 6) überhaupt durchführbar ist, ohne dass eine KI
Vorwissen über GenesisAeon mitbringt.

## Vorschlag und Durchführung

2026-06-24: Blindtest erstmals real durchgeführt, per zwei frischen
Subagenten (eigene Claude-Sonnet-4.6-Instanzen ohne jeden
Konversationskontext, nur das jeweilige README-Quickstart als Eingabe,
kein Web-Zugriff auf GenesisAeon-Hintergrund).

- **Testfall 1**: `genesis-scope` allein (`pip install` + `scope.run_cycle`
  Quickstart aus dem echten PyPI-README).
- **Testfall 2**: `genesis-os` allein (`pip install` + GenesisOS-Quickstart,
  aber mit einer von Claude selbst verkürzten/paraphrasierten
  Terminologietabelle statt dem vollständigen Original-README —
  methodischer Schwachpunkt, siehe unten).

### Ergebnis Testfall 1: genesis-scope

- **Install**: `pip install genesis-scope` erfolgreich, Version 1.0.0,
  keine Build-Probleme.
- **Ausführung**: Quickstart-Snippet lief fehlerfrei:
  `coherence_score=0.496`, `drift_status='anchored'`,
  `utac_state={sigma: 0.158, q4_state: 12, q4_label: '1100'}`. CLI
  `scope status` ebenfalls fehlerfrei.
- **Bewertung**: Technisch ja, semantisch nein: Werte sind in sich
  konsistent, aber ohne jede Erklärung, was "gut"/"erwartet" bedeutet,
  was `n_sessions=38` modelliert, oder warum `drift_status` "anchored"
  und nicht "drifting" ist. Blindtest (Regel 6) damit **FALSE**.

### Ergebnis Testfall 2: genesis-os

- **Install**: `pip install genesis-os` erfolgreich, zog überraschend
  schweren Dependency-Stack (numpy/scipy/pandas/sklearn/statsmodels/
  networkx/pydantic) für ein als "Core" beworbenes Minimalpaket.
- **Ausführung**: Quickstart lief fehlerfrei: `Phase='Initiation'`,
  `Entropy=0.9986` (Eingabe war `entropy=0.4` — ein 2.5x-Sprung ohne
  jede Erklärung im Test-Material).
- **Bewertung**: Auch mit Terminologietabelle (CREP/Gamma/UTAC/Phi/
  Tension) blieb unklar, was die Output-Werte für einen Nutzer
  bedeuten — die Tabelle erklärt Formeln, nicht Interpretation.
  Blindtest ebenfalls **FALSE**, aber: das Original-README (von Johann
  im Chat nachgereicht, vollständiger als das paraphrasierte
  Testmaterial) enthält zusätzlich Architektur-Übersicht,
  Lagrangian-Formalismus und Zenodo-Zitation — dieser reichere Kontext
  wurde im Subagenten-Test **nicht** geprüft, da das Testmaterial vor
  dem Erhalt des vollständigen READMEs erstellt wurde.

## Kernbefund: Präzisierung durch Johann

Johann (Chat, 2026-06-24): `genesis-scope` wurde bisher nie tatsächlich
benutzt, und es fehlen die Referenzen (z.B. reale Sessions,
Sigillin-Anker, Concept-Map-Inhalte), die später von KI-Agenten selbst
eingespeist/integriert werden sollen. Das reframt den Befund: die
fehlende Interpretierbarkeit von `coherence_score`/`drift_status` ist
**nicht** primär ein Doku-Problem, sondern ein struktureller Zustand —
das Paket ist ein Skelett, dessen Quickstart-Ausgabe auf
Default-/Leerzustand läuft, nicht auf echten semantischen Inhalten. Ein
Blindtest gegen ein noch nie befülltes System kann strukturell kein
"sinnvolles Ergebnis" liefern, unabhängig von Doku-Qualität.

## Erwartetes Ergebnis

- `genesis-scope` besteht den Genesis-Blindtest (Regel 6) in der
  jetzigen, unbefüllten Form **nicht** — unabhängig von `kategorie`
  programm/hilfsprogramm.
- Die eigentliche Kernfrage hat sich verschoben: nicht "ist die Doku
  gut genug", sondern "kann ein Paket, das per Design erst durch
  spätere KI-Integration (Referenzen/Anker/Map-Inhalte) sinnvoll wird,
  überhaupt einen klassischen Blindtest bestehen, bevor diese
  Integration stattgefunden hat?" — das ist eine offene
  Architekturfrage für Regel 6 selbst bei KI-nativen Paketen.

## Nächster Schritt

Diese Präzisierung als eigene Folgefrage in `01_Ideen/` aufnehmen
(Blindtest-Definition für Pakete, die erst durch KI-Nutzung befüllt
werden). `genesis-os`-Quickstart bei Gelegenheit mit dem vollständigen
Original-README (nicht der paraphrasierten Kurzfassung) erneut blind
testen, um den methodischen Schwachpunkt dieses Laufs zu schließen.

## Betrachtete Alternativen

- Sofort als `hilfsprogramm` einordnen — verworfen, weil das eine
  vorschnelle Entscheidung ohne Test wäre (verstößt gegen Regel 8)
- Sofort als `programm`/Core einordnen — verworfen, weil das Regel 7
  ohne weitere Prüfung verletzen würde
- Befund als reines Doku-Problem buchen und "README verbessern" als
  nächsten Schritt eintragen — verworfen nach Johanns Präzisierung: das
  würde die eigentliche Ursache (fehlende Referenzdaten/
  Nie-Benutzt-Zustand) verdecken.
