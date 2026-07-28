# Genesis-Blindtest für `mirror-machine`: FALSE — "Reflexion" ist ein reines Echo, "Phase Transition" ist echt

## Problem

`mirror-machine` (P-MIRROR) ist ein Programm-Kandidat (Anwendungsschicht
auf dem Core). Muss laut Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe (inkl. Hinweis, die fehlende
Beispiel-Sigil-Datei selbst nachzubauen), installierte real und führte
jeden dokumentierten Befehl/API-Aufruf aus — inklusive gezielter
Gegenproben, ob `beta`/`steps` echten Einfluss haben.

## Ergebnis

**Install:** `mirror-machine 1.0.0`. `__version__` in `__init__.py`
wieder auf "0.1.0" — erneut derselbe Scaffold-Rest-Bug.

**Gemischtes, differenziertes Bild — erstmals in dieser Kette eine
Funktion, die *echt* ist, neben einer, die es nicht ist:**

1. **`reflect()` ist ein reines Echo, keine Berechnung.** Verifiziert:
   `mm.state["reflection"]` ist programmatisch exakt gleich einer
   flachen Kopie der Eingabe-YAML — die Funktion tut nichts außer
   `dict(data)`. Der Docstring behauptet, dies "verkörpere das Mirror
   Principle" und verarbeite ein "trilayer YAML" — beides nirgends im
   Code wiederzufinden. Kein Schema, keine Validierung: jede
   Dict-förmige YAML wird anstandslos akzeptiert.
2. **`phase_transition()` ist dagegen echte, parametersensitive
   Mathematik.** Gegenprobe mit 8 verschiedenen `beta`/`steps`-
   Kombinationen zeigt reale, unterschiedliche Kurven (z. B.
   `beta=0.0625` → Peak 0.904, `beta=5.0` → Peak 1.613). Formel
   (`core.py`): `sigmoid(β·(t−5)) · (1 + 0.618·sin(2πt))` über
   `t=linspace(0,10,steps)` — kein hartkodierter Blindgänger wie bei
   mehreren Geschwisterpaketen dieser Session.
3. **Aber: `phase_transition()` ignoriert die Sigil-Daten komplett.**
   Das README suggeriert, Reflexion und Phasenübergang hingen
   zusammen ("Mirror Principle simulation") — tatsächlich ist
   `phase_transition()` eine von `mm.state` komplett unabhängige
   Methode, die kein Sigil-Argument entgegennimmt.
4. **"Peak emergence" ist nicht auf [0,1] begrenzt** (1.613 bei
   `beta=5.0`), trotz Namensgebung, die eine begrenzte Kennzahl
   suggeriert.
5. **Rohe, unbehandelte Python-Tracebacks bei Fehleingaben** —
   fehlende Datei oder nicht-Dict-YAML werfen ungefangene
   `FileNotFoundError`/`ValueError` mit vollständigem internen
   Stacktrace, keine nutzerfreundliche CLI-Fehlermeldung.
6. **Neue Variante des Unicode-Musters: stille Textkorruption statt
   Crash.** `mirror --help` enthält einen Gedankenstrich ("–"), der
   unter erzwungener cp1252-Konsole (`chcp 1252`, echtes `cmd.exe`,
   nicht nur Git Bash) **nicht crasht**, sondern still durch ein
   Ersatzzeichen "�" ersetzt wird — `rich`s Legacy-Windows-Fallback
   schluckt den Kodierungsfehler, statt ihn zu werfen. Anders als bei
   `medium-modulation`/`fieldtheory`/`cosmic-moment`/`sigillin`/
   `utac-core` (dort: Absturz) — hier: stille Verstümmelung, was
   potenziell unauffälliger und dadurch tückischer ist.

**Blindtest-Verdikt: FALSE.** Aber differenzierter als die bisherigen
Befunde: `phase_transition()` ist tatsächlich interpretierbar-nah
dran (reproduzierbare, parametersensitive Kurve), scheitert aber an
fehlender Referenzskala und der Entkopplung von der beworbenen
Sigil-Verbindung. `reflect()` scheitert fundamentaler — es berechnet
schlicht nichts.

## Erwartetes Ergebnis

Neunter FALSE-Befund insgesamt (vierter unter den Programm-
Kandidaten), aber der bisher differenzierteste: nicht "alles kaputt",
sondern eine echte, eine unechte Funktion nebeneinander, plus eine neue
Unicode-Fehlervariante (stille Korruption statt Absturz) zur bereits
dokumentierten Sammlung in `windows-unicode-crash-pattern`.

## Nächster Schritt

Vier Findings zur Weitergabe an Johann: (1) `reflect()` entweder mit
echter Verarbeitung hinterlegen oder als reinen Pass-Through
kennzeichnen, statt "Mirror Principle" zu behaupten; (2)
`phase_transition()` tatsächlich mit den Sigil-Daten verknüpfen, wenn
das die beworbene Funktion sein soll; (3) Fehlerbehandlung für
fehlende/fehlerhafte Sigil-Dateien ergänzen (keine rohen Tracebacks);
(4) `windows-unicode-crash-pattern` um diese stille-Korruption-Variante
ergänzen — nicht nur Abstürze, auch unbemerkte Zeichenersetzung gehört
zum selben Root-Cause-Cluster.

## Alternativen betrachtet

**`phase_transition()` als vollwertig TRUE werten, weil die Mathematik
echt ist.** Verworfen: echte Parametersensitivität allein reicht
nicht für Regel 6 — es fehlt weiterhin jede Referenzskala/Erklärung,
was ein "gutes" Ergebnis wäre, und die beworbene Verbindung zur
Sigil-Reflexion existiert nicht. Der Gesamtbefund für das Paket bleibt
FALSE, auch wenn eine Teilkomponente besser abschneidet als üblich.
