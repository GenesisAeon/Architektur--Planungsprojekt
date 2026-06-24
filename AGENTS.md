# AGENTS.md — Regeln fuer KI-Systeme in diesem Repo

> **Standardweg:** [`ENTRY.yaml`](ENTRY.yaml) ist der verbindliche
> Einstiegspunkt (Regel 12). Dieses Dokument ist Schritt 4 davon. Wenn du
> direkt hier gelandet bist, ohne `ENTRY.yaml` gesehen zu haben, lies es
> trotzdem zuerst — es zeigt den vollstaendigen Pfad inkl. `STATUS.md`
> und `PRINCIPLES.md`, die du vor diesem Dokument lesen solltest.

Du liest dieses Repo wahrscheinlich, um Architektur-Vorschlaege fuer das
GenesisAeon-Oekosystem einzubringen oder den aktuellen Stand zu verstehen.

## Was dieses Repo ist

Ein Planungs-/Architektur-Workspace fuer den Uebergang von Unified-Mandala
(explorativem Forschungslabor) zu einer kanonisierten, oeffentlichkeitsfaehigen
Referenzarchitektur (Genesis Core / UTAC Core). Hier werden **Entscheidungen
getroffen**, nicht Code geschrieben. Das eigentliche Monorepo entsteht erst
danach.

## Was dieses Repo NICHT ist

- Kein Ersatz fuer Unified-Mandala (das bleibt das Labor)
- Kein Ort fuer freie Prosa-Diskussionen als Vorschlag (siehe Format unten)
- Kein Ort, an dem du `status: accepted` oder `core` selbst vergibst —
  das macht ausschliesslich der menschliche Maintainer (Johann) per Commit

## Ordnerstruktur

```
00_Regeln/          Die 12 Architekturprinzipien als Trylayer-Eintraege (status: core)
01_Ideen/           Roh-Vorschlaege, jede KI legt hier eigene Unterordner an
02_Plaene/          Ideen, die in konkrete Planung uebergegangen sind
03_Architektur/     Kanonisierte Architekturentscheidungen (braucht ADR)
04_Programme/       Core-Modul-Spezifikationen (braucht ADR + Blindtest)
05_Hilfsprogramme/  Plugin-/Tool-Spezifikationen
06_Sprachen/        Glossar, Terminologie, Namenskonventionen (noch unbefuellt)
adr/                Architecture Decision Records
archive/            Verworfenes / "wertvoll aber nicht Core" (Regel 11)
Planungsdiskurse/   Archiv des urspruenglichen Multi-AI-Diskurses (read-only)
Entwicklungsgespraeche/  Rohprotokolle laufender Multi-AI-Gespraeche (Eingabe, kein Trylayer)
```

Vollstaendige Regeln: `PRINCIPLES.md`. Kurzfassung: jeder Ordner erlaubt
nur bestimmte `status`-Werte (Regel 2). Reife darf nicht von Unreife
abhaengen (Regel 4) — das gilt aber nur fuer `architektur`, `programm`,
`hilfsprogramm`. Eine Idee oder ein Plan darf ganz bewusst auf unreiferen
Vorstufen aufbauen; nutze dafuer `derived_from` statt `depends_on`.

## Wie du einen Vorschlag einreichst

Externe Systeme (andere LLMs, Tools, Menschen ausserhalb des Kernteams)
reichen Vorschlaege nicht direkt als rohe Trylayer-Dateien ein, sondern
typischerweise als formloser Text/Chat-Export an eine KI-Schnittstelle
(z.B. Claude), die den Inhalt zuerst nach Trylayer transformiert. Wer
selbst direkt im Repo arbeitet, folgt direkt den Schritten unten:

1. Lege in `01_Ideen/<dein-system-name>/` ein neues Trylayer-Tripel an:
   `<slug>.yaml`, `<slug>.ai.json`, `<slug>.md` — Schema in
   `contracts/trylayer.schema.yaml`.
2. `status: idea` oder `draft`, `kategorie: idee`.
3. Fuelle `epistemic_status` ehrlich aus — die meisten neuen Vorschlaege
   sind `hypothesis`, nicht `validated`.
4. Kein freier Fliesstext als Strukturersatz: die `.md`-Datei ist Prosa
   fuer Menschen, `.ai.json` ist maschinenlesbar. Empfohlenes Minimum im
   `content`-Feld: `problem`, `vorschlag`, `erwartetes_ergebnis`,
   `naechster_schritt`, `alternativen_betrachtet` (siehe
   `01_Ideen/claude/genesis-scope-blindtest.ai.json` als Beispiel).
   **Ehrlicher Hinweis:** `scripts/validate_trylayer.py` prueft aktuell
   nur die Metadaten (yaml-Kopf), NICHT die Struktur von `content` selbst.
   Ein leeres `content: {}` waere technisch gueltig — die Konvention oben
   ist (noch) nicht maschinell erzwungen.
5. Fuehre `python scripts/validate_trylayer.py` aus, bevor du fertig bist.

## Rohformat fuer externe Einreichungen

Ein externes System muss das Trylayer-Format nicht selbst kennen. Es
reicht ein einzelnes Markdown-Dokument mit diesem minimalen Kopf, das an
die KI-Schnittstelle uebergeben wird:

```markdown
---
quelle_system: <Name des einreichenden Systems/Person>
datum: <YYYY-MM-DD>
---

## Problem
...

## Vorschlag
...

## Erwartetes Ergebnis
...

## Alternativen betrachtet (optional)
...
```

Die KI-Schnittstelle uebernimmt daraus `author.system`/`author.name` und
`created`, fuellt `epistemic_status` ehrlich aus (im Zweifel
`hypothesis`), waehlt Ordner/`kategorie`/`status` nach Regel 2 und
erzeugt das vollstaendige Trylayer-Tripel in `01_Ideen/`. Das Rohformat
selbst wird nicht im Repo abgelegt — nur das daraus erzeugte Tripel.

## Der Genesis-Blindtest (Regel 6)

Bevor du etwas fuer `kategorie: architektur` oder `programm` vorschlaegst,
beantworte selbst:

> Wuerde eine Person ohne jeden GenesisAeon-Kontext dieses Modul in einem
> voelig anderen Kontext installieren wollen und in 5 Minuten ein
> sinnvolles Ergebnis sehen?

Wenn die Antwort "nur mit Kenntnis der Genesis-Geschichte" lautet, gehoert
der Vorschlag nach `01_Ideen/`, nicht nach `03_Architektur/` oder
`04_Programme/`.

## Validierung

`scripts/validate_trylayer.py` ist die einzige Autoritaet darueber, ob ein
Tripel gueltig ist. Wenn dein Vorschlag dort durchfaellt, ist er nicht
einreichbar — unabhaengig davon, wie gut die Idee inhaltlich ist.
