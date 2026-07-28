# Genesis-Blindtest für `sonification`: FALSE — Flaggschiff-Demo erzeugt einen unhörbaren Ton

## Problem

`sonification` (P-SONIC) ist ein Programm-Kandidat. Muss laut Regel 6
den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, installierte real, führte alle drei
CLI-Befehle und die Python-API aus und verifizierte die erzeugten
WAV-/MIDI-Dateien tatsächlich mit `wave`/FFT-Analyse bzw. MIDI-
Byte-Inspektion (nicht nur "Datei existiert").

## Ergebnis

**Install:** `genesisaeon-sonification 1.0.0`. Distributionsname-
Mismatch (`genesisaeon-sonification` vs. `import sonification`)
funktioniert wie dokumentiert.

**Der interessanteste Einzelbefund der ganzen Session:**

1. **`soni wave --freq 1.618 --duration 5` erzeugt einen für Menschen
   unhörbaren Ton.** Per FFT-Analyse verifiziert: die WAV-Datei
   kodiert tatsächlich buchstäblich 1,618 Hz — weit unter der
   menschlichen Hörschwelle (~20 Hz). Der Code (`sin(2π·freq·t)`)
   skaliert `freq` nirgends auf einen hörbaren Basiston (z. B.
   1,618×220 Hz). Die README-Formulierung "φ-based frequency"
   suggeriert ein hörbares musikalisches Ergebnis — tatsächlich klingt
   die Datei wie nahezu vollständige Stille. Ein Nutzer, der die Datei
   öffnet und "keinen Ton" hört, hat keine Möglichkeit, innerhalb von
   5 Minuten zu unterscheiden, ob das korrekt oder ein Bug ist — beide
   Fälle klingen identisch.
2. **`soni entropy-gate --beta 0.0625` crasht** — MIDI-Datei wird
   korrekt geschrieben, aber die anschließende Erfolgsmeldung mit
   "β" (Griechischer Buchstabe, U+03B2) crasht mit
   `UnicodeEncodeError` auf cp1252 (sechster/siebter bestätigter
   Unicode-Fall in dieser Kette). Interessanter Kontrast: der
   Gedankenstrich in `soni --help` crasht *nicht* (cp1252 bildet ihn
   zufällig ab, wenn auch als Mojibake) — nur echte griechische
   Buchstaben lösen den harten Crash aus.
3. **`soni mandala --bpm 120` schreibt gar keine Datei.** Trotz
   README-Suggestion eines "rhythm pattern"-Outputs gibt der Befehl nur
   Text aus — und zeigt dabei nur die ersten 8 von 36 berechneten
   Beats, ohne das zu kennzeichnen. Die zugrundeliegende
   Resonanzkurve ist im Code selbst als Kommentar markiert:
   *"Placeholder resonance – integrate with mandala-visualizer via
   [stack] extra"*.
4. **`entropy-gate`s MIDI-Tonhöhen-Mapping ist dagegen echt und
   reproduzierbar** — `pitch = 60 + 24·β·i`, per Hand nachgerechnet und
   exakt gegen die echten MIDI-Note-Events bestätigt. Aber diese Formel
   taucht nirgends im README oder in der CLI-Hilfe auf — aus dem
   Artefakt allein (den MIDI-Noten) lässt sich weder β=0,0625
   rekonstruieren noch verifizieren, dass das Mapping sinnvoll statt
   willkürlich ist.
5. **`__version__` = "0.1.0" vs. installiert 1.0.0** — wieder
   bestätigt, sichtbar auch über `soni version`.

**Blindtest-Verdikt: FALSE.** Besonders bemerkenswert: hier scheitert
nicht primär Code-Qualität oder Absturzfreiheit, sondern die
Wahrnehmbarkeit selbst — ein Audio-Tool, dessen Flaggschiff-Beispiel
ein Ergebnis erzeugt, das sich wie Stille anhört, kann per Definition
kein "sinnvolles, in 5 Minuten nachvollziehbares Ergebnis" liefern,
egal wie korrekt die zugrundeliegende Mathematik ist.

## Erwartetes Ergebnis

Zwölfter FALSE-Befund insgesamt (siebter unter den Programm-
Kandidaten). Erster Fall, bei dem das Kernproblem die menschliche
Wahrnehmbarkeit des Outputs selbst ist, nicht (nur) Code-Korrektheit.

## Nächster Schritt

Fünf Findings zur Weitergabe an Johann: (1) `freq`-Parameter auf einen
hörbaren Basiston skalieren (z. B. `freq · 220 Hz` statt `freq` direkt
als Hz), oder zumindest im README klarstellen, dass 1,618 Hz absichtlich
unhörbar/als Datensignal gedacht ist; (2) griechische Buchstaben aus
Erfolgsmeldungen entfernen (siehe `windows-unicode-crash-pattern`); (3)
`soni mandala` entweder eine echte Datei erzeugen lassen oder im README
als reine Text-Vorschau kennzeichnen, plus den Placeholder-Status
sichtbar machen; (4) das β→Pitch-Mapping in README/CLI-Hilfe
dokumentieren, damit es aus dem Artefakt selbst nachvollziehbar wird;
(5) `__version__`-Sync.

## Alternativen betrachtet

**Den 1,618-Hz-Befund als Nutzerfehler werten (README sagt ja explizit
"φ-based frequency", der Nutzer hätte das hinterfragen können).**
Verworfen: Regel 6 verlangt ein *innerhalb von 5 Minuten* nachvollziehbares
Ergebnis für jemanden ohne Vorwissen — dass ein Audio-Tool sein eigenes
Paradebeispiel als unhörbaren Ton ausliefert, ohne das zu erklären, ist
genau die Art Interpretierbarkeitslücke, die der Blindtest aufdecken
soll, keine Bedienungsungenauigkeit des Nutzers.
