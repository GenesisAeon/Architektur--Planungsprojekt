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
