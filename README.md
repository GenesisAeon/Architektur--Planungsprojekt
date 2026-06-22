# Architektur--Planungsprojekt

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) definiert die verbindliche
> Lesereihenfolge fuer dieses Repo (Regel 12). Dieses README ist Schritt 1
> davon — wenn du hier zufaellig zuerst gelandet bist, lies trotzdem
> `ENTRY.yaml`, um den vollstaendigen Pfad zu sehen.

Planungs-/Architektur-Workspace für den Übergang des GenesisAeon-
Ökosystems von Unified-Mandala (explorativem Forschungslabor) zu einer
kanonisierten, öffentlichkeitsfähigen Referenzarchitektur (Genesis Core /
UTAC Core). Hier werden Entscheidungen getroffen — das eigentliche
Monorepo entsteht erst danach.

**Bist du ein KI-System?** Lies zuerst [`AGENTS.md`](AGENTS.md).

## Mission (ADR-002)

> GenesisAeon generates, maintains and provides semantic maps, navigable
> paths and contextual structures for LLMs and agent-based systems. Humans
> act as curators, researchers and architects, shaping these maps through
> rigorous inquiry.

Verbindlicher Scope-Filter fuer jeden Beitrag in diesem Repo: Hilft er
dabei, semantische Karten, Pfade oder Kontextstrukturen fuer Agenten
besser zu erzeugen, zu pflegen oder bereitzustellen? Wenn nein, gehoert er
wahrscheinlich nicht in den Core. Begruendung und Begriffszuordnung:
[`adr/adr-002-mission-statement-v1.md`](adr/adr-002-mission-statement-v1.md).

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
00_Regeln/          Die 12 Architekturprinzipien als Trylayer-Einträge
01_Ideen/            Roh-Vorschläge (status: idea, draft)
02_Plaene/           Konkretisierte Planung (status: draft, review)
03_Architektur/      Kanonisierte Entscheidungen (status: accepted, core)
04_Programme/        Core-Modul-Spezifikationen
05_Hilfsprogramme/   Plugin-/Tool-Spezifikationen
06_Sprachen/         Glossar, Terminologie (noch unbefüllt)
adr/                 Architecture Decision Records
archive/             Verworfenes / "wertvoll aber nicht Core"
Planungsdiskurse/    Archiv des ursprünglichen Multi-AI-Diskurses (read-only)
Entwicklungsgespraeche/ Rohprotokolle laufender Multi-AI-Gespräche (Eingabe, kein Trylayer)
```

## Validierung

```bash
python scripts/validate_trylayer.py
```

Läuft als pre-commit-Hook und in CI ([`.github/workflows/trylayer.yml`](.github/workflows/trylayer.yml)).

---

## KI als Schnittstelle

Wenn Ideen oder Vorschläge von anderen Systemen (anderen LLMs, Tools,
Menschen ausserhalb des Kernteams) eingebracht werden sollen, läuft das
über ein KI-System (z.B. Claude), das den Vorschlag erst Repo-konform
nach Trylayer-Format aufbereitet (siehe `AGENTS.md`), bevor er
eingereicht wird. Das hält die Eingangsschwelle für Externe niedrig,
ohne die Formatstrenge des Repos aufzuweichen.

---

Hinweis: `_diamond-setup-legacy/` enthaelt Reste des `diamond-setup`-
Scaffolds, aus dem dieses Repo ursprünglich erzeugt wurde (Python-
Projektgenerator, fachlich nicht Teil dieses Planungsprojekts). Sie
wurden dorthin verschoben, um den Repo-Root sauber zu halten, bleiben
aber per Git-Historie nachvollziehbar.
