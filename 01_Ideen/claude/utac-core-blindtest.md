# Genesis-Blindtest für `utac-core`: FALSE — erster dokumentierter Befehl läuft gar nicht

## Problem

`utac-core` (P-CORE) ist das strukturelle Zentrum der vorgeschlagenen
Core-Kette — laut `02_Plaene/genesis-core-scope.md` das siebte und
letzte Kettenglied, von dem `sigillin`, `mandala-visualize`,
`sonification`, `aeon-ai` u. a. abhängen. Muss laut Regel 6 den
Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real und führte jeden
dokumentierten Befehl/API-Aufruf aus.

## Ergebnis

**Install:** `utac-core 1.0.0`, als "Production/Stable" klassifiziert.

**Das schwerwiegendste Ergebnis der bisherigen Kette:**

1. **Der allererste Quickstart-Befehl läuft überhaupt nicht.**
   `utac fit --beta 0.0625` schlägt sofort fehl:
   ```
   Error: No such option: --beta (Possible options: --theta)
   ```
   Die reale CLI-Signatur von `fit` kennt nur `--r`/`--theta` — kein
   `--beta`-Flag existiert. Ein Erstnutzer, der dem README wörtlich
   folgt, scheitert an Zeile 1.
2. **Alle vier CLI-Befehle crashen zusätzlich unter Windows-
   Standardkonsole.** `UnicodeEncodeError` für β/σ/Φ-Glyphen,
   reproduzierbar bei `fit`, `frame-principle`, `rig` und `logistic` —
   vierter bestätigter Fall des Unicode-Crash-Musters in der Kette
   (nach `medium-modulation`, `fieldtheory`, `cosmic-moment`), hier
   aber am schwerwiegendsten: ohne `PYTHONIOENCODING=utf-8` bekommt
   ein Windows-Erstnutzer **null** funktionierende Befehle, nur
   Tracebacks.
3. **`__version__` = "0.1.0" vs. installiert 1.0.0** — wieder
   bestätigt.
4. **Echte Formel-Diskrepanz im README-eigenen Python-Beispiel.** Die
   Mathematik-Tabelle sagt `v_RIG = β·ln(t+1)·σ_Φ`, mit β als
   unabhängigem, gefittetem Parameter. Aber `v_rig(t=10.0)` im README-
   Beispiel nutzt implizit den Funktions-Default `beta=SIGMA_PHI` —
   **nicht** das zwei Zeilen zuvor im selben Code-Block berechnete
   `beta_fit(...)`-Ergebnis (0.089286). Nachgerechnet: mit dem
   gefitteten β ergäbe sich `0.013381112`, tatsächlich ausgegeben wird
   aber `0.009366778` (= σ_Φ²·ln(11)). Das README-Beispiel suggeriert,
   `beta_fit` und `v_rig` würden zusammenspielen — tun sie nicht.

**Nach manuellem Workaround (`PYTHONIOENCODING=utf-8`, `--beta` durch
gültige Flags ersetzt) laufen die Befehle und liefern intern konsistente
Werte** (`utac_logistic` z. B. korrekt im Sigmoid-Bereich [0,1]), aber:

**Blindtest-Verdikt: FALSE.** Von vier Quickstart-CLI-Befehlen läuft
einer gar nicht wie dokumentiert, alle vier scheitern nativ unter
Windows. Von vier Python-API-Werten stimmt einer exakt
(`frame_principle`), einer ist plausibel aber unerklärt
(`utac_logistic`), und zwei (`beta_fit`, `v_RIG`) liefern Zahlen ohne
jede Referenzskala — bei `v_RIG` zusätzlich mit der oben beschriebenen
Formel-Diskrepanz.

## Erwartetes Ergebnis

Siebter FALSE-Befund in der Kette — und der bislang schwerwiegendste,
weil das strukturelle Zentrum der gesamten Kette betroffen ist:
`utac-core`s eigener Quickstart funktioniert nicht einmal
oberflächlich, bevor man überhaupt zur Interpretierbarkeitsfrage kommt.

## Nächster Schritt

Vier Findings zur Weitergabe an Johann: (1) `utac fit --beta` entweder
implementieren oder aus dem README entfernen/durch die echten
`--r`/`--theta`-Flags ersetzen; (2) Unicode-Zeichen aus allen vier
CLI-Befehlen entfernen (jetzt vierter Fall — eine ökosystemweite,
mechanische Suche nach β/σ/Φ/∝/→ in allen `cli.py`-Dateien wäre jetzt
sinnvoll, siehe Sammelbefund unten); (3) `__version__`-Sync; (4)
`v_rig`-Beispiel im README korrigieren, damit es tatsächlich das
gefittete β verwendet, oder den Default-Mechanismus explizit erklären.

**Sammelbefund über die ganze Kette:** vier von sieben getesteten
Kettengliedern (`medium-modulation`, `fieldtheory`, `cosmic-moment`,
`utac-core`) haben denselben Unicode-Crash-Typ unter Windows. Das ist
kein Einzelfall mehr, sondern ein wiederkehrendes Scaffold-/Vorlagen-
Problem — lohnt einen eigenen, ökosystemweiten Fix-Vorschlag statt
Einzelkorrekturen pro Paket.

## Alternativen betrachtet

**Den `--beta`-Fehler als Tippfehler im README abtun, der leicht zu
korrigieren wäre.** Nicht verworfen als Einschätzung des Schweregrads
(es IST leicht zu beheben), aber wichtig: es ist trotzdem ein
Blocker für Regel 6 in der jetzigen Form — der Befund bleibt FALSE,
unabhängig davon, wie einfach der Fix wäre (Regel 5/6: ehrlicher
Status jetzt, nicht vorweggenommene Bewertung des erwarteten Fixes).
