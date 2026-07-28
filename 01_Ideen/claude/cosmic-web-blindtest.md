# Genesis-Blindtest für `cosmic-web`: FALSE — "Emergence" ist Rauschen, aber ein ganzer undokumentierter Simulator steckt im Paket

## Problem

`cosmic-web` (P-COSMICWEB) ist ein Programm-Kandidat. Muss laut
Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real, führte alle drei
CLI-Befehle bei mehreren Parameterwerten aus, verifizierte
Seed-Determinismus per Doppellauf, und prüfte das Dashboard per echtem
HTTP-Request.

## Ergebnis

**Install:** `cosmic-web 1.0.1`. **`__version__` stimmt überein — kein
Versions-Bug** (drittes positives Gegenbeispiel).

**Der nuancierteste Befund der ganzen Kette — echte Substanz UND ein
fundamentaler Etikettenschwindel, nebeneinander:**

1. **Unicode-Crash im allerersten Quickstart-Befehl.** `cweb render
   --nodes 50 --edges 100` crasht sofort unter Windows-Standardkonsole
   ("≈"-Zeichen, U+2248, cp1252). Achter/neunter bestätigter Fall des
   Musters — hier trifft es explizit den ersten Befehl, den ein
   Erstnutzer laut README ausführen würde.
2. **"Degree" und "Centrality" sind echte, wohldefinierte
   Graphenkennzahlen** — echter NetworkX-Knotengrad bzw. echte
   `betweenness_centrality` — und verändern sich korrekt mit
   Graphgröße/-struktur.
3. **Aber "Emergence" — das namensgebende Konzept des gesamten
   Pakets — ist reines, strukturunabhängiges Zufallsrauschen.**
   Direkt im Code verifiziert: `emergence = rng.uniform(0.1, 1.0)` pro
   Knotenindex, aus einer eigenen RNG-Sequenz, die Grad, Zentralität,
   Kanten oder sonstige Graphstruktur nie berührt. Beweis: bei
   `seed=42` sind die Emergence-Werte für Knoten 0-9 bei
   `--nodes 50 --edges 100` und `--nodes 10 --edges 5` **bytegleich**
   — weil sie nur vom Knotenindex abhängen, nicht vom Graphen. Das
   README bewirbt genau dieses Konzept ("emergence visualization",
   "emergence metrics", "simulate emergent propagation") als
   Kernfunktion.
4. **Seed-Determinismus ist echt und korrekt** — zwei unabhängige
   Läufe mit `seed=42` liefern bytegleiche Graphen und Metriken.
5. **`simulate_emergence()`s Diffusion ist echte, sinnvolle
   Mathematik** (mittelwerterhaltende Nachbar-Mittelung, Extremwerte
   nähern sich über Zeit dem Mittel an) — propagiert aber eine
   willkürliche Anfangsbedingung (das Rauschen aus Punkt 3).
6. **Dashboard funktioniert echt** — per `curl` verifiziert, liefert
   echten Plotly-Scatterplot ("Degree vs Emergence") mit denselben
   Daten wie die CLI, keine Fehlerseite.
7. **Größter Überraschungsfund: ein komplett undokumentierter,
   hochentwickelter N-Body-Kosmologie-Simulator steckt im Paket.**
   `CosmicWebSimulator` (aus `universums_sim.py`, top-level re-exportiert)
   implementiert Zel'dovich-Anfangsbedingungen, CIC-Massenzuweisung,
   FFT-Poisson-Löser, Leapfrog-Integration, Planck-2018-kosmologische
   Parameter und Powerspektrum-Schätzung — lief fehlerfrei, produziert
   plausiblen Output. **Nichts davon steht im README** (weder
   Architektur-Diagramm noch Quickstart noch Python-API-Abschnitt).
8. **Kleinerer Code-Fehler:** ein Kommentar in `_init_zel_dovich()`
   behauptet, die RNG werde "extern via `np.random.seed()`" gesät —
   sachlich falsch, NumPys `default_rng()`-Generator wird vom
   Legacy-Seed nie beeinflusst; die beabsichtigte externe Steuerung
   greift also nie.
9. **Stack-Integration-Tabelle stark unvollständig:** tatsächliches
   `[stack]`-Extra zieht 12 Pakete, README nennt nur die
   `entropy-table`-Bridge.

**Blindtest-Verdikt: FALSE.** Trotz echter Graphenbibliothek, echtem
Determinismus, echtem Dashboard und einem versteckten, funktionierenden
Simulator: das titelgebende Konzept ("Emergence") ist beim
5-Minuten-Test nicht von echtem Rauschen zu unterscheiden — es sieht
plausibel aus (Bereich 0,1-1,0, glatte Veränderung während der
Simulation), ist es aber nicht.

## Erwartetes Ergebnis

Dreizehnter FALSE-Befund insgesamt (achter unter den Programm-
Kandidaten), aber der bislang am stärksten gemischte: mehr echte
Substanz als in jedem vorherigen Programm-Kandidaten-Befund, plus ein
genuiner positiver Überraschungsfund (der versteckte Simulator), aber
das Kernversprechen des Pakets hält nicht.

## Nächster Schritt

Fünf Findings zur Weitergabe an Johann: (1) "Emergence" entweder aus
echten Graphstruktur-Eigenschaften berechnen (z. B. Clustering-
Koeffizient, lokale Dichte) oder als "Anfangsbedingung (zufällig)"
kennzeichnen statt als Kernkonzept zu bewerben; (2) Unicode-Zeichen aus
CLI-Ausgaben entfernen; (3) den RNG-Seeding-Kommentar in
`universums_sim.py` korrigieren (echte Reproduzierbarkeit fehlt dort);
(4) **den versteckten `CosmicWebSimulator` ins README aufnehmen** —
das ist echte, funktionierende Arbeit, die aktuell niemand findet; (5)
Stack-Integration-Tabelle vervollständigen.

## Alternativen betrachtet

**Das Paket wegen der echten Graphenbibliothek und des versteckten
Simulators als Grenzfall/TRUE werten.** Verworfen: Regel 6 fragt nach
dem, was der dokumentierte Quickstart tatsächlich liefert — und der
zentrale, beworbene Begriff des Pakets hält einer Gegenprobe nicht
stand. Der versteckte Simulator ist ein wertvoller Fund für einen
separaten Vorschlag (README erweitern), ändert aber nicht das
Blindtest-Verdikt für das dokumentierte Material.
