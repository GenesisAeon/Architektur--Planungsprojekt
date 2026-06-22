# Trylayer + ENTRY.yaml als Agenten-Navigationsschicht

**Status:** accepted · **Epistemic Status:** validated · **Related ADR:** ADR-001, ADR-002

## Entscheidung

`ADR-002` ordnet "Agent-based Systems" und "Navigable Paths/Contextual
Structures" der Mission zu, ohne zu sagen, wo das konkret schon passiert.
Dieser Eintrag haelt fest: **dieses Repo selbst ist bereits eine
lauffaehige, minimale Instanz der Mission** — nicht fuer ein externes
Domaenenpaket, sondern fuer sich selbst als Wissensbasis.

Konkret:

- `ENTRY.yaml` ist eine reine Datenstruktur (bewusst ohne Prosa, siehe
  Kommentar in der Datei), die ein Agent in einem einzigen Parse-Schritt
  lesen kann, um den vollstaendigen, deterministischen Lesepfad durch das
  Repo zu kennen (Regel 12).
- Das Trylayer-Format (`.yaml`/`.ai.json`/`.md` je Slug) ist eine
  navigierbare Kontextstruktur: jeder Eintrag trägt Status, Reifegrad,
  Herkunft (`derived_from`) und Abhaengigkeiten (`depends_on`) maschinell
  auswertbar, ohne dass ein Agent Fliesstext interpretieren muss.
- Beides funktioniert ohne LLM-Inferenz und ohne Internetzugriff
  (`scripts/validate_trylayer.py` ist deterministisches Python), erfuellt
  also nebenbei auch Regel 7.

## Begruendung

Der Genesis-Blindtest besteht hier im engeren Sinn bereits: Ein Agent ohne
GenesisAeon-Kontext, der `ENTRY.yaml` parst, erhaelt einen vollstaendigen,
korrekten Lesepfad (README -> STATUS -> PRINCIPLES -> AGENTS ->
optional 00_Regeln/Planungsdiskurse) und kann direkt danach einen
gueltigen Beitrag einreichen — verifizierbar durch
`scripts/validate_trylayer.py`, nicht nur behauptet. Das ist genau das,
was die Mission unter "navigable paths and contextual structures for ...
agent-based systems" meint, hier in der einfachsten moeglichen Form:
Selbstanwendung des Prinzips auf das Planungsrepo selbst.

**Bewusste Grenze:** Dieser Eintrag behauptet NICHT, dass MCP-spezifische
Protokoll-Integration (Model Context Protocol als konkretes Transport-/
Tool-Schema) bereits existiert — das ist eine andere, noch offene Frage
(siehe `02_Plaene/adr002-begriffszuordnung-verifikationsplan.md`). Er
behauptet nur, dass die zugrunde liegende Navigationslogik (ein Agent
kann sich ohne LLM-Heuristik deterministisch orientieren) bereits
lauffaehig ist.

## Alternativen betrachtet

**Warten, bis ein externes Paket (z.B. `genesis-scope`) den Blindtest
besteht, bevor irgendein "Navigable Paths"-Eintrag `accepted` wird.**
Verworfen: das wuerde ignorieren, dass dieses Repo selbst bereits ein
gueltiges, kleines Beispiel ist — und wuerde den naechsten Beitragenden
ohne zitierbaren Bezugspunkt fuer "was bedeutet das konkret" lassen.

## Bezug zur Begriffszuordnung (ADR-002)

Deckt einen Teilaspekt von *Agent-based Systems -> MCP-/Agent-Integration*
und *Navigable Paths -> Cartography/Pheromones/Drift/Traces* ab — naemlich
den generischen, paketunabhaengigen Navigationsmechanismus. Die
domaenenspezifischen Teile (echtes MCP-Protokoll, Cartography/Pheromones
als konkrete Pakete) bleiben offen.
