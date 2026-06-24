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

## Alternativen betrachtet

**genesis-os selbst als alleinigen Core definieren, alles andere als
Plugin.** Verworfen: `genesis-os` hängt selbst von `entropy-table` ab und
liegt oberhalb der T0–T16-Kette — es orchestriert das mathematische
Fundament, ist es aber nicht selbst.

**Den gesamten T0–T16-Stack als "Core" behandeln.** Verworfen: verletzt
Regel 8 und macht den Blindtest unmöglich — niemand ohne Genesis-Kontext
würde verstehen, warum z.B. ein Asteroiden-Dynamik-Paket Teil eines
generischen Engine-Kerns sein soll.
