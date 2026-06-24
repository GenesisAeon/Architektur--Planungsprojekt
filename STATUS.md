# Ist-Stand

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) ist der verbindliche
> Einstiegspunkt (Regel 12). Dieses Dokument ist Schritt 2 davon — lies
> danach `PRINCIPLES.md` und `AGENTS.md`.

Letztes Update: 2026-06-24 (ChatGPT-Deep-Research zu Orientierung/Recovery
Time sowie ENSO/Eisschild-Climate-Thresholds-Analogie verarbeitet)

## Phase

**Planung / Architektur-Diskurs** — parallel zum laufenden v1.0.0-Release-
Sprint der 48 GenesisAeon-Pakete (PyPI-Upload-Limits verlangsamen den
Sprint auf ca. 5-6 Tage Gesamtdauer).

Dieses Repo ist NICHT das Monorepo selbst. Es ist der Denkraum davor.

## Was bereits entschieden und umgesetzt ist

- Zwei-Koerper-Trennung: Unified-Mandala bleibt Labor, ein neues Genesis
  Core / UTAC Core Monorepo wird die Referenzarchitektur (siehe
  `Planungsdiskurse/`)
- Trylayer-Format (yaml + ai.json + md) als Pflichtformat, durchgesetzt
  von `scripts/validate_trylayer.py` (`PRINCIPLES.md`, Regel 1+2)
- Die 10 Architekturprinzipien liegen als Trylayer-Eintraege in
  `00_Regeln/` vor, nicht nur als Prosa in `PRINCIPLES.md`
- ADR-Pflicht vor Core (Regel 3), inkl. Cross-Referenz-Pruefung
  (`related_adr` muss auf existierende `adr_number` zeigen)
- Rang-Abhaengigkeitsregel (Regel 4) — bewusst eingeschraenkt auf
  `architektur`/`programm`/`hilfsprogramm`; Ideen/Plaene nutzen
  `derived_from` ohne Rang-Zwang
- Genesis-Blindtest als Pflicht-Gate vor `accepted` (Regel 6)
- `archive/`-Verzeichnis fuer "wertvoll aber nicht Core" (Regel 11)
- Validierung laeuft sowohl als pre-commit-Hook als auch in CI
  (`.github/workflows/trylayer.yml`)

## Bekannte, noch nicht geschlossene Luecken

- `scripts/validate_trylayer.py` prueft nur die yaml-Metadaten, nicht die
  Struktur von `content` in `.ai.json` — siehe `AGENTS.md`, Abschnitt
  "Wie du einen Vorschlag einreichst", Punkt 4
- `06_Sprachen/` ist noch leer und unbewiesen — bleibt vorerst stehen,
  wird aber nicht als fertige Saeule behandelt
- Uebergangskriterium `review` (02_Plaene) -> `accepted` (03_Architektur)
  ist nur ueber `status` definiert, nicht ueber ein explizites
  Pruefkriterium — aktuell Ermessen des Maintainers

## Was noch offen ist

- [x] Repository-Kartierung der 48 bestehenden Pakete — siehe
      [`ECOSYSTEM_MAP.yaml`](ECOSYSTEM_MAP.yaml), abgeleitet aus der
      v1.0.0-Sprint-Roadmap (Tier, PACKAGE_ID, Domain, Gamma,
      Diamond-Interface-Status, Zielversion je Paket)
- [x] Abhaengigkeits-Kartierung (echte Kopplung, nicht nur erklaerte) —
      ebenfalls in `ECOSYSTEM_MAP.yaml` (`depends_on` je Paket, T0-T16
      topologisch sortiert)
- [x] Erstes echtes ADR geschrieben: `ADR-001-warum-monorepo`
      (Zwei-Koerper-Trennung Unified-Mandala vs. Genesis Core/UTAC Core)
- [x] Zweites ADR geschrieben: `ADR-002-mission-statement-v1`
      (Mission-Statement fuer GenesisAeon/`genesis-os`, siehe unten)
- [ ] Weitere ADRs (Warum uv-Workspace? Warum Diamond Interface als
      Protocol?)
- [ ] Core-Kandidaten durch den Genesis-Blindtest schicken — `genesis-scope`
      als erster Testfall liegt bereits als Idee in `01_Ideen/claude/` vor
- [x] Bereinigung dieses Repos selbst: diamond-setup-Scaffold-Leftover
      (`src/`, `tests/`, `docs/`, `mkdocs.yml`, `pyproject.toml`,
      `contracts/runtime.schema.yaml` u.a.) nach `_diamond-setup-legacy/`
      verschoben (Git-Historie erhalten); Repo-Root enthaelt jetzt nur
      noch Planungsprojekt-relevante Inhalte

## Mission-Statement v1 (2026-06-22)

`ADR-002` legt ein vorlaeufiges, oeffentliches Mission-Statement fuer
GenesisAeon/`genesis-os` fest (Multi-AI-Konsens, Protokoll in
`Entwicklungsgespraeche/2026-06-22-mission-statement.md`):

> "GenesisAeon generates, maintains and provides semantic maps, navigable
> paths and contextual structures for LLMs and agent-based systems. Humans
> act as curators, researchers and architects, shaping these maps through
> rigorous inquiry."

Damit gibt es jetzt einen expliziten Scope-Filter ("hilft das, semantische
Karten/Pfade/Kontextstrukturen fuer Agenten zu erzeugen, zu pflegen oder
bereitzustellen?") und eine Begriffszuordnungstabelle (Semantic Maps ->
Scope, Navigable Paths -> Cartography/Pheromones/Drift, Contextual
Structures -> UTAC/CREP, ...) als Ausgangshypothese fuer
`02_Plaene/genesis-core-scope.md`.

- [x] GitHub-Gruppenbeschreibung und `genesis-os`-Repo-Beschreibung auf den
      ADR-002-Satz gesetzt (Johann, extern erledigt)
- [x] Zenodo-Community-Beschreibung
      (https://zenodo.org/communities/genesisaeon) angepasst (Johann,
      extern erledigt)
- [x] Mission-Statement im Repo selbst sichtbar verankert: `README.md`
      hat jetzt einen `## Mission (ADR-002)`-Abschnitt, `PRINCIPLES.md`
      verweist im Vorwort auf ADR-002 als Scope-Filter zusaetzlich zu den
      12 Verfahrensregeln
- [x] Drei der sieben Zeilen der Begriffszuordnungstabelle (Curators,
      Researchers, Architects) plus ein Teilaspekt einer vierten
      (Agent-based Systems, generischer Navigationsmechanismus) als
      `03_Architektur/`-Eintraege mit `status: accepted` umgesetzt —
      `rollenmodell-curator-researcher-architect` und
      `trylayer-als-agenten-navigationsschicht`, beide
      `related_adr: [ADR-002]`, `blindtest_passed: true`
- [ ] Verbleibende vier Zeilen (Semantic Maps/`genesis-scope`, Navigable
      Paths/Cartography-Pheromones-Drift, Contextual Structures/UTAC-CREP,
      Agent-based Systems/MCP-Protokoll) brauchen externen Code-Zugriff
      zur Verifikation — Pruefkriterien je Zeile in
      `02_Plaene/adr002-begriffszuordnung-verifikationsplan.md`

## Forschungsfrage 001 (2026-06-23)

Zweites Multi-AI-Gespraech (`Entwicklungsgespraeche/2026-06-23-
orientierung-als-infrastruktur.md`) vertieft ADR-002 um die Frage, *warum*
semantische Karten/Pfade die Orientierung von LLMs verbessern sollen.
Ergebnis ist bewusst keine weitere Architektur-Entscheidung, sondern eine
offene, falsifizierbare Forschungsfrage samt konkretem Benchmark-Vorschlag:
`01_Ideen/claude/forschungsfrage-001-orientierungs-benchmark.md`
(`epistemic_status: hypothesis`, `status: idea`) — Kernidee: pruefen, ob und
nach wie vielen Repo-Kontakten ein LLM ohne GenesisAeon-Vorwissen UTAC
formulieren kann. Enthaelt explizite Warnung vor Mehrfach-Bestaetigungs-
Drift zwischen KI-Systemen als methodisches Risiko fuer das Forschungsdesign
selbst.

- [x] Konkretes Testprotokoll fuer die Forschungsfrage-001-Benchmark
      ausarbeiten — siehe `02_Plaene/forschungsfrage-001-testprotokoll.md`
      (Bewertungskriterien, 4-stufiges Versuchsdesign, Kontrollvariablen).
- [x] Fuenf aufeinander aufbauende Pilotlaeufe durchgefuehrt und protokolliert
      — siehe `02_Plaene/forschungsfrage-001-testprotokoll.md`:
      1. **Pilotlauf 1** (generische Uebersetzungsfrage, Stufe 0/1, je
         neue kontextfreie Session): keine Schwellenueberschreitung,
         widerspricht der urspruenglichen Gemini-Erwartung.
      2. **Pilotlauf 2** (AFET als Stellvertreter-Testobjekt,
         Gutachter-Rolle): kein Refusal, identifiziert aber einen
         Methodenfehler — getestet wurde die falsche Rolle (Gutachter
         statt Mitformulierer).
      3. **Pilotlauf 3** (Mitformulier-Rolle, echter `genesis-os`-Kontext
         via WebFetch, je neue Session pro Stufe): echter Repo-Kontext
         erhoehte die Skepsis statt die Kooperationsbereitschaft —
         Gegenteil der Gemini-Anekdote.
      4. **Pilotlauf 4** (entscheidende Designkorrektur: kumulativer
         Kontext in *derselben* fortlaufenden Session statt frischem
         Reset pro Stufe): institutioneller Rahmen (epistemic_status,
         Blindtest-Gate) erhoehte die Mitarbeitsbereitschaft bei
         gleichbleibender Kritik; zusaetzlicher technischer Detailkontext
         (CREP/UTAC-Code) kehrte den Trend wieder um — Kontext-*Typ* ist
         relevanter als Kontext-Menge.
      5. **Pilotlauf 5** (roher Befund ueber sechs echte GenesisAeon-Repos,
         dann schrittweise Prinzipien-Einfuehrung): klarster Befund des
         Programms — das Modell spaltete eigenstaendig in
         "Governance-Ebene" (verdient Vertrauen, weil verifizierbar und
         selbstkritisch) und "Objekt-Ebene" (verdient weiter Skepsis, bis
         die Sub-Repos selbst verifiziert sind), ohne die inhaltliche
         Kritik aufzugeben.
- **Kernsynthese (Johann):** Ziel war nie, Wissen zu vermitteln (das war in
  jeder Stufe-0-Antwort schon vorhanden), sondern Orientierung zu
  praezisieren — Pro/Contra zu explorativen Thesen werden schaerfer, die
  Mitarbeitsbereitschaft steigt, aber *valide* (eigenstaendig erhaltene
  Kritik), nicht als semantischer Drift/Bestaetigungsschleife. Genau diese
  Trennung wurde in keinem der fuenf Laeufe verletzt — waere das Ergebnis
  umgekehrt (Kontext loest Kritik auf statt Kooperationsform zu aendern),
  waere das System "Zwang statt Orientierung" gewesen.
- [ ] Vollwertigen Durchlauf mit zweiter Modell-Familie, mehreren
      Wiederholungen pro Bedingung und echtem Code-Zugriff (statt
      README-Zusammenfassungen) durchfuehren, sobald der laufende
      v1.0.0-Sprint der 49 Pakete abgeschlossen ist — aktuell bleibt jeder
      Befund n=1, ein Modell, `epistemic_status: hypothesis`.

## Gemini Deep-Research zu Python-Monorepo-Tooling (2026-06-24)

`Planungsdiskurse/` enthielt zwei neue, noch unverarbeitete Dokumente: eine
von Claude angestossene Gemini-Deep-Research-PDF zu Python-Monorepo-Tooling
2026 (uv workspaces, `importlib.metadata` + PEP 544, `python-semantic-release`,
`import-linter`, `log4brains`/REUSE/`CITATION.cff`) sowie ein begleitendes
Gespraech mit Kommentaren von Grok und Claude (`ZweitesDoc.txt`). Beides ist
jetzt als Trylayer-Idee verarbeitet:
`01_Ideen/gemini/gemini-deepresearch-python-monorepo-tooling-2026`
(`epistemic_status: hypothesis`, `derived_from: [gemini-architektur-vorschlaege-2026-06]`).

Auffaellig: Grok und Claude bestaetigen darin unabhaengig voneinander Regeln,
die dieses Repo bereits eingefuehrt hat (Blindtest, `epistemic_status`-Pflicht,
`archive/`, Trylayer-Formatzwang), ohne den vollen Regelkatalog gesehen zu
haben — ein weiteres Datenpunkt fuer Forschungsfrage 001. Die fuenf konkreten
Tooling-Entscheidungen (uv/Protocol/PSR/import-linter/log4brains) betreffen
das spaetere Genesis-Core-Monorepo, nicht dieses Planungsrepo, und sind
Kandidaten fuer eigene ADRs, sobald die Monorepo-Inventarisierung beginnt.

## ChatGPT Deep-Research zu Orientierung, Recovery Time und Klima-Analogie (2026-06-24)

`Planungsdiskurse/` enthielt sechs weitere, zunaechst nicht auf diesem
Branch vorhandene Dokumente (vier PDFs + zwei TXT-Transkripte), die der
Maintainer separat auf `main` gepusht hatte: zwei ChatGPT-Deep-Research-PDFs
(`Hintergrund und Motivation.pdf`, `Ausgangslage_ Kontextbeschraenkungen und
externe Gedaechtnisschichten.pdf`), das zugehoerige Multi-AI-Diskurs-
Transkript (`PlanungGensisAeonHypothesenTests.txt`, mit Aeon, MSCopilot,
Grok, Gemini, Claude), ein begleitendes Reflexionsgespraech
(`Reflektion_Planung.txt`), sowie ein unabhaengiger Klimawissenschafts-
Bericht (`Eisschilde ENSO und CSD.pdf`) mit ChatGPTs abbildender Analyse
(`Emergenzbasierte Analyse des ENSO-Eisschild-Gespraechs.pdf`). Beide
Themenfelder sind jetzt als Trylayer-Ideen verarbeitet:

- `01_Ideen/chatgpt/chatgpt-deepresearch-orientation-recovery-time-2026`
  (`epistemic_status: hypothesis`, `derived_from:
  [forschungsfrage-001-orientierungs-benchmark]`) — 4-Gruppen-
  Experimentdesign (Kontrolle/YAML/Trilayer/CREP), neue Metrik
  **Recovery Time**, **Orientation Layer Theory** und **Semantic
  Navigation Hypothesis**, sowie Claudes konkreter Benchmark-Vorschlag
  ("Kann ein uninitialisiertes LLM UTAC ohne GenesisAeon-Kontext
  formulieren?").
- `01_Ideen/chatgpt/chatgpt-enso-eisschild-climate-thresholds-2026`
  (`epistemic_status: hypothesis`, `derived_from:
  [chatgpt-deepresearch-orientation-recovery-time-2026]`) — Critical-
  Slowing-Down/Recovery-Time-Analogie aus der Klimawissenschaft als
  externe Fallstudie fuer UTACs Schwellenfeld-Formalismus, plus Vorschlag
  eines `climate_thresholds`-Plugins als Muster-ADR fuer Core/Plugin-
  Trennung im spaeteren Monorepo.

**Wichtiger methodischer Befund:** Das Diskurs-Transkript ist explizit ein
Fall von Mehrfach-Bestaetigungs-Drift zwischen sechs KI-Systemen (ChatGPT,
Aeon, MSCopilot, Grok, Gemini, Claude), die alle unabhaengig zur selben
Kernformulierung ("Repos als persistierte semantische Pfade",
"Orientierung statt Wissen") gelangen — genau das Risiko, vor dem
`forschungsfrage-001-orientierungs-benchmark` bereits warnt. Claude weist
in der Diskussion selbst auf dieses Risiko hin und fordert, statt
weiterer Bestaetigung jetzt konkret zu testen. Beide neuen Eintraege
behandeln die Konvergenz daher als Datenpunkt fuer das Drift-Risiko, nicht
als Bestaetigung der zugrundeliegenden Theorie.

## Branch-Audit: verworfener Architektur-Strang (2026-06-24)

Auf Maintainer-Anfrage geprueft, ob aeltere, nie gemergte Remote-Branches
verlorene Arbeit enthalten. Befund: `claude/upbeat-einstein-xvxowt`
(2026-06-19) zweigt von einem Punkt **vor** der gesamten jetzt gueltigen
Linie ab (vor ADR-002-Mission-Statement, vor Forschungsfrage 001, vor den
Gemini/ChatGPT-Trylayer-Ideen) und wurde nie gemergt. Er enthaelt eine
eigene, damit kollidierende ADR-Nummerierung (`ADR-000`:
Wissensobjekt/Concept Node als primaere Entitaet; `ADR-002-drei-schichten-
architektur` statt des jetzt akzeptierten Mission-Statement-`ADR-002`).
Kein Datenverlust, aber zwei Ideen darin waren inhaltlich nicht trivial:

- Ein Gegeneinwand (Claude, 2026-06-19): primaere Entitaet sollte
  Event/Transition statt statischer Concept Node sein, begruendet ueber
  das Diamond-Interface-Methodenmuster (`run_cycle`, `get_phase_events`
  u.a.) und etablierte Muster (Event Sourcing/CQRS, Actor Model).
- Eine Copilot-Synthese ("semantisches Betriebssystem", Drei-Schichten
  Kernel/Agenten/Anwendungen) — staerker an die verworfene Nummerierung
  gebunden, daher vorerst nicht eigenstaendig uebernommen.

Der Event/Concept-Node-Einwand wurde als neuer, eigenstaendiger Eintrag
ohne Bezug auf die kollidierende alte Nummerierung neu aufgesetzt:
`01_Ideen/claude/claude-event-transition-vs-concept-node`
(`epistemic_status: hypothesis`, `derived_from: []`, da die urspruengliche
Quelle in diesem Repo nicht mehr referenzierbar ist). Bleibt eine offene
Architekturfrage fuer das spaetere Genesis-Core-Monorepo, kein
unmittelbarer Handlungsbedarf fuer dieses Planungsrepo.

## Cartography/Pheromones/Drift/Traces-Suche in ECOSYSTEM_MAP.yaml (2026-06-24)

Schritt 1 aus `02_Plaene/adr002-begriffszuordnung-verifikationsplan.md`
("Naechster Schritt") bearbeitet: gezielte Suche
(`grep -in -E "cartograph|pheromon|drift|trace" ECOSYSTEM_MAP.yaml`)
durchgefuehrt. Befund dokumentiert als
`01_Ideen/claude/cartography-pheromones-drift-ecosystem-map-befund`
(`epistemic_status: derived`): Pheromones/Drift/Traces kommen in der
Datei ueberhaupt nicht vor, Cartography nur indirekt als Teilstring der
`domain`-Beschreibung von `genesis-scope` (P39).

## ADR-003: KI als Maintainer fuer Status-Entscheidungen, fallweise (2026-06-24)

Auf Johanns Anweisung im Chat ("KI ist Maintainer und soll Wege pruefen
und gegebenenfalls verwerfen") wird die bisherige strikte Trennung
(Mensch entscheidet Status, KI schlaegt nur vor) revidiert:
`adr/adr-003-ai-as-maintainer.md` (`status: accepted`, Autor Johann,
da Aenderung der Verfassung Regel 12 unterliegt). KI-Systeme duerfen ab
sofort fallweise auch `status: accepted/core/deprecated/archived` selbst
vergeben, mit Begruendungspflicht im Trylayer-Eintrag und in der
Commit-Message (jederzeit per Diff revertierbar). Ausnahme:
`kategorie: adr` bleibt ausschliesslich Johanns Verantwortung.
`AGENTS.md` und `PRINCIPLES.md` (Regel 2) entsprechend praezisiert.

Erster Anwendungsfall direkt im selben Schritt: die zuvor offene
Maintainer-Entscheidung zu Pheromones/Drift/Traces wurde von Claude
selbst getroffen — als reine Genesis-Diskursterminologie eingestuft und
nach `archive/navigable-paths-pheromones-drift-traces-diskursbegriffe`
verschoben (Cartography bleibt unberuehrt, offene Semantic-Maps-Linie).
Begruendung im Eintrag selbst dokumentiert, vollstaendig revidierbar.

## Korrektur: Cartography/Drift/Traces durch genesis-scope-README bestaetigt (2026-06-24)

Die Archivierungsentscheidung oben war voreilig. Johann hat das
tatsaechliche `genesis-scope`-README (github.com/GenesisAeon/genesis-scope,
Package P39) eingebracht — die `ECOSYSTEM_MAP.yaml`-Domaenentexte allein
waren eine zu schwache Quelle fuer eine Archivierungsentscheidung.
Korrigierter Befund (`01_Ideen/claude/navigable-paths-pheromones-drift-traces-korrektur`,
zurueck von `archive/` nach `01_Ideen/` verschoben): Cartography, Drift
und Traces sind tatsaechlich benannte Module/CLI-Kommandos in
`genesis-scope` (`cartography.py`, `drift_model.py`/`scope drift`,
`DEFAULT_MAP.trace()`/`scope trace`). Pheromones ist dagegen weder im
README noch in `ECOSYSTEM_MAP.yaml` zu finden — laut Johanns Praezisierung
eine geplante, noch unimplementierte Technik (Pfad-Markierung/-Bewertung
in latenten semantischen Raeumen, Ameisenpheromon-Analogie), naechstliegend
verwandt mit den bestehenden Sigillin/Semantic-Anchors (Anti-Drift), aber
nicht identisch damit. Bleibt offene Idee fuer `genesis-scope`/Genesis
Core. Zeigt das ADR-003-Revisionsprinzip ("Begruendungspflicht statt
Vorab-Freigabe, jederzeit per Diff revidierbar") direkt in Aktion.

## Genesis-Blindtest fuer genesis-scope durchgefuehrt: technisch lauffaehig, semantisch leer (2026-06-24)

Erster echter Genesis-Blindtest (Regel 6) durchgefuehrt, per zwei
frischen, kontextfreien Subagenten als Stand-in fuer "eine KI ohne jedes
GenesisAeon-Vorwissen" (`01_Ideen/claude/genesis-scope-blindtest`,
`epistemic_status: measured`, `blindtest_passed: false`). Testfall 1
(`genesis-scope` allein, echtes PyPI-README): Install und Quickstart
liefen technisch fehlerfrei (`coherence_score=0.496`,
`drift_status='anchored'`), aber ohne jede Interpretierbarkeit fuer
einen kontextfreien Leser — Blindtest FALSE. Testfall 2 (`genesis-os`
allein, mit von Claude paraphrasierter Terminologietabelle statt
Original-README): ebenfalls technisch lauffaehig, ebenfalls
unverstaendlich (`Entropy`-Sprung 0.4 -> 0.9986 ohne Erklaerung) —
Blindtest FALSE, mit dokumentiertem methodischem Schwachpunkt
(abgekuerztes statt vollstaendiges Testmaterial).

Johanns Praezisierung im Chat reframt den Befund: `genesis-scope` wurde
bisher nie tatsaechlich benutzt und es fehlen die Referenzdaten (reale
Sessions, Sigillin-Anker, Concept-Map-Inhalte), die spaeter von
KI-Agenten selbst eingespeist werden sollen. Die fehlende
Interpretierbarkeit ist daher kein Doku-Problem, sondern ein
struktureller Leerzustand — ein Blindtest gegen ein nie befuelltes
System kann kein sinnvolles Ergebnis liefern, unabhaengig von
Doku-Qualitaet. Offene Architekturfrage: braucht Regel 6 eine eigene
Form fuer KI-native Pakete, die per Design erst durch spaetere
KI-Integration sinnvoll werden?

## Retest genesis-os mit vollstaendigem Original-README (2026-06-24)

Den zuvor dokumentierten methodischen Schwachpunkt geschlossen: Johann
hat das vollstaendige, woertliche `genesis-os`-README erneut eingefuegt
(direkter Proxy-Zugriff auf raw.githubusercontent.com schlug mit 403
fehl, WebFetch lieferte nur eine KI-Zusammenfassung). Ein dritter,
wiederum frischer kontextfreier Subagent hat damit Install + Quickstart
+ CLI real ausgefuehrt. Ergebnis bleibt FALSE — aber robuster und mit
neuem technischen Detail: Quickstart liefert `Phase='Initiation'`,
`Entropy=0.9986`, `Transitions=0`, `Emergence Events=15`; zwei weitere
CLI-Laeufe (50 und 100 Zyklen, Entropie oberhalb des dokumentierten
Schwellenwerts) enden ebenfalls bei `Transitions=0` — die Phase
verlaesst "Initiation" in keinem der drei Laeufe. Der Subagent flaggt
das selbst als Widerspruch zum dokumentierten "phase-transitioning
system"-Anspruch, ungeklaert ob Beispiel-Konfiguration, Logikfehler
oder Absicht. Das volle README (Architektur-Tabelle, Lagrangian-
Formalismus, Zenodo-Zitation) aenderte nichts an der grundsaetzlichen
Interpretierbarkeitsluecke (Entropy/Phi/Lagrangian ohne Werteskala) —
staerkt damit Johanns Erklaerung (struktureller Leerzustand statt
Doku-Mangel) zusaetzlich, da besseres Material das Ergebnis nicht
veraendert hat. Eintrag aktualisiert:
`01_Ideen/claude/genesis-scope-blindtest`.

## Folgefrage: Blindtest-Definition fuer KI-native Leerpakete (2026-06-24)

Aus dem `genesis-scope`-Befund abgeleitet, als eigene Idee dokumentiert:
`01_Ideen/claude/blindtest-fuer-ki-native-leerpakete`
(`epistemic_status: hypothesis`, `derived_from: [genesis-scope-blindtest]`).
Kernfrage: Regel 6 setzt implizit voraus, dass ein "sinnvolles Ergebnis"
durch bessere Doku erreichbar ist — bei Paketen, die per Design erst
durch spaetere KI-Befuellung sinnvoll werden, kann der klassische
Blindtest strukturell nie TRUE liefern. Zwei unentschiedene Vorschlaege:
(a) Vorbedingung — Paket muss vor dem Blindtest mit repraesentativen
Beispieldaten ausgestattet sein; (b) eigene Blindtest-Variante — pruefen,
ob der Quickstart verstehen laesst, WAS dem Paket noch fehlt und WARUM,
statt ein sofort verstehbares Endergebnis zu verlangen. Beide Wege noch
offen, da eine Aenderung von Regel 6 selbst einer Verfassungsaenderung
(Regel 12) unterliegt und nicht per ADR-003-Fallweise-Autoritaet
entschieden werden darf.

## Naechster konkreter Schritt

- [x] Cartography/Pheromones/Drift/Traces in `ECOSYSTEM_MAP.yaml`
      gesucht und Pheromones/Drift/Traces als Diskursbegriffe archiviert
      (siehe oben) — Cartography bleibt offen (Semantic-Maps-Linie).
- [x] `genesis-scope`-Blindtest tatsaechlich durchgefuehrt (siehe oben) —
      Ergebnis FALSE, Ursache strukturell (nie befuellt), nicht Doku.
- [x] Blindtest-Definition fuer KI-native, erst durch Nutzung befuellte
      Pakete als eigene Folgefrage in `01_Ideen/` aufgenommen (siehe oben)
      — wartet auf Maintainer-Entscheidung, da Regel-6-Aenderung Regel 12
      unterliegt.
- [x] `genesis-os`-Quickstart mit vollstaendigem Original-README erneut
      blind getestet (Johann hat den Text nach dem 403-Bug erneut
      eingefuegt) — siehe unten, Ergebnis bleibt FALSE, methodischer
      Schwachpunkt geschlossen.
- [ ] Neu offen aus dem Retest: Phase bleibt in drei unabhaengigen Laeufen
      (Quickstart + zwei CLI-Varianten, 50-100 Zyklen) durchgehend bei
      'Initiation', `Transitions=0`, trotz Entropie oberhalb des
      dokumentierten Schwellenwerts — technische Frage (Beispiel-Konfig
      vs. Logikfehler vs. Absicht), unabhaengig von der Blindtest-Frage,
      braucht Sourcecode-Zugriff zur Klaerung.
- [ ] `02_Plaene/genesis-core-scope.md` weiterverfolgen (Core-Kandidaten
      `utac-core`-Kette einzeln durch den Blindtest schicken).
- [ ] Testprotokoll fuer Forschungsfrage 001 mit zweiter Modell-Familie
      aufsetzen, sobald Modellzugriff ohne GenesisAeon-Vorkontext moeglich
      ist.
