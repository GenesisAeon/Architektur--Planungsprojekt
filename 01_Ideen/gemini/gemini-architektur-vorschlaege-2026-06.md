# Gemini-Vorschläge zu ADR-Prozess, Plugin-Interface, Workspace, Releases und Core-Identifikation

**Status:** idea · **Epistemic Status:** hypothesis · **Autor:** Gemini

## Problem

Gemini hatte keinen direkten Zugriff auf dieses Repo (Zugriff verweigert
oder privat) und hat seine Vorschläge daher aus Allgemeinwissen über das
GenesisAeon-Ökosystem formuliert — ohne `PRINCIPLES.md`, `AGENTS.md` oder
den bestehenden ADR-Prozess (`adr/adr-001-warum-monorepo`) gesehen zu
haben. Die Vorschläge überlappen teils mit bereits getroffenen
Entscheidungen.

## Vorschlag

1. **ADR-Tooling (log4brains):** Statische, durchsuchbare ADR-Website
   generieren. Das Repo hat aber schon einen eigenen, schlankeren
   Trylayer-Tripel-ADR-Prozess — log4brains wäre höchstens Ergänzung,
   kein Ersatz.
2. **Plugin-Interface ("Diamond Interface"):** `typing.Protocol`
   (PEP 544) für strukturelle Typisierung statt Vererbung; Capability
   Negotiation über `importlib.metadata`-Entry-Points mit einer
   `plugin_api_version`, die der Core vor dem Laden prüft, um
   inkompatible Plugins ohne Laufzeitfehler abzuweisen.
3. **uv-Workspace-Struktur:** zentrale `pyproject.toml` mit
   `[tool.uv.workspace]`, `members = ["plugins/*"]`; Plugins referenzieren
   den Core lokal über `workspace = true`. Dazu `import-linter` in der CI
   gegen Querabhängigkeiten zwischen Plugins.
4. **Release-Automatisierung:** Independent Versioning + Conventional
   Commits via `python-semantic-release` (conventional-monorepo-Parser)
   mit `path_filters` pro Plugin, sodass z.B. `feat(worldview): ...` nur
   die Version von `worldview` anhebt.
5. **Core-Identifikation per AST-Analyse:** Fan-in/Fan-out-Metriken via
   Graphenanalyse, um Module mit hohem Fan-in/niedrigem Fan-out objektiv
   als Core-Kandidaten zu identifizieren statt rein gefühlsbasiert.

## Erwartetes Ergebnis

- Prüfung durch den Maintainer, welche der fünf Punkte gegenüber
  ADR-001 und `PRINCIPLES.md` neue Information liefern vs. bereits
  abgedeckt sind.
- Punkte 2 und 5 sind konkrete, prüfbare Techniken für offene Probleme
  dieses Repos (Diamond-Interface, Core-Abgrenzung) — Kandidaten für
  eigene, präzisere Ideen.
- Punkte 1 und 3 sind Tooling-Entscheidungen für das *spätere* Monorepo,
  nicht für dieses Planungsrepo.

## Nächster Schritt

Maintainer entscheidet, ob einzelne Punkte (insbesondere Capability
Negotiation per Entry-Point-Metadaten und Fan-in/Fan-out-Analyse für die
Core-Auswahl) als eigene Ideen mit konkretem Bezug zu den 48 bestehenden
Paketen aufgenommen werden, oder ob die Vorschläge zu generisch/redundant
sind.

## Betrachtete Alternativen

- Direkt als `architektur`/`programm` einordnen — verworfen, da Gemini
  das Repo nicht gesehen hat und Genesis-Blindtest sowie ADR-Pflicht
  (Regel 3, 6) noch nicht durchlaufen wurden.
- Ignorieren, da generisch — verworfen, weil Punkte 2 und 5 konkrete,
  prüfbare Techniken für offene Probleme sind.
