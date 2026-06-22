# Architekturprinzipien (Verfassung)

Dieses Dokument ist die einzige Quelle der Wahrheit fuer die Regeln dieses
Repos. Jede Aenderung an diesen Prinzipien braucht ein eigenes ADR
(`adr/`). Diese Regeln sind kein Stilvorschlag, sondern werden durch
`scripts/validate_trylayer.py` maschinell durchgesetzt (CI + pre-commit).

Diese Regeln definieren *wie* Beitraege aufgenommen werden. *Was*
aufgenommen wird, entscheidet zusaetzlich das Mission-Statement in
`adr/adr-002-mission-statement-v1.md` (Regel 8 angewendet): jeder Beitrag
muss erkennbar semantische Karten, Pfade oder Kontextstrukturen fuer
Agenten erzeugen, pflegen oder bereitstellen helfen.

## Regel 1 — Trylayer-Pflicht

Jede Wissenseinheit (Idee, Plan, Architekturentscheidung, Programm-,
Hilfsprogramm- oder Begriffsdefinition) existiert ausschliesslich als
Dreifach-Datei mit identischem Slug:

```
<slug>.yaml       Index/Metadaten (siehe contracts/trylayer.schema.yaml)
<slug>.ai.json     AI-Vollversion (Metadaten + vollstaendiger struktur. Inhalt)
<slug>.md          Menschenversion (Prosa, Begruendung, Kontext)
```

Ein unvollstaendiges Tripel ist ungueltig. Es gibt keine Ausnahme.

## Regel 2 — Ordner bestimmt erlaubten Status

Jeder Ordner akzeptiert nur Einträge mit bestimmtem `status`:

| Ordner               | kategorie       | erlaubter status              |
|----------------------|-----------------|--------------------------------|
| `00_Regeln/`         | regel           | `core` (nur via ADR aenderbar) |
| `01_Ideen/`          | idee            | `idea`, `draft`                |
| `02_Plaene/`         | plan            | `draft`, `review`               |
| `03_Architektur/`    | architektur     | `accepted`, `core`             |
| `04_Programme/`      | programm        | `accepted`, `core`             |
| `05_Hilfsprogramme/` | hilfsprogramm   | `accepted`, `core`             |
| `06_Sprachen/`       | sprache         | `accepted`, `core`             |
| `adr/`               | adr             | `accepted`                      |

Ein Eintrag, dessen Status nicht zum Ordner passt, ist ungueltig. Eine
Idee, die reift, wird nicht editiert — sie wird in den naechsten Ordner
**verschoben** (neuer Pfad = neue Entscheidung, sichtbar im Diff).

## Regel 3 — Kein Core ohne ADR

`kategorie` in `architektur`, `programm`, `hilfsprogramm` mit
`status` in `accepted` oder `core` MUSS ein nicht-leeres `related_adr`
Feld haben. Eine Architekturentscheidung ohne dokumentierte Begruendung
existiert nicht.

ADR-Eintraege selbst tragen wie jeder Trylayer-Eintrag einen normalen
lowercase-`id`-Slug (z.B. `adr-001-warum-monorepo`), zusaetzlich aber ein
Pflichtfeld `adr_number` (`ADR-001`), ueber das andere Eintraege per
`related_adr` referenzieren. Die beiden Felder kollidieren bewusst nicht
im selben Pattern.

## Regel 4 — Reife darf nicht von Unreife abhaengen

Status-Rang: `idea`=0 < `draft`=1 < `review`=2 < `accepted`=3 < `core`=4.

Diese Regel gilt **nur** fuer `kategorie` in `architektur`, `programm`,
`hilfsprogramm`: jeder Eintrag in `depends_on` muss dort einen Rang >=
dem eigenen Rang haben. Ein `accepted`-Modul darf nicht heimlich von
einer `idea` abhaengen. Wenn eine Architektur eine Idee braucht, muss die
Idee zuerst selbst durch die Kette Idee -> Plan -> Architektur (mit ADR)
reifen.

Fuer `idee` und `plan` gilt diese Pruefung bewusst NICHT — ein Plan baut
per Definition auf Ideen auf, die noch nicht reif sind. Dafuer gibt es das
separate Feld `derived_from`: reine Herkunfts-Referenz ohne Rang-Zwang,
um zu dokumentieren, aus welchen Ideen ein Plan synthetisiert wurde.

## Regel 5 — Epistemic Status ist Pflicht

Jeder Eintrag deklariert `epistemic_status`:
`validated | measured | derived | hypothesis | speculative`.
Kein Eintrag darf als selbstverstaendlich wahr erscheinen, ohne zu sagen,
auf welcher Erkenntnisstufe er steht.

## Regel 6 — Genesis-Blindtest vor `accepted`

Bevor ein Eintrag in `kategorie` `architektur` oder `programm` von
`review` zu `accepted` wechselt, muss der Blindtest beantwortet sein:

> Kann eine Person ohne jeden GenesisAeon-Kontext den Quickstart der
> README folgen und innerhalb von 5 Minuten ein sinnvolles, korrektes
> Ergebnis sehen — ohne die Genesis-/Unified-Mandala-Geschichte zu kennen?

Ergebnis wird im Feld `blindtest_passed` (true/false) dokumentiert.
`false` oder `null` blockiert den Wechsel zu `accepted`.

## Regel 7 — Core funktioniert ohne LLM und ohne Internet

`kategorie: programm` mit `status: core` darf keine Laufzeitabhaengigkeit
zu einem LLM oder einer Netzwerkverbindung haben. KI-gestuetzte Features
sind immer Plugin (`hilfsprogramm`), nie Core.

## Regel 8 — Keine privilegierte Domaene

Kein Modul bekommt Sonderrechte im Core, weil es historisch wichtig war.
Aufnahme entscheidet ausschliesslich ueber Regel 3, 4 und 6 — nicht ueber
Herkunft oder Begeisterung.

## Regel 9 — Unified-Mandala ist Quelle, nicht Ziel

Dieses Repo zitiert und destilliert aus Unified-Mandala, kopiert es aber
nicht. Inhalte, die nur mit Kenntnis der Genesis-Erzaehlung Sinn ergeben,
bleiben in `01_Ideen/` oder wandern nach `archive/` (Regel 11) — sie
werden nicht `accepted`.

## Regel 10 — Validierung ist nicht optional

`scripts/validate_trylayer.py` laeuft als pre-commit-Hook und in CI.
Ein Commit, der Regel 1-7 verletzt, wird zurueckgewiesen.

## Regel 11 — Verwerfen ist kein Loeschen

`archive/` nimmt Eintraege jeder `kategorie` mit `status: deprecated` oder
`archived` auf. Die urspruengliche `kategorie` bleibt erhalten (ein
verworfener Architektur-Vorschlag bleibt `kategorie: architektur`, nur
sein `status` aendert sich). Das beendet die Diskussion "Gehoert das in
den Core?" ohne den Inhalt zu zerstoeren — Unified-Mandala bleibt die
vollstaendige Historie, `archive/` ist der kuratierte Zwischenstand
innerhalb dieses Repos.

## Regel 12 — Es gibt genau einen Standardweg ins Repo

`ENTRY.yaml` ist der einzige verbindliche Einstiegspunkt. Jede KI (und
jeder Mensch), die/der zum ersten Mal mit diesem Repo arbeitet, folgt der
darin definierten Reihenfolge (`README.md` -> `STATUS.md` ->
`PRINCIPLES.md` -> `AGENTS.md` -> optional `00_Regeln/` und
`Planungsdiskurse/`) — unabhaengig davon, bei welcher Datei sie/er zuerst
gelandet ist. Jede Einstiegsdatei (`README.md`, `AGENTS.md`, `STATUS.md`)
verweist deshalb selbst zuerst auf `ENTRY.yaml`, statt sich auf einen
einzigen "richtigen" Lesepfad zu verlassen, den man zufaellig kennen
muss. `scripts/validate_trylayer.py` prueft, dass alle in `ENTRY.yaml`
referenzierten Dateien/Ordner tatsaechlich existieren.
