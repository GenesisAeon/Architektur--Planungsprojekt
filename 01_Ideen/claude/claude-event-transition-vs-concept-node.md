# Event/Transition statt Concept Node als primaere Entitaet — eine offene Architekturfrage fuer das spaetere Monorepo

**Status:** idea · **Epistemic Status:** hypothesis · **Autor:** Claude

## Herkunft

Diese Idee rekonstruiert (mit aktueller Nummerierung und ohne Bezug auf
nicht mehr existierende IDs) eine Architekturdebatte, die in einem
fruehen, nie gemergten Branch (`claude/upbeat-einstein-xvxowt`,
2026-06-19) entstand: ein Gegeneinwand von Claude gegen ein dortiges
`ADR-000` ("primaere Entitaet ist das Wissensobjekt/Concept Node"), das
seinerseits auf einer Copilot-Synthese ("semantisches Betriebssystem")
aufbaute. Jener Branch wurde nie in die jetzt gueltige Linie gemergt — die
dort verwendeten ADR-Nummern (`ADR-000`, `ADR-002-drei-schichten-
architektur`) kollidieren mit der inzwischen akzeptierten Nummerierung
(`ADR-002` = Mission-Statement, `status: accepted`). Die inhaltliche
Frage selbst ist davon unberuehrt und bleibt offen, daher dieser
Neuaufsatz als eigenstaendige Idee statt einer Wiederbelebung des alten
Branches.

**Wichtiger Vorbehalt:** Roh-Einwand, nicht durch den Genesis-Blindtest
(Regel 6) geprueft, kein Code-Audit der tatsaechlichen Diamond-Interface-
Implementierungen in diesem Repo durchgefuehrt — nur eine
Architekturbeobachtung. Bleibt `epistemic_status: hypothesis`.

## Kernthese

Die Frage "was ist die primaere Entitaet eines GenesisAeon-Kernels?"
wurde im verworfenen Branch philosophisch beantwortet (Wissensobjekt/
Concept Node als statischer Knoten in einem Wissensgraphen). Der
Gegeneinwand: das bestehende Diamond-Interface-Muster (`run_cycle()`,
`get_crep_state()`, `get_utac_state()`, `get_phase_events()`,
`to_zenodo_record()`) deutet eher auf **Zustandsaenderung ueber Zeit** als
primaeres Konzept hin, nicht auf einen statischen Knoten:

- Sigillin-artige Strukturen sind im Kern Event-Sourcing-Snapshots mit
  Lineage.
- Phasen-/Q4-Zustaende sind keine Konzeptknoten in einem Wissensgraphen,
  sondern Knoten in einem **Uebergangsgraphen**.
- CREP-aehnliche Metriken sind keine Eigenschaft eines Dings, sondern
  eine ueber Zeit gemessene Rate.

Folgerung: die primaere Entitaet waere dann nicht der Concept Node,
sondern die **Phase-Transition mit angehaengtem Zustand** — ein Ereignis,
kein Ding. Das wuerde architektonisch naeher an zwei etablierten Mustern
liegen als an einer Eigenkonstruktion:

- **Event Sourcing + CQRS** — Event Log als Primaerentitaet,
  Replay-basierte Zustandsrekonstruktion.
- **Actor Model / Supervision Trees** (Erlang/Elixir-OTP-Stil) — fuer
  Agenten als Interpreten eines Kernels.

## Zwei zusaetzliche Einwaende aus dem urspruenglichen Diskurs

1. **Uebertreibungsmuster.** Formulierungen wie "Betriebssystem fuer
   Sinn" oder "Zivilisationskomponente" wiederholen ein Muster, das
   andernorts bereits zu Falsifikationsproblemen gefuehrt hat
   (domaenenspezifische Ergebnisse zu einem universellen Framework
   zusammengesetzt). Solche Sprache wuerde den eigenen Genesis-Blindtest
   (Regel 6) eher durchfallen lassen.
2. **Namenskollision.** Der im urspruenglichen Diskurs verwendete Begriff
   "Semantic Kernel" ist bereits durch Microsofts gleichnamiges
   LLM-Orchestrierungs-SDK belegt. Fuer ein oeffentlichkeitsfaehiges
   Referenz-Repo sollte das vor jeder Begriffsfestlegung geklaert werden.

## Erwartetes Ergebnis

- Klaerung, ob "primaere Entitaet = Event/Transition" oder "primaere
  Entitaet = statischer Knoten" (oder eine komplementaere Formulierung:
  Event als primaer, Concept Node als daraus abgeleitete Projektion) die
  tragfaehigere Grundannahme fuer das spaetere Genesis-Core-Monorepo ist.
- Falls die Frage relevant bleibt: ein eigenes ADR dafuer, sobald die
  Monorepo-Inventarisierung beginnt (vgl. STATUS.md, "Weitere ADRs").
- Falls nicht: bewusste Ablage nach `archive/` mit Begruendung (Regel 11),
  statt stillschweigendem Verschwinden.

## Naechster Schritt

Maintainer entscheidet, ob diese Frage jetzt schon vertieft wird (z. B.
durch einen tatsaechlichen Code-Audit der Diamond-Interface-
Implementierungen in den 48 Paketen, sobald deren Inventarisierung
beginnt) oder ob sie bis zur Genesis-Core-Monorepo-Phase als offene Frage
stehen bleibt.

## Betrachtete Alternativen

- Den alten Branch `claude/upbeat-einstein-xvxowt` direkt mergen oder
  dessen Dateien unveraendert kopieren — verworfen: die dortige
  ADR-Nummerierung (`ADR-000`, `ADR-002-drei-schichten-architektur`)
  kollidiert mit der inzwischen akzeptierten Nummerierung in diesem Repo;
  eine direkte Uebernahme wuerde zwei widersprechende ADR-002-Definitionen
  ins selbe Repo bringen.
- Den Branch und seine Ideen vollstaendig ignorieren — verworfen: die
  inhaltliche Architekturfrage (Event vs. Concept Node) ist unabhaengig
  von der ADR-Nummerierung weiterhin relevant fuer das spaetere Monorepo.
- Die Copilot-Idee ("semantisches Betriebssystem") ebenfalls separat neu
  aufsetzen — vorerst zurueckgestellt: sie ist staerker an die verworfene
  Drei-Schichten-Nummerierung gebunden und weniger eigenstaendig
  pruefbar als der Event/Concept-Node-Einwand; kann bei Bedarf spaeter
  ebenfalls neu formuliert werden.
