# Genesis-Blindtest für `implosive-genesis` (Core-Kandidat, 2. Kettenglied): TRUE mit zwei kleinen Doku-Bugs

**Status:** idea · **Epistemic Status:** measured · **Autor:** Claude

## Warum dieses Paket

`implosive-genesis` ist nach `02_Plaene/genesis-core-scope.md` das
zweite Glied der vorgeschlagenen Core-Kette (`entropy-table` ->
`implosive-genesis` -> `entropy-governance` -> ... -> `utac-core`).
`entropy-table` hat den Blindtest in v2.0.1 bestanden (siehe
`01_Ideen/claude/entropy-table-blindtest`) — `implosive-genesis` ist
der nächste zu prüfende Baustein. Johann hat das vollständige, wörtliche
README (github.com/GenesisAeon/implosive-genesis) im Chat eingebracht;
ein frischer kontextfreier Subagent hat es real getestet.

## Durchführung

2026-06-25, ein frischer Subagent ohne GenesisAeon-Vorwissen, kein
Web-Zugriff auf Hintergrund. `pip install implosive-genesis` +
CLI-Exploration aller dokumentierten Befehle + Python-API-Beispiel aus
dem README, alle real ausgeführt in einer frischen venv.

## Befund: Install

`pip install implosive-genesis` installiert **v1.0.0**. Das README
behauptet an mehreren Stellen "v0.4.0 (current — final release)" —
Versionsdiskrepanz analog zu `entropy-table`, aber die Installation
selbst läuft sauber ohne fehlende Dependencies. Auffällig: der interne
Banner von `ig chronology-validate` zeigt weiterhin "v0.4.0" an, obwohl
`pip show`/`ig version` v1.0.0 melden — die Versionsangabe ist nicht
konsistent über den Code verteilt.

## Befund: CLI

**Funktionierend** — 6 von 8 dokumentierten Befehlen liefern echten,
interpretierbaren numerischen Output:

- `ig oipk-calc` (OIPK-Kernel-Tabelle)
- `ig chronology-validate` (10/10 bestanden)
- `ig fractal-render --depth 8 --ascii` (ASCII-Tesserakt)
- `ig entropy-price-sympy --steps 10000` (E_price = 8.944374e-23 J)
- `ig list-templates` (minimal/genesis)
- `ig anesthesia-test --duration 300` (Kohärenzverlust/-erholung)

**Bug: `full-summary` nicht im CLI**: `ig full-summary` — im README als
CLI-Befehl dokumentiert — existiert nicht: `Error: No such command
'full-summary'`. Die Funktion ist nur über die Python-API
(`model.full_summary(...)`) erreichbar, nicht als CLI-Subcommand.
Kritisch: das ist der **erste** in der README-Liste genannte Befehl —
ein Nutzer, der die Liste der Reihe nach abarbeitet, crasht sofort beim
ersten Versuch.

**Bug: `cmb-test`-Flag mit Unterstrich**: `ig cmb-test --n_sim 5000`
(exakt wie im README) crasht: `Error: No such option: --n_sim
(Possible options: --n-sim)`. Die README verwendet Unterstrich, das
tatsächliche Typer-CLI verlangt Bindestrich. Mit korrigiertem
`--n-sim 100` (reduzierte Sample-Zahl wegen Laufzeit) funktioniert der
Befehl und liefert ein echtes Falsifikationsergebnis (FALSIFIZIERT,
p=0.01).

## Befund: Python-API

Alle drei dokumentierten Importe und Aufrufe funktionieren exakt wie im
README beschrieben: `compute_vrig(n=3, samples=5_000, seed=42)` liefert
`V_RIG = 2187.5237 ± 12.0173 km/s` (README-Beispiel zeigt 2187.34 ±
12.02 bei 50.000 Samples statt 5.000 — die Abweichung ist plausibel auf
die geringere Sample-Zahl zurückzuführen, kein Bug). `FramePrinciple.
coherence_length`/`stability_at` liefert eine echte numerische Tabelle.
`ImplosiveGenesisModel().full_summary(n=3, temperature=2.725)` liefert
ein strukturiertes Ergebnisobjekt mit echten physikalisch anmutenden
Zahlen.

## Bewertung

Deutlich besser als der erste `entropy-table`-Befund (v2.0.0):
Installation läuft fehlerfrei, 6 von 8 CLI-Befehlen und die komplette
Python-API liefern sofort echten, interpretierbaren Output ohne jede
manuelle Korrektur. Die zwei gefundenen Probleme sind reine
Dokumentations-/CLI-Konsistenzfehler (fehlender CLI-Wrapper für
`full-summary`, Flag-Namenskonvention Unterstrich vs. Bindestrich),
kein struktureller Defekt wie bei `entropy-table` v2.0.0 (fehlende
Dependency, fehlende Daten, hartkodierte Pfade). Genesis-Blindtest
(Regel 6) damit insgesamt **TRUE**, aber mit einer wichtigen
Einschränkung: weil `full-summary` der **erste** in der README-Liste
genannte Befehl ist, crasht ein Nutzer, der stur der Dokumentation in
Reihenfolge folgt, bereits beim ersten Versuch — das kann einen
ungeduldigen kontextlosen Nutzer durchaus abschrecken, bevor er die
funktionierenden Befehle überhaupt erreicht.

## Einordnung als Core-Kandidat

Im Gegensatz zu `entropy-table` v2.0.0 ist `implosive-genesis` von
Anfang an im Kern funktionsfähig — das technische Fundament
(V_RIG-Berechnung, OIPK-Kernel, Tesseract-Rendering,
Chronology-Validator) liefert echten wissenschaftlichen Content. Die
zwei gefundenen Bugs sind nach demselben Muster wie bei `entropy-table`
konkret und behebbar (CLI-Befehl ergänzen, Flag-Namen synchronisieren),
kein architektonisches Problem. Damit ist `implosive-genesis` als
zweites Kettenglied der Core-Kette der zweite Baustein, der den
verschärften Maßstab für Core-Kandidaten erfüllt — mit offenen, klar
benannten Fixes für die nächste Version.

## Erwartetes Ergebnis

- `implosive-genesis` besteht den Genesis-Blindtest (Regel 6) in der
  jetzigen pip-install-Form **TRUE**, aber mit zwei konkreten
  Dokumentations-/CLI-Bugs, die vor einem `status: accepted` behoben
  werden sollten.
- Versionsdiskrepanz README (v0.4.0 "current") vs. tatsächlich
  installiertes v1.0.0 ist derselbe Bugtyp wie bei `entropy-table` —
  ein wiederkehrendes Muster über mehrere GenesisAeon-Pakete,
  möglicherweise einen gemeinsamen Release-Prozess-Fix wert.
- Die zwei CLI-Bugs (fehlender `full-summary`-Wrapper,
  `--n_sim`/`--n-sim`-Inkonsistenz) sind leicht behebbar und sollten
  als konkrete Findings an den Maintainer (Johann) gemeldet werden.

## Betrachtete Alternativen

- Den Befund trotz der zwei Bugs als FALSE werten, weil der erste
  dokumentierte CLI-Befehl crasht — verworfen: die Mehrheit der Befehle
  und die komplette API funktionieren sofort mit echtem Output, das
  unterscheidet sich qualitativ von `entropy-table` v2.0.0, wo praktisch
  nichts funktionierte. TRUE mit klar benannten Einschränkungen ist die
  ehrlichere Einordnung (Regel 5).
- Den `--n_sim`-Fehler als gravierenden Bug werten — verworfen: es ist
  eine triviale Flag-Namenskonvention (Typer wandelt Unterstriche zu
  Bindestrichen), kein funktionaler Defekt, sobald man die
  Fehlermeldung liest, die den korrekten Namen direkt vorschlägt.
