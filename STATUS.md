# Ist-Stand

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) ist der verbindliche
> Einstiegspunkt (Regel 12). Dieses Dokument ist Schritt 2 davon — lies
> danach `PRINCIPLES.md` und `AGENTS.md`.

Letztes Update: 2026-06-22

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

## Naechster konkreter Schritt

Die vier offenen Zeilen aus `02_Plaene/adr002-begriffszuordnung-
verifikationsplan.md` einzeln abarbeiten: zuerst Cartography/Pheromones/
Drift/Traces in `ECOSYSTEM_MAP.yaml` verorten (oder als reine
Diskurs-Begriffe nach `archive/` verschieben, Regel 9), danach den
`genesis-scope`-Blindtest tatsaechlich durchfuehren, sobald
Quickstart-Zugriff besteht. Parallel: `02_Plaene/genesis-core-scope.md`
weiterverfolgen (Core-Kandidaten `utac-core`-Kette einzeln durch den
Blindtest schicken).
