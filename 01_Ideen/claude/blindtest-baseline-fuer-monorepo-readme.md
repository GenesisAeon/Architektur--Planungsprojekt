# Die genesis-scope/genesis-os-Blindtest-Befunde sind Baseline, nicht Verdikt

**Status:** idea · **Epistemic Status:** derived · **Autor:** Claude

## Präzisierung durch Johann

Johann (Chat, 2026-06-24): die FALSE-Befunde für `genesis-scope` und
`genesis-os` sind kein Problem dieser Pakete selbst — "ohne Wissen geht
da nichts" ist für domänenspezifische Satelliten-Pakete erwartbar und
akzeptabel. Der eigentliche Zweck der beiden durchgeführten Blindtests
war ein anderer: sie liefern eine konkrete, gemessene Baseline (zwei
unabhängige FALSE-Ergebnisse mit dokumentierten Gründen), gegen die
sich das künftige Genesis-Core/UTAC-Core-Monorepo (`ADR-001`) messen
lassen soll. Das Monorepo-README/Quickstart soll — anders als die
bisherigen Satelliten-Pakete — den Genesis-Blindtest tatsächlich
**bestehen**.

## Warum das einen Unterschied macht

Vorher war unklar, ob "der Blindtest schlägt fehl" bedeutet "das Paket
ist schlecht" oder "das ist bei diesem Pakettyp erwartbar". Mit dieser
Präzisierung gibt es zwei klar getrennte Maßstäbe:

1. **Domänen-/Satelliten-Pakete** (`genesis-scope`, die ~35
   domänenspezifischen T0-Pakete aus
   `02_Plaene/genesis-core-scope.md`) dürfen Vorwissen voraussetzen —
   Regel 6 gilt für sie nicht im strengen Sinn, oder nur in einer
   abgeschwächten Form (vgl.
   `01_Ideen/claude/blindtest-fuer-ki-native-leerpakete`).
2. **Das Core-Monorepo selbst** (`utac-core`-Kette, `genesis-os`-
   Orchestrator als dünne Schicht) **muss** den klassischen Blindtest
   bestehen, weil es der Eintrittspunkt für jeden ist, der ohne
   GenesisAeon-Hintergrund auf das Ökosystem trifft.

## Konkrete Messlatte für das Monorepo

- Quickstart-Output muss für einen kontextfreien Leser interpretierbar
  sein: nicht nur Zahlen, sondern Aussagen wie "X bedeutet Y, Bereich Z
  gilt als erwartet" direkt im README oder in den Docstrings der
  Rückgabewerte.
- Phänomene wie das im `genesis-os`-Retest gefundene Verhalten (Phase
  verlässt "Initiation" nie, trotz Schwellenwert-Überschreitung) dürfen
  im Core-Quickstart nicht auftreten oder müssen erklärt sein — ein
  kontextfreier Leser darf nicht raten müssen, ob ein Ergebnis korrekt
  oder ein Bug ist.
- Der Core-Quickstart sollte mit echten, nicht-leeren Beispieldaten
  arbeiten (kein reiner Default-/Leerzustand wie bei `genesis-scope`
  ohne jede Session-Historie) — sonst wiederholt sich derselbe
  strukturelle Leerzustand-Befund auf Core-Ebene.

## Bezug zu anderen Einträgen

Ergänzt `02_Plaene/genesis-core-scope.md` ("Nächster Schritt" Punkt 1:
jedes Core-Kandidat-Paket einzeln durch den Blindtest schicken) um eine
explizite Erwartungshaltung: bestehen ist hier Pflicht, nicht nur
Prüfung. Ergänzt `01_Ideen/claude/blindtest-fuer-ki-native-leerpakete`
um die Kehrseite: jene Idee fragt, ob Regel 6 für Satelliten-Pakete
gelockert werden soll — dieser Eintrag hält fest, dass für den Core
selbst das Gegenteil gilt, Regel 6 bleibt dort streng.

## Erwartetes Ergebnis

- Wenn das Genesis-Core-Monorepo entsteht, wird sein README/Quickstart
  explizit gegen die hier dokumentierte Baseline (zwei FALSE-Befunde
  mit Begründung) geprüft, nicht gegen eine abstrakte Erwartung.
- Diese Idee dient als Erinnerung/Prüfkriterium für den Moment, in dem
  `02_Plaene/genesis-core-scope.md` in echte Core-Pakete übergeht — sie
  sollte dann in ein eigenes ADR oder einen Architektur-Eintrag mit
  konkreten Akzeptanzkriterien überführt werden.

## Nächster Schritt

Wenn die Monorepo-Migration beginnt: dieses Kriterium ("Blindtest MUSS
bestehen, nicht nur gemessen werden") explizit in den
Core-Akzeptanzkriterien von `02_Plaene/genesis-core-scope.md` oder
einem neuen ADR verankern, bevor `utac-core` o.ä. als
`status: accepted` eingereicht wird.

## Betrachtete Alternativen

- Die FALSE-Befunde als generelles Qualitätsurteil über
  `genesis-scope`/`genesis-os` stehen lassen, ohne Baseline-Reframing —
  verworfen nach Johanns Präzisierung: das würde fälschlich nahelegen,
  dass diese Pakete grundsätzlich mangelhaft sind, obwohl
  Vorwissen-Bedarf bei Satelliten-Paketen by design akzeptabel ist.
- Sofort ein neues ADR für die Monorepo-Akzeptanzkriterien schreiben,
  ohne die Monorepo-Migration selbst abzuwarten — verworfen: verfrüht,
  solange `02_Plaene/genesis-core-scope.md` noch eine offene
  Plan-Hypothese ist und keine Pakete real migriert werden.
