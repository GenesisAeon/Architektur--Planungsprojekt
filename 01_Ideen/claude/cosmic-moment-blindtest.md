# Genesis-Blindtest für `cosmic-moment`: FALSE — Demo-Schwelle garantiert "100/100" by Konstruktion

## Problem

`cosmic-moment` (P-MOMENT) ist das fünfte Kettenglied der Core-Kette.
Bereits im `version-string-drift-audit` als weiterer `__version__`-Fall
vorgemerkt. Muss laut Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real und führte jeden
dokumentierten Befehl/API-Aufruf aus.

## Ergebnis

**Install:** `cosmic-moment 1.0.0` — README selbst zitiert
`pip install cosmic-moment==0.1.0`, was nicht der tatsächlich
aufgelösten Version entspricht (dritte Variante der Versions-Diskrepanz
neben `entropy-table`/`implosive-genesis`).

**Mehrere echte Bugs/Inkonsistenzen:**

1. **`cm collapse --t 3.14` crasht unter Windows** — dritter
   bestätigter Fall des Unicode-Crash-Musters (nach
   `medium-modulation`, `fieldtheory`): `cli.py` druckt ein
   "→"-Zeichen direkt über `rich`, `UnicodeEncodeError` auf cp1252.
   Nur mit `PYTHONIOENCODING=utf-8` umgehbar, README erwähnt das nicht.
2. **Die Demo-Schwelle im README garantiert "100/100 erkannt" durch
   Konstruktion, nicht durch Datenanalyse.** `cm detect --threshold
   0.618` (der genaue README-Wert, golden-ratio-bezogen) meldet
   "Detected 100 cosmic moment(s)" — das komplette Sample, ungefiltert.
   Verifiziert durch Schwellen-Sweep: 0.0 bis 0.927 liefern alle
   100/100; erst ab ~0.93 beginnt die Zahl zu sinken (97/100 bei 0.93,
   21/100 bei 1.5). Grund: die feste Formel mit den Standardwerten
   (S_A=1.0, S_V=1.618, depth=0.5) hat ein Minimum von ~0.927 — bereits
   über dem dokumentierten Default-Threshold 0.618. Das
   Flaggschiff-Beispiel meldet also *garantiert* "alle erkannt",
   unabhängig davon, was ein Nutzer über die Funktion von `--threshold`
   glaubt.
3. **`collapse()` berechnet nichts.** Gibt nur den Input-Zeitpunkt
   zurück und hartkodiert `'new_layer': 'consciousness'` sowie
   `'collapsed': True` für JEDEN Input — auch für unsinnige Werte
   (z. B. t=-999 würde dieselbe Struktur liefern). Kein Kriterium,
   keine Berechnung, nichts zu überprüfen.
4. **`ChronologyValidator`-Ergebnis wird berechnet, aber verworfen.**
   Das README bewirbt die "10-part chronology check"-Integration; der
   Code ruft sie in `detect()` tatsächlich auf, verwirft aber das
   Ergebnis vollständig — nie geprüft, nie im Output sichtbar, rein
   dekorativ.
5. **`__version__` = "0.1.0" vs. installiert 1.0.0** — bestätigt, aber
   diesmal eine *tote* Konstante: wird nirgends im Code gelesen, es
   gibt kein `cm --version`-Flag. Unsichtbar für Nutzer, anders als bei
   `medium-modulation`/`entropy-governance`, wo es in Output/Exports
   leckt.
6. **Nebenbefunde:** `matplotlib[animation]`-Extra existiert nicht
   (Pip-Warnung beim Install, transitiv über `implosive-genesis`); CLI-
   Hilfetext hat ein Mojibake-Zeichen statt Gedankenstrich.

**Blindtest-Verdikt: FALSE.** Nichts im Output erklärt, warum 100 oder
21 "cosmic moments" erkannt wurden, was "consciousness layer"
numerisch bedeutet, oder was ein "falsches" Ergebnis wäre — keine
Referenzskala, keine Fehlergrenze. Liest sich wie evokative Prosa um
einen deterministischen Sinus, nicht wie ein interpretierbares
wissenschaftliches Ergebnis.

## Erwartetes Ergebnis

Sechster FALSE-Befund in der Kette. Besonders bemerkenswert: das
README-eigene Demo-Beispiel ist so konstruiert, dass es *garantiert*
"vollständige Erkennung" zeigt — das ist keine zufällige Doku-
Ungenauigkeit, sondern ein struktureller Design-Fehler in der Wahl der
Default-Werte relativ zum Default-Threshold.

## Nächster Schritt

Vier Findings zur Weitergabe an Johann: (1) Default-Threshold/Default-
Parameter so wählen, dass die Demo tatsächlich eine Teilmenge zeigt,
nicht garantiert 100 %; (2) `collapse()` mit echter Berechnung
hinterlegen oder als Platzhalter kennzeichnen; (3)
`ChronologyValidator`-Ergebnis tatsächlich auswerten statt zu
verwerfen, oder die Integration aus dem README entfernen, bis sie
genutzt wird; (4) Unicode-Zeichen aus CLI-Strings entfernen (dritter
Fall — lohnt sich jetzt eine ökosystemweite Suche, siehe
`fieldtheory-en-blindtest`).

## Alternativen betrachtet

**Den 100/100-Befund als Zufall/Rundungsfehler werten.** Verworfen:
der Schwellen-Sweep zeigt einen klaren, erklärbaren Mechanismus
(Formel-Minimum liegt über dem Default-Threshold) — kein Zufall,
sondern eine überprüfbare strukturelle Eigenschaft der gewählten
Default-Werte.
