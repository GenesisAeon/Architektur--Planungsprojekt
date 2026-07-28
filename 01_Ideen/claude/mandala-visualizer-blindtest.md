# Genesis-Blindtest für `mandala-visualizer`: FALSE — Crash nach erfolgreichem Speichern täuscht Totalausfall vor

## Problem

`mandala-visualizer` (P-MANDALA-VIZ) ist ein Programm-Kandidat. Muss
laut Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real, führte alle
CLI-Befehle und die Python-API aus und verifizierte die erzeugten
Bilddateien tatsächlich mit PIL/NumPy (nicht nur "Datei existiert").

## Ergebnis

**Install:** `mandala-visualizer 1.0.0`. **`__version__` stimmt
überein — kein Versions-Bug** (zweites positives Gegenbeispiel neben
`fieldtheory` EN).

**Ein besonders tückischer Bug-Typ: Erfolg, gefolgt von irreführendem
Crash.**

1. **`mviz render`/`mviz dashboard` speichern die PNG-Datei korrekt,
   crashen aber danach beim Ausgeben der Erfolgsmeldung** —
   `UnicodeEncodeError` beim "→"-Zeichen in der Rich-Konsolenausgabe
   (`cli.py` Zeilen 33/45). Verifiziert: `mandala.png` (107.572 Byte),
   `entropy-gate.png` (100.640 Byte) und `climate-dashboard.png`
   (143.767 Byte) sind bereits korrekt geschrieben, **bevor** der Crash
   auftritt. Ein Erstnutzer sieht einen erschreckenden Traceback +
   Exit-Code 1 und würde vernünftigerweise annehmen, das Rendern sei
   komplett fehlgeschlagen — obwohl die Datei tatsächlich da ist.
   Python-API (ohne Rich-Konsolenausgabe) crasht dagegen gar nicht.
2. **Bilder sind echt, nicht leer/entartet** — mit PIL/NumPy verifiziert:
   reale RGBA-Bilder, hunderte unterschiedliche Farben, keine
   Blankokanvas.
3. **Aber die Namen halten nicht, was sie versprechen:**
   `mviz render --type cosmic-web` ist buchstäblich
   `networkx.star_graph(20)` mit Spring-Layout — visuell ein Stern mit
   20 Speichen, kein "kosmisches Netz" (in der Astrophysik ein
   filamentäres Gitter) und nicht im Ansatz fraktal. `climate_dashboard`
   enthält keine echten Klimadaten, nur zwei synthetische
   Sinus-/Kosinuskurven.
4. **`mermaid_grafana_bridge()` ignoriert sein Eingabe-Argument
   komplett** — der Code markiert den `data`-Parameter explizit als
   ungenutzt (`# noqa: ARG001`). Egal was übergeben wird, die Ausgabe
   ist ein hartkodierter, identischer String.
5. **"fraktal" wird mehrfach in Docstrings/CLI-Hilfe erwähnt, aber
   keiner der drei Renderer implementiert irgendetwas Fraktales** —
   keine Rekursion, keine Selbstähnlichkeit, keine L-Systeme.
6. **Stack-Integration-Tabelle unvollständig:** README listet 5
   Pakete, das tatsächliche `[stack]`-Extra zieht 8 (zusätzlich
   `entropy-governance`, `implosive-genesis`, `medium-modulation` —
   undokumentiert).

**Blindtest-Verdikt: FALSE.** Differenziert: zwei der drei Renderings
(`entropy-gate`, das rechte Dashboard-Panel) sehen für einen Laien auf
den ersten Blick tatsächlich mandala-/blütenartig aus — das ist mehr
als bei den meisten bisherigen Befunden. Aber der irreführende
Crash-nach-Erfolg, die komplett falsche "cosmic-web"-Namensgebung, und
die eingabe-ignorierende Bridge-Funktion summieren sich zu einem klaren
FALSE.

## Erwartetes Ergebnis

Elfter FALSE-Befund insgesamt (sechster unter den Programm-
Kandidaten), aber mit einer neuen, besonders relevanten Bug-Kategorie:
Absturz *nach* erfolgreicher Aktion, der beim Nutzer den Eindruck eines
Totalausfalls erzeugt, obwohl das eigentliche Ergebnis (die Bilddatei)
bereits korrekt vorliegt.

## Nächster Schritt

Vier Findings zur Weitergabe an Johann: (1) Unicode-Zeichen aus den
Erfolgsmeldungen entfernen — hier besonders wichtig, weil die Datei
sonst fälschlich als "nicht erzeugt" erscheint; (2) `cosmic-web`-
Rendering durch ein tatsächlich netzartiges/filamentäres Layout
ersetzen oder umbenennen; (3) `mermaid_grafana_bridge()` entweder
tatsächlich aus `data` generieren oder als Platzhalter kennzeichnen;
(4) Stack-Integration-Tabelle um die drei fehlenden Pakete ergänzen.

## Alternativen betrachtet

**Den Crash-nach-Erfolg als weniger schwerwiegend werten, weil die
Datei ja tatsächlich entsteht.** Verworfen: aus Nutzersicht zählt die
wahrgenommene Fehlermeldung, nicht der interne Zustand — ein Exit-Code
1 mit Traceback ist ein Blindtest-Blocker, unabhängig davon, was im
Hintergrund bereits korrekt gelaufen ist.
