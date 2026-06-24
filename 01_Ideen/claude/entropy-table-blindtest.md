# Genesis-Blindtest für `entropy-table` (Core-Kandidat): technisch defekt, nicht nur semantisch unklar

**Status:** idea · **Epistemic Status:** measured · **Autor:** Claude

## Warum dieses Paket

`entropy-table` ist nach `02_Plaene/genesis-core-scope.md` der erste
Schritt der vorgeschlagenen Core-Kette (`entropy-table` ->
`implosive-genesis` -> ... -> `utac-core`). Nach der Präzisierung in
`01_Ideen/claude/blindtest-baseline-fuer-monorepo-readme` **muss** ein
Core-Kandidat den Blindtest bestehen, anders als Satelliten-Pakete.
Johann hat das vollständige, wörtliche README
(github.com/GenesisAeon/entropy-table) im Chat eingebracht; ein
frischer kontextfreier Subagent hat es real getestet.

## Durchführung

2026-06-24, ein frischer Subagent ohne GenesisAeon-Vorwissen, kein
Web-Zugriff auf Hintergrund. Versuch von zwei Pfaden: (1) `pip install
entropy-table` + CLI-Exploration, (2) `git clone` + `uv sync` +
Quickstart-Kommandos aus der README. Pfad 2 konnte technisch nicht
ausgeführt werden (siehe unten).

## Befund Pfad 1: pip install

- **Install**: `pip install entropy-table` installiert **v2.0.0**,
  nicht das in der README behauptete "v1.0.0 stable" —
  Versionsdiskrepanz zwischen README und PyPI.
- **Bug: fehlende Dependency**: `entropy-table --help` wirft sofort
  `ModuleNotFoundError: No module named 'typer'` — `typer` wird von
  `cli.py` verwendet, ist aber nicht als Dependency deklariert. Erst
  nach manuellem `pip install typer` startet die CLI überhaupt.
- **Bug: keine Daten im Paket**: Das PyPI-Paket enthält kein `atlas/`-
  Verzeichnis (Domains/Relations/Claims) — nur `cli.py`, `compute/`,
  `core/`, `commands/`. Es gibt schlicht keine Beispieldaten, gegen die
  irgendein Befehl etwas zeigen könnte.
- **Bug: `validate-all` crasht**: `entropy-table validate-all` stürzt
  ab mit `FileNotFoundError` für einen hartkodierten relativen Pfad
  (z.B. `.../site-packages/.../atlas/schema/domain.schema.json`), der
  voraussetzt, dass man aus dem Quellrepo heraus arbeitet, nicht aus
  einem installierten Paket.
- **Bug: `health` schreibt an falschen Ort**: `entropy-table health
  --ci-check` "gelingt" technisch, schreibt aber `outputs/
  atlas_health.md` an einen offensichtlich falschen Ort (unter dem
  Python-site-packages-Pfad) — Pfadauflösung auch hier fehlerhaft, nur
  nicht fatal. Inhalt: Total Domains: 0, Total Relations: 0, Total
  Claims: 0, alle Checks vakuos "erfolgreich".
- **Bug: CLI-Hilfetext lügt**: Das genaue Quickstart-Kommando
  `entropy-table metrics --format markdown` aus der README schlägt
  fehl: `error: unrecognized arguments: --format markdown` — obwohl
  `entropy-table metrics --help` `--format` als gültige Option
  auflistet. Hilfetext und tatsächlicher Argument-Parser widersprechen
  sich.

## Befund Pfad 2: git clone

Konnte in der Sandbox nicht ausgeführt werden: `git clone` auf
github.com sowie `WebFetch` auf `raw.githubusercontent.com` scheiterten
am Netzwerk-Proxy (403), und das GitHub-MCP-Tool hat
`genesisaeon/entropy-table` nicht im erlaubten Repo-Scope dieser
Session. Der Subagent hat dies explizit als ungetesteten, nicht
fabrizierten Pfad gemeldet, statt Ergebnisse zu erfinden — selbst ein
relevanter Befund: die README setzt uneingeschränkten GitHub-Zugriff
voraus und bietet keinen funktionierenden Fallback (z.B. Beispieldaten
im PyPI-Paket) für Umgebungen mit eingeschränktem Netzwerk.

## Bewertung

Anders als bei `genesis-scope`/`genesis-os` (technisch lauffähig, aber
semantisch nicht interpretierbar) ist der Befund hier stärker:
`entropy-table` ist auf dem per README dokumentierten Pip-Install-Pfad
schlicht **defekt** — fehlende Dependency, fehlende Daten, hartkodierte
Pfade, ein Hilfetext, der nicht zum tatsächlichen Parser passt. Kein
einziger Befehl hat jemals echten wissenschaftlichen Inhalt
(Entropieproduktionsraten, Markov-Ketten, Lindblad-Gleichungen)
gezeigt — alle Kommandos enden in Crashes oder vakuosen Nullresultaten.
Blindtest (Regel 6) damit klar **FALSE**, mit einer stärkeren
Implikation als bei den vorherigen Tests: hier ist nicht nur die
Interpretierbarkeit unklar, sondern die Grundfunktion selbst nicht
demonstrierbar.

## Einordnung als Core-Kandidat

Nach `blindtest-baseline-fuer-monorepo-readme` muss ein Core-Kandidat
den Blindtest bestehen, bevor er `status: accepted` erhält.
`entropy-table` als erster Schritt der vorgeschlagenen Core-Kette
scheitert nicht nur am Maßstab, sondern bereits an grundlegender
Funktionsfähigkeit des Pip-Install-Pfads — das ist ein konkretes
technisches Risiko für `02_Plaene/genesis-core-scope.md`, nicht nur
eine Dokumentationsfrage.

## Erwartetes Ergebnis

- `entropy-table` besteht den Genesis-Blindtest (Regel 6) in der
  jetzigen pip-install-Form **nicht**.
- Die gefundenen Bugs (fehlende `typer`-Dependency, fehlende
  Atlas-Daten im Paket, hartkodierte Pfade, CLI-Hilfetext-Diskrepanz)
  sind konkrete, behebbare technische Probleme — kein architektonisches
  Problem wie bei `genesis-scope`. Das unterscheidet diesen Befund von
  den vorherigen.
- Der git-clone-Pfad bleibt ungetestet (Sandbox-Netzwerkbeschränkung)
  — möglich, dass dieser Pfad funktioniert und die README dort korrekt
  wäre; das muss separat verifiziert werden, sobald Zugriff besteht.

## Einordnung durch Johann

Johann (Chat, 2026-06-24): nicht sicher, aber vermutet, dass es nach
dem v1.0.0-Sprint noch offene CI-Fehler gab, die erst behoben werden
sollten, sobald alle 48/49 Pakete auf PyPI verfügbar sind — die
gefundenen Bugs könnten also bereits bekannte, in Arbeit befindliche
Probleme sein, kein neuer Befund für die Maintainer. Unabhängig davon
räumt er ein: die README-Behauptung "v1.0.0" ist nicht konform mit dem
tatsächlich installierten v2.0.0 — dieser Punkt bleibt ein echter
Befund, kein Sandbox-Artefakt.

## Nächster Schritt

Nicht mehr als ungemeldeten Bugreport behandeln, da die gefundenen
Probleme vermutlich Teil einer bereits bekannten, laufenden
Post-Sprint-CI-Bereinigung sind (unbestätigt). Stattdessen offen
lassen, bis der Sprint/die CI-Bereinigung abgeschlossen ist, und den
Blindtest dann erneut durchführen — der jetzige FALSE-Befund bleibt als
Messwert zum jetzigen Zeitpunkt stehen (Regel 11, kein Löschen), gilt
aber nicht als finales Urteil über das fertige Paket. Die
README/PyPI-Versionsdiskrepanz (v1.0.0 behauptet, v2.0.0 installiert)
bleibt als eigenständiger, unabhängig vom CI-Stand bestehender Befund.

## Betrachtete Alternativen

- Den Befund als reine Interpretierbarkeitsfrage wie bei
  `genesis-scope` behandeln — verworfen: die gefundenen Probleme sind
  echte Crashes/fehlende Dependencies, kein Interpretationsproblem.
- Ergebnisse für den ungetesteten git-clone-Pfad spekulativ ausfüllen,
  um eine vollständigere Bewertung zu liefern — verworfen: widerspricht
  Regel 5 (ehrlicher `epistemic_status`); der Subagent hat zurecht
  keine erfundenen Ergebnisse gemeldet.
