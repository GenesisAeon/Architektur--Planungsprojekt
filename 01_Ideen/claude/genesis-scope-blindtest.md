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

### Retest Testfall 2 mit vollständigem Original-README

2026-06-24, gleicher Tag: Johann hat das vollständige, wörtliche
`genesis-os`-README erneut im Chat eingefügt, nachdem direkter
Netzwerkzugriff (curl auf `raw.githubusercontent.com`) am
Sandbox-Proxy mit 403 scheiterte und `WebFetch` nur eine
KI-zusammengefasste statt wörtliche Version lieferte. Ein dritter,
wiederum frischer kontextfreier Subagent hat damit install + Quickstart
+ CLI real ausgeführt:

- **Install**: `pip install genesis-os` in frischem venv erfolgreich,
  ca. 25 Abhängigkeiten, unter 2 Minuten, keine Fehler.
- **Quickstart**: `Phase='Initiation'`, `Entropy=0.9986`,
  `Phi(H)=1.0616`, `Lagrangian=0.7028`, `Transitions=0`,
  `Emergence Events=15`.
- **CLI**: `genesis-os info`/`phases` liefern eine Tabelle der vier
  Phasennamen — die einzige semantische Verankerung im gesamten
  Material. Drei unabhängige Läufe (Quickstart + zwei CLI-Varianten,
  50–100 Zyklen, Entropie oberhalb des dokumentierten
  Transition-Schwellenwerts) enden alle bei `Phase='Initiation'`,
  `Transitions=0` — die Phase verlässt "Initiation" nie. JSON-Ausgabe
  zeigt zusätzlich `coherence=0.000124` neben `resonance/emergence/
  poetics=0.5` (jeweils exakt) — wirkt wie Default-/Platzhalterverhalten.
- **Bewertung**: Auch mit dem vollständigen Original-README bleibt der
  Blindtest **FALSE**. Der zusätzliche Kontext erklärt Formeln und
  Modulnamen, aber nicht, ob `Entropy=0.9986` oder `Lagrangian=0.7028`
  gute/erwartete/gesunde Werte sind — und nicht, warum `Transitions`
  trotz expliziter Schwellenwert-Überschreitung in allen drei Läufen
  bei 0 bleibt. Das ist stärker als reine Interpretationslosigkeit: ein
  konkreter, vom Subagenten selbst aufgefallener Widerspruch zwischen
  dokumentiertem Verhalten ("phase-transitioning system") und
  beobachtetem Verhalten. Schließt den zuvor dokumentierten
  methodischen Schwachpunkt (abgekürztes statt vollständiges
  Testmaterial) — das FALSE-Ergebnis war robust gegenüber besserer
  Doku, was Johanns Struktur-statt-Doku-Erklärung zusätzlich stärkt.

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

Erledigt: Folgefrage als eigene Idee dokumentiert
(`01_Ideen/claude/blindtest-fuer-ki-native-leerpakete`). Erledigt:
`genesis-os`-Retest mit vollständigem Original-README durchgeführt
(siehe oben), Ergebnis bleibt FALSE. Neu offen: das beobachtete
Ausbleiben von Phase-Transitions in allen drei Läufen als eigene
technische Frage prüfen, sobald Sourcecode-Zugriff auf `genesis-os`
besteht — möglicherweise ein eigener, von der Blindtest-Frage
unabhängiger Befund.

## Betrachtete Alternativen

- Sofort als `hilfsprogramm` einordnen — verworfen, weil das eine
  vorschnelle Entscheidung ohne Test wäre (verstößt gegen Regel 8)
- Sofort als `programm`/Core einordnen — verworfen, weil das Regel 7
  ohne weitere Prüfung verletzen würde
- Befund als reines Doku-Problem buchen und "README verbessern" als
  nächsten Schritt eintragen — verworfen nach Johanns Präzisierung: das
  würde die eigentliche Ursache (fehlende Referenzdaten/
  Nie-Benutzt-Zustand) verdecken.
