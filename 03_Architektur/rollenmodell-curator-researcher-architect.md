# Rollenmodell: Curator, Researcher, Architect

**Status:** accepted · **Epistemic Status:** validated · **Related ADR:** ADR-002

## Entscheidung

`ADR-002` beschreibt Menschen in der GenesisAeon-Mission als "curators,
researchers and architects, shaping these maps through rigorous inquiry".
Dieser Eintrag haelt fest, dass diese drei Rollen in *diesem* Repo bereits
existieren — nicht als Zukunftsplan, sondern als Mechanismus, der heute
durch `scripts/validate_trylayer.py` und die Verfassung (`PRINCIPLES.md`)
durchgesetzt wird:

| Mission-Rolle | Konkreter Mechanismus in diesem Repo |
|----------------|----------------------------------------|
| **Curator**    | Maintainer-Gate (`AGENTS.md`: "Kein Ort, an dem du `status: accepted`/`core` selbst vergibst — das macht ausschliesslich der menschliche Maintainer per Commit"). Kuration heisst hier konkret: Statuswechsel freigeben, nicht Inhalt erfinden. |
| **Researcher** | Regel 5 (Epistemic-Status-Pflicht) — jeder Eintrag muss seine Erkenntnisstufe (`validated`/`measured`/`derived`/`hypothesis`/`speculative`) ehrlich deklarieren. Dazu die Begruendungs- und Alternativen-Pflicht in jedem ADR. |
| **Architect**  | Regel 3 (Kein Core ohne ADR) plus `adr/` selbst — jede Architekturentscheidung mit Tragweite bekommt ein referenzierbares ADR, bevor sie `accepted`/`core` werden darf. |

## Begruendung

Diese Zuordnung erfuellt den Genesis-Blindtest aus Regel 6 konkret: eine
Person ohne jeden GenesisAeon-Kontext kann `AGENTS.md` und `PRINCIPLES.md`
lesen und innerhalb von 5 Minuten verstehen, *was* ein Curator/Researcher/
Architect in diesem Repo tatsaechlich tut, und es direkt anwenden (einen
Trylayer-Eintrag mit korrektem `epistemic_status` anlegen, ein ADR
schreiben, einen Statuswechsel beim Maintainer anfragen). Es handelt sich
nicht um eine Behauptung ueber ein externes System, sondern um eine
Beschreibung von Mechanismen, die in diesem Repo bereits lauffaehig sind
und durch `scripts/validate_trylayer.py` erzwungen werden — daher
`epistemic_status: validated` statt `hypothesis`.

## Alternativen betrachtet

**Diese Zuordnung nur in `ADR-002` selbst belassen, kein eigener
Architektur-Eintrag.** Verworfen: `ADR-002` begruendet eine Entscheidung,
beschreibt aber nicht die laufenden Mechanismen im Detail; ein
referenzierbarer `03_Architektur`-Eintrag macht das Rollenmodell direkt
zitierbar fuer kuenftige Beitraege, ohne das gesamte ADR lesen zu muessen.

## Bezug zur Begriffszuordnung (ADR-002)

Deckt zwei der sieben Zeilen aus der Begriffszuordnungstabelle in
`ADR-002` ab: *Curators -> Governance-Prozess* und *Architects ->
ADRs/Core-Design*. *Researchers -> Provenance/Evidence-Pflichten* ist hier
mitenthalten (Regel 5). Die verbleibenden vier Zeilen (Semantic Maps,
Navigable Paths, Contextual Structures, Agent-based Systems) betreffen
externe Pakete und sind in
`02_Plaene/adr002-begriffszuordnung-verifikationsplan.md` offen.
