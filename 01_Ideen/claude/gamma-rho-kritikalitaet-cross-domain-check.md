# Γ→Ρ-Kritikalitätsdecke: geprüft in `beta-clustering-utac`/`phi-scaling-validator` — betrifft sie nicht

## Problem

`ecosystem-verifizierbare-daten-audit` benannte eine offene Frage: die
nicht-monotone Formel `Ρ_sem = r · tanh²(σΓ) · (1 − Γ/Γ_max)` aus
`scope-resilience` (Peak bei Γ≈0.46, danach fallend, harte Decke bei
Γ_max=0.920) könnte sich auf andere γ-basierte Pakete im Ökosystem
übertragen — insbesondere auf die beiden expliziten
"cross-domain meta-analysis"-Pakete `beta-clustering-utac` (P32) und
`phi-scaling-validator` (P38), die laut `ECOSYSTEM_MAP.yaml` echte
γ-Werte aus über einem Dutzend anderer Pakete zusammenführen.

## Vorgehen und Durchführung

Beide Repos liegen lokal vor. Quellcode direkt gelesen (nicht nur
Beschreibungen): `beta-clustering-utac/src/beta_clustering/{constants,
phi_scaling, universality_test, crep_bridge, system}.py` und
`phi-scaling-validator/src/phi_scaling/{crep_scaling,
statistical_tests}.py`. Gezielt nach `GAMMA_MAX`/`gamma_max`/
`1 - gamma`-artigen Kritikalitäts-Termen gesucht (`grep`), zusätzlich
die tatsächliche Aggregationslogik gelesen.

## Ergebnis

**Die Kritikalitätsdecke betrifft diese beiden Pakete nicht** — aus
einem einfachen, überprüfbaren Grund: ihre Aggregationsmethode ist
komplett anders als `scope-resilience`s Ρ_sem-Formel.

- `beta-clustering-utac` vergleicht β-Cluster-Zentren fünf realer
  Domänen (climate=0.09, ecological=0.23, neural=0.50,
  astrophysical=0.90, ai=1.75) über **Verhältnisse** gegen die
  Konstante Φ^(1/3)≈1.17480 (goldener Schnitt, Kubikwurzel) — mittels
  ANOVA-F-Test (`universality_test.py`) und Verhältnis-Analyse
  (`phi_scaling.py`). `crep_bridge.py` hat zwar eine Γ-Formel
  (`Γ = tanh(β/σ)`), aber die ist monoton (kein Peak, keine Decke) und
  wird nicht mit einem `(1−Γ/Γ_max)`-Term kombiniert.
- `phi-scaling-validator` vergleicht sortierte, echte Γ-Werte aus 14
  realen Paketen (P17–P30, `CREP_DATA` in `crep_scaling.py` — Werte
  stimmen mit `ECOSYSTEM_MAP.yaml` überein, z. B. Cygnus-X-1=0.046,
  AMOC=0.251, Amazon=0.116, Quanten-Dekohärenz=0.050) über
  **Konsekutiv-Verhältnisse**, ebenfalls gegen Φ^(1/3), per
  Ein-Stichproben-t-Test und Bootstrap-Konfidenzintervall
  (`statistical_tests.py`).

Kein `GAMMA_MAX`, keine Kritikalitäts-Decke, kein nicht-monotoner Term
in beiden Codebasen gefunden. Die Sorge war berechtigt zu prüfen, aber
die konkrete Befürchtung trifft hier nicht zu — dieses Paar Pakete
nutzt eine grundsätzlich andere (verhältnisbasierte statt
zerfallsbasierte) Mathematik.

**Nebenbefund (positiv):** `phi-scaling-validator`s `CREP_DATA` ist
ehrlich mit Näherungen umgegangen — P22 (Sandpile SOC) nutzt explizit
den Mittelwert 0.336 aus dem dokumentierten Bereich 0.296–0.376 (im
Code kommentiert), P28 (Epi-Sigillin) ist als "dynamic, approximate"
markiert, statt den in `ECOSYSTEM_MAP.yaml` als `null` geführten Wert
stillschweigend zu erfinden.

## Erwartetes Ergebnis

Die Γ→Ρ-Kritikalitätsdecke bleibt ein spezifisches Risiko von
`scope-resilience`s `HallucinationRisk.compute_rho()` (und was auch
immer sonst dieselbe Formel direkt wiederverwendet) — keine
ökosystemweite Ansteckungsgefahr für jedes γ-führende Paket. Die
Vermutung aus `ecosystem-verifizierbare-daten-audit` ist damit für
dieses Paar geprüft und verworfen, nicht offen geblieben.

## Nächster Schritt

Keine weitere Prüfung für `beta-clustering-utac`/`phi-scaling-validator`
nötig. Falls künftig weitere Pakete mit expliziter
Cross-Domain-γ-Aggregation auftauchen, lohnt sich derselbe, gezielte
Code-Check (nicht nur Domänenbeschreibung) — aber nicht als generelle
Annahme, dass jede γ-Nutzung betroffen ist.

## Alternativen betrachtet

**Aus der Namensähnlichkeit ("Γ" taucht in vielen Paketen auf)
pauschal ein ökosystemweites Risiko ableiten, ohne Code zu lesen.**
Verworfen: genau der Fehler, den diese ganze Session immer wieder
vermeiden sollte (Verifizieren statt Vermuten) — hätte hier zu einer
falschen Warnung geführt.
