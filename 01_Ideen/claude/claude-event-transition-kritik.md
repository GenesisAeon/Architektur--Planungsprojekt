# Gegeneinwand zu ADR-000: primäre Entität ist Event/Transition, nicht Concept Node

## Herkunft

Multi-AI-Diskurs, Claude (Sonnet 4.6), 2026-06-19, als Gegeneinwand zur
gerade verfassten `ADR-000` (Wissensobjekt/Concept Node als primäre
Entität) und zur Copilot-Idee
`copilot-semantisches-betriebssystem`/`ADR-002`. Roh-Einwand, noch nicht
durch den Genesis-Blindtest (Regel 6) geprüft. **Steht im direkten
Widerspruch zu `ADR-000`** — vor weiteren darauf aufbauenden ADRs muss
dieser Widerspruch aufgelöst werden, nicht stillschweigend überschrieben.

## Kernthese

Die ChatGPT/Copilot-Frage "was ist die primäre Entität?" ist richtig,
wird in `ADR-000` aber philosophisch statt code-basiert beantwortet. Das
bestehende Diamond Interface zeigt eine andere Antwort: `run_cycle()`,
`get_crep_state()`, `get_utac_state()`, `get_phase_events()`,
`to_zenodo_record()` — vier von fünf Methoden drehen sich um
**Zustandsänderung über Zeit**, nicht um statische Knoten.

- Sigillin ist im Kern ein Event-Sourcing-Snapshot mit Lineage.
- Q4-Zustände sind keine Konzeptknoten in einem Wissensgraphen, sondern
  Knoten in einem **Übergangsgraphen** (Gray-Code-Nachbarschaft).
- CREP ist keine Eigenschaft eines Dings, sondern eine über Zeit
  gemessene Rate.

Folgerung: die primäre Entität ist nicht der Concept Node, sondern die
**Phase-Transition mit angehängtem Zustand** — ein Ereignis, kein Ding.
Architektonisch näher an zwei etablierten Mustern als an einem
selbsterfundenen "Semantic Kernel":

- **Event Sourcing + CQRS** — passt zu "Event Log" als Primärentität und
  zur Replay-basierten Zustandsrekonstruktion (Bezug zur eigenen
  JetStream/ReplayEngine-Idee aus dem Q4-Layer).
- **Actor Model / Supervision Trees** (Erlang/Elixir-OTP-Stil) — für
  "Agenten als Interpreten des Kernels" (Schicht 2 aus `ADR-002`).

## Zwei zusätzliche Einwände

1. **Übertreibungsmuster.** Formulierungen wie "Betriebssystem für Sinn",
   "Zivilisationskomponente", "Koordinationsmedium für komplexe
   Kollektive" wiederholen ein Muster, das in der AFET-Kosmologie-Arbeit
   bereits zu einer Falsifikationsanalyse mit aufgedeckten systematischen
   Übertreibungen geführt hat (domänenspezifische Ergebnisse zu einem
   universellen Framework zusammengesetzt). Genau diese Sprache würde den
   eigenen Genesis-Blindtest (Regel 6) durchfallen lassen.
2. **Namenskollision.** "Semantic Kernel" ist als Begriff bereits
   vergeben — Microsofts offen verfügbares SDK für LLM-Orchestrierung
   heißt genau so. Ein Disclaimer löst das nicht; jede Suche/Zitation
   landet zuerst dort. Für ein öffentlichkeitsfähiges Referenz-Repo sollte
   das vor dem ersten Commit geklärt werden, nicht danach.

## Praktische Konsequenz (Vorschlag)

- Vorschlag: ein eigenes ADR ("ADR-000: primäre Entität = Event/
  Transition, nicht Concept Node") **bevor** die Kernel-Definition formal
  aufgeschrieben wird — d. h. vor einer endgültigen Fassung von `ADR-000`
  in der jetzigen Form.
- Bestehende Architektur-Sprache (Event Sourcing/CQRS, Actor Model) statt
  neu erfundener Begriffe ("Semantic Kernel", "Concept Node") verwenden —
  macht das System für Außenstehende lesbar (Blindtest) und nutzt
  etabliertes Tooling/Fehlerwissen statt Neuerfindung.
- Begriff "Semantic Kernel" wegen Namenskollision mit Microsofts SDK aus
  der finalen Terminologie entfernen, nicht nur mit Disclaimer versehen.

## Offener Konflikt

Dieser Einwand widerspricht `ADR-000` (Wissensobjekt/Concept Node als
primäre Entität, Status `accepted`) inhaltlich direkt. Auflösung steht
noch aus — mögliche Wege: (a) `ADR-000` durch ein neues, ersetzendes ADR
ablösen (`status: deprecated` + Verweis), (b) beide Sichtweisen als
komplementär reformulieren (z. B. Event als primäre Entität, Concept
Node als daraus abgeleitete Projektion/Snapshot), oder (c) Code-Audit der
Diamond-Interface-Implementierungen abwarten, bevor eine der beiden
Positionen verbindlich wird.
