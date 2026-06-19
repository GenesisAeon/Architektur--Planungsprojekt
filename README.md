# Architektur--Planungsprojekt

Planungs-/Architektur-Workspace für den Übergang des GenesisAeon-
Ökosystems von Unified-Mandala (explorativem Forschungslabor) zu einer
kanonisierten, öffentlichkeitsfähigen Referenzarchitektur (Genesis Core /
UTAC Core). Hier werden Entscheidungen getroffen — das eigentliche
Monorepo entsteht erst danach.

**Bist du ein KI-System?** Lies zuerst [`AGENTS.md`](AGENTS.md).

## Ist-Stand

→ [`STATUS.md`](STATUS.md)

## Regeln

→ [`PRINCIPLES.md`](PRINCIPLES.md) — die Verfassung, maschinell durch
[`scripts/validate_trylayer.py`](scripts/validate_trylayer.py) durchgesetzt.

## Format: Trylayer

Jede Wissenseinheit (Idee, Plan, Architekturentscheidung, Programm- oder
Hilfsprogramm-Spezifikation, Begriffsdefinition) liegt als Dreifach-Datei
vor:

```
<slug>.yaml       Index/Metadaten (schnelle Navigation)
<slug>.ai.json     AI-Vollversion (vollständig strukturierter Inhalt)
<slug>.md          Menschenversion (Prosa, Begründung)
```

Schema: [`contracts/trylayer.schema.yaml`](contracts/trylayer.schema.yaml)

## Struktur

```
00_Regeln/          Die 10 Architekturprinzipien als Trylayer-Einträge
01_Ideen/            Roh-Vorschläge (status: idea, draft)
02_Plaene/           Konkretisierte Planung (status: draft, review)
03_Architektur/      Kanonisierte Entscheidungen (status: accepted, core)
04_Programme/        Core-Modul-Spezifikationen
05_Hilfsprogramme/   Plugin-/Tool-Spezifikationen
06_Sprachen/         Glossar, Terminologie (noch unbefüllt)
adr/                 Architecture Decision Records
archive/             Verworfenes / "wertvoll aber nicht Core"
Planungsdiskurse/    Archiv des ursprünglichen Multi-AI-Diskurses (read-only)
```

## Validierung

```bash
python scripts/validate_trylayer.py
```

Läuft als pre-commit-Hook und in CI ([`.github/workflows/trylayer.yml`](.github/workflows/trylayer.yml)).

---

Hinweis: `src/`, `contracts/runtime.schema.yaml`, `tests/`, `docs/`,
`mkdocs.yml` und `pyproject.toml` sind aktuell noch Reste des
`diamond-setup`-Scaffolds, aus dem dieses Repo ursprünglich erzeugt wurde.
Sie gehören fachlich nicht zu diesem Planungsprojekt — siehe `STATUS.md`,
offener Punkt "Bereinigung".
