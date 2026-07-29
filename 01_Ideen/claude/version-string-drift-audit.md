# Versions-Drift-Audit: `__version__` in `__init__.py` läuft bei mind. 5 Paketen vom echten Release auseinander

## Problem

`entropy-table` und `implosive-genesis` hatten beide eine
README-vs-PyPI-Versions-Diskrepanz. `ecosystem-verifizierbare-daten-audit`
vermutete daraus ein systematisches Release-Hygiene-Problem über den
ganzen v1.0.0-Sprint. Das brauchte eine echte, mechanische Prüfung
über alle 48 Pakete, nicht nur die zwei bereits bekannten Fälle.

## Vorgehen und Durchführung

Ein Skript hat für jedes lokal vorliegende Paket (47 von 48 haben
einen lokalen Checkout unter `D:\mandala\<repo>`) drei Werte verglichen:
`pyproject.toml`s `version`-Feld, die tatsächlich auf PyPI publizierte
neueste Version (`pip index versions <name>`), und Versions-Erwähnungen
im README-Fließtext. Erste Rohergebnisse enthielten viel Rauschen
(README-Erwähnungen alter Versionen in Changelog-artiger Prosa sind
normal, keine Bugs) — deshalb zusätzlich gezielt der `__version__`-String
in jedes Pakets `src/<paket>/__init__.py` geprüft, der eigentlich
Release-Version und Paket-Metadatum synchron halten sollte.

## Ergebnis

**Eine echte Diskrepanzklasse bestätigt: mindestens 5 von 47 geprüften
Paketen haben ein internes `__version__` in `__init__.py`, das beim
Diamond-Setup-Scaffold-Standardwert `"0.1.0"` steckengeblieben ist,
obwohl `pyproject.toml` und PyPI längst 1.0.0/1.1.0 zeigen:**

| Paket | `__version__` in `__init__.py` | `pyproject.toml`/PyPI |
|---|---|---|
| `entropy-governance` | `0.1.0` | `1.0.0` |
| `quantum-genesis` | `0.1.0` | `1.0.0` |
| `AdvancedWeightingSystems` | `0.1.0` | `1.0.0` |
| `universums-sim` | `0.1.0` | `1.0.0` |
| `cosmic-moment` | `0.1.0` | `1.0.0` |

Zum Vergleich, korrekt synchronisiert: `diamond-setup` (2.2.0),
`spiking-aeon` (1.0.0), `cellular-genesis` (1.0.0), `worldview` (1.0.0),
`genesis-os` (1.0.11) — der Fehler ist also nicht universell, aber
real und wiederkehrend, kein Einzelfall.

**Das ist nicht kosmetisch — direkt bestätigt am Beispiel
`entropy-governance-blindtest`:** die veraltete `__version__`-Zeichenkette
leckt in `eg version`s Ausgabe und in jede von `table-export` erzeugte
YAML-Datei (`metadata.version: 0.1.0`), obwohl das tatsächlich
installierte Paket 1.0.0 ist. Jeder, der Exportdaten weitergibt, gibt
damit eine falsche Versionsangabe mit.

`amoc-utac` zeigt eine kleinere, andere Variante desselben
Musters: `pyproject.toml` sagt 1.1.0, PyPI hat aber bereits 1.1.1 —
hier ist der lokale Checkout hinter der veröffentlichten Version
zurück, nicht das Paket selbst inkonsistent.

**Nachtrag (2026-07-29) — grösster bisher gefundener Einzelfall:**
`unified-mandala` (siehe `unified-mandala-blindtest`) zeigt dasselbe
Grundmuster in deutlich grösserer Sprungweite: `pip show` liefert die
tatsächlich installierte PyPI-Version **1.0.0**, während sowohl das
interne `__version__` als auch das CLI-eigene Banner bei **0.3.2**
verharren — mehrere Minor-/Major-Releases Rückstand, nicht nur ein
einzelner vergessener Scaffold-Default. Bestätigt, dass dieses Muster
nicht auf kleine Core-Kettenglieder beschränkt ist, sondern auch das
grösste bisher getestete Paket betrifft.

## Erwartetes Ergebnis

Ein klar abgegrenzter, wiederkehrender Bug-Typ (stale `__version__` in
`__init__.py`, wahrscheinlich ein Diamond-Setup-Scaffold-Default, der
beim ersten echten Release-Bump vergessen wurde) statt vager
README-Versions-Verwirrung. Betrifft mindestens 5 Pakete, potenziell
mehr, die (noch) nicht einzeln durch den Blindtest gelaufen sind.

## Nächster Schritt

An Johann weiterzugeben: `__version__` in den fünf genannten Paketen
auf den echten Release-Stand heben, idealerweise durch Kopplung an
`pyproject.toml` (z. B. via `importlib.metadata.version(__name__)`
statt hartkodierter Zeichenkette) ersetzen, um erneutes Auseinanderlaufen
strukturell auszuschließen. Für `amoc-utac`: lokalen Checkout auf
1.1.1 synchronisieren. Diese fünf (plus `amoc-utac`) sind noch nicht
einzeln blindgetestet — falls sie später in die Core-Kette aufgenommen
werden sollen, gehört der `__version__`-Fix zu den Vorbedingungen.

## Alternativen betrachtet

**Jede rohe README-Versionserwähnung als Bug werten (erster, zu
naiver Skript-Durchlauf).** Verworfen: erzeugte zu viele
Falsch-Positive aus normaler Changelog-Prosa (z. B.
`implosive-genesis`s README erwähnt 0.1.0–0.4.0 als Historie, kein
aktueller Fehlbezug). Stattdessen der präzisere, tatsächlich
nutzer-sichtbare `__version__`-String direkt geprüft.
