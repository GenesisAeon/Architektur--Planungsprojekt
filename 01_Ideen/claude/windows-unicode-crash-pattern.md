# Windows-Unicode-Crash-Muster: 5 von 5 gezielt geprüften Kettengliedern betroffen

## Problem

Während der Genesis-Blindtests der Core-Kette fiel wiederholt derselbe
Absturz auf: CLI-Befehle crashen unter Windows-Standardkonsole
(cp1252-Codepage), weil mathematische Unicode-Sonderzeichen (∝, β, σ,
Φ, →, ✓/✗) direkt in `rich`-gerenderte Strings (Typer-`help=`-Texte,
CLI-Ausgaben, teils sogar PyPI-Zusammenfassungen) eingebettet sind.
Ab dem vierten Kettenglied-Test wurde gezielt danach gesucht — das
verdient einen eigenen, ökosystemweiten Befund statt fünf
Einzelerwähnungen in den jeweiligen Blindtest-Einträgen.

## Vorgehen und Durchführung

Fünf unabhängige, kontextfreie Subagenten-Blindtests (Core-Kette,
`medium-modulation`/`cosmic-moment`/`fieldtheory`/`sigillin`/
`utac-core`) liefen jeweils auf echten, frischen Windows-Umgebungen
und dokumentierten den exakten Fehlertext, wo aufgetreten.

## Ergebnis

**Alle fünf gezielt darauf geprüften Kettenglieder zeigen densel­ben
Absturz-Typ:**

| Paket | Auslösendes Zeichen | Betroffener Befehl |
|---|---|---|
| `medium-modulation` | ∝ | `mm --help`, `pip show` |
| `cosmic-moment` | → | `cm collapse` |
| `fieldtheory` (EN) | ∝ | `ft --help`, `pip show` |
| `sigillin` | ✓/✗ | `sig validate`/`inspect`/`render` |
| `utac-core` | β/σ/Φ | alle vier CLI-Befehle (schwerster Fall) |

Immer derselbe Mechanismus: `rich`s Legacy-Windows-Konsolen-Renderer
kann das jeweilige Zeichen auf `cp1252` (Windows-Standard-Codepage)
nicht kodieren, `UnicodeEncodeError: 'charmap' codec can't encode
character ...`. Workaround (`PYTHONIOENCODING=utf-8` /
`PYTHONUTF8=1`) funktioniert, wird aber in keinem der fünf READMEs
erwähnt. Bei `utac-core` betrifft es *alle vier* dokumentierten
Quickstart-Befehle gleichzeitig — ein Windows-Erstnutzer ohne
manuelles UTF-8-Setup bekommt dort keinen einzigen funktionierenden
Befehl.

Die übrigen drei bereits getesteten Kettenglieder
(`entropy-table`, `implosive-genesis`, `entropy-governance`) wurden
nicht gezielt auf dieses Muster geprüft, da es erst beim vierten Test
auffiel — keine Aussage darüber, ob sie betroffen sind oder nicht.

## Erwartetes Ergebnis

Ein einziger, wiederkehrender Root-Cause-Typ statt fünf isolierter
Einzel-Bugs: mathematische Unicode-Symbole in `rich`/Typer-`help=`-
Strings ohne Rücksicht auf Windows-Standard-Terminals. Passt zum
bereits dokumentierten `__version__`-Drift-Muster
(`version-string-drift-audit`) als zweite, unabhängige,
scaffold-artige Fehlerklasse über mehrere Pakete hinweg.

## Nächster Schritt

An Johann weiterzugeben als ökosystemweiter Fix-Vorschlag, nicht als
fünf Einzelkorrekturen: entweder (a) alle mathematischen
Unicode-Zeichen in CLI-Hilfetexten/-Ausgaben durch ASCII-Äquivalente
ersetzen (z. B. "proportional to", "beta", "->"), oder (b) die
Diamond-Setup-Scaffold-Vorlage so anpassen, dass generierte
`cli.py`-Dateien standardmäßig UTF-8-Ausgabe erzwingen (z. B. via
`sys.stdout.reconfigure(encoding="utf-8")` oder eine
Rich-Console-Konfiguration), damit künftige Pakete den Fehler gar
nicht erst erben. Die noch nicht auf dieses Muster geprüften
Kettenglieder (`entropy-table`, `implosive-genesis`,
`entropy-governance`) sollten bei Gelegenheit nachträglich geprüft
werden.

## Alternativen betrachtet

**Als fünf getrennte, paketspezifische Bugs belassen (wie ursprünglich
in den einzelnen Blindtest-Einträgen notiert).** Nicht falsch, aber
unvollständig: ohne diesen zusammenführenden Eintrag sieht es nach
fünf unabhängigen Zufällen aus, statt nach einem einzigen,
systematischen Scaffold-Problem mit einem einzigen sinnvollen Fix.
