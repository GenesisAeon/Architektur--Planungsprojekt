# Genesis-Blindtest für `sigillin`: FALSE — "CREP-Validierung" prüft nur Feld-Existenz, nicht Werte

## Problem

`sigillin` (P-SIGIL) ist das siebte Kettenglied der Core-Kette. Muss
laut Regel 6 den Genesis-Blindtest bestehen.

## Vorgehen und Durchführung

Ein frischer, kontextfreier Subagent bekam ausschließlich das
vollständige README als Eingabe, musste die Beispiel-Sigil-Datei selbst
aus dem README-Text nachbauen (keine mitgelieferte Beispieldatei), und
führte jeden dokumentierten Befehl/API-Aufruf aus — inklusive gezielter
Gegenproben mit absichtlich unsinnigen Werten.

## Ergebnis

**Install:** `sigillin 1.0.0`. **`__version__`** in `__init__.py`
hartkodiert auf **"0.4.0"** — wieder derselbe Scaffold-Rest-Bug
(siebter bestätigter Fall).

**Der schwerwiegendste bisherige Befund der Kette:**

1. **"CREP-Validierung" prüft nur Feld-Existenz, keine Werte.**
   `validate_crep()`/`assert_crep()` sind wörtlich
   `all(k in self.data for k in CREP_KEYS)`. Direkte Gegenprobe:
   ein Sigil mit `coherence: -99999`, `resonance: "banana"` (String
   statt Zahl), `emergence: 123456789`, `poetics: 42` (Int statt Text)
   wurde als **`validate_crep(): True`** akzeptiert, `assert_crep()`
   warf keine Exception. Kein Wertebereich-Check, kein Typ-Check,
   keinerlei Plausibilitätsprüfung — die README-Behauptung "Every
   sigil is validated against four pillars" ist irreführend: nichts
   an "coherence"/"resonance"/"emergence" als *sinnvolle Zahlen* wird
   je geprüft.
2. **`render_mandala()`s "Peak"-Wert ist komplett losgelöst von den
   Sigil-Daten.** Gegenprobe: dieselbe Funktion gegen das echte Sigil
   (0.97/0.88/0.92) und ein zweites mit allen drei Werten auf 0.01
   ausgeführt — die beiden Ausgabe-Spektren sind **bit-identisch**
   (`(spec1 == spec2).all() == True`). Der eigene Docstring der
   Funktion gibt es zu: `"placeholder MandalaMap binding"` — sie ist
   buchstäblich `np.sin(t·depth)·1.618`, eine reine Funktion des
   `depth`-CLI-Parameters (Default φ=0.618), berührt `self.data` nie.
3. **`[stack]`-Hinweis wird von Rich-Markup verschluckt.**
   `bind_to_field()` gibt `"...pip install sigillin[stack]"` zurück,
   aber `cli.py` gibt das ungeschützt an `console.print()` weiter —
   Rich interpretiert `[stack]` als Style-Tag und entfernt es
   stillschweigend. Verifiziert direkt reproduziert. Ergebnis: die CLI
   sagt dem Nutzer wörtlich, er solle `pip install sigillin` ausführen
   — genau den Befehl, den er bereits ausgeführt hat, statt des Extras,
   das er eigentlich braucht.
4. **Crash unter Windows-Standardkonsole** (fünfter bestätigter Fall
   des Unicode-Musters) — `✓`/`✗`-Zeichen, `UnicodeEncodeError` auf
   cp1252, betrifft `validate`/`inspect`/`render` gleichermaßen.
5. **Ein komplett undokumentiertes, größeres API existiert.**
   `sigillin/__init__.py` exportiert `SigillinRecord`, `Q4StateData`,
   `CREPValues` (mit einem zusätzlichen `Gamma`-Feld, das im README
   nicht vorkommt), `UTACState`, `NarrativeMetadata`,
   `ValidationResult`, plus `create_sigillin`/`serialize_sigillin`/
   `deserialize_sigillin`/`validate_sigillin`/`link_sigillins`/
   `compute_sigillin_id` (SHA256-Lineage-IDs) — nichts davon im README
   erwähnt. Ein echter Erstnutzer würde diese Hälfte des Pakets nie
   entdecken.

**Blindtest-Verdikt: FALSE.** Und zwar in einer besonders klaren Form:
die zentrale, namensgebende Behauptung des Pakets ("CREP-validierte
Sigile") hält einer direkten Gegenprobe nicht stand — validiert wird
nur Struktur, nicht Bedeutung, und die visuelle "Resonanz"-Ausgabe ist
laut eigenem Code ein erklärter Platzhalter, der die Eingabedaten
komplett ignoriert.

## Erwartetes Ergebnis

Achter FALSE-Befund in der Kette, mit dem bislang direktesten
Widerspruch zwischen Marketing-Behauptung und Code-Realität.

## Nächster Schritt

Fünf Findings zur Weitergabe an Johann: (1) `validate_crep()` um
echte Wertebereichs-/Typ-Prüfung erweitern, oder README-Behauptung
präzisieren ("struktur-validiert", nicht "CREP-validiert"); (2)
`render_mandala()` entweder tatsächlich aus `self.data` berechnen oder
im README explizit als Platzhalter kennzeichnen; (3) `[stack]` in
Rich-`console.print()`-Aufrufen escapen (`rich.markup.escape()`); (4)
`__version__`-Sync (achter Fall, siehe `version-string-drift-audit`);
(5) README um die tatsächlich vorhandene erweiterte API
(`SigillinRecord`/`Q4StateData`/Lineage-IDs) ergänzen oder die Trennung
absichtlich dokumentieren, falls das öffentliche vs. interne API sein
soll.

## Alternativen betrachtet

**Den Befund milder einordnen, weil die Funktionen technisch fehlerfrei
laufen (kein Crash im Kern-Pfad).** Verworfen: "läuft ohne Absturz"
und "tut das, was es behauptet" sind hier zwei verschiedene Dinge —
genau die Unterscheidung, die Regel 6 treffen soll. Ein Blindtest, der
nur auf Absturzfreiheit prüft, hätte diesen Befund verpasst.
