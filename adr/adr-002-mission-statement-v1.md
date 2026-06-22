# ADR-002 — Mission-Statement v1 fuer GenesisAeon / genesis-os

## Kontext

Die GenesisAeon-Organisation (GitHub-Gruppenbeschreibung) und `genesis-os`
hatten bisher keine einheitliche, oeffentlich verstaendliche
Selbstbeschreibung. Vorherige Formulierungsversuche kreisten um zu grosse
Anspruechszuschreibungen ("Wissensplattform", "Gemeinwohlplattform",
"Klimaplattform", "Zivilisationskomponente", "semantisches Betriebssystem
fuer Sinn") — beeindruckend, aber weder testbar noch direkt in Architektur
uebersetzbar, und ohne Kenntnis der Genesis-Erzaehlung kaum verstaendlich
(verstoesst gegen den Geist von Regel 6, Genesis-Blindtest).

Ein Multi-AI-Gespraech (Claude, ChatGPT, Grok, MSCopilot, Johann,
2026-06-22; vollstaendiges Protokoll:
`Entwicklungsgespraeche/2026-06-22-mission-statement.md`) hat folgenden
Satz erarbeitet und im Konsens als vorlaeufige Mission identifiziert:

> "GenesisAeon generates, maintains and provides semantic maps, navigable
> paths and contextual structures for LLMs and agent-based systems. Humans
> act as curators, researchers and architects, shaping these maps through
> rigorous inquiry."

## Entscheidung

Dieser Satz wird als Mission-Statement v1 fuer die GenesisAeon-
Organisationsbeschreibung und fuer `genesis-os` uebernommen
(Maintainer-Entscheidung, Johann, 2026-06-22). Er gilt als vorlaeufiger,
aber bindender Bezugspunkt fuer dieses Architektur-Repo, nicht als
endgueltige Vision.

Damit verbunden ist eine Rollenverteilung mit direkten
Architekturkonsequenzen:

- **Primaerer Nutzer/Adressat der Infrastruktur:** LLMs und
  agentenbasierte Systeme (Konsumenten/Navigatoren der semantischen
  Karten).
- **Primaerer Gestalter:** Menschen als Curators, Researchers, Architects
  (Governance, Provenance, ADRs/Core-Design).

Vorlaeufige Begriffszuordnung (Ausgangshypothese, noch nicht durch
Blindtest/eigene ADRs bestaetigt):

| Mission-Begriff         | Vermutete Entsprechung im Oekosystem        |
|--------------------------|----------------------------------------------|
| Semantic Maps            | `genesis-scope` / Scope-Konzept              |
| Navigable Paths          | Cartography, Pheromones, Drift, Traces       |
| Contextual Structures    | UTAC/CREP, semantische Graphen               |
| Agent-based Systems      | MCP-/Agent-Integration                       |
| Curators                 | Governance-Prozess in diesem Repo            |
| Researchers              | Provenance/Evidence-Pflichten                |
| Architects               | ADRs, Core-Design                            |

## Begruendung

- Der Satz besteht den Genesis-Blindtest informell: er ist ohne
  Vorwissen ueber GenesisAeon verstaendlich und beschreibt testbares
  Verhalten statt eines Anspruchs.
- Er filtert Scope: jede neue Idee laesst sich daran messen, ob sie hilft,
  semantische Karten/Pfade/Kontextstrukturen fuer Agenten zu erzeugen, zu
  pflegen oder bereitzustellen. Wenn nein, gehoert sie wahrscheinlich nicht
  in den Core (operationalisiert Regel 8, keine privilegierte Domaene).
- Er macht aus der bisher impliziten Rollentrennung (Mensch vs. KI) eine
  explizite, prueefbare Architekturentscheidung statt einer offenen Frage.

## Alternativen betrachtet

**Keine eigene ADR, Satz nur als Prosa in README/Gruppenbeschreibung
fuehren.** Verworfen: Regel 3 verlangt ein ADR vor jeder groesseren
Architekturentscheidung, sobald daraus Core-Klassifikation und Scope-
Filterregeln abgeleitet werden — genau das passiert hier.

**Auf die ausfuehrlichere Variante mit "develops"/"curates" statt
"generates" warten, bevor etwas eingefroren wird.** Verworfen (Johann,
explizit): die Wortwahl-Feinschliffe (ChatGPT: "develops", Claude:
"curates") sind sprachlich interessant, aendern aber die Substanz nicht.
Ein bereits oeffentlich verwendeter Satz wird nicht nachtraeglich wegen
Wortgeschmacks geaendert — neue Erkenntnisse bekommen ein neues ADR mit
`supersedes`, nicht eine stille Bearbeitung dieses Satzes.

## Konsequenzen

- Die Begriffszuordnungstabelle oben ist eine Ausgangshypothese fuer
  `02_Plaene/genesis-core-scope.md` und die anstehenden Blindtests pro
  Paket — sie ersetzt keine einzelne Paket-Entscheidung.
- Aenderungen an der GitHub-Gruppenbeschreibung, an der `genesis-os`-
  Repo-Beschreibung und an der Zenodo-Community-Beschreibung sind externe,
  manuelle Schritte ausserhalb dieses Repos (Johann); dieses ADR
  dokumentiert nur die Entscheidung und ihre Begruendung.
- Naechster Schritt fuer dieses Repo: aus der Begriffszuordnungstabelle
  konkrete `01_Ideen/`- bzw. `02_Plaene/`-Eintraege ableiten (`derived_from`
  auf dieses ADR), bevor irgendeine Zeile der Tabelle als
  `03_Architektur/`-Eintrag mit `status: accepted` landet.
