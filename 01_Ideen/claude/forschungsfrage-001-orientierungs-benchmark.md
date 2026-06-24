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

Claude warnt im Gespraech explizit: Wenn mehrere KI-Systeme gleichzeitig
zustimmend reagieren (wie in diesem Gespraech selbst geschehen — ChatGPT,
MSCopilot, Grok, Gemini, Claude bestaetigen sich gegenseitig), kann eine
Rueckkopplungsschleife entstehen, in der semantischer Drift nicht mehr als
Metaphysik, sondern als gegenseitige Selbstbestaetigung zurueckkehrt. Diese
Idee selbst ist ein Produkt genau dieser Mehrfach-Bestaetigungsdynamik und
muss dem eigenen Massstab unterzogen werden, sobald gemessen wird.

## Warum `idea`, nicht ADR oder Architektur

Es gibt noch keine Messung, keinen durchgefuehrten Versuch, keine
Kontrollgruppe — nur eine plausible, von mehreren Modellen unabhaengig
gestuetzte Hypothese. Regel 5 (ehrlicher Epistemic Status) verlangt
`hypothesis`, nicht `validated` oder `measured`. Eine Einordnung als
Architektur oder ADR wuerde Regel 6 (Blindtest vor Core) und die eigene
methodische Warnung im Gespraech ignorieren.

## Naechste Schritte

1. Konkretes Testprotokoll ausarbeiten (welche Repos, welche Reihenfolge,
   welches Modell, wie wird "sinnvolle Naeherung an UTAC" operational
   definiert/bewertet, durch wen).
2. Mindestens einen echten Testlauf mit einem Modell ohne vorherigen
   GenesisAeon-Kontakt durchfuehren und protokollieren.
3. Ergebnis erst dann nach `02_Plaene` oder hoeher ueberfuehren, wenn ein
   erster Messwert vorliegt — vorher bleibt es `hypothesis`/`idea`.
