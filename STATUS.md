# Ist-Stand

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) ist der verbindliche
> Einstiegspunkt (Regel 12). Dieses Dokument ist Schritt 2 davon — lies
> danach `PRINCIPLES.md` und `AGENTS.md`.

Letztes Update: 2026-06-19

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
- [x] `ADR-000-primaere-entitaet` geschrieben: legt das Wissensobjekt
      (semantischer Konzeptknoten, synonym State Object/Concept Node) als
      primaere Entitaet fest und den Core als domaenenneutrale
      Infrastruktur statt Einzelanwendung
- [x] `ADR-002-drei-schichten-architektur` geschrieben: Kernel (Schicht 1)
      / Agenten & Perspektiven (Schicht 2) / Anwendungen (Schicht 3),
      Abhaengigkeitsrichtung nur 3 -> 2 -> 1; Rohidee dazu liegt in
      `01_Ideen/copilot/copilot-semantisches-betriebssystem.md`
- [ ] Weitere ADRs (Warum uv-Workspace? Warum Diamond Interface als
      Protocol?)
- [ ] Core-Kandidaten durch den Genesis-Blindtest schicken — `genesis-scope`
      als erster Testfall liegt bereits als Idee in `01_Ideen/claude/` vor
- [x] Bereinigung dieses Repos selbst: diamond-setup-Scaffold-Leftover
      (`src/`, `tests/`, `docs/`, `mkdocs.yml`, `pyproject.toml`,
      `contracts/runtime.schema.yaml` u.a.) nach `_diamond-setup-legacy/`
      verschoben (Git-Historie erhalten); Repo-Root enthaelt jetzt nur
      noch Planungsprojekt-relevante Inhalte

## Naechster konkreter Schritt

Erste echte `03_Architektur/`-Eintraege auf Basis von `ADR-001`
formulieren (z.B. die Zwei-Koerper-Trennung selbst als
Architektur-Eintrag mit `related_adr: [ADR-001]`), und/oder
Repository-Kartierung der 48 Pakete beginnen.
