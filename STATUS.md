# Ist-Stand

Letztes Update: 2026-06-19

## Phase

**Planung / Architektur-Diskurs** — parallel zum laufenden v1.0.0-Release-
Sprint der 48 GenesisAeon-Pakete (PyPI-Upload-Limits verlangsamen den
Sprint auf ca. 5-6 Tage Gesamtdauer).

Dieses Repo ist NICHT das Monorepo selbst. Es ist der Denkraum davor.

## Was bereits entschieden ist

- Zwei-Koerper-Trennung: Unified-Mandala bleibt Labor, ein neues Genesis
  Core / UTAC Core Monorepo wird die Referenzarchitektur (siehe
  `Planungsdiskurse/`)
- Trylayer-Format (yaml + ai.json + md) als Pflichtformat fuer jede
  Wissenseinheit in diesem Repo (siehe `PRINCIPLES.md`, Regel 1)
- Genesis-Blindtest als Aufnahmekriterium fuer den Core (Regel 6)

## Was noch offen ist

- [ ] Repository-Kartierung der 48 bestehenden Pakete
- [ ] Abhaengigkeits-Kartierung (echte Kopplung, nicht nur erklaerte)
- [ ] Erste ADRs schreiben (Warum Monorepo? Warum uv-Workspace? Warum
      Diamond Interface als Protocol?)
- [ ] Core-Kandidaten durch den Genesis-Blindtest schicken — `genesis-scope`
      als erster Testfall
- [ ] Graveyard/Archiv-Verzeichnis fuer "wertvoll aber nicht Core"
- [ ] Bereinigung dieses Repos selbst: `src/`, `contracts/`, `scripts/`,
      `tests/`, `docs/`, `mkdocs.yml`, `pyproject.toml` sind aktuell noch
      unveraendertes diamond-setup-Scaffold-Leftover und gehoeren fachlich
      nicht in dieses Planungsrepo

## Naechster konkreter Schritt

Inventarisierung starten: erstes Trylayer-Tripel in `01_Ideen/` fuer
`genesis-scope` anlegen und durch den Blindtest schicken.
