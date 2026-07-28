# Vorschlag: Scope des Genesis Core / UTAC Core

## Problem

`ADR-001` legt fest, dass ein eigenes Genesis Core / UTAC Core Monorepo
entsteht — aber nicht, *was* konkret hinein gehört. `ECOSYSTEM_MAP.yaml`
listet alle 48 Pakete mit echten Abhängigkeiten (T0–T16), aber ohne
Klassifikation nach Regel 7 (Core funktioniert ohne LLM und ohne
Internet) und Regel 8 (keine privilegierte Domäne).

## Vorschlag

**Kernthese:** Der Core ist nicht "genesis-os als ein großes Paket",
sondern eine schmale, deterministische Laufzeit-Kette ohne LLM-/
Netzwerk-Abhängigkeit. Alles, was Visualisierung, Domänen-Anwendung oder
KI-Inferenz ist, bleibt Programm bzw. Hilfsprogramm/Plugin und hängt vom
Core ab — nicht umgekehrt.

### Core-Kandidaten

Die Fundament-Kette aus `ECOSYSTEM_MAP.yaml` (Tier `released` bis `T6`),
alle mathematisch/deterministisch, kein "AI core", kein reines UI:

`entropy-table` → `implosive-genesis` → `entropy-governance` →
`medium-modulation` → `cosmic-moment` → `fieldtheory` → `sigillin` →
**`utac-core`** (strukturelles Zentrum der Kette).

**Hinweis zur Reihenfolge (2026-06-26):** Diese Kette bildet die
*technische Abhängigkeitsordnung* aus `ECOSYSTEM_MAP.yaml` ab (echte
Code-Imports), nicht die *historische Erfindungsreihenfolge*. Johann hat
klargestellt, dass die tatsächliche Entstehungsgeschichte umgekehrt
verlief: zuerst `sigillin`, dann `CREP` als Metrik dafür, dann
`unified-mandala`, dann `fieldtheory` und `UTAC`. Die beiden Reihen
fallen nicht zusammen — eine Idee kann zuerst entstehen und trotzdem
technisch erst spät in der Abhängigkeitskette stehen (weil andere Module
erst nachträglich als Fundament darunter gebaut wurden). Für den
Blindtest und die Core/Programm/Hilfsprogramm-Klassifikation ist die
technische Kette weiterhin maßgeblich (Regel 8: keine privilegierte
Domäne, keine Bevorzugung nach Entstehungsdatum) — der historische
Hinweis dient nur dem Verständnis, warum die Pakete so benannt/verknüpft
sind, wie sie es sind.

### Programm-Kandidaten

Bauen direkt auf dem Core auf, sind Anwendungs-/Visualisierungsschicht,
kein erkennbarer LLM-Bedarf — muss aber pro Paket im Blindtest geprüft
werden: `mandala-visualize`, `implosive-origin-utac`, `sonification`,
`climate-dashboard`, `mirror-machine`, `cosmic-web`, `unified-mandala`.

### Hilfsprogramm-Kandidaten (Regel 7)

Domäne/Beschreibung deutet auf LLM-/AI-Abhängigkeit hin — diese können
nach Regel 7 nie Core werden:

- `aeon-ai` — explizit "AI core engine"
- `genesis-scope` — explizit "human-AI navigation layer" (bereits als
  Blindtest-Kandidat in `01_Ideen/claude/` markiert)
- `AdvancedWeightingSystems` — "neural-statistical CREP weighting"
- `worldview` — "philosophisch-ethische CREP-Bewertung"
- `gemeinwohl` — "common-good normative scoring"

### Die übrigen ~35 Domänen-Pakete

Die große Mehrheit der T0-Pakete (`amazon-utac`, `sandpile-utac`,
`quantum-genesis` etc.) sind weder Core noch generisches Programm:
domänenspezifische Hilfsprogramme/Plugins, die den Core (`utac-core`/
CREP) als Bibliothek nutzen, um eine einzelne wissenschaftliche
Fragestellung zu bearbeiten — passend zur ursprünglichen
Diamond-Template-Architektur und zu Regel 8 (keine privilegierte
Domäne).

### Sonderfall genesis-os

`genesis-os` (Orchestrator) ist vermutlich Core, aber als dünne
Orchestrierungsschicht — nicht als Container für AI-Logik. Es darf
Plugins laden, die LLM nutzen, ohne selbst eine LLM-Laufzeitabhängigkeit
zu haben. Das muss am echten Code verifiziert werden, bevor `genesis-os`
als Architektur-Eintrag mit `status: accepted` eingereicht wird.

## Erwartetes Ergebnis

Eine vorläufige Drei-Klassen-Karte (Core/Programm/Hilfsprogramm) für alle
48 Pakete als Ausgangshypothese für die kommenden Genesis-Blindtests.
Kein Paket wechselt durch diesen Plan selbst den Status — das passiert
erst einzeln pro Paket nach Blindtest + ADR (Regel 3, Regel 6).

## Nächster Schritt

1. Jedes Core-Kandidat-Paket einzeln durch den Genesis-Blindtest schicken
   und als eigenen Trylayer-Eintrag in `03_Architektur/` anlegen
   (`related_adr: [ADR-001]` plus ein neues ADR für die Kernfrage "warum
   genau diese Kette").
2. Prüfen, ob `fieldtheory` (T4, EN) und `Feldtheorie` (T0, DE) tatsächlich
   Duplikate sind — falls ja, wird die Core-Kette kürzer.
3. `genesis-os`' tatsächlichen Code prüfen, bevor es als Core-Orchestrator
   eingereicht wird.
4. Für jeden Hilfsprogramm-Kandidaten per Code-Review bestätigen, ob eine
   LLM-Laufzeitabhängigkeit wirklich vorliegt — die Einordnung hier
   basiert nur auf der Domänen-Beschreibung aus der Roadmap, nicht auf
   Code-Inspektion.
5. **Maßstab für Schritt 1 präzisiert (2026-06-24):** die Genesis-
   Blindtests gegen `genesis-scope`/`genesis-os` (beide FALSE, siehe
   `01_Ideen/claude/genesis-scope-blindtest`) sind die Baseline, nicht
   ein Verdikt über diese Satelliten-Pakete — siehe
   `01_Ideen/claude/blindtest-baseline-fuer-monorepo-readme`. Für den
   Core selbst gilt anders als für Domänen-Pakete: der Blindtest muss
   bestehen, bevor ein Core-Kandidat `status: accepted` bekommt.
6. **Erster Core-Kandidat real getestet, Befund konkret schlechter als
   erwartet (2026-06-24):** `entropy-table` (Kettenanfang) durch den
   Blindtest geschickt — siehe `01_Ideen/claude/entropy-table-blindtest`.
   Ergebnis: nicht nur semantisch unklar wie bei den Satelliten-Paketen,
   sondern auf dem dokumentierten `pip install`-Pfad technisch defekt
   (fehlende `typer`-Dependency, keine Atlas-Daten im Paket,
   hartkodierte Pfade, CLI-Hilfetext widerspricht dem echten Parser).
   Der `git clone`-Pfad blieb wegen Sandbox-Netzwerkbeschränkung
   ungetestet. Falls sich dieser Befund bestätigt, ist die vorgeschlagene
   Core-Kette bereits am ersten Glied blockiert — unabhängig von der
   architektonischen Frage, was in den Core gehört.
7. **Re-Test nach Fix: erster Core-Kandidat besteht den Blindtest
   (2026-06-25):** Johann hat alle sechs Bugs aus Schritt 6 behoben und
   als v2.0.1 auf PyPI veröffentlicht. Ein erneuter, frischer Subagent
   hat verifiziert: alle sechs Bugs FIXED, `pip install entropy-table`
   liefert jetzt ein funktionierendes CLI mit echten Atlas-Daten und
   echten Entropieproduktions-Berechnungen — siehe
   `01_Ideen/claude/entropy-table-blindtest`, `blindtest_passed: true`.
   `entropy-table` ist damit der erste Baustein der vorgeschlagenen
   Core-Kette, der den verschärften Maßstab für Core-Kandidaten
   tatsächlich erfüllt. Die übrigen Kettenglieder
   (`implosive-genesis` → ... → `utac-core`) sind weiterhin einzeln zu
   testen.
8. **Zweites Kettenglied (`implosive-genesis`) getestet, TRUE mit zwei
   kleinen Doku-Bugs (2026-06-25):** siehe
   `01_Ideen/claude/implosive-genesis-blindtest`, `blindtest_passed:
   true`. `pip install implosive-genesis` (v1.0.0, README behauptet
   "v0.4.0 current" — dieselbe Versionsdiskrepanz wie bei
   `entropy-table`) liefert sofort funktionierendes CLI (6 von 8
   dokumentierten Befehlen) und eine vollständig funktionierende
   Python-API mit echtem wissenschaftlichem Output (V_RIG-Berechnung,
   OIPK-Kernel, Tesseract-Rendering, Chronology-Validator). Zwei
   konkrete, leicht behebbare Bugs: `ig full-summary` ist dokumentiert,
   existiert aber nicht im CLI (nur via Python-API); `ig cmb-test
   --n_sim` crasht wegen Unterstrich statt Bindestrich. Qualitativ
   deutlich besser als der erste `entropy-table`-Befund — kein
   struktureller Defekt, sondern reine
   Dokumentations-/CLI-Konsistenzfehler, zur Weitergabe an Johann
   vorgesehen.
9. **Drittes Kettenglied (`entropy-governance`) getestet, FALSE mit
   zwei echten Bugs (2026-07-29):** siehe
   `01_Ideen/claude/entropy-governance-blindtest`, `blindtest_passed:
   false`. `pip install entropy-governance` (v1.0.0) liefert
   funktionierendes CLI + Python-API, alle Formeln arithmetisch
   korrekt — aber `--steps` beeinflusst die "Tesseract Slices"-Tabelle
   nicht (hartkodiert auf 4 Zeilen, empirisch mit 10/200/1000 Schritten
   bestätigt), das eigene `__version__` in `__init__.py` steckt auf
   "0.1.0" fest und leckt in CLI-Output und Export-YAMLs (derselbe
   Bug-Typ in mind. 4 weiteren Paketen, siehe
   `version-string-drift-audit`), und die dokumentierten S∝A/S∝V-
   Kernformeln existieren im Code nur als ungenutzte SymPy-Platzhalter.
   Fehlende Referenzskala/Einheiten für alle Ausgabewerte — Blindtest
   FALSE. Zur Weitergabe an Johann vorgesehen, Re-Test nach Fix analog
   zu `entropy-table`.
10. **Viertes Kettenglied (`medium-modulation`) getestet, FALSE
    (2026-07-29):** siehe `01_Ideen/claude/medium-modulation-blindtest`.
    Installiert sauber, aber `mm --help` crasht unter Windows (∝-Zeichen,
    cp1252), `__version__` steckt auf "0.1.0" fest, und
    `coupling_factor`s `modulation_depth`-Parameter hat nachweislich
    keinerlei Effekt (hartkodiertes `t=0.0` macht den Modulationsterm
    immer Null) — direkte Konsequenz: zwei als unterschiedlich
    präsentierte Größen (`modulated_entropy`, `coupling_factor`)
    liefern identische Zahlen.
11. **Fünftes Kettenglied (`cosmic-moment`) getestet, FALSE
    (2026-07-29):** siehe `01_Ideen/claude/cosmic-moment-blindtest`.
    Bemerkenswertester Einzelbefund der ganzen Kette: die
    README-eigene Demo-Schwelle (0.618) liegt strukturell unter dem
    Minimum der Default-Formel (~0.927) — das Flaggschiff-Beispiel
    meldet dadurch *garantiert* "100/100 erkannt", unabhängig von der
    tatsächlichen Funktion des Schwellenwerts. Zusätzlich: `collapse()`
    berechnet nichts (hartkodierte Rückgabe für jeden Input), der
    beworbene `ChronologyValidator`-Check wird aufgerufen, aber sein
    Ergebnis verworfen, und ein dritter Fall des Unicode-Crash-Musters.
12. **Sechstes Kettenglied (`fieldtheory`, EN) getestet, FALSE
    (2026-07-29):** siehe `01_Ideen/claude/fieldtheory-en-blindtest`.
    Bereits als kein Duplikat von `Feldtheorie` (DE) bestätigt (siehe
    `fieldtheory-feldtheorie-kein-duplikat`). Kein `__version__`-Bug
    hier (positives Gegenbeispiel). Aber: README-eigenes
    "Override"-Beispiel nutzt zufällig exakt die CLI-Defaultwerte (No-Op,
    keine echte Demonstration), vierter Unicode-Crash-Fall, und
    `derive_lagrangian()` liefert zwei nicht zueinander passende
    Gleichungen (die gezeigte Lagrangian hat kein `Ṡ`, aus dem sich die
    gezeigte Euler-Lagrange-Gleichung herleiten ließe — sie stammt
    nachweislich aus einer zweiten, nie zurückgegebenen internen Form).
13. **Siebtes Kettenglied (`sigillin`) getestet, FALSE (2026-07-29):**
    siehe `01_Ideen/claude/sigillin-blindtest`. Schwerwiegendster
    Einzelbefund der Kette: die namensgebende "CREP-Validierung" prüft
    nachweislich nur Feld-*Existenz*, keine Werte (ein Sigil mit
    `coherence: -99999`, `resonance: "banana"` etc. besteht die
    Validierung anstandslos). `render_mandala()` ist laut eigenem
    Docstring ein erklärter Platzhalter und bit-identisch unabhängig
    von den Sigil-Daten. Zusätzlich: `[stack]`-Empfehlung wird von
    Rich-Markup verschluckt (CLI empfiehlt versehentlich den bereits
    ausgeführten Befehl), fünfter Unicode-Crash-Fall, und ein
    komplett undokumentiertes, größeres API (`SigillinRecord` u. a.).
14. **Achtes und letztes Kettenglied (`utac-core`, strukturelles
    Zentrum) getestet, FALSE (2026-07-29):** siehe
    `01_Ideen/claude/utac-core-blindtest`. Schwerwiegendster Befund
    überhaupt: der allererste Quickstart-Befehl (`utac fit --beta
    0.0625`) läuft gar nicht (`--beta` existiert nicht als Flag), alle
    vier CLI-Befehle crashen zusätzlich nativ unter Windows (sechster
    Unicode-Fall), `__version__`-Mismatch bestätigt, und das
    README-eigene `v_RIG`-Beispiel verwendet nachweislich nicht das im
    selben Code-Block gefittete β, sondern still den Funktions-Default.

**Sammelbefund über die ganze Kette (2026-07-29):** von acht
getesteten Kettengliedern bestehen zwei (`entropy-table` nach Fix,
`implosive-genesis`), sechs nicht. Zwei wiederkehrende Fehlerklassen
ziehen sich durch mehrere Pakete unabhängig voneinander: (a)
`__version__`-Drift in `__init__.py` — bei gezielter Prüfung bestätigt
in 5 von 8 Kettengliedern (`entropy-governance`, `medium-modulation`,
`cosmic-moment`, `sigillin`, `utac-core`; `fieldtheory` EN ist sauber
synchronisiert; `entropy-table`/`implosive-genesis` hatten einen
anderen, früher gefundenen Versions-Bug-Typ — README-Prosa-Behauptung
vs. tatsächliche Version — und wurden nicht gezielt auf das interne
`__version__`-Feld geprüft; siehe `version-string-drift-audit`) und
(b) ein Windows-Unicode-Crash durch mathematische Sonderzeichen (∝, β,
σ, Φ, →, ✓/✗) in CLI-Hilfetexten/-Ausgaben über `rich` — bestätigt in
5 von 8 Kettengliedern (`medium-modulation`, `cosmic-moment`,
`fieldtheory`, `utac-core`, `sigillin`; die übrigen drei wurden nicht
gezielt auf dieses Muster geprüft, da es erst ab dem vierten Test
auffiel). Beides sieht nach demselben zugrundeliegenden Scaffold-/
Vorlagen-Ursprung aus (`diamond-setup`) und verdient einen einzigen,
ökosystemweiten Fix-Vorschlag statt Einzelkorrekturen — siehe eigener
Trylayer-Eintrag
`windows-unicode-crash-pattern`.

15. **Alle sechs kleineren Programm-Kandidaten getestet, alle sechs
    FALSE (2026-07-29):** `mandala-visualizer`, `climate-dashboard`,
    `mirror-machine`, `sonification`, `cosmic-web`, `implosive-origin-
    utac` — siehe die jeweiligen `01_Ideen/claude/*-blindtest`-Einträge.
    Kein einziger besteht den Blindtest unverändert, aber die Befunde
    sind qualitativ vielfältiger als in der Core-Kette:
    - `mandala-visualizer`: CLI crasht erst *nach* erfolgreichem
      PNG-Export (irreführend statt blockierend); "cosmic-web"-Render
      ist ein simpler `networkx.star_graph(20)`;
      `mermaid_grafana_bridge()` ignoriert sein `data`-Argument
      vollständig (`# noqa: ARG001`); `__version__` sauber (Gegenbeispiel).
    - `climate-dashboard`: sauberster Beleg für rein dekorative
      "Stack Integration" — keines der 10 gelisteten Pakete wird in
      `cli.py`/`app.py` tatsächlich importiert; `mandala_peaks` ist ein
      einzelner Skalar, der auf jede Zeile gebroadcastet wird, keine
      echte Peak-Erkennung; `__version__`-Leck sogar im Footer des
      Live-Dashboards; `--steps` funktioniert dagegen echt (positiv);
      erster Fall von stiller Mojibake-Korruption statt Absturz.
    - `mirror-machine`: `reflect()` ist ein reines Echo (programmatisch
      verifiziert); `phase_transition()` ist echte, parametersensitive
      Mathematik, aber vollständig vom Sigil-Zustand entkoppelt; zweiter
      Fall stiller Unicode-Mojibake statt Absturz.
    - `sonification`: bemerkenswertester Einzelfund der ganzen Charge —
      `soni wave --freq 1.618` erzeugt einen für Menschen *unhörbaren*
      Ton (1,618 Hz, per FFT verifiziert); `soni mandala` schreibt gar
      keine Datei; `entropy-gate`'s Pitch-Mapping ist real, aber
      undokumentiert.
    - `cosmic-web`: bislang am stärksten gemischter Befund — echte
      NetworkX-Metriken, echter Determinismus, echtes Dashboard, *und*
      ein komplett undokumentierter, funktionierender N-Body-Kosmologie-
      Simulator (`CosmicWebSimulator`) — aber das titelgebende Konzept
      "Emergence" ist nachweislich reines, strukturunabhängiges Rauschen.
    - `implosive-origin-utac`: als `SPECULATIVE` gekennzeichnet und mit
      ungewöhnlich ehrlichen Docstrings ("status: SPECULATIVE" direkt im
      Code); zwei der drei Kernbehauptungen (`r`, `crep_gamma`) stimmen
      exakt; aber `k_RIG` ist intern widersprüchlich (Code sagt 0,304,
      ein Docstring sagt 0,097) und `n_efolds` hat nachweislich null
      Effekt auf jede Vorhersage trotz einer echt laufenden ODE.

    Ergänzung zum Unicode-Crash-Muster: zwei neue Fälle bestätigt
    (`sonification`, `cosmic-web`) sowie ein neuer Sub-Typ — stille
    Mojibake-Korruption statt Absturz (`mirror-machine`,
    `climate-dashboard`) — noch nicht in
    `windows-unicode-crash-pattern` nachgetragen. `__version__`-Drift:
    weiterhin bestätigt bei `sonification`; `mandala-visualizer` und
    `cosmic-web` sind saubere Gegenbeispiele (jetzt insgesamt vier).

## Alternativen betrachtet

**genesis-os selbst als alleinigen Core definieren, alles andere als
Plugin.** Verworfen: `genesis-os` hängt selbst von `entropy-table` ab und
liegt oberhalb der T0–T16-Kette — es orchestriert das mathematische
Fundament, ist es aber nicht selbst.

**Den gesamten T0–T16-Stack als "Core" behandeln.** Verworfen: verletzt
Regel 8 und macht den Blindtest unmöglich — niemand ohne Genesis-Kontext
würde verstehen, warum z.B. ein Asteroiden-Dynamik-Paket Teil eines
generischen Engine-Kerns sein soll.
