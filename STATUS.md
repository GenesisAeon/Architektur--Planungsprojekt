# Ist-Stand

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) ist der verbindliche
> Einstiegspunkt (Regel 12). Dieses Dokument ist Schritt 2 davon — lies
> danach `PRINCIPLES.md` und `AGENTS.md`.

Letztes Update: 2026-06-24 (Gemini-Deep-Research zu Python-Monorepo-Tooling
verarbeitet)

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

## Naechster konkreter Schritt

Die vier offenen Zeilen aus `02_Plaene/adr002-begriffszuordnung-
verifikationsplan.md` einzeln abarbeiten: zuerst Cartography/Pheromones/
Drift/Traces in `ECOSYSTEM_MAP.yaml` verorten (oder als reine
Diskurs-Begriffe nach `archive/` verschieben, Regel 9), danach den
`genesis-scope`-Blindtest tatsaechlich durchfuehren, sobald
Quickstart-Zugriff besteht. Parallel: `02_Plaene/genesis-core-scope.md`
weiterverfolgen (Core-Kandidaten `utac-core`-Kette einzeln durch den
Blindtest schicken), und das Testprotokoll fuer Forschungsfrage 001
aufsetzen, sobald Modellzugriff ohne GenesisAeon-Vorkontext moeglich ist.
