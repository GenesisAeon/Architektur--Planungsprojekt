# Genesis-Blindtest für `entropy-governance`: FALSE, mit zwei echten Bugs

## Problem

`entropy-governance` (P-GOV-1) ist das dritte Kettenglied der
vorgeschlagenen Core-Kette (`02_Plaene/genesis-core-scope.md`), nach
`entropy-table` (TRUE nach Fix) und `implosive-genesis` (TRUE mit
kleinen Doku-Bugs). Muss laut Regel 6 den Genesis-Blindtest bestehen,
bevor es als `03_Architektur/`-Eintrag mit `status: accepted`
eingereicht werden kann.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent (kein GenesisAeon-Vorwissen)
bekam ausschließlich das vollständige, echte README als Eingabe und
wurde angewiesen, `pip install entropy-governance` real auszuführen,
jeden Quickstart-Befehl real laufen zu lassen und die Ergebnisse
ungeschönt zu berichten — exakt dieselbe Methodik wie bei
`entropy-table-blindtest`/`implosive-genesis-blindtest`.

## Ergebnis

**Install:** `pip install entropy-governance` installierte real
v1.0.0, passend zur README-Zitation. Keine Installationsfehler.

**Quickstart:** Alle vier CLI-Befehle (`eg entropy-price`,
`eg governance-sim`, `eg duality`, `eg table-export`) sowie die
Python-API liefen fehlerfrei und produzierten Werte, die die
dokumentierten Formeln korrekt wiedergeben (verifiziert:
`entropy_price`, `duality_factor` und `crep` stimmen exakt mit ihren
Formeln überein).

**Zwei echte, verifizierte Bugs gefunden:**

1. **`--steps` beeinflusst die "Tesseract Slices"-Tabelle überhaupt
   nicht.** In `cli.py::cmd_governance_sim` ist
   `ts.slice(t_start=0.0, n_steps=4)` hartkodiert. Empirisch bestätigt:
   `--steps 10`, `--steps 200` und `--steps 1000` drucken alle
   dieselbe 4-Zeilen-Tabelle (t=0.0/0.1/0.2/0.3). Das README suggeriert,
   `--steps 200` konfiguriere Tesseract-Slices UND CREP gemeinsam — in
   Wirklichkeit ist die Slice-Tabelle rein dekorativ/statisch.
2. **Versions-String-Inkonsistenz.** `pip show entropy-governance`
   meldet `1.0.0` (passend zu PyPI/Wheel/Zitation), aber das Paket-
   eigene `__version__` in `entropy_governance/__init__.py` ist
   hartkodiert auf `"0.1.0"` — bestätigt durch direkte Code-Prüfung.
   Das ist keine kosmetische Kleinigkeit: `eg version` gibt
   "entropy-governance 0.1.0" aus, und **jede** `table-export`-YAML
   stempelt `metadata.version: 0.1.0`. Wer Domänendaten exportiert,
   bekommt eine Datei, die intern eine andere Version behauptet als
   die tatsächlich installierte.

**Zusätzlicher, nicht-blockierender Befund:** die README-"Physics"-
Sektion zeigt `S(t) = κ·A(t)` und `S(t) = λ·ln V(t)` als Kern-Dualitäts-
Gleichungen. Im Code existieren diese nur als ungenutzte, nie
aufgerufene SymPy-Platzhalter-Symbole (`DUALITY_A`, `DUALITY_V`) —
weder exportiert noch aus CLI/API berechenbar. Tatsächlich berechenbar
sind nur `entropy_price` (eine Ratenformel) und `duality_factor` (eine
gemischte Kombination) — keins von beiden berechnet wörtlich S∝A oder
S∝V wie dargestellt.

**Blindtest-Verdikt: FALSE.** Die Arithmetik ist intern konsistent
und korrekt (mehrfach gegenprobiert), aber es fehlt jede Referenzskala
oder Einheit: nichts im README oder CLI-Output sagt, ob ein gegebener
`P_E`-, `CREP`- oder `D`-Wert sinnvoll, gut, schlecht oder physikalisch
plausibel für "Governance" ist. Zusätzlich: die Tesseract-Tabelle
ignoriert sichtbar eines ihrer eigenen dokumentierten Flags — ein
konkreter technischer Fehler, nicht nur fehlende Interpretierbarkeit
(ähnlich dem `genesis-os`-Befund: Transitions=0 trotz dokumentierten
Schwellenwerts).

## Erwartetes Ergebnis

`entropy-governance` besteht den Genesis-Blindtest in der jetzigen
Form nicht — dritter FALSE-Befund nach `genesis-scope`/`genesis-os`,
aber anders als bei diesen: hier gibt es zusätzlich zwei konkrete,
leicht behebbare technische Bugs (statt reiner
Interpretierbarkeitslücke), plus einen Dokumentations-Implementierungs-
Gap bei den Kern-Physik-Formeln.

## Nächster Schritt

Zwei Findings zur Weitergabe an Johann: (1) `--steps` muss die
Tesseract-Slice-Anzahl tatsächlich steuern, nicht hartkodiert auf 4
bleiben; (2) `__version__` in `entropy_governance/__init__.py` auf
"1.0.0" synchronisieren (und idealerweise automatisiert an
`pyproject.toml` koppeln, um erneutes Auseinanderlaufen zu vermeiden —
siehe `readme-vs-pyproject-version-mismatch-audit` für denselben
Bug-Typ in mind. 4 weiteren Paketen). Re-Test nach Fix vorgesehen,
analog zu `entropy-table`s FALSE→TRUE-Zyklus.
`02_Plaene/genesis-core-scope.md` entsprechend ergänzt.

## Alternativen betrachtet

**Den Befund als reine Interpretierbarkeitslücke werten (wie bei
`genesis-scope`/`genesis-os`).** Verworfen: hier gibt es zusätzlich
zwei konkrete, reproduzierbare technische Bugs (ignoriertes CLI-Flag,
Versions-Inkonsistenz) — das ist eine andere Fehlerklasse und verdient
eigene Nennung, nicht nur "auch semantisch unklar".
