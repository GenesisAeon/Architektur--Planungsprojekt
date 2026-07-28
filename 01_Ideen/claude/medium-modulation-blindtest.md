# Genesis-Blindtest für `medium-modulation`: FALSE, mit totem Parameter und Windows-Crash

## Problem

`medium-modulation` (P-MEDIUM) ist das vierte Kettenglied der Core-Kette
(nach `entropy-table` TRUE, `implosive-genesis` TRUE,
`entropy-governance` FALSE). Muss laut Regel 6 den Genesis-Blindtest
bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real und führte jeden
dokumentierten Befehl/API-Aufruf aus — gleiche Methodik wie bei den
vorherigen Kettenglied-Tests.

## Ergebnis

**Install:** `medium-modulation 1.0.0` installierte sauber (zieht
`entropy-governance 1.0.0`, `entropy-table 2.0.1`,
`implosive-genesis 1.0.0` als echte Abhängigkeiten).

**Vier echte, verifizierte Bugs:**

1. **`mm --help` crasht unter Windows.** Die CLI-Hilfe (und die PyPI-
   Zusammenfassung) enthält das Zeichen "∝" — nicht darstellbar in
   cp1252, dem Windows-Standard-Terminal-Encoding.
   `UnicodeEncodeError: 'charmap' codec can't encode character '∝'`.
   Ein Windows-Erstnutzer, der `mm --help` vor den dokumentierten
   Befehlen ausprobiert, crasht sofort.
2. **`__version__` = "0.1.0" vs. installiert 1.0.0** — derselbe
   Scaffold-Rest-Bug wie in mindestens 5 anderen Paketen (siehe
   `version-string-drift-audit`), hier ein sechster bestätigter Fall.
3. **`coupling_factor`s `modulation_depth`-Parameter hat keinerlei
   Effekt.** Verifiziert: `coupling_factor(A=1.0, V=1.618,
   modulation_depth=0.0/0.5/0.99)` liefert immer exakt
   `1.236054994952565`. Ursache: die Funktion ruft intern
   `modulated_entropy(..., t=0.0)` auf, und der Modulationsterm ist
   `1 + depth·sin(freq·t)` — mit hartkodiertem `t=0.0` ist
   `sin(freq·0)=0` immer, der `depth`-Term also immer mit Null
   multipliziert. Die Funktion ist als "dynamic coupling strength" /
   "tunable... depth" dokumentiert, ist aber tatsächlich ein
   statischer, depth- und frequenzunabhängiger gewichteter Mittelwert
   `φ⁻¹·A + (1−φ⁻¹)·V`. Direkte Konsequenz: `modulated_entropy` und
   `coupling_factor` liefern in den README-Beispielen numerisch
   identische Werte (`1.236054994952565` bei beiden), obwohl als zwei
   verschiedene physikalische Konzepte präsentiert.
4. **CLI hat drei Subcommands (`modulate`, `spectrum`, `couple`), README
   dokumentiert nur zwei** — `couple` (genau der Befehl mit dem
   toten Parameter aus Bug 3) ist im Quickstart gar nicht erwähnt.

**Blindtest-Verdikt: FALSE.** Keine Referenzskala/Einheit für
`S_mod`/`kappa`/Spektrum-Werte, keine Erklärung, warum zwei angeblich
unterschiedliche Konzepte identische Zahlen liefern (was sich als
echter Bug herausstellt, nicht als Zufall), und "Resonanzspektrum"
suggeriert physikalische Struktur (Peak/Resonanzfrequenz/Dämpfung),
die der Code nicht hat — es ist ein reiner Sinus, ausgewertet an den
Stichprobenpunkten selbst.

## Erwartetes Ergebnis

Vierter FALSE-Befund in der Kette (nach `genesis-scope`, `genesis-os`,
`entropy-governance`), mit konkreten, technischen Bugs wie bei
`entropy-governance` — kein reines Interpretierbarkeitsproblem.

## Nächster Schritt

Drei Findings zur Weitergabe an Johann: (1) `∝`-Zeichen aus
CLI-Hilfetext/PyPI-Summary entfernen oder Encoding absichern; (2)
`modulation_depth` in `coupling_factor`/`mm couple` tatsächlich wirksam
machen (der `t=0.0`-Hardcoding-Bug); (3) `__version__`-Sync, siehe
`version-string-drift-audit` (jetzt 6. bestätigter Fall:
`medium-modulation` ergänzt die Liste). `02_Plaene/genesis-core-scope.md`
entsprechend ergänzt.

## Alternativen betrachtet

**Den Unicode-Crash als reines Windows-Randproblem abtun.** Verworfen:
ein erheblicher Teil realer Erstnutzer dürfte auf Windows mit
Standard-Codepage arbeiten — das ist kein exotischer Edge Case, sondern
eine reale Zugangsbarriere direkt beim ersten dokumentierten Befehl
(`--help`).
