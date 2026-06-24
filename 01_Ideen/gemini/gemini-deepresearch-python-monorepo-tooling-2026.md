# Gemini Deep-Research: Python-Monorepo-Tooling fuer GenesisAeon

**Status:** idea · **Epistemic Status:** hypothesis · **Autor:** Gemini
(Recherche), kommentiert von Grok und Claude

## Problem

Nach dem ersten Multi-AI-Diskurs
(`Planungsdiskurse/ErsterDiskursMonorepoPlattform.txt`) hatte Gemini
generische Vorschlaege ohne Repo-Zugriff geliefert
(`01_Ideen/gemini/gemini-architektur-vorschlaege-2026-06`). Claude schlug
daraufhin einen gezielten Deep-Research-Prompt vor, der explizit nach
Versionsstaenden und Beispiel-Links statt nach Lehrbuch-Konzepten fragt.
Das Ergebnis liegt als PDF vor
(`Planungsdiskurse/Wissenschaftliche Python Architektur Recherche.pdf`,
~77 Quellen) und wurde von Grok und Claude kommentiert
(`Planungsdiskurse/ZweitesDoc.txt`). Diese Idee verarbeitet beide
Dokumente repo-konform.

**Wichtiger Vorbehalt:** Die Recherche ist eine Web-Synthese (Stand
2025/2026), nicht durch dieses Repo selbst verifiziert. Keine der
genannten Tool-Versionen, Benchmarks oder Vergleiche wurde gegen die 48
echten GenesisAeon-Pakete getestet. Bleibt `epistemic_status: hypothesis`.

## Vorschlag

1. **Monorepo-Tooling:** `uv workspaces` (Astral) fuer das spaetere
   Genesis-Core-Monorepo. Wurzel-`pyproject.toml` mit
   `[tool.uv.workspace]`, `members = ["core", "plugins/*"]`; jedes Plugin
   referenziert den Core ueber `core = { workspace = true }`. Begruendung:
   schnellere, striktere Isolation als Hatch/PDM/Pants/Bazel; Praezedenzfall
   Apache Airflow (120+ Provider-Pakete via uv workspaces).

2. **Diamond-Interface-Architektur:** `importlib.metadata.entry_points()`
   kombiniert mit `typing.Protocol` (PEP 544) statt Vererbung/ABCs — der
   Core definiert das Interface nur als Protokoll, kein zirkulaerer
   Import. Capability-Negotiation ueber `plugin_api_version` im
   Entry-Point-Metadaten-Dictionary (Vorbild: SpectroChemPy), die der Core
   vor dem Laden prueft.

3. **Release-Automatisierung:** `python-semantic-release` (PSR) ab
   v10.4.0 mit `conventional-monorepo`-Parser, Conventional-Commits-Praefixe
   pro Paket plus `path_filters` — Independent statt Lockstep Versioning.

4. **Architektur-Enforcement in CI:** `import-linter` (AST-basiert) erzwingt
   Schichtenarchitektur (Core unten, Plugins oben, keine Querimporte).
   Ergaenzend: NetworkX-Graphenanalyse (Fan-in/Fan-out) zur objektiven
   Core-Kandidaten-Identifikation beim Schnitt aus unified-mandala.

5. **Governance/Foerderfaehigkeit:** `log4brains` (MADR) fuer ADRs,
   REUSE-Spezifikation (SPDX-Header) und `CITATION.cff` im Root —
   Voraussetzungen fuer Sovereign Tech Fund und FAIR4RS/EU-Horizon.
   Permissive Lizenz fuer den Core, gemischte Lizenzen pro Plugin moeglich
   (keine GPL-Viralitaet, da Plugins nur dynamisch geladen werden).

6. **Reproduzierbarkeit als Hartkriterium:** `uv.lock` + Nix Flakes fuer
   bit-exakte Offline-Reproduzierbarkeit bei der Zenodo-Archivierung,
   Property-based Testing (Hypothesis), Pure-Python-Fallback-Pattern
   (`try: import genesis_rust_accel` → Fallback auf NumPy/JAX).

7. **Grok/Claude-Ergaenzungen aus dem begleitenden Gespraech** — auffaellig
   ist, dass die meisten davon bereits durch bestehende Regeln dieses
   Planungsrepos abgedeckt sind, ohne dass Grok/Claude den vollen
   Regelkatalog im Detail referenziert haben:
   - Genesis-Blindtest operationalisieren (`pip install` + Quickstart +
     5 Minuten) — deckungsgleich mit `PRINCIPLES.md` Regel 6.
   - `epistemic_status` als Pflichtfeld — deckungsgleich mit Regel 5 und
     `contracts/trylayer.schema.yaml`.
   - Graveyard/Experimental-Verzeichnis — deckungsgleich mit `archive/`
     und Regel 11.
   - `genesis-scope` als ersten Blindtest-Testfall — identisch mit
     `01_Ideen/claude/genesis-scope-blindtest`.
   - Formatdisziplin im Architektur-Repo selbst — deckungsgleich mit dem
     Trylayer-Zwang (Regel 1).

## Erwartetes Ergebnis

- Pruefung, welche Punkte ADR-Kandidaten fuer das spaetere Monorepo sind
  (1–6) und welche nur eine unabhaengige Bestaetigung bestehender Regeln
  dieses Planungsrepos sind (7).
- Punkte 1–5 bilden eine konsistente, technisch begruendete Kurzliste fuer
  `04_Programme`/`05_Hilfsprogramme`, sobald die Inventarisierung des
  eigentlichen Monorepos beginnt.
- Kein Punkt ist durch dieses Repo selbst verifiziert — bleibt Hypothese.

## Naechster Schritt

Maintainer entscheidet: (a) ob 1–5 als separate ADR-Entwuerfe vorbereitet
werden, wenn die Monorepo-Inventarisierung beginnt (vgl. `STATUS.md`,
"Weitere ADRs: Warum uv-Workspace? Warum Diamond Interface als
Protocol?"), (b) ob Punkt 7 ohne neuen Trylayer-Eintrag bleibt, da er nur
bestaetigt, und (c) ob Punkt 6 (Nix/PBT/Fallback) eine eigene, praezisere
Idee mit Bezug auf ein konkretes Paket aus `ECOSYSTEM_MAP.yaml` verdient.

## Betrachtete Alternativen

- Direkt als `architektur`/`programm` einordnen — verworfen: betrifft das
  spaetere Monorepo, nicht dieses Planungsrepo, kein ADR/Blindtest hier
  durchlaufen (Regel 3, 6).
- `gemini-architektur-vorschlaege-2026-06` editieren statt neuer Eintrag —
  verworfen: Regel 2 sieht Verschieben statt Editieren fuer reifende
  Ideen vor; `derived_from` dokumentiert die Herkunft stattdessen.
- Punkt 7 ignorieren, da redundant — verworfen: die Redundanz selbst ist
  ein Befund (zwei unabhaengige KI-Systeme bestaetigen unabhaengig
  Regeln, die sie nicht vollstaendig gesehen haben).
