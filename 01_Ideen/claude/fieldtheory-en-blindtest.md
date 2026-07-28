# Genesis-Blindtest für `fieldtheory` (EN): FALSE, mit Lagrangian-Inkonsistenz und Windows-Crash

## Problem

`fieldtheory` (EN, T4) ist das sechste Kettenglied der Core-Kette.
Bereits als eigenständiges, kein Duplikat von `Feldtheorie` (DE)
bestätigt (siehe `fieldtheory-feldtheorie-kein-duplikat`). Muss laut
Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe (explizit angewiesen, es nicht mit
irgendeinem deutschen "Feldtheorie"-Projekt zu verwechseln), installierte
real und führte jeden dokumentierten Befehl/API-Aufruf aus.

## Ergebnis

**Install:** `fieldtheory 1.0.1`. **`__version__` stimmt mit der
installierten Version überein — kein Versions-Bug hier**, im
Gegensatz zu den meisten anderen Kettengliedern (gutes Gegenbeispiel,
zeigt dass der Scaffold-Bug nicht universell ist).

**Drei echte Bugs/Inkonsistenzen gefunden:**

1. **README-eigenes "Override"-Beispiel ist ein No-Op.** Der Quickstart
   zeigt `ft simulate --s-a 1.0 --s-v 1.618 --depth 0.5 --threshold 0.618`
   als Beispiel für Parameter-Override — das sind aber exakt die
   CLI-eigenen Default-Werte. Output ist byte-identisch zum ersten
   Beispiel ohne Flags. Echte Overrides funktionieren nachweislich
   (verifiziert mit `--s-a 5.0 --s-v 0.1 --depth 0.9 --threshold 0.3` →
   andere Werte), aber das dokumentierte Beispiel demonstriert selbst
   keinen einzigen Override.
2. **`ft --help` crasht unter Windows** — derselbe Unicode-Bug-Typ wie
   bei `medium-modulation`: das "∝"-Zeichen im Typer-`help=`-String
   (`cli.py` Zeile 15) ist nicht cp1252-darstellbar. Zweiter
   bestätigter Fall desselben Musters in der Kette.
3. **`derive_lagrangian()` liefert zwei nicht zueinander passende
   Gleichungen.** Das zurückgegebene `lagrangian`-Feld ist die
   *statische* `L = S_A·S_V/(S_A+S_V) - (1+δ)/t²` (kein `S(t)`, kein
   kinetischer Term). Das `euler_lagrange`-Feld wird aber aus einer
   **komplett anderen, nie zurückgegebenen internen** Lagrangian
   `L_dyn = ½Ṡ² - (1+δ)/(t²(S/S_V+1))` abgeleitet. Die zwei
   ausgegebenen Zeilen unter `ft lagrangian` beschreiben also nicht
   dasselbe physikalische System — die gezeigte
   Euler-Lagrange-Gleichung lässt sich aus der gezeigten Lagrangian gar
   nicht herleiten, weil letzterer jeder `Ṡ`-Term fehlt, den man
   differenzieren könnte.

**Nebenbefund:** `cosmic_moments` (69 bei `steps=100`, 138 bei
`steps=200`) ist bei Code-Lektüre schlicht eine Zählung, wie viele der
`steps`-Stichproben unter `threshold · max(Serie)` einer monoton
fallenden Kurve liegen — im Grunde eine Umparametrisierung von
`steps`/`threshold`, keine Erkennung diskreter "Kollaps-Ereignisse"
(keine Oszillation, kein Zufall, nichts einem physikalischen
Singularitäts-Ereignis Ähnliches in den zugrundeliegenden Daten).

**Blindtest-Verdikt: FALSE.** Reproduzierbar (dieselben Parameter
liefern verlässlich dieselben, intern konsistenten Werte unter
Parameteränderung), aber nicht interpretierbar — keine Referenzskala,
kein Validierungsfall, keine Erklärung, was ein "gutes" `S_mod_mean`
oder eine plausible `cosmic_moments`-Zahl wäre. Reproduzierbarkeit ist
hier explizit nicht gleich Interpretierbarkeit.

## Erwartetes Ergebnis

Fünfter FALSE-Befund in der Kette. Anders als bei den vorherigen: kein
`__version__`-Bug hier (positives Gegenbeispiel), aber eine neue
Fehlerklasse (interne Formel-Inkonsistenz zwischen zwei Feldern
derselben Funktion) sowie der zweite Fall des Windows-Unicode-Crashs.

## Nächster Schritt

Drei Findings zur Weitergabe an Johann: (1) das README-Override-Beispiel
durch echte, vom Default abweichende Werte ersetzen; (2) `∝`-Zeichen aus
`cli.py`s `help=`-String entfernen (zweiter Fall desselben Bugs wie bei
`medium-modulation` — evtl. lohnt sich eine ökosystemweite Suche nach
diesem Zeichen in allen CLI-Hilfetexten); (3) `derive_lagrangian()`
entweder dieselbe Lagrangian für beide Felder verwenden, oder die
dynamische Variante explizit mit zurückgeben und dokumentieren, warum
zwei verschiedene Formen existieren.

## Alternativen betrachtet

**`cosmic_moments`-Nebenbefund als eigenständigen Blocker werten.**
Verworfen für dieses Verdikt: es ist kein Bug im engeren Sinn (der Code
tut, was er tut, konsistent), sondern verstärkt nur den bereits
tragenden Interpretierbarkeits-Befund — separat genannt, aber nicht
als vierter "Bug" gezählt.
