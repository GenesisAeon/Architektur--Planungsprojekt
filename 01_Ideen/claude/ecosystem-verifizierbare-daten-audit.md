# Ökosystemweiter Befund: was tatsächlich verifizierbare Daten erzeugt

## Problem

Johann fragte nach einer ausführlichen, ökosystemweiten Einschätzung:
was aus den 48 GenesisAeon-Paketen erzeugt tatsächlich verifizierbare
Daten und hat echten Nutzen — als Grundlage dafür, was als Nächstes
gebaut werden sollte. Dieses Repo hat dafür bereits die richtige
Methodik (Genesis-Blindtest, Regel 6) und vier reale Befunde
(`entropy-table`, `implosive-genesis`, `genesis-scope`, `genesis-os`).
Dieser Eintrag führt diese Befunde mit unabhängigen, in derselben
Sitzung durchgeführten Untersuchungen in `Feldtheorie`, `unified-mandala`
und `genesis-tip`/`scope-resilience` zusammen — nicht als neue
Blindtests, sondern als Synthese bereits gemessener Ergebnisse.

## Zusammenführung der Befunde

### Was dieses Repo bereits weiß (Regel 6, real durchgeführt)

| Paket | Ergebnis | Kernbefund |
|---|---|---|
| `entropy-table` | FALSE → TRUE (nach Fix) | Erst technisch defekt (fehlende Dependency, falsche PyPI-Version, hartkodierte Pfade), nach v2.0.1 echt lauffähig mit 31 realen Atlas-Datendateien |
| `implosive-genesis` | TRUE | Sofort lauffähig, echter wissenschaftlicher Output (V_RIG, OIPK, Tesseract), nur 2 kleine Doku-/CLI-Bugs |
| `genesis-scope` | FALSE | Technisch fehlerfrei, aber strukturell leer — nie mit echten Sigillin-Ankern/Sessions befüllt |
| `genesis-os` | FALSE | Läuft technisch, aber `Transitions=0` in drei unabhängigen Läufen trotz Entropie oberhalb der dokumentierten Schwelle — Widerspruch zum eigenen Anspruch als "phase-transitioning system" |

### Was diese Sitzung unabhängig dazu beigetragen hat

**`Feldtheorie` (DE, T0)** — vermutlich das dichteste real-verifizierte
Datenreservoir im gesamten Ökosystem. `analysis/results/` enthält 138
echte Fit-Ergebnisse mit eigenem Trilayer-Index. Stichprobe: die
Behauptung β=3.47±0.47 für Wei's PaLM-Skalierungsdaten wurde gegen die
echte `llm_beta_extractor.json` geprüft — exakt bestätigt
(`beta_mean: 3.4695`, `beta_std: 0.4655`), inklusive ΔAIC gegen ein
Power-Law-Nullmodell und der ehrlichen Selbstauskunft
`"within_canonical_band": false"`. Literaturbelegte Realdaten (NGRIP
Ice Core, Gajer et al. 2012 Science, ENROLL-HD, Human Microbiome
Project, Patel et al. 2015 Cell) bestätigt. Direkt relevant für
`02_Plaene/genesis-core-scope.md`, Schritt 2 (offene Duplikat-Frage
`fieldtheory` T4/EN vs. `Feldtheorie` T0/DE): falls beide tatsächlich
Duplikate sind, ist die deutsche Version aufgrund dieser Tiefe die
naheliegende Kandidatin zum Behalten — das braucht aber einen echten
Code-Diff, keine Namens-Vermutung (siehe eigener, offener Task).

**`genesis-tip` (P50) + `scope-resilience` (P41) + `resilience-core`** —
ein echtes, vorregistriertes Falsifikations-Framework mit
CREPGate-Disziplin, im Geist genau das, was dieses Repo mit Regel 5/6
verlangt. Drei unabhängige Versuche in dieser Sitzung (synthetischer
Dummy-Agent, Replay echter historischer Antworten, echte Live-Antworten
eines Qwen-Modells) fanden alle denselben konstanten `tip_score=1.0` —
zurückgeführt auf `metrics/consistency_scorer.py`s enge Regex-Muster,
die auf natürlichem Text praktisch nie feuern (im Paket-eigenen
Docstring bereits als Zukunftsarbeit vermerkt: "a full semantic
comparison would require an LLM-judge"). Ein optionaler LLM-Judge wurde
nachgerüstet und funktioniert nachweislich (isolierter Sanity-Check
sowie 8 von 24 echten Testpaaren erfolgreich beurteilt), aber ein
kostenloses Grok-Kontingent hat den vollständigen n≥30-Test bisher
verhindert.

**`unified-mandala`** — gemischtes Bild: ein echtes, verifiziertes
Codexwork-Automatisierungssystem (mehrstufige ToDo-/Fraktal-Pipeline,
65 reale "Fraktal"-Durchläufe, stichprobenartig gegen echte Dateien
bestätigt), aber viele "Simulation"-Pakete sind selbst-deklarierte
Platzhalter (`governance_simulator`/`singularity_simulator` sagen
wörtlich "placeholder" im eigenen Docstring). Ein kleinerer, aber
echter Kern (`nullfield_wave.py`, ein realer 1D-Wellengleichungslöser,
nachweislich lokal ausgeführt via kompiliertem `.pyc`; `universe-sim`,
ein echter, laufender Go-Microservice, selbst als Prototyp deklariert)
liegt dazwischen.

## Drei ökosystemweite Muster

1. **Der wiederkehrende Engpass ist fehlende echte Nutzungsdaten, nicht
   Codequalität.** `genesis-scope` (kein Sigillin-Store befüllt) und
   `genesis-tip` (keine echte Session-Korpus, jetzt teilweise
   geschlossen) haben strukturell dasselbe Problem: der Mechanismus
   funktioniert, wurde aber nie mit echtem Material gefüttert. Das
   spricht dafür, echte Daten einzuspeisen zu priorisieren, bevor neue
   Mechanismen entstehen.

2. **Die Γ→Ρ-Kritikalitätsdecke aus `scope-resilience` ist vermutlich
   kein Einzelfall.** `ECOSYSTEM_MAP.yaml` listet echte γ-Werte für über
   ein Dutzend Pakete (`amazon-utac` γ=0.116, `amoc-utac` γ=0.251,
   `sandpile-utac` γ=0.296/0.376 u.a.), und `beta-clustering-utac`/
   `phi-scaling-validator` betreiben explizit
   "cross-domain meta-analysis" darüber. Falls die zugrundeliegende
   Formel dieselbe nicht-monotone Form hat (Ρ steigt bis zu einem
   Peak-Γ und fällt danach, mit einer harten Decke bei Γ_max), könnte
   eine naive Cross-Domain-Aggregation an derselben Stelle scheitern
   wie der heutige Proxy-Test in `genesis-tip`. Noch nicht geprüft —
   eigener Task.

3. **Versions-Diskrepanz zwischen README und PyPI ist bei zwei von zwei
   bisher getesteten Core-Kandidaten aufgetreten** (`entropy-table`:
   README v1.0.0, installiert v2.0.0; `implosive-genesis`: README
   "v0.4.0 current", installiert v1.0.0). Das deutet auf ein
   systematisches Release-Hygiene-Problem aus dem v1.0.0-Sprint hin,
   nicht auf Einzelfälle.

## Erwartetes Ergebnis

Eine gemeinsame, repo-übergreifende Sicht auf "was ist real", die die
bisherigen Einzelbefunde dieses Repos ergänzt, ohne sie zu ersetzen —
plus drei konkrete, prüfbare Folgefragen (Duplikat-Check, Γ→Ρ-Audit,
Versions-Audit), die aus den Mustern oben direkt ableitbar sind.

## Nächster Schritt

Wird als eigene Roadmap sequenziell abgearbeitet (siehe Task-Liste der
laufenden Sitzung): Blindtest-Kette mit `entropy-governance`
fortsetzen; `fieldtheory`/`Feldtheorie`-Duplikat per Code-Diff klären;
Γ→Ρ-Kritikalitätscheck für `beta-clustering-utac`/
`phi-scaling-validator`; `genesis-tip`-Judge-Test abschließen, sobald
das Grok-Kontingent zurückgesetzt ist; README-vs-PyPI-Versionsaudit
über alle 48 Pakete.

## Alternativen betrachtet

**Nur den bisherigen vier Blindtest-Befunden folgen, ohne externe
Session-Funde einzubeziehen.** Verworfen: die Feldtheorie- und
genesis-tip-Funde sind unabhängig gewonnen und direkt relevant für
offene Fragen dieses Repos (Duplikat-Frage, Core-Kandidaten-Reife) —
sie wegzulassen würde bereits vorhandenes Wissen ignorieren.

**Sofort alle drei Folgefragen selbst beantworten, statt sie als
offene Aufgaben zu dokumentieren.** Verworfen für diesen Eintrag: jede
der drei Fragen braucht eigene Untersuchung mit eigenem Belegstand:
richtig als eigene, separate Einträge zu behandeln, nicht als
Seitenbemerkung hier.
