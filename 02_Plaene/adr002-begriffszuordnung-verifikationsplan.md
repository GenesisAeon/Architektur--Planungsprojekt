# Verifikationsplan: ADR-002-Begriffszuordnung (externe Pakete)

## Problem

`ADR-002` enthaelt eine Begriffszuordnungstabelle (Semantic Maps,
Navigable Paths, Contextual Structures, Agent-based Systems, Curators,
Researchers, Architects). Drei der sieben Zeilen sind bereits durch
`03_Architektur/rollenmodell-curator-researcher-architect.md`
(Curators, Researchers, Architects) und ein Teilaspekt einer vierten Zeile
durch `03_Architektur/trylayer-als-agenten-navigationsschicht.md`
(Agent-based Systems, generischer Teil) abgedeckt — beide ohne Bezug auf
externen Code, weil sie Mechanismen *dieses* Repos beschreiben.

Die verbleibenden Zeilen verweisen auf konkrete externe Pakete
(`genesis-scope`, Cartography/Pheromones/Drift, UTAC/CREP, MCP-Protokoll).
Diese koennen von hier aus **nicht** verifiziert werden: dieses Repo
enthaelt keinen Code dieser Pakete, nur Beschreibungen aus
`ECOSYSTEM_MAP.yaml` und der Sprint-Roadmap. Eine Einordnung als
`accepted` ohne Code-Pruefung wuerde Regel 6 (Genesis-Blindtest) und
Regel 5 (ehrlicher Epistemic Status) verletzen.

## Vorschlag

Pro offener Zeile ein konkretes, pruefbares Kriterium festhalten, statt
die Hypothese unveraendert stehen zu lassen oder vorschnell zu bestaetigen:

| Mission-Begriff | Vermutete Entsprechung | Was fehlt zur Verifikation |
|-------------------|--------------------------|-------------------------------|
| Semantic Maps | `genesis-scope` | Bereits als Blindtest-Kandidat markiert (`01_Ideen/claude/genesis-scope-blindtest`). Braucht echten Zugriff auf das Quickstart/README von `genesis-scope`, nicht nur die Domaenen-Beschreibung aus der Roadmap. |
| Navigable Paths | Cartography, Pheromones, Drift, Traces | **Korrigiert 2026-06-24** (siehe `01_Ideen/claude/navigable-paths-pheromones-drift-traces-korrektur`): Cartography, Drift und Traces sind durch das tatsaechliche `genesis-scope`-README (P39) bestaetigt — eigene Module/CLI-Kommandos (`cartography.py`, `drift_model.py`/`scope drift`, `DEFAULT_MAP.trace()`/`scope trace`), nicht nur Roadmap-Domaenentext. Pheromones ist NICHT im README enthalten und bleibt eine offene, noch unimplementierte Designidee (Pfade durch latente semantische Raeume markieren/bewerten, analog Ameisenpheromone) — naechstliegender, aber nicht identischer bestehender Mechanismus: Sigillin/semantic anchors (Anti-Drift, nicht Pfad-Markierung). Eine vorherige Einstufung aller drei Begriffe als reine Diskursterminologie (archive/) war voreilig (zu schwache Quelle: ECOSYSTEM_MAP.yaml statt echtes Paket-README) und wurde zurueckgenommen. |
| Contextual Structures | UTAC/CREP, semantische Graphen | `utac-core` ist bereits Core-Kandidat in `02_Plaene/genesis-core-scope.md` (Fundament-Kette). Verifikation laeuft ueber denselben Plan, nicht separat hier. **Update 2026-06-24** (aus den Forschungsfrage-001-Pilotlaeufen, siehe `02_Plaene/forschungsfrage-001-testprotokoll.md`): CREP/UTAC sind real als Code in `genesis-os` vorhanden (Gamma(C,R,E,P)=(C\*R\*E\*P)^(1/4), UTAC-Logistic-ODE, `afet/`-Modul als "Thermodynamic consistency layer"/"AFET + Landauer Consistency") — keine reine Diskurs-Terminologie mehr. Aber: UTAC wird in `Feldtheorie` ("Universal Threshold Activation-Coupling") und `sa-sv-duality` ("Universal Trajectory of Action-Coherence") unterschiedlich ausgeschrieben — eine noch ungeklaerte Cross-Repo-Inkonsistenz, die vor jeder Einstufung als `validated`/`accepted` aufgeloest werden muss. Bisher nur README-Ebene (WebFetch), kein direkter Quellcode-Zugriff — vollwertige Verifikation steht aus, blockiert durch den laufenden v1.0.0-Sprint. |
| Agent-based Systems (MCP-Teil) | MCP-/Agent-Integration | Kein MCP-Server-/Client-Code in diesem Oekosystem identifiziert. Offene Frage: existiert eine MCP-Implementierung bereits in einem der 48 Pakete, oder ist das eine zukuenftige Anforderung? |

## Erwartetes Ergebnis

Fuer jede Zeile entweder (a) ein eigener `01_Ideen/`-Eintrag mit konkretem
naechstem Pruefschritt, sobald Code-Zugriff besteht, oder (b) eine
explizite Verschiebung nach `archive/` mit Begruendung, falls sich der
Begriff als reine Genesis-Diskurs-Terminologie ohne externe Entsprechung
herausstellt (Regel 9).

## Naechster Schritt

1. ~~Cartography/Pheromones/Drift/Traces in `ECOSYSTEM_MAP.yaml` suchen
   lassen~~ — erledigt am 2026-06-24, siehe
   `01_Ideen/claude/cartography-pheromones-drift-ecosystem-map-befund`.
   Befund negativ/unklar: kein eigenes Paket gefunden. Offen bleibt die
   Maintainer-Entscheidung, ob es sich um reine Diskurs-Metaphern
   (-> `archive/`) oder unklassifizierte Teilmodule (-> Code-Pruefung
   noetig) handelt.
2. `genesis-scope`-Blindtest tatsaechlich durchfuehren, sobald
   Quickstart-Zugriff besteht (Maintainer-Aufgabe, siehe
   `01_Ideen/claude/genesis-scope-blindtest.md`).
3. MCP-Frage als eigene Idee in `01_Ideen/` einreichen, sobald klar ist,
   ob es um Bestandscode oder eine neue Anforderung geht.

## Alternativen betrachtet

**Alle vier verbleibenden Zeilen sofort als `03_Architektur`-Eintraege mit
`status: accepted` anlegen, basierend auf der Domaenen-Beschreibung aus
der Roadmap.** Verworfen: das wuerde Regel 6 und Regel 5 verletzen — eine
Domaenen-Beschreibung ist keine Code-Verifikation, und `epistemic_status:
validated` waere unehrlich fuer etwas, das nur `hypothesis` ist.

**Die vier Zeilen ignorieren, bis die externen Pakete in dieses Repo
migriert werden.** Verworfen: das wuerde "Eventualitaeten" beim
spaeteren Monorepo-Aufbau erhoehen statt verringern — explizite,
pruefbare offene Fragen jetzt sind besser als implizite Annahmen spaeter.
