# Genesis-Blindtest für `resilience-core`: FALSE — README-Kalibrierung stimmt mit keinem der vier Referenzwerte überein

## Problem

Johann fragte direkt (nicht als Teil der Core-Kandidaten-Sequenz aus
`02_Plaene/genesis-core-scope.md`, sondern anlässlich der aktuellen
Donau-/Rhein-Niedrigwasserlage, siehe `D:\mandala\KlimaAktuell\
KlimaLageEuropaAktuell.txt`), ob `resilience-core` (P40) und
`entropy-governance` das Konzept "kritische Verlangsamung nahe
Kipppunkt + Nachwirkung bleibt nach der Störung" (critical slowing
down, Scheffer et al. 2009) bereits sauber abbilden — als Grundlage
für ein mögliches neues Modul, das 2026er Realdaten einspeist und
Resilienzschwächung + Folgen vorhersagen soll.

`resilience-core` bewirbt sich selbst genau dafür: Ρ =
|λ*|·(1−Γ/Γ_max)·coupling_factor, mit vier "kalibrierten
Referenzwerten" (AMOC, Arctic, Sandpile, Quantum) im README.

## Vorgehen und Durchführung

Frische Installation (`pip install -e`, lokaler Quellcode, da PyPI
per SSL durch Avast blockiert war — siehe
[[feedback_avast_diamond_setup]]) in isoliertem venv. Alle vier
README-Quickstart-Beispiele real ausgeführt (`compute_rho`,
`ResilienceCore(domain=...).run_cycle()`), Γ-Sweep über den vollen
Bereich [0.05, 0.98] gefahren, anschließend direkte Code-Inspektion
von `rho_calculator.py`, `eigenrate.py`, `coupling.py`,
`constants.py`, `system.py` — dieselbe Methodik wie bei
`entropy-governance-blindtest`.

## Ergebnis

**Install:** lief sauber, v1.0.0, keine Fehler.

**Alle vier README-"Calibrated Reference Values" reproduziert und
falsifiziert:**

| Domain | README behauptet Ρ | Tatsächlicher Code-Output |
|---|---|---|
| Quantum (Γ=0.050) | ≈ 0.90 | 0.0114 (Faktor ~79 zu niedrig) |
| Sandpile (Γ=0.296) | ≈ 0.75 | 0.2223 (Faktor ~3.4 zu niedrig) |
| AMOC (Γ=0.251) | ≈ 0.65 | 0.1834 (Faktor ~3.5 zu niedrig) |
| Arctic (Γ=0.920) | ≈ 0.05 | **exakt 0.0** |

**Root Cause 1 — `domain` ist für die Rho-Berechnung selbst wirkungslos.**
`RhoCalculator.compute()` nutzt nur `eigenrate.compute(gamma)` (r=1.0,
σ=2.2 global, unabhängig vom Domain-String) und
`coupling.coupling_factor(domain)` — letzteres liefert ohne
registrierte Kopplungen für jeden beliebigen Domain-String 1.0. Es
gibt keinerlei domänenspezifische Kalibrierung von r, σ oder Γ_max
irgendwo im Code. Die vier "kalibrierten" Zeilen in der README-Tabelle
sind eine einzige globale Formel, angewendet auf vier verschiedene
Γ-Werte — keine per-Domäne-Kalibrierung.

**Root Cause 2 — `BENCHMARK_GAMMA`/`BENCHMARK_RHO` sind tote Daten.**
Beide Dicts sind in `constants.py` definiert und werden in
`__init__.py` re-exportiert, aber von keiner einzigen Funktion im
Paket gelesen (verifiziert per `grep` über den kompletten `src`-Baum).
Exakt derselbe Fehlertyp wie die ungenutzten `DUALITY_A`/`DUALITY_V`-
SymPy-Platzhalter aus [[entropy-governance-blindtest]].

**Root Cause 3 — `GAMMA_MAX` ist selbstreferentiell auf den Arctic-
Wert gesetzt.** `GAMMA_MAX = 0.920`, Kommentar "Maximum observed Γ in
the CREP Atlas (ERA5 Arctic — most saturated system)" — also exakt
der Γ-Wert, mit dem Arctic selbst getestet wird. Das garantiert
mathematisch `criticality_margin = 1 − 0.920/0.920 = 0` für Arctic,
unabhängig von jeder echten Kalibrierung. Die README-Behauptung "Ρ ≈
0.05, near collapse" (also klein aber ungleich null) ist damit für
dieses Γ_max per Konstruktion unerreichbar.

**Root Cause 4 — nicht-monotone Formel, bereits als Risiko bekannt.**
Ρ(Γ) = r·tanh²(σΓ)·(1−Γ/Γ_max) steigt bis zu einem Peak bei Γ≈0.46
und fällt danach wieder — bestätigt im eigenen Γ-Sweep (Peak
Ρ≈0.293 bei Γ=0.50, danach fallend bis exakt 0 bei Γ≥Γ_max). Dies ist
**dieselbe Formel mit identischem `GAMMA_MAX=0.920`**, die
[[gamma-rho-kritikalitaet-cross-domain-check]] bereits in
`scope-resilience/src/scope_resilience/hallucination_risk.py`
(`Ρ_sem = r·tanh²(σΓ)·(1−Γ/Γ_max)`, ebenfalls `GAMMA_MAX=0.920`,
verifiziert per direktem Code-Vergleich) identifiziert hatte. Der
dortige Cross-Domain-Check prüfte nur `beta-clustering-utac`/
`phi-scaling-validator` (betroffen: nein, andere Mathematik) — auf
`resilience-core` selbst wurde die Prüfung noch nicht angewendet,
obwohl `ecosystem-verifizierbare-daten-audit.md` `resilience-core`
bereits namentlich neben `scope-resilience`/`genesis-tip` als
verwandtes Falsifikations-Framework nennt. Diese Lücke ist mit diesem
Blindtest geschlossen: **die Kritikalitätsdecke ist kein Einzelfall
von `scope-resilience`, sondern in mindestens zwei Paketen mit
identischem Code vorhanden.**

**Was arithmetisch korrekt ist:** `tanh²(σΓ)` als monoton wachsende
Annäherung an "kritische Verlangsamung" (Erholungsrate sinkt Richtung
Γ_max) ist konzeptionell die richtige Idee und deckt sich mit Scheffer
et al. 2009 (critical slowing down). Das Problem liegt nicht in der
Grundidee, sondern in der Kombination mit dem `(1−Γ/Γ_max)`-Faktor
(der die Kurve wieder herunterzieht) und der fehlenden echten
Domänen-Kalibrierung.

**Verdikt: FALSE.** Die "Calibrated Reference Values"-Tabelle ist
Dokumentations-Fiktion, nicht durch den Code erzeugt. `domain` ist ein
Bezeichner ohne Rechenwirkung außerhalb manuell registrierter
Kopplungen. Kein Hysterese-/Nachwirkungs-Mechanismus vorhanden (Ρ ist
rein zustandslos in Γ — es gibt keinen "bleibt nach der Störung
geschwächt"-Zustand, jeder `run_cycle()`-Aufruf ist unabhängig vom
vorherigen).

## Erwartetes Ergebnis

`resilience-core` besteht den Genesis-Blindtest in der jetzigen Form
nicht. Für Johanns eigentliche Frage (critical slowing down +
Hysterese/Nachwirkung modellieren) bedeutet das: die Grundidee
(`tanh²(σΓ)`) ist brauchbar, aber (a) die Domänen-Kalibrierung muss
echt implementiert werden (heute Dekoration), (b) `GAMMA_MAX` darf
nicht mehr am eigenen Extremwert hängen, (c) ein neues Modul dürfte
sich NICHT blind auf `resilience-core`s Domain-Parameter oder
Referenzwerte verlassen, ohne das selbst zu kalibrieren, und (d) für
"Folgen bleiben nach dem Ausschlag" fehlt aktuell jeder Zustand
zwischen Zyklen — das wäre ein echter Zusatzbaustein, kein
vorhandenes Feature.

## Nächster Schritt

Zwei Findings zur Weitergabe an Johann: (1) `BENCHMARK_GAMMA`/
`BENCHMARK_RHO` entweder wirklich verdrahten (Kalibrierungs-Check beim
Domain-Konstruktor) oder aus README/Export entfernen, um die
Diskrepanz nicht weiter zu behaupten; (2) `GAMMA_MAX` sollte nicht am
Arctic-eigenen Γ hängen, sondern an einem unabhängig begründeten
Maximalwert. Dieselbe Prüfung wäre für `scope-resilience` selbst
sinnvoll (dort bisher nur als Verdacht dokumentiert, nicht per
Γ-Sweep verifiziert) — als Anschlussarbeit vorgemerkt, nicht Teil
dieses Blindtests.

## Alternativen betrachtet

**Den Fund nur als "Doku-Ungenauigkeit" werten und übergehen.**
Verworfen: die Diskrepanz betrifft alle vier von vier beworbenen
Referenzwerten (kein Ausreißer), und `GAMMA_MAX`s Selbstbezug auf
Arctic ist ein struktureller Konstruktionsfehler, kein Rundungsfehler
— das ist derselbe Bug-Schweregrad wie `entropy-governance`s
ignoriertes `--steps`-Flag, nicht bloß Kosmetik.
