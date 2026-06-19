# ADR-000 — Was ist die primäre Entität des Systems?

## Kontext

`ADR-001` legt fest, dass ein eigenes Genesis Core / UTAC Core Monorepo
entsteht, und `02_Plaene/genesis-core-scope.md` beginnt, den Core von
Programmen und Hilfsprogrammen abzugrenzen. Beide Dokumente setzen
implizit voraus, *worum* es im System überhaupt geht, ohne das je explizit
zu benennen. Diese Lücke wird sichtbar, sobald man das System mit anderen
Plattformen vergleicht: Wikipedia hat den Artikel, GitHub das Repository,
Reddit die Diskussion, Discord die Nachricht — jede Plattform hat eine
primäre Entität, um die sich Datenmodell, UI und Governance organisieren.

Ohne diese Festlegung wackelt jede nachfolgende Architekturentscheidung:
Monorepo-Struktur, Datenmodell, Plugin-System und die Einordnung von
Modulen wie `genesis-scope` und `genesis-os` hängen davon ab, ob das
System als einzelne Domänenanwendung (Klima, Forschung, Gemeinwohl,
soziales Netzwerk) gedacht wird oder als domänenübergreifendes Fundament,
auf dem solche Anwendungen erst aufgesetzt werden.

## Entscheidung

Die primäre Entität des Systems ist nicht eine Domänenanwendung, sondern
ein **Wissensobjekt** (semantischer Konzeptknoten) — ein adressierbarer
Zustand im Wissensraum, der von Menschen und Agenten gemeinsam erzeugt,
verknüpft und navigiert werden kann.

Damit ist Genesis Core / UTAC Core kein Endprodukt für eine einzelne
Domäne (Klimaplattform, Forschungsplattform, soziales Netzwerk), sondern
eine **Infrastruktur für kollektive Orientierung in komplexen
Wissensräumen**, auf der domänenspezifische Anwendungen (Forschung,
Gemeinwohl, Klima, KI-Kollaboration, persönlicher Wissensraum) als
Programme bzw. Hilfsprogramme/Plugins aufgesetzt werden, nicht als Teil
des Cores selbst.

**Primärer Konsument der Wissensobjekte ist das LLM/Agent, nicht der
Mensch direkt** (siehe "Ergänzung 2" unten) — Menschen kuratieren die
semantischen Karten, Modelle konsumieren sie zur Initialisierung und
Orientierung in einer Aufgabe.

## Begründung

- Module wie `genesis-scope` (human-AI navigation layer) und die
  Pheromonpfad-/semantische-Kartografie-Konzepte aus den
  Planungsdiskursen sind bereits implizit auf ein Wissensobjekt als
  Adressierungseinheit ausgelegt, nicht auf Dateien, Chatnachrichten oder
  Posts.
- Regel 8 (keine privilegierte Domäne) verlangt ohnehin, dass der Core
  keine einzelne Anwendungsdomäne bevorzugt. Eine domänenspezifische
  primäre Entität (z. B. "Klimamodell" oder "Forschungsartikel") würde
  dieser Regel widersprechen; ein domänenneutrales Wissensobjekt erfüllt
  sie.
- `02_Plaene/genesis-core-scope.md` ordnet alle ~35 domänenspezifischen
  Pakete bereits als Hilfsprogramme/Plugins ein, die den Core als
  Bibliothek nutzen — das ist nur konsistent, wenn der Core selbst
  domänenneutral bleibt und sich um eine gemeinsame, domänenunabhängige
  Entität organisiert.
- Eine explizite Festlegung jetzt verhindert, dass spätere ADRs
  (Datenmodell, Diamond-Interface-Protokoll, Plugin-System) implizit
  unterschiedliche Annahmen über die primäre Entität treffen.

## Alternativen betrachtet

**Keine primäre Entität festlegen, sondern pro Domänenanwendung
unterschiedliche Datenmodelle zulassen.** Verworfen: macht eine
gemeinsame Governance-Ebene (Regel 4, Rang-Abhängigkeit) und ein
einheitliches Plugin-System praktisch unmöglich, da jedes Programm seine
eigene Grundentität mitbringen würde.

**Die primäre Entität explizit auf eine Domäne festlegen (z. B.
"Forschungsartikel" oder "Klimaszenario").** Verworfen: verletzt Regel 8
und würde den Core faktisch zu einer Forschungs- oder Klimaplattform
machen, auf der alles andere nur noch Anhängsel wäre — widerspricht der
in `genesis-core-scope.md` bereits begonnenen domänenneutralen
Core/Programm/Hilfsprogramm-Trennung.

**Datei/Dokument als primäre Entität (wie bei klassischen
Wissensmanagement-Tools).** Verworfen: bildet die in den
Planungsdiskursen beschriebene semantische Verknüpfung zwischen
Konzepten, Agentenperspektiven und Wissensräumen nicht ab — ein
Dateibegriff ist zu grobkörnig für Pheromonpfade und semantische
Kartografie.

## Konsequenzen

- Nachfolgende ADRs zu Datenmodell, Diamond-Interface und Plugin-System
  müssen sich auf das Wissensobjekt als primäre Entität beziehen
  (`related_adr: [ADR-000]`).
- `genesis-scope` und vergleichbare Module sind candidate dafür, die
  Navigations- und Verknüpfungsschicht über Wissensobjekten zu sein —
  das ist im Genesis-Blindtest (Regel 6) explizit zu prüfen, bevor ein
  entsprechender Architektur-Eintrag `accepted` wird.
- Domänenspezifische Anwendungen (Klima, Forschung, Gemeinwohl, KI-
  Kollaboration) bleiben Programme/Hilfsprogramme, die Wissensobjekte
  über den Core erzeugen und verknüpfen — sie definieren keine eigene
  primäre Entität.

## Ergänzung: Terminologie und Schichtenfrage

Ein zweiter Multi-AI-Diskurs (MSCopilot, 2026-06-19) bestätigt die hier
getroffene Entscheidung unabhängig und schlägt zusätzlich die Begriffe
**State Object** und **Concept Node** als gleichwertige, in anderen
Communities geläufigere Bezeichnungen für dasselbe Konzept vor. Dieses
ADR hält an "Wissensobjekt / semantischer Konzeptknoten" als
Primärbegriff fest (Kontinuität mit der bisherigen Trylayer-Terminologie),
akzeptiert "State Object" / "Concept Node" aber als Synonyme in
Folgedokumenten.

Derselbe Diskurs wirft zusätzlich die Frage auf, *wie* der Core organisiert
sein muss, um Wissensobjekte zu verwalten (Kernel-artige Schichtung
Core/Agenten/Anwendungen). Das ist eine eigenständige Entscheidung mit
eigener Begründung und Alternativenabwägung und wird daher nicht hier,
sondern in `ADR-002-drei-schichten-architektur` behandelt, das auf dieses
ADR aufbaut (`related_adr: [ADR-000, ADR-001]`). Die zugrunde liegende
Rohidee ist dokumentiert in
`01_Ideen/copilot/copilot-semantisches-betriebssystem.md`.

## Ergänzung 2: LLM als primärer Konsument (Korrektur des semantischen Drifts)

Ein dritter Multi-AI-Diskurs (ChatGPT, Claude, MSCopilot, 2026-06-19,
ausgelöst durch eine eigene Beobachtung von Johann) identifiziert
rückwirkend einen semantischen Drift in den vorherigen Diskursrunden:
Formulierungen wie "Betriebssystem für Sinn", "Zivilisationskomponente"
oder "Koordinationsmedium für komplexe Kollektive" (siehe
"Ergänzung" oben und `ADR-002`) wurden zunehmend abstrakt und
menschenzentriert, während die ursprüngliche, konkrete Intention hinter
Sigillin/Scope/CREP nie eine Plattform *für* Menschen mit KI-Beteiligung
war, sondern eine Infrastruktur, **deren eigentlicher Endnutzer das
LLM/Agent ist**.

### Entscheidungs-Update

- **Primärer Konsument:** LLM/Agent — nicht der Mensch direkt. Ein
  konkretes Nutzungsbild: ein Wissenschaftler sagt sinngemäß "liebes LLM,
  hol dir die semantischen Bedeutungspfade zu Thema X auf dieser
  Plattform, damit du für unsere Arbeit initialisiert bist."
- **Rolle des Menschen:** Kurator/Architekt der semantischen Karten, nicht
  Hauptnutzer der Abfrageoperation selbst.
- **Primäre Entität bleibt das Wissensobjekt** (Semantic Node) — das
  bestätigt die ursprüngliche Entscheidung dieses ADR. Neu hinzu kommt
  eine **primäre Operation**: **Semantic Path Retrieval** — das
  Abrufen einer Sequenz zusammenhängender Wissensobjekte (Semantic Path)
  zu einem Thema, nicht nur eines einzelnen Knotens.
- **Pfad als Synthese mit dem Event/Transition-Einwand**
  (`01_Ideen/claude/claude-event-transition-kritik.md`): der Einwand,
  dass Sigillin/Q4/CREP faktisch Übergänge über Zeit modellieren statt
  statische Knoten, wird durch den Semantic Path teilweise aufgenommen,
  ohne die Basis-Entität zu ändern — ein Pfad **ist** eine Sequenz von
  Übergängen zwischen Wissensobjekten, mit einem CREP-Kohärenzwert (Γ)
  als Qualitätsmaß für den Pfad selbst. Vollständig aufgelöst ist der
  Konflikt damit nicht (der Einwand würde die Basis-Entität selbst zur
  Transition machen, dieses ADR hält am Knoten als Basis fest) — das
  bleibt für ein Code-Audit der Diamond-Interface-Implementierungen
  offen.

### Begründung

- Bestehende RAG-Systeme liefern Ähnlichkeit, GraphRAG liefert
  Graphstruktur — keines von beiden liefert ein Kohärenz-/Qualitätssignal
  für einen Pfad selbst. Ein Sigillin-Pfad mit hohem CREP (Γ) ist nicht
  nur thematisch verwandt, sondern in sich konsistent — das ist die
  begründbare Differenzierung gegenüber bestehenden Retrieval-Ansätzen,
  kein Marketing-Begriff.
- Diese Formulierung positioniert das System in einer bereits etablierten,
  benannten Kategorie (Model Context Protocol/MCP, `llms.txt`, GraphRAG)
  statt einen neuen Begriff ("Semantic Kernel", "semantisches
  Betriebssystem") zu erfinden — das löst gleichzeitig die in
  `claude-event-transition-kritik.md` benannte Sorge vor
  Übertreibungssprache und die Namenskollision mit Microsofts
  "Semantic Kernel"-SDK.
- Ein LLM-first-Konsumentenmodell ist konkret genug, um den
  Genesis-Blindtest (Regel 6) zu bestehen: "ein LLM ruft strukturierte
  Bedeutungspfade zu einem Thema ab" ist überprüfbar und implementierbar,
  anders als "Infrastruktur für kollektive Orientierung" allein.

### Konsequenzen

- `ADR-002` (Drei-Schichten-Architektur) muss in einem Folge-ADR auf
  dieses Konsumentenmodell geprüft werden: Schicht 2 (Agenten &
  Perspektiven) ist primär die Schnittstelle, über die LLMs Semantic-Path-
  Retrieval-Anfragen an Schicht 1 stellen — nicht nur eine
  Interpretationsschicht für menschliche Nutzer.
- Der Begriff "Semantic Kernel" wird wegen der Namenskollision mit
  Microsofts SDK nicht als Repo-Terminologie übernommen; stattdessen wird
  in zukünftigen Architektur-Dokumenten auf etablierte Begriffe
  (Model Context Protocol, GraphRAG, `llms.txt`) Bezug genommen.
- Jedes künftige Architektur-/Programm-Modul, das auf Wissensobjekten
  aufbaut, muss explizit angeben, ob sein primärer Konsument ein
  LLM/Agent oder ein Mensch ist — Default ist LLM/Agent, menschliche
  Kuratierungs-Werkzeuge sind die Ausnahme, nicht die Regel.
- Der offene Konflikt mit `claude-event-transition-kritik` (Node vs.
  Transition als Basis-Entität) bleibt für die Architekturdetails
  bestehen, ist aber für die Zweckbestimmung des Systems (LLM-first
  statt Human-first) nicht mehr entscheidend — beide Sichtweisen sind mit
  einem LLM als primärem Konsumenten kompatibel.
