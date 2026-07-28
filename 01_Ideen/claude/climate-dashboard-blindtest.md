# Genesis-Blindtest für `climate-dashboard`: FALSE — "Stack Integration" ist komplett unbenutzter Code

## Problem

`climate-dashboard` (P-CLIMATE-UI) ist ein Programm-Kandidat. Muss laut
Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real, führte `cdash
aggregate` in zwei Varianten aus und verifizierte das Dashboard
tatsächlich per echtem HTTP-Request (nicht nur "startet ohne Crash").

## Ergebnis

**Install:** `climate-dashboard 1.0.0`. Dashboard läuft echt —
`curl` auf `/` liefert HTTP 200 mit echtem Dash-HTML, `/_dash-layout`
liefert echte, unterschiedliche Datenarrays für die drei Signale.
`--steps` hat einen echten, verifizierten Effekt (Zeilenzahl und
`mandala_peaks`-Wert skalieren nachweislich mit `--steps` 100→200).

**Der sauberste Beweis der ganzen Kette, dass eine "Stack
Integration"-Tabelle rein dekorativ ist:**

1. **Keines der in der README-Tabelle gelisteten zehn Pakete
   (`entropy-governance`, `medium-modulation`, `utac-core`,
   `mandala-visualizer`, `sonification`, `entropy-table`,
   `cosmic-moment`, `fieldtheory`, `sigillin`, `implosive-genesis`)
   wird irgendwo in `cli.py` oder `app.py` importiert.** Der `[stack]`-
   Extra ist korrekt in der Paket-Metadaten deklariert (`Provides-Extra`
   verifiziert), aber selbst wenn installiert, würde sich am
   tatsächlichen Output von `cdash run`/`aggregate` nichts ändern —
   kosmetisch/unbenutzt.
2. **`entropy_table_bridge.py`** — im README-eigenen Struktur-Baum als
   echte Integration aufgeführt — **ist toter Code**, von nirgends
   aufgerufen.
3. **Die komplette Berechnung ist drei Zeilen reiner NumPy-Code ohne
   externe Abhängigkeit:** `duality = sin(t·1.618)`,
   `modulation = duality·0.618`, `utac = 0.0625·ln(t+1)` — der Code
   sagt es selbst im Kommentar: `# placeholder from entropy-governance`.
   Diese Ehrlichkeit im Code wird aber nicht ins README durchgezogen,
   dessen "What you get"-Liste einen echten Multi-Paket-Pipeline
   suggeriert.
4. **`mandala_peaks` ist fehlbenannt und irreführend.** Keine
   echte Peak-Erkennung (kein `scipy.signal.find_peaks` o. ä.) —
   ein einzelner Schwellenwert-Überschreitungs-Zähler wird als
   identischer Skalar in jede Zeile geschrieben. Aktiv irreführend
   bei `.describe()`: `min == mean == max` für eine Spalte, die wie
   eine Pro-Zeile-Statistik aussieht.
5. **Dashboard zeigt nur drei simple Linienplots**, obwohl die
   README-Einleitung "mandala resonance and sonified output"
   verspricht — weder Mandala-Plot noch Audio-Code existiert in
   `app.py`.
6. **`__version__` = "0.1.0" leckt sogar in die laufende Dashboard-
   Oberfläche** — die Fußzeile der echten, laufenden App zeigt
   hartkodiert "climate-dashboard v0.1.0", während `pip show` 1.0.0
   meldet. Sichtbarer für Endnutzer als bei jedem vorherigen Fall.
7. **`cdash run` hat kein `--steps`, nur `aggregate` hat es** — die
   Dashboard-Visualisierung selbst kann nie angepasst werden.
8. **Stille Textkorruption statt Absturz** (wie bei `mirror-machine`):
   Gedankenstrich und Box-Zeichnungszeichen werden unter cp1252 zu "�"
   statt zu crashen.

**Blindtest-Verdikt: FALSE.** Technisch das robusteste Paket der
Programm-Kandidaten bisher (echter Server, echter `--steps`-Effekt,
kein Absturz) — aber die zentrale Behauptung ("visualizes the
GenesisAeon stack") ist nachweislich falsch: es visualisiert drei
freistehende Sinuskurven ohne jede Verbindung zu den genannten
Paketen.

## Erwartetes Ergebnis

Zehnter FALSE-Befund insgesamt (fünfter unter den Programm-
Kandidaten). Erster Fall mit vollständigem, sauberem Beweis, dass eine
ganze "Stack Integration"-Tabelle unbenutzt ist — nicht nur
unvollständig demonstriert wie bei `entropy-governance`/`cosmic-moment`,
sondern komplett unabhängig vom Code.

## Nächster Schritt

Fünf Findings zur Weitergabe an Johann: (1) entweder die Stack-
Integration tatsächlich implementieren oder die README-Behauptung auf
das reduzieren, was der Code wirklich tut (drei unabhängige
Platzhalter-Kurven); (2) `mandala_peaks` umbenennen oder durch echte
Peak-Erkennung ersetzen; (3) `__version__`-Sync (auch in der
Footer-Zeichenkette in `app.py`, nicht nur `__init__.py`); (4)
`entropy_table_bridge.py` entfernen oder tatsächlich verdrahten; (5)
`--steps` auch für `cdash run` verfügbar machen, falls das gewollt ist.

## Alternativen betrachtet

**Den Befund milder werten, weil Server und `--steps`-Effekt echt
funktionieren.** Verworfen als Gesamtverdikt: robuste Technik ändert
nichts daran, dass die zentrale inhaltliche Behauptung des Pakets
("visualisiert den GenesisAeon-Stack") nicht zutrifft — Regel 6 fragt
nach einem sinnvollen, korrekten Ergebnis, nicht nur nach
Absturzfreiheit.
