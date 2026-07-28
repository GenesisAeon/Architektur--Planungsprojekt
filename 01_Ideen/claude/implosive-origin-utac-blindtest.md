# Genesis-Blindtest für `implosive-origin-utac`: FALSE — echte Selbstkritik im Code, aber k_RIG stimmt nicht und `n_efolds` ist wirkungslos

## Problem

`implosive-origin-utac` (P33) ist ein Programm-Kandidat, explizit als
"SPECULATIVE" gekennzeichnet. Muss laut Regel 6 den Genesis-Blindtest
bestehen — die Selbstkennzeichnung als spekulativ befreit nicht vom
Test, ändert aber möglicherweise die Bewertung der Ehrlichkeit.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe (mit dem expliziten Hinweis, die
"SPECULATIVE"-Kennzeichnung sei Teil des echten Materials, kein Grund
zur Abwertung), installierte real, führte das Quickstart aus und
rechnete alle drei Kernbehauptungen (`r≈0.004`, `k_RIG≈0.097`,
`crep_gamma≈0.57`) von Hand nach.

## Ergebnis

**Install:** `implosive-origin-utac 1.1.0`. **`__version__` stimmt
überein — kein Versions-Bug** (viertes positives Gegenbeispiel).

**Der differenzierteste Befund der ganzen Kette:**

1. **`r ≈ 0,004` stimmt exakt** — `SIGMA_PHI² = (1/16)² = 0,00390625`.
2. **`crep_gamma ≈ 0,57` stimmt exakt** — von Hand nachgerechnet
   `(0,8·0,7·0,5·0,4)^0,25 = 0,5785015217038155`, bit-identisch zum
   Code-Output.
3. **Aber `k_RIG ≈ 0,097 Mpc⁻¹` stimmt NICHT.** Der Code liefert
   tatsächlich **0,304 Mpc⁻¹** — Faktor 3,13 daneben. Das ist kein
   reines README-Drift: der Code widerspricht sich intern selbst — ein
   Kommentar in `constants.py` sagt "≈0,304 Mpc⁻¹", ein Docstring in
   `dm_power_spectrum.py` für dieselbe Größe sagt "≈0,097 Mpc⁻¹". Zwei
   interne Kommentare widersprechen sich UND dem tatsächlich
   berechneten Wert, der wiederum weder zum README noch zu einem der
   beiden eigenen Docstrings passt.
4. **`n_efolds` hat exakt null Effekt auf alle drei Kernvorhersagen.**
   Getestet mit `n_efolds ∈ {1, 10, 60, 200, 1000}` — `tensor_scalar_r`,
   `dm_suppression_k`, `crep_gamma` sind bei jedem Wert bitidentisch.
   Grund: alle drei sind hartkodierte Konstanten
   (`SIGMA_PHI**2`, `K_RIG_MPC`, feste CREP-Defaults `C=0.8/R=0.7/
   E=0.5/P=0.4`) — die ODE-Integration läuft tatsächlich (echte
   numerische Arbeit passiert), ihr Ergebnis fließt aber nie in die
   berichteten Vorhersagen ein. `run_cycle(n_efolds=60)` ist Theater um
   statische Arithmetik. Zusätzlich: `n_efolds_actual` meldet 8,55
   unabhängig vom angeforderten Wert (60) — die Trajektorie erreicht
   ihren Fixpunkt immer nach ~8,5 e-folds.
5. **`DISCLAIMER.md`**, auf die das README explizit verweist, **wird
   nicht mit dem Wheel ausgeliefert** — ein Nutzer, der `pip install`
   macht, kann den Disclaimer, den das README zu lesen empfiehlt,
   lokal gar nicht finden.
6. **Unicode-Crash nuanciert:** das wörtliche Quickstart-Snippet
   crasht NICHT (der verwendete Gedankenstrich ist zufällig
   cp1252-kodierbar) — aber eine echte Abhängigkeit dieses Pakets
   (`diamond_setup.protocol`) enthält denselben Fehlertyp (ein
   "→"-Zeichen in einem Docstring), der bei geringfügig tieferer
   Erkundung (z. B. Quellcode-Inspektion) denselben Crash auslöst.

**Bemerkenswert — echte, im Code selbst verankerte Ehrlichkeit:**
mehrere Docstrings geben offen zu, dass Konstanten willkürlich gewählt
sind (`frame_principle_r()`: *"Whether r = σ_Φ² or r = 16σ_Φ²
depends on how σ_Φ maps to ε... This returns the direct form"*;
`n_s_estimate()`: *"this simple estimate does not account for η; for
illustration only"*). Jeder `summary()`/`euclid_testable()`-Rückgabewert
trägt selbst `'status': 'SPECULATIVE — ...'` — nicht nur README-
Marketing, sondern im Code verankert. Das ist eine deutlich ehrlichere
epistemische Haltung als bei den meisten bisher getesteten Paketen.

**Blindtest-Verdikt: FALSE.** Die "spekulativ"-Kennzeichnung deckt die
wissenschaftliche Unsicherheit der Hypothese ehrlich ab — sie deckt
aber nicht den separaten, unabhängigen Befund, dass `k_RIG` intern
widersprüchlich ist und dass `run_cycle()` als Simulation präsentiert
wird, deren Eingabe nachweislich nichts bewirkt.

## Erwartetes Ergebnis

Vierzehnter FALSE-Befund insgesamt (neunter unter den Programm-
Kandidaten), aber der bislang am stärksten differenzierte: echte
Selbstkritik im Code selbst verdient ausdrückliche Anerkennung, ändert
aber nichts an zwei eigenständigen, überprüfbaren Fehlern.

## Nächster Schritt

Vier Findings zur Weitergabe an Johann: (1) `k_RIG`-Wert klären —
welcher der beiden widersprüchlichen internen Werte (0,304 vs. 0,097)
ist beabsichtigt, und README/Docstrings entsprechend vereinheitlichen;
(2) entweder `run_cycle(n_efolds=...)` tatsächlich in die berichteten
Vorhersagen einfließen lassen, oder ehrlich kennzeichnen, dass die
Kernvorhersagen unabhängig von der Simulation feste Konstanten sind;
(3) `DISCLAIMER.md` ins Wheel aufnehmen; (4) die zugrundeliegende
`diamond-setup`-Abhängigkeit auf denselben Unicode-Fehlertyp prüfen
(siehe `windows-unicode-crash-pattern`).

## Alternativen betrachtet

**Das Paket wegen seiner ungewöhnlichen Ehrlichkeit milder werten als
die übrigen FALSE-Befunde, evtl. sogar TRUE.** Teilweise berücksichtigt
(ausdrückliche Anerkennung im Text oben), aber nicht als Verdikt-
Änderung: die "speculative"-Kennzeichnung behandelt die
wissenschaftliche Unsicherheit der zugrundeliegenden Hypothese, nicht
die separate Frage, ob der Code intern konsistent ist und tut, was er
zu tun behauptet (Regel 6). Ein ehrlich gekennzeichnetes Paket kann
trotzdem eigenständige technische Fehler haben.
