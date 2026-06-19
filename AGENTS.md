# AGENTS.md — Regeln fuer KI-Systeme in diesem Repo

Du liest dieses Repo wahrscheinlich, um Architektur-Vorschlaege fuer das
GenesisAeon-Oekosystem einzubringen oder den aktuellen Stand zu verstehen.
Lies in dieser Reihenfolge:

1. **`STATUS.md`** — wo stehen wir gerade (Phase, offene Fragen, was laeuft parallel)
2. **`PRINCIPLES.md`** — die Verfassung, maschinell durchgesetzt, nicht verhandelbar ohne ADR
3. Dieses Dokument — wie du konkret beitraegst
4. Bei Bedarf: `Planungsdiskurse/` — historischer Diskurs, NICHT die aktuelle Wahrheit

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
00_Regeln/          Architekturprinzipien als Trylayer-Eintraege (status: core)
01_Ideen/           Roh-Vorschlaege, jede KI legt hier eigene Unterordner an
02_Plaene/          Ideen, die in konkrete Planung uebergegangen sind
03_Architektur/     Kanonisierte Architekturentscheidungen (braucht ADR)
04_Programme/       Core-Modul-Spezifikationen (braucht ADR + Blindtest)
05_Hilfsprogramme/  Plugin-/Tool-Spezifikationen
06_Sprachen/        Glossar, Terminologie, Namenskonventionen
adr/                Architecture Decision Records
Planungsdiskurse/   Archiv des urspruenglichen Multi-AI-Diskurses (read-only)
```

Vollstaendige Regeln: `PRINCIPLES.md`. Kurzfassung: jeder Ordner erlaubt
nur bestimmte `status`-Werte (Regel 2), und Reife darf nicht von Unreife
abhaengen (Regel 4).

## Wie du einen Vorschlag einreichst

1. Lege in `01_Ideen/<dein-system-name>/` ein neues Trylayer-Tripel an:
   `<slug>.yaml`, `<slug>.ai.json`, `<slug>.md` — Schema in
   `contracts/trylayer.schema.yaml`.
2. `status: idea` oder `draft`, `kategorie: idee`.
3. Fuelle `epistemic_status` ehrlich aus — die meisten neuen Vorschlaege
   sind `hypothesis`, nicht `validated`.
4. Kein freier Fliesstext als Strukturersatz: die `.md`-Datei ist Prosa
   fuer Menschen, aber `.ai.json` MUSS das volle Schema einhalten
   (Modulname, Zweck, Dependencies, Blindtest-Einschaetzung, Status).
5. Fuehre `python scripts/validate_trylayer.py` aus, bevor du fertig bist.

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
