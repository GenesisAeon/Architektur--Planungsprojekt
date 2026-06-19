# ADR-002 — Drei-Schichten-Architektur: Kernel, Agenten/Perspektiven, Anwendungen

## Kontext

`ADR-000` legt fest, dass die primäre Entität des Systems das
Wissensobjekt (semantischer Konzeptknoten, synonym "State Object" /
"Concept Node") ist, und dass Genesis Core / UTAC Core eine
domänenneutrale Infrastruktur für kollektive Orientierung ist, nicht eine
einzelne Domänenanwendung. Offen bleibt dabei, *wie* der Core intern
organisiert sein muss, um Wissensobjekte zu verwalten, und wie sich
Module wie `genesis-scope`, `genesis-os` und die rund 35
domänenspezifischen Pakete aus `02_Plaene/genesis-core-scope.md` zueinander
verhalten. Ohne eine explizite Schichtung droht, dass Navigations-/
Agentenlogik (z. B. `genesis-scope` als "human-AI navigation layer") und
reine Domänenlogik (z. B. `climate-dashboard`) im selben Topf landen und
Regel 7 (kein Core mit LLM-/Internet-Abhängigkeit) und Regel 8 (keine
privilegierte Domäne) schwer durchsetzbar werden.

## Entscheidung

Das System wird in drei Schichten organisiert, die jeweils auf der
darunterliegenden aufbauen, nicht umgekehrt:

1. **Schicht 1 — Kernel (Core).** Verwaltet ausschließlich Wissensobjekte
   und ihre Struktur: Zustand, Beziehungen (semantischer Graph),
   Versionierung, Event-Log und Governance-Regeln. Deterministisch, ohne
   LLM- oder Netzwerk-Abhängigkeit (Regel 7). Entspricht der in
   `02_Plaene/genesis-core-scope.md` skizzierten Fundament-Kette
   (`entropy-table` → … → `utac-core`) plus einer dünnen
   Orchestrierungsschicht (`genesis-os`, siehe dortiger "Sonderfall").
2. **Schicht 2 — Agenten & Perspektiven.** Interpretiert und navigiert die
   vom Kernel verwalteten Wissensobjekte, ohne selbst neue Kern-Datentypen
   einzuführen: Navigationslogik (`genesis-scope`), Multi-Agent-/LLM-
   Adapter, Perspektivenräume, Simulationen. Darf LLM- und
   Netzwerkzugriffe haben — genau deshalb ist diese Schicht laut Regel 7
   kategorisch von Schicht 1 getrennt und kann nie selbst Core werden.
3. **Schicht 3 — Anwendungen.** Domänenspezifische Programme/
   Hilfsprogramme, die Schicht 1 und 2 als Bibliothek nutzen, um eine
   einzelne fachliche Fragestellung zu bearbeiten (Forschung, Klima,
   Gemeinwohl, persönlicher Wissensraum). Austauschbar, ohne dass Schicht
   1 oder 2 sich ändern müssen.

Jede Abhängigkeit verläuft von oben nach unten (3 → 2 → 1). Keine
Schicht darf eine Abhängigkeit in die umgekehrte Richtung einführen.

## Begründung

- Die Trennung deckt sich mit der bereits in `genesis-core-scope.md`
  begonnenen Drei-Klassen-Karte (Core/Programm-Kandidaten/Hilfsprogramm-
  Kandidaten) — Schicht 1 entspricht den Core-Kandidaten, Schicht 2 den
  dort explizit als "nie Core" markierten LLM-/AI-abhängigen Paketen
  (`aeon-ai`, `genesis-scope`, `AdvancedWeightingSystems`, `worldview`,
  `gemeinwohl`), Schicht 3 den übrigen ~35 Domänenpaketen.
- Eine explizite Kernel/Agenten-Trennung macht Regel 7 (kein Core ohne
  LLM-/Internet-Unabhängigkeit) technisch durchsetzbar: jedes Modul mit
  LLM-Bedarf ist per Definition Schicht 2, nie Schicht 1 — unabhängig
  davon, wie zentral es sich anfühlt (z. B. `genesis-scope`).
  ("Semantic Kernel" im wörtlichen, nicht im Microsoft-Sinne; siehe
  `01_Ideen/copilot/copilot-semantisches-betriebssystem.md`.)
- Die Top-down-Abhängigkeitsrichtung (3 → 2 → 1) ist eine Verschärfung
  von Regel 4 (Rang-Abhängigkeit) auf Schichtenebene und verhindert, dass
  eine Domänenanwendung (Schicht 3) den Kernel um domänenspezifische
  Konzepte erweitert — das würde Regel 8 (keine privilegierte Domäne)
  verletzen.
- `genesis-os` lässt sich damit präzise einordnen: dünne
  Orchestrierungsschicht innerhalb von Schicht 1, die Schicht-2-Plugins
  laden darf, ohne selbst eine LLM-Laufzeitabhängigkeit zu haben — exakt
  wie im "Sonderfall genesis-os" in `genesis-core-scope.md` gefordert.

## Alternativen betrachtet

**Zwei Schichten (Core vs. Anwendungen), Agentenlogik dem Core
zuschlagen.** Verworfen: würde `genesis-scope` und vergleichbare
LLM-/Navigationsmodule zwingen, entweder im Core zu landen (Verstoß gegen
Regel 7) oder als gewöhnliche Domänenanwendung behandelt zu werden
(verschleiert ihre tatsächliche Querschnittsrolle über alle Domänen).

**Vier oder mehr Schichten (z. B. zusätzliche UI- oder
Persistenz-Schicht).** Verworfen für dieses ADR: zu diesem Zeitpunkt gibt
es keinen am Code verifizierten Bedarf für weitere Schichten; zusätzliche
Differenzierung kann in separaten ADRs ergänzt werden, ohne diese
Drei-Schichten-Grundstruktur zu verändern.

**Keine formale Schichtung, Einordnung pro Modul ausschließlich über den
Genesis-Blindtest (Regel 6) ohne übergeordnetes Modell.** Verworfen: der
Blindtest prüft, ob ein einzelnes Modul verständlich und domänenneutral
ist, beantwortet aber nicht, wie Module sich strukturell zueinander
verhalten dürfen — ohne Schichtenmodell bliebe die Abhängigkeitsrichtung
zwischen Navigations-/Agentenmodulen und Domänenpaketen ungeklärt.

## Konsequenzen

- Jeder neue Architektur-/Programm-/Hilfsprogramm-Eintrag muss bei der
  Aufnahme in `03_Architektur/`, `04_Programme/` oder `05_Hilfsprogramme/`
  einer der drei Schichten zugeordnet werden; das geschieht im jeweiligen
  Genesis-Blindtest (Regel 6).
- Schicht-1-Kandidaten aus der Fundament-Kette
  (`02_Plaene/genesis-core-scope.md`) werden einzeln durch den Blindtest
  geschickt und erhalten `related_adr: [ADR-000, ADR-002]`.
- `genesis-scope` wird als erster Schicht-2-Testfall (Regel 6) behandelt,
  nicht als Core-Kandidat.
