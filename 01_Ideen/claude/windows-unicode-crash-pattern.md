# Windows-Unicode-Crash-Muster: 9 von 9 gezielt geprüften Paketen betroffen, plus stille Mojibake-Variante

## Problem

Während der Genesis-Blindtests der Core-Kette fiel wiederholt derselbe
Absturz auf: CLI-Befehle crashen unter Windows-Standardkonsole
(cp1252-Codepage), weil mathematische Unicode-Sonderzeichen (∝, β, σ,
Φ, φ, π, α, →, ✓/✗, Subskript-Ziffern) direkt in `rich`-gerenderte
Strings (Typer-`help=`-Texte, CLI-Ausgaben, teils sogar
PyPI-Zusammenfassungen) eingebettet sind. Ab dem vierten
Kettenglied-Test wurde gezielt danach gesucht — das verdient einen
eigenen, ökosystemweiten Befund statt isolierter Einzelerwähnungen in
den jeweiligen Blindtest-Einträgen. Zusätzlich zeigte sich bei zwei
weiteren Paketen eine zweite, verwandte, aber unterscheidbare
Ausprägung: **stille Mojibake-Korruption statt Absturz** — `rich`s
Legacy-Windows-Fallback verschluckt den Kodierungsfehler manchmal und
druckt `�`/falsche Zeichen, statt eine Exception zu werfen.

## Vorgehen und Durchführung

Neun unabhängige, kontextfreie Subagenten-Blindtests liefen jeweils auf
echten, frischen Windows-Umgebungen (Core-Kette:
`medium-modulation`/`cosmic-moment`/`fieldtheory`/`sigillin`/
`utac-core`; Programm-Kandidaten: `sonification`/`cosmic-web`/
`mirror-machine`/`climate-dashboard`; Orchestrierungskern:
`unified-mandala`) und dokumentierten den exakten Fehlertext, wo
aufgetreten.

## Ergebnis

**Absturz-Variante — neun von neun gezielt darauf geprüften Pakete
betroffen:**

| Paket | Auslösendes Zeichen | Betroffener Befehl |
|---|---|---|
| `medium-modulation` | ∝ | `mm --help`, `pip show` |
| `cosmic-moment` | → | `cm collapse` |
| `fieldtheory` (EN) | ∝ | `ft --help`, `pip show` |
| `sigillin` | ✓/✗ | `sig validate`/`inspect`/`render` |
| `utac-core` | β/σ/Φ | alle vier CLI-Befehle (schwerster Fall in der Core-Kette) |
| `sonification` | β | `soni entropy-gate` (nach korrektem MIDI-Write) |
| `cosmic-web` | ≈ | `cweb render` (allererster Quickstart-Befehl) |
| `unified-mandala` | ₀/→/₂/α/φ/π/− | 8 von 9 CLI-Befehlen (breitester Einzelfall überhaupt) |

Immer derselbe Mechanismus: `rich`s Legacy-Windows-Konsolen-Renderer
kann das jeweilige Zeichen auf `cp1252` (Windows-Standard-Codepage)
nicht kodieren, `UnicodeEncodeError: 'charmap' codec can't encode
character ...`. Workaround (`PYTHONIOENCODING=utf-8` /
`PYTHONUTF8=1`) funktioniert durchgängig, wird aber in keinem der neun
READMEs erwähnt. Bei `unified-mandala` zeigte sich eine wichtige
Nuance: das Risiko ist konsolenabhängig — eine native, interaktive
PowerShell-7-Sitzung ist unter PEP 528 automatisch UTF-8-fähig und
crasht nicht, während git-bash/MSYS-Terminals, Output-Umleitung
(`| Out-File`) und ältere PowerShell-5.1-Konfigurationen den Fehler
real auslösen — also weiterhin ein sehr plausibles Szenario für einen
grossen Teil realer Windows-Entwicklungsumgebungen.

**Stille Mojibake-Variante — zwei bestätigte Fälle (kein Absturz, aber
falsche Ausgabe):**

| Paket | Betroffenes Zeichen | Effekt |
|---|---|---|
| `mirror-machine` | Gedankenstrich | wird lautlos zu `�` statt zu crashen |
| `climate-dashboard` | Box-Zeichnungszeichen | Tabellenrahmen im Dashboard-Footer korrumpiert |

Diese Variante ist potenziell tückischer als der harte Absturz: ein
Nutzer merkt nicht, dass etwas falsch ist — das Programm läuft
"erfolgreich" durch, liefert aber sichtbar kaputten Text, was Regel 6
("sinnvolles, korrektes Ergebnis") auf eine andere Art verletzt als ein
klarer Crash.

Die übrigen, nicht gezielt auf dieses Muster geprüften Pakete
(`entropy-table`, `implosive-genesis`, `entropy-governance`,
`mandala-visualizer`, `implosive-origin-utac`) machen keine Aussage
darüber, ob sie betroffen sind oder nicht — bei `mandala-visualizer`
wurde stattdessen eine verwandte, aber andere Absturz-Variante
gefunden (Crash *nach* erfolgreichem Datei-Export, siehe
`mandala-visualizer-blindtest`).

## Erwartetes Ergebnis

Ein einziger, wiederkehrender Root-Cause-Typ (plus eine verwandte
stille Variante) statt neun isolierter Einzel-Bugs: mathematische
Unicode-Symbole in `rich`/Typer-`help=`-Strings ohne Rücksicht auf
Windows-Standard-Terminals. Passt zum bereits dokumentierten
`__version__`-Drift-Muster (`version-string-drift-audit`) als zweite,
unabhängige, scaffold-artige Fehlerklasse über praktisch das gesamte
Ökosystem hinweg — von den kleinsten Core-Kettengliedern bis zum
grössten getesteten Paket (`unified-mandala`, 8 von 9 CLI-Befehlen).

## Nächster Schritt

An Johann weiterzugeben als ökosystemweiter Fix-Vorschlag, nicht als
neun Einzelkorrekturen: entweder (a) alle mathematischen
Unicode-Zeichen in CLI-Hilfetexten/-Ausgaben durch ASCII-Äquivalente
ersetzen (z. B. "proportional to", "beta", "->"), oder (b) die
Diamond-Setup-Scaffold-Vorlage so anpassen, dass generierte
`cli.py`-Dateien standardmäßig UTF-8-Ausgabe erzwingen (z. B. via
`sys.stdout.reconfigure(encoding="utf-8")` oder eine
Rich-Console-Konfiguration), damit künftige Pakete den Fehler gar
nicht erst erben — sowie (c) einen expliziten `PYTHONIOENCODING=utf-8`-
Hinweis in alle betroffenen READMEs, solange (b) noch nicht
ökosystemweit umgesetzt ist. Die noch nicht auf dieses Muster
geprüften Pakete (`entropy-table`, `implosive-genesis`,
`entropy-governance`, `implosive-origin-utac`) sollten bei Gelegenheit
nachträglich geprüft werden.

## Alternativen betrachtet

**Als neun getrennte, paketspezifische Bugs belassen (wie ursprünglich
in den einzelnen Blindtest-Einträgen notiert).** Nicht falsch, aber
unvollständig: ohne diesen zusammenführenden Eintrag sieht es nach neun
unabhängigen Zufällen aus, statt nach einem einzigen, systematischen
Scaffold-Problem mit einem einzigen sinnvollen Fix.

**Die stille Mojibake-Variante als denselben Befund wie den harten
Absturz behandeln, ohne sie separat zu kennzeichnen.** Verworfen: beide
haben denselben Root-Cause (cp1252-Inkompatibilität), aber
unterschiedliche Nutzer-Konsequenzen (sichtbarer Fehler vs. unbemerkt
falsches Ergebnis) — für die Priorisierung eines Fixes und für Regel 6
ist diese Unterscheidung relevant.
