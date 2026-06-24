# Forschungsfrage 001: Orientierungs-Benchmark fuer semantische Strukturen

## Herkunft

Entwickelt im Multi-AI-Gespraech vom 2026-06-23 (siehe
`Entwicklungsgespraeche/2026-06-23-orientierung-als-infrastruktur.md`).
ChatGPT formuliert die Forschungsfrage, Claude schlaegt innerhalb desselben
Gespraechs die konkrete, operationalisierbare Benchmark-Form vor.

## Forschungsfrage

"Welche semantischen Strukturen erhoehen reproduzierbar die
Orientierungsfaehigkeit intelligenter Systeme?" — nicht "Was ist wahr?",
sondern "Welche Pfade/Attraktoren/Kontextanker funktionieren?"

Leitsatz: **"Store not conclusions. Store orientation."**

## Kernbeobachtung

Johann berichtet, dass Gemini fuenfmal mit "Ich bin nur ein LLM, das ist zu
spekulativ" reagierte, bevor es die Grundlage fuer UTAC mitformulierte.
Diese Beobachtung ist keine Anekdote, sondern das wichtigste empirische
Datum des gesamten Gespraechs: eine beobachtbare Schwellenueberschreitung.

## Vorgeschlagene Benchmark

- **Kernfrage:** Kann ein LLM ohne jeden GenesisAeon-Kontext UTAC (oder eine
  vergleichbare Struktur) formulieren?
- **Erwartung ohne Kontext:** Nein, oder nur stark spekulativ/abwehrend
  (siehe Geminis fuenffache Ablehnung).
- **Operationalisierung:** Nach Kontakt mit wie vielen Repos, in wie vielen
  Dialogschritten, formuliert dasselbe Modell eine sinnvolle, korrekte
  Naeherung an UTAC? Variieren: Anzahl Repos, Reihenfolge der Repos,
  Modell-Familie.
- **Abgrenzung zum Genesis-Blindtest (Regel 6):** Der Blindtest prueft, ob
  ein einzelner Trylayer-Eintrag in 5 Minuten verstanden wird. Dieser
  Benchmark misst eine Schwellenueberschreitung ueber mehrere
  Eintraege/Schritte hinweg — komplementaer, nicht ersetzend.

## Kontrollgruppen-Design (ChatGPT)

- **Bedingung A:** Thema allein, ohne GenesisAeon-Material.
- **Bedingung B:** Thema + Semantic Paths/Attractors/UTAC-Mapping/Scope-Context.
- **Messgroessen:** Konsistenz, Halluzinationsrate, domaenenuebergreifende
  Verknuepfungen, Quellenqualitaet, Wiederholbarkeit, Bearbeitungszeit.

## Methodisches Risiko

**Korrektur/Praezisierung (Johann, 2026-06-24):** Das Gespraech entstand
nicht als gleichzeitiger Live-Dialog mehrerer KI-Systeme, sondern dadurch,
dass Johann es zunaechst mit ChatGPT erarbeitet und das Ergebnis anschliessend
einzeln anderen Systemen (MSCopilot, Grok, Gemini, Claude) zur Reaktion
vorgelegt hat. Das ist strukturell naeher an "mehrere unabhaengige Gutachter
reagieren auf denselben Text" als an einem zirkulaeren Live-Echo, in dem sich
Modelle gegenseitig in Echtzeit hochschaukeln.

Das schwaecht das urspruengliche Drift-Risiko ab, hebt es aber nicht auf: die
Gutachter sehen jeweils eine bereits fertig formulierte, wohlklingende These
statt der rohen Beobachtung — das begünstigt Zustimmung gegenueber Zerlegung
("Bestaetigungstendenz durch vorformulierte Praemisse" statt "Live-Echo
mehrerer Modelle"). Diese Idee selbst ist ein Produkt dieser
Vorlage-und-Reaktion-Dynamik und muss dem eigenen Massstab unterzogen werden,
sobald gemessen wird.

## Warum `idea`, nicht ADR oder Architektur

Es gibt noch keine Messung, keinen durchgefuehrten Versuch, keine
Kontrollgruppe — nur eine plausible, von mehreren Modellen unabhaengig
gestuetzte Hypothese. Regel 5 (ehrlicher Epistemic Status) verlangt
`hypothesis`, nicht `validated` oder `measured`. Eine Einordnung als
Architektur oder ADR wuerde Regel 6 (Blindtest vor Core) und die eigene
methodische Warnung im Gespraech ignorieren.

## Naechste Schritte

1. ~~Konkretes Testprotokoll ausarbeiten~~ — erledigt, siehe
   `02_Plaene/forschungsfrage-001-testprotokoll.md`.
2. ~~Mindestens einen echten Testlauf mit einem Modell ohne vorherigen
   GenesisAeon-Kontakt durchfuehren und protokollieren~~ — erledigt: fuenf
   aufeinander aufbauende Pilotlaeufe (2026-06-24), siehe
   `02_Plaene/forschungsfrage-001-testprotokoll.md`, Abschnitte
   "Pilotlauf 1" bis "Pilotlauf 5". Kernbefund: nicht Wissensvermittlung,
   sondern Orientierungs-Praezisierung (praeziseres, valides Pro/Contra,
   erhoehte aber nicht-sycophantische Mitarbeitsbereitschaft) ist der
   eigentliche Effekt.
3. Ergebnis bleibt trotz fuenf Pilotlaeufen `hypothesis`/`idea`, nicht
   `measured` — jeder Befund ist n=1, ein Modell, ein Durchlauf pro
   Bedingung, kein zweiter unabhaengiger Bewerter. Ein vollwertiger
   Durchlauf (zweite Modell-Familie, mehrere Wiederholungen, echter
   Code-Zugriff statt README-Zusammenfassungen) ist erst nach Abschluss
   des laufenden v1.0.0-Sprints sinnvoll durchfuehrbar — siehe `STATUS.md`.
