# Genesis-Blindtest für unified-mandala (P-MANDALA, Orchestrierungskern): FALSE

## Problem

`unified-mandala` ist laut eigenem README **P-MANDALA** in der GenesisAeon-
Ökosystem-Registry — "the orchestration core (UI, CREP, agents) that wires
the CREP evaluator, SigillinBridge, PolicyGate, and the 17+ adapter registry
together into a single self-reflecting cycle (`MandalaOrchestrator.run_cycle`)".
Regel 6 verlangt: kann eine Person ohne jeden GenesisAeon-Kontext den
Quickstart der README folgen und innerhalb von 5 Minuten ein sinnvolles,
korrektes Ergebnis sehen?

Das README ist ungewöhnlich zweigeteilt: ein per `pip install unified-mandala`
erreichbarer Python/CLI-Strang (direkt vergleichbar mit allen bisher
getesteten Paketen) und ein separater, viel schwererer Node/pnpm/Docker/
NATS/Ollama/OPA-Vollstack-Strang ("TL;DR – 5-Minute Quick Start"). Beide
wurden getrennt geprüft.

## Vorschlag und Durchführung

**Python/CLI-Strang:** Ein frischer, kontextfreier Subagent bekam
ausschliesslich den README-Ausschnitt zu `pip install unified-mandala`, dem
Python Quick Start und den 9 CLI-Befehlen als Eingabe, installierte real,
führte den kompletten Quick-Start-Codeblock und alle 9 CLI-Befehle aus,
rechnete die Landauer-Formel von Hand nach, inspizierte den Code auf die
φ=0.618-Behauptung, und testete Parametersensitivität von `MetaQuestEngine`
und `PlanetaryCouplingChain` über je 3+ Eingabewerte.

**Vollstack-Strang:** Direkt durch eigene Lektüre des vollständigen READMEs
(676 Zeilen) und Gegenprobe im Repo selbst (`package.json`, referenzierte
Scripts) geprüft, ohne den Stack tatsächlich hochzufahren — die
Infrastrukturanforderungen (Docker, NATS-JetStream-Server, zwei per Ollama
zu ziehende LLM-Modelle, OPA-Binary) sprechen strukturell bereits gegen die
eigene "5-Minute"-Behauptung, unabhängig vom Testergebnis.

## Ergebnis

### Python/CLI-Strang

- **Versions-Mismatch, neue Variante:** `pip install unified-mandala`
  installiert **1.0.0** (aktuellste PyPI-Version). Aber
  `unified_mandala.__version__` sowie das CLI-Banner melden **"0.3.2"** —
  exakt die Version, die das README als "current" bewirbt. Der
  interne `__version__`-String hinkt der echten PyPI-Version hinterher
  (nicht der übliche "0.1.0-Scaffold-Default", sondern ein genuiner, seit
  mehreren Releases nicht nachgezogener Wert) — passt in dieselbe
  Fehlerklasse wie `version-string-drift-audit`, mit einer neuen,
  größeren Sprungweite (0.3.2 → 1.0.0, mehrere Minor-/Major-Versionen).
- **Landauer-Formel stimmt exakt:** E = k_B·T·ln(2) bei T=300K von Hand
  nachgerechnet: 2,870979e-21 J. Code-Output: 2,871e-21 J. Übereinstimmung.
- **φ=0.618 ist echt, kein Marketing:** `FRACTAL_SINGULARITY =
  0.618033988749895` ist im Code der tatsächliche Schwellenwert `φ_c` im
  Tainter-Term der Euler-Maruyama-Driftfunktion und steuert einen echten
  `above_singularity`-Zustandsflag. Positiver, seltener Befund in dieser
  Testreihe.
- **MetaQuestEngine reagiert echt auf Eingaben:** vier verschiedene
  (phi, entropy)-Paare wählen erkennbar unterschiedliche Tiers
  (GROUNDING/PROBING/SYNTHESIS/CHALLENGE) mit inhaltlich passendem Text.
  Nebenbefund: wiederholte Aufrufe mit *identischen* Eingaben liefern
  unterschiedlichen Text bei gleichem Tier — bucket-basiert plus
  Zufallskomponente innerhalb des Buckets, weder rein deterministisch
  noch reine Textschablone.
- **PlanetaryCouplingChain teilweise unsensibel:** `crep_phase` ist echt
  kontinuierlich und monoton in `energy_EJ` (0,1695 bei 10 EJ → 0,1737 bei
  620 EJ → 0,2028 bei 5000 EJ). Aber das kategoriale `stress_level` bleibt
  über den gesamten realistischen Bereich (10–5000 EJ, bis zum ~8-Fachen
  des tatsächlichen jährlichen Weltenergieverbrauchs laut IEA) konstant
  auf "stable" — es eskaliert erst bei unrealistischen Werten
  (50.000+ EJ). Die Schwellenwerte im Code sind real (nicht hartkodiert
  auf einen Wert), aber im gesamten plausiblen Eingabebereich praktisch
  wirkungslos — eher eine Doku-/UX-Lücke als ein reiner Bug.
- **CLI: 9/9 CLI-Befehle crashen ausserhalb einer nativen PowerShell-7-
  Konsole.** Mit `PYTHONIOENCODING=utf-8` gesetzt laufen alle 9 Befehle
  fehlerfrei. Ohne diesen Override (z. B. in git-bash/MSYS-Terminals,
  bei Output-Umleitung, oder älteren PowerShell-5.1-Konfigurationen)
  crashen 8 von 9 Befehlen mit `UnicodeEncodeError` — jeweils an einem
  anderen griechischen Buchstaben oder Mathematiksymbol
  (₀, →, ₂, α, φ, π, −). Damit siebter/achter bestätigter Fall des
  ökosystemweiten Unicode-Crash-Musters (siehe
  `windows-unicode-crash-pattern`), diesmal an der CLI-Ebene eines
  deutlich grösseren, produktiveren Pakets. Bemerkenswerte Nuance: das
  Risiko ist konsolen-/terminalabhängig — git-bash (eines der beiden in
  dieser Aufgabenumgebung angebotenen Terminals) crasht real, eine reine
  interaktive PowerShell-7-Sitzung dagegen nicht automatisch.
- Kein Installationsfehler, keine leere/Stub-Installation — echte,
  substanzielle Abhängigkeiten (numpy, scipy, pydantic, rich, typer,
  loguru, networkx).

### Vollstack-Strang ("TL;DR – 5-Minute Quick Start")

- Die im README als "5-Minute Quick Start" bezeichnete Sektion verlangt
  tatsächlich: Node ≥20 + pnpm 10.17.0 via Corepack, `pnpm install` +
  `pnpm build`, Docker (für ein Offline-Bundle oder NATS-JetStream-
  Container), einen laufenden NATS-JetStream-Server, optional ein
  komplettes Prometheus/Grafana-Monitoring-Profil — und weiter unten im
  selben README ein zweites "🚀 Quick Start (All-in-One, Port-Aware)"
  mit Ollama-Installation plus zwei per `ollama pull` zu ziehenden
  LLM-Modellen (`qwen2.5:7b`, `nomic-embed-text`), einem OPA-Binary und
  einer eigenen Policy-Bundle-Pipeline (`opa:bundle`/`opa:sign`/
  `opa:verify`).
- Die referenzierten Scripts/Commands sind real vorhanden (Stichprobe:
  `dev:all`, `nats:doctor`, `test:jetstream`, `opa:cover` existieren
  tatsächlich in `package.json`/`scripts/`) — kein Vaporware, aber der
  Umfang steht in klarem Missverhältnis zur eigenen "5 Minuten"-
  Bezeichnung. Für einen kontextfreien Leser ist allein das Ziehen von
  zwei LLM-Modellen per Ollama und das Hochfahren eines
  NATS-JetStream-Containers realistisch nicht in 5 Minuten zu schaffen,
  unabhängig von Fachkenntnis.
- Diese Einschätzung ist `derived` (aus README- und Repo-Lektüre), nicht
  `measured` (der Stack wurde nicht tatsächlich hochgefahren) — sie
  betrifft die Angemessenheit der Selbstbeschreibung, nicht die
  Funktionsfähigkeit des Stacks selbst.

## Verdikt

**FALSE.** Zwei unabhängige, im Python/CLI-Strang tatsächlich verifizierte
Gründe reichen bereits: (1) `pip show` zeigt 1.0.0, README/CLI-Banner/
`__version__` zeigen 0.3.2, ohne Erklärung; (2) 8 von 9 dokumentierten
CLI-Befehlen crashen in mehreren realistischen Windows-Terminal-
Konfigurationen mit `UnicodeEncodeError`, ohne Hinweis auf das Risiko oder
einen Workaround im README. Der separate Vollstack-Strang untergräbt
zusätzlich strukturell die eigene "5-Minute"-Behauptung durch seinen realen
Umfang.

Gleichzeitig der bislang substanziellste Einzelbefund der ganzen Testreihe:
die Kernformel (Landauer) stimmt exakt, der zentrale φ=0.618-Parameter ist
echt und mathematisch wirksam (kein Marketing), und zwei der vier
API-Objekte (`MetaQuestEngine`, `PlanetaryCouplingChain`) reagieren
nachweislich echt auf variierte Eingaben statt Platzhalter-Konstanten
zurückzugeben.

## Erwartetes Ergebnis

Fünfzehnter FALSE-Befund insgesamt, aber der differenzierteste: mehr echte,
verifizierte mathematische Substanz als in jedem zuvor getesteten
Programm-Kandidaten, bei gleichzeitig zwei klaren, konkreten
Blindtest-Fehlern.

## Nächster Schritt

Fünf Findings zur Weitergabe an Johann: (1) `__version__`/CLI-Banner auf
1.0.0 nachziehen; (2) `PYTHONIOENCODING=utf-8`-Hinweis (oder
`chcp 65001`) explizit ins README aufnehmen, da das Ökosystem-typische
Unicode-Crash-Muster hier auf CLI-Ebene besonders breit auftritt (8 von 9
Befehlen); (3) `stress_level`-Schwellenwerte in `planetary/coupling.py`
für den realistischen Energiebereich (10–5000 EJ) nachschärfen oder die
Kategorie-Grenzen dokumentieren; (4) die "5-Minute Quick Start"-Bezeichnung
präzisieren oder den Vollstack-Pfad als "vollständiges Setup (30+ Minuten)"
umbenennen; (5) den reinen Python/CLI-Pfad (der tatsächlich in 5 Minuten
funktioniert, sobald die Encoding-Falle behoben ist) im README stärker vom
Vollstack-Pfad abgrenzen, da beide aktuell im selben Dokument
ununterschieden nebeneinanderstehen.

## Alternativen betrachtet

**Den Vollstack-Strang ebenfalls tatsächlich hochfahren (Docker, NATS,
Ollama, OPA) statt nur strukturell zu bewerten.** Verworfen für diese
Testrunde: der Aufwand (Modell-Downloads, Container-Orchestrierung)
steht ausser Verhältnis zum Erkenntnisgewinn gegenüber der bereits klaren
strukturellen Diskrepanz zur eigenen "5-Minute"-Behauptung; kann bei
Bedarf als eigener, separater Test nachgeholt werden, falls Johann das
für den nächsten Loop priorisiert.

**Den Gesamt-Befund allein am Vollstack-Umfang festmachen und den
Python/CLI-Strang ignorieren.** Verworfen: der Python/CLI-Strang ist
über `pip install unified-mandala` genauso eigenständig erreichbar wie
bei jedem anderen getesteten Paket und verdient eine eigene, vollständige
Prüfung — die hier auch tatsächlich die überzeugendste positive
Einzelsubstanz der ganzen Testreihe zutage gefördert hat (Landauer-Formel,
echter φ-Parameter).
