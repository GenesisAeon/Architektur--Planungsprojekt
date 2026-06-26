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
| `genesis-scope` noch offen, wartet auf Blindtest | **praeziser als urspruenglich bewertet** | bestehender Blindtest testete nur den jetzigen unbefuellten Skelett-Zustand; ein Test mit echten semantischen Pfaden/Karten steht noch aus (haengt wie `genesis-os` am v1.0.0-PyPI-Sprint) — Johanns Praezisierung: "relativ getestet" |
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

## Navigierbarkeit als eigene Achse, getrennt von Inhaltsvalidierung (Nachtrag, Johanns Praezisierung)

Johann weist auf einen Punkt hin, der in der obigen Analyse zu kurz kam:
die Frage "liefert das Modell neue/korrekte Inhalte?" (oben beantwortet
mit "nein, Destillat statt Validierung") ist nicht dieselbe Frage wie
"konnte sich das Modell im Repo *orientieren*, ohne sich zu verlaufen
oder zu konfabulieren?" — und letzteres ist ein eigenstaendiger,
positiver Befund.

Johanns Beobachtung aus anderen Deep-Research-Durchlaeufen: bei Repos
mit diffusem/schlecht organisiertem Inhalt haben Modelle teilweise
**andere/falsche Repos gelesen** oder Inhalte halluziniert, weil die
Orientierung selbst fehlschlug. Im Vergleich dazu hat das Modell hier:

- das richtige Repo durchgaengig korrekt identifiziert und referenziert,
- die tatsaechliche Ordnerstruktur (`03_Architektur/`, `contracts/`,
  `AGENTS.md`, `ENTRY.yaml`) fehlerfrei gefunden und wiedergegeben,
- seine Quellen explizit benannt und auf echte Dateien (`STATUS.md`,
  `ECOSYSTEM_MAP.yaml`) zurueckgefuehrt, statt frei zu erfinden, woher
  die Information kommt.

Die beiden inhaltlichen Fehler (veralteter genesis-scope-Stand,
vermutlich fabriziertes Abhaengigkeitsdiagramm) sind **inhaltliche**
Fehler, keine **navigatorische** Fehlleitung — das Modell hat sich nicht
im falschen Repo oder in der falschen Datei verirrt, es hat im richtigen
Repo an einer Stelle einen ueberholten Zwischenstand zitiert bzw. ein zu
glattes Diagramm erzeugt. Das ist ein qualitativ anderer Fehlertyp als
Halluzination durch fehlende Orientierung.

**Praezisierung zu genesis-scope:** Das war kein "veraltet/falsch" im
Sinne eines Fehlers, sondern trifft den tatsaechlich offenen Punkt
praeziser, als ich es im urspruenglichen Befund dargestellt habe. Der
bestehende Blindtest (`genesis-scope-blindtest.md`) hat explizit nur den
**jetzigen, unbefuellten Skelett-Zustand** getestet ("FALSE... in der
jetzigen, unbefuellten Form"). Ein erneuter Test mit echten semantischen
Pfaden/Karten/Sigillin-Ankern steht noch aus, weil diese Inhalte —
analog zu `genesis-os` — von den v1.0.0-PyPI-Paketen abhaengen, die der
laufende Sprint gerade blockiert. "Relativ getestet" (Johanns
Formulierung) trifft den Zustand besser als mein urspruengliches
"veraltet/falsch": der bisherige Test bleibt fuer den Skelett-Zustand
gueltig, sagt aber nichts ueber den noch nicht existierenden befuellten
Zustand aus. Das PDF, das genesis-scope als "wartet noch auf
Evaluation" beschreibt, liegt damit naeher an der Wahrheit, als mein
erster Befund nahelegte.

**Fazit dieses Nachtrags:** Zwei getrennte, beide gueltige
Beobachtungsachsen zu diesem PDF — (1) gute Navigierbarkeit/Orientierung
und niedrige Konfabulationsneigung als reales, positives Signal fuer die
Struktur dieses Repos im Kontrast zu diffuseren Repos, UND (2) die
inhaltlichen Aussagen des Berichts (Diagramm, Recovery-Time-"Neuheit")
bleiben unabhaengig davon nicht ungeprueft uebernehmbar. Keine der beiden
Achsen hebt die andere auf.

## Naechster Schritt

Keine automatische Uebernahme von PDF-Inhalten (Diagramm, ADR-Skizze) in
Architekturdokumente. Falls Johann das `climate_thresholds`-Plugin-Muster
oder die Recovery-Time-Metrik weiterverfolgen will, sollte das an die
bereits bestehenden Eintraege
`chatgpt-deepresearch-orientation-recovery-time-2026` und
`chatgpt-enso-eisschild-climate-thresholds-2026` anknuepfen, nicht an
dieses PDF als neue Quelle.
