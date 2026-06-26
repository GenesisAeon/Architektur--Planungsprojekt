# Analyse von `Planungsdiskurse/Zusammenfassung.pdf`

## Kontext

Johann legte `Planungsdiskurse/Zusammenfassung.pdf` direkt auf `main` ab:
ein ChatGPT-Deep-Research-Bericht, der das **oeffentliche GitHub-Repo per
Live-Browsing** untersucht hat (README.md, STATUS.md, ECOSYSTEM_MAP.yaml,
`00_Regeln/`, `02_Plaene/`, `03_Architektur/`), zusammen mit dem vollen
Rechercheaktivitaets-Trace. Johanns Frage: was davon bringt uns weiter,
und ist das ein gutes Beispiel dafuer, wie ein "leeres" Modell auf das
GenesisAeon-Konzept reagiert.

## Methodischer Unterschied zu vorherigen Multi-KI-Episoden

Im Unterschied zu Aeons direkten Chat-Antworten oder dem fruehren
sechs-KI-Diskurs-Transkript (`STATUS.md`, 2026-06-24) hatte dieses Modell
**echten, eigenstaendigen Tool-Zugriff** auf das rohe oeffentliche Repo
statt vorgefertigter Prosa — strukturell vergleichbar mit Pilotlauf 5 aus
`forschungsfrage-001-testprotokoll.md` (frischer Agent, echtes
Rohmaterial, kein vorab destillierter Text). Das macht es zu einem
echteren Testfall fuer "unabhaengige Reaktion" als die meisten
vorherigen Episoden.

## Verifizierte Befunde

| Behauptung | Befund | Pruefung |
|---|---|---|
| `03_Architektur/`-Ordnerinhalt | **korrekt** | `ls 03_Architektur/` stimmt exakt mit PDF-Beschreibung ueberein |
| `genesis-scope` noch offen, wartet auf Blindtest | **veraltet/falsch** | `01_Ideen/claude/genesis-scope-blindtest.*` existiert bereits, laut `STATUS.md` (2026-06-24) bereits mit negativem Ergebnis ("technisch lauffaehig, semantisch leer") durchgefuehrt |
| Mermaid-Diagramm: vollvermaschte Abhaengigkeiten (jedes Fundament-Modul → jedes Modul jeder Folgeebene) | **vermutlich fabriziert/ueberregularisiert** | `grep` gegen `ECOSYSTEM_MAP.yaml` zeigt selektive, spezifische `depends_on`-Listen (z.B. `medium-modulation`: genau 3 Abhaengigkeiten; `cosmic-moment`: genau 4) — keine uniforme Vollvermaschung |
| "Recovery Time"/"Orientation Layer Theory" als neue Beitraege | **keine unabhaengige Konvergenz** | `STATUS.md` Zeile 188 dokumentiert "Recovery Time" bereits unter genau diesem Titel (ChatGPT Deep-Research vom 2026-06-24). Das PDF zitiert selbst `STATUS.md`/`forschungsfrage-001-testprotokoll.md` als Quellen |
| `04_Programme/`, `05_Hilfsprogramme/`, `06_Sprachen/` als leere Platzhalter; `contracts/trylayer.schema.yaml`, `AGENTS.md`, `ENTRY.yaml` existieren | **korrekt** | jeweils nur `README.md` in den drei Ordnern; alle genannten Dateien existieren im Repo-Root |

## Antwort auf Johanns Framing-Frage

Es ist **kein** Beispiel fuer ein "leeres Modell", das eigenstaendig auf
das Konzept reagiert. Es ist ein Modell mit echtem Tool-Zugriff, das

- die Repo-Struktur groesstenteils korrekt wiedergibt,
- an einer Stelle einen veralteten Zwischenstand zitiert statt des
  aktuellen,
- an einer Stelle eine Grafik produziert, die plausibler aussieht als
  sie durch die Quelldaten gedeckt ist,
- und sein zentrales inhaltliches "Ergebnis" (Recovery Time) direkt aus
  unserem eigenen bereits publizierten `STATUS.md`/Ideen-Material zieht,
  statt es neu zu erfinden.

Das ist strukturell dasselbe **"Destillat statt Validierung"**-Muster,
das in diesem Repo schon mehrfach beobachtet wurde (Multi-Modell-Echo als
Warnsignal, nicht als Bestaetigung) — nur diesmal mit Tool-Zugriff statt
mit Chat-Antworten.

## Was uns tatsaechlich weiterbringt

1. Ein schwacher, aber echter Datenpunkt fuer Destillierbarkeit (vgl.
   `02_Plaene/destillierbarkeit-testprotokoll.md`): die dokumentierte
   Struktur (`03_Architektur/`, `contracts/`, `AGENTS.md`, `ENTRY.yaml`)
   ist fuer einen aussenstehenden, tool-gestuetzten Leser konsistent
   auffindbar — allerdings ohne die dort geforderte Kontrollgruppe und
   ohne Rohmaterial-Beschraenkung (das Modell hatte vollen
   README/STATUS-Zugriff, nicht nur reduzierte Rohdaten).
2. Konkreter Hinweis, bereits abgeschlossene Tests (wie
   `genesis-scope-blindtest`) deutlicher/aktueller in `STATUS.md` oder
   README erkennbar zu machen, da sonst auch externe Tools auf veraltete
   Zwischenstaende referenzieren.
3. Warnung: das vorgeschlagene Mermaid-Abhaengigkeitsdiagramm und die
   ADR-Skizze fuer ein `climate_thresholds`/ENSO-Plugin aus dem PDF
   sollten **nicht direkt uebernommen werden**, ohne sie gegen
   `ECOSYSTEM_MAP.yaml` zu pruefen — sie wirken plausibel, sind aber an
   mindestens einer Stelle nachweislich nicht datengetreu.

## Naechster Schritt

Keine automatische Uebernahme von PDF-Inhalten (Diagramm, ADR-Skizze) in
Architekturdokumente. Falls Johann das `climate_thresholds`-Plugin-Muster
oder die Recovery-Time-Metrik weiterverfolgen will, sollte das an die
bereits bestehenden Eintraege
`chatgpt-deepresearch-orientation-recovery-time-2026` und
`chatgpt-enso-eisschild-climate-thresholds-2026` anknuepfen, nicht an
dieses PDF als neue Quelle.
