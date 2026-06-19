# ADR-001 — Warum Genesis Core / UTAC Core als eigenes Monorepo

## Kontext

Das GenesisAeon-Ökosystem ist aus Unified-Mandala entstanden: einem
explorativen Forschungslabor mit 48 Micro-Packages, dialogisch und
rekursiv gewachsener Terminologie (Mandala-, Genesis-, Sigillin-Begriffe)
und einer Historie, die nur mit Kenntnis des ursprünglichen Diskurses
Sinn ergibt. Für ein Forschungslabor ist das völlig in Ordnung — es
kollidiert aber mit dem Ziel, eine öffentlichkeitsfähige, wissenschaftlich
nüchterne Referenzarchitektur zu haben, die auch ohne Kenntnis der
Genesis-Erzählung verstanden und genutzt werden kann.

Der ursprüngliche Multi-AI-Diskurs (siehe
`Planungsdiskurse/ErsterDiskursMonorepoPlattform.txt`) hat das Problem so
zusammengefasst: Micro-Packages und Monorepo sind keine Alternativen,
sondern lösen unterschiedliche Probleme. Micro-Packages liefern
Deployment-Granularität, Versionierungsflexibilität und Experimentierfreude.
Ein Monorepo liefert einheitliche Build-Pipelines, gemeinsame Typen und
Protokolle, konsistente Versionierung und Architektur-Governance.

## Entscheidung

Es wird ein neues, separates Monorepo (Genesis Core / UTAC Core) als
Referenzarchitektur aufgebaut. Unified-Mandala wird **nicht** umbenannt,
refaktoriert oder ersetzt — es bleibt vollständig als Labor und
historische Quelle bestehen ("Zwei-Körper-Trennung"). Das neue Monorepo
zitiert und destilliert aus Unified-Mandala, kopiert dessen Struktur aber
nicht 1:1 (siehe PRINCIPLES.md, Regel 9 — Unified-Mandala ist Quelle,
nicht Ziel).

Dieses Planungsrepo (`Architektur--Planungsprojekt`) ist dabei explizit
der Denkraum *vor* dem eigentlichen Monorepo, nicht das Monorepo selbst.

## Begründung

- Eine nachträgliche Bereinigung von Unified-Mandala selbst würde die
  Historie zerstören, die als Forschungsgedächtnis wertvoll ist.
- Eine klare Trennung erlaubt es, im neuen Monorepo von Anfang an strenge
  Aufnahmekriterien durchzusetzen (Genesis-Blindtest, ADR-Pflicht, kein
  Core ohne LLM-/Internet-Unabhängigkeit — Regeln 3, 6, 7), ohne
  bestehenden Code im Labor sofort migrieren oder löschen zu müssen.
- Der parallele v1.0.0-Sprint der 48 bestehenden Pakete zeigt, dass
  Unified-Mandala als Labor weiterhin aktiv genutzt wird — eine sofortige
  Vereinheitlichung in ein einziges Repo würde diesen Sprint blockieren
  statt ihn zu unterstützen.

## Alternativen betrachtet

**Unified-Mandala selbst schrittweise bereinigen und als
Referenzarchitektur weiterführen.** Verworfen, weil das die explorative
Historie zerstören oder stark verschleiern würde; eine Trennung von
Labor- und Referenz-Funktion wäre im selben Repo ohne klare Statusgrenze
schwer durchsetzbar.

**Alles in den 48 Micro-Packages lassen, kein Monorepo.** Verworfen, weil
das laut Diskurs zu semantischer Drift, Tooling-Overhead und
Dokumentations-Chaos führt — es gibt keine gemeinsame Governance-Ebene
für Typen, Protokolle und Architekturentscheidungen.

## Konsequenzen

Jede Aufnahme eines Moduls aus Unified-Mandala in das neue Monorepo
durchläuft den Genesis-Blindtest (Regel 6) und braucht ein eigenes ADR,
sobald es als `architektur`/`programm`/`hilfsprogramm` auf `accepted`
wechseln soll (Regel 3).
