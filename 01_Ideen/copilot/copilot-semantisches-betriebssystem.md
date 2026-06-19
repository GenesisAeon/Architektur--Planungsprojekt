# Semantisches Betriebssystem: GenesisAeon als Kernel für Wissensobjekte

## Herkunft

Multi-AI-Diskurs zwischen Johann und Microsoft Copilot, 2026-06-19, als
Ergänzung zu einer vorherigen ChatGPT-Diskussion (siehe
`derived_from`-Bezug zu ADR-000). Roh-Synthese, noch nicht durch den
Genesis-Blindtest (Regel 6) geprüft.

## Kernthese

GenesisAeon baut kein Produkt für eine einzelne Domäne, sondern ein
**semantisches Betriebssystem** — wörtlich gemeint, nicht metaphorisch:
ein Kernel, der nicht Prozesse, Dateien oder Hardware verwaltet, sondern
Konzepte, Beziehungen, Perspektiven, Zustände, Entscheidungen und
Agenten. Die primäre Entität ist ein **State Object** / **Concept Node**
(Synonyme für das in ADR-000 als "Wissensobjekt" festgelegte Konzept).

Daraus folgt eine Drei-Schichten-Struktur:

1. **Semantic Kernel (Core).** Primäre Entitäten: State Object, Concept
   Node, Semantic Graph, Event Log, Governance Rules, Runtime.
2. **Agents & Perspectives.** Interpretiert den Kernel: `genesis-scope`,
   UTAC, Multi-Agent-Adapter, LLM-Interfaces, Simulationen,
   perspektivische Räume.
3. **Anwendungen.** Austauschbare Domänenschicht: Forschungsplattform,
   Gemeinwohlplattform, Klimaplattform, Wissensräume, persönliche
   Notizsysteme, Multi-Agent-Workflows.

Zusammenfassender Satz aus dem Diskurs: "GenesisAeon baut ein
semantisches Betriebssystem für kollektive Orientierung — ein Kernel,
der Wissen, Perspektiven und Agenten in einem gemeinsamen Raum
koordinierbar macht."

## Bezug zu bestehenden Entscheidungen

- Bestätigt unabhängig die Kernaussage von `ADR-000`
  (Wissensobjekt/State Object als primäre Entität, Plattform als
  Infrastruktur statt Einzelanwendung).
- Liefert die Begründung und Struktur für `ADR-002`
  (Drei-Schichten-Architektur Kernel/Agenten/Anwendungen).

## Offene Punkte für den Blindtest

- Ob "Semantic Kernel" als Begriff im Repo übernommen wird oder nur als
  Erklärhilfe dient (Verwechslungsgefahr mit Microsofts
  "Semantic Kernel"-Framework — im Diskurs explizit als rein
  konzeptionelle Namensgleichheit markiert, keine technische
  Abhängigkeit).
- Ob `genesis-os` tatsächlich als Teil von Schicht 1 (dünne
  Orchestrierung) oder als eigenständiges Schicht-1.5-Konzept geführt
  werden sollte — noch nicht am Code verifiziert.
