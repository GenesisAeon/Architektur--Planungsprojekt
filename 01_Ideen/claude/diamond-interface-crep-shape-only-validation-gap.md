# Diamond-Interface-Validator prüft nur Form, nie Bedeutung von CREP -- Ursache für leere `get_crep_state()`-Werte

## Problem

Johanns Frage, ob CREP als echte domänenübergreifende Brücke definiert
bleiben könnte, führte zu einer Kette echter Code-Funde: `afet-tensions`
(P34) liefert `get_crep_state()["P"] = 0.8` hartkodiert; `resilience-core`
(P40, siehe [[resilience-core-blindtest]]) liefert `"P" =
float(not state.near_collapse)`, ein wiederverwendetes internes Flag statt
einer eigens für die Domäne hergeleiteten Größe. Frage: liegt der Fehler
im einzelnen Paket, oder tiefer im System?

## Vorgehen und Durchführung

Direkte Code-Inspektion (nicht Vermutung) auf drei Ebenen:
1. `Feldtheorie/setup/universal_skeleton_builder.py` -- der Skeleton-
   Builder, den Johann als Beleg für die Designabsicht zitierte.
2. `afet-tensions`/`resilience-core`: Suche nach `sigillin_metrics.yaml`
   (der im Builder dokumentierte Anpassungs-Artefakt).
3. `diamond_setup.validation.validate_diamond_instance` (per
   `inspect.getsource`, echter installierter Code, nicht Doku) -- der
   tatsächliche Validator, gegen den `contracts/diamond.interface.yaml`
   in beiden Paketen verweist.

## Ergebnis

**Die Designabsicht ist real und im Code dokumentiert (Johann hatte
recht):** `universal_skeleton_builder.py` definiert CREP explizit als
"Coherence, Resonance, Emergence, Potential" mit dem Kommentar "ADAPT
THIS to your project: Change weights... Replace metrics entirely" und
liefert dokumentierte Alternativ-Templates fuer Business (ROI:
Profit/Efficiency/Risk/Opportunity) und Engineering (KPI:
Quality/Safety/Testability/Maintainability). Der vorgesehene Weg: die
generierte `config/sigillin_metrics.yaml` von Hand mit echter,
domänenspezifischer Begründung pro Buchstabe füllen.

**Aber:** Weder `afet-tensions` noch `resilience-core` besitzen
irgendwo im Repo eine `sigillin_metrics.yaml` -- der vorgesehene
Anpassungsschritt wurde nie durchlaufen. Stattdessen implementieren
beide `get_crep_state()` direkt in Python, ohne Bezug zu diesem
Konfigurationsmechanismus.

**Die tiefere Ursache liegt in einer dritten, davon unabhängigen
Schicht:** `contracts/diamond.interface.yaml` (in beiden Paketen
identisch) referenziert `diamond_setup.protocol.DiamondPackage` /
`diamond_setup.validation.validate_diamond_instance` als den
tatsächlich durchgesetzten Vertrag. Dessen Quellcode (per
`inspect.getsource`, echt installiertes Paket):

```python
for method, expected_type, keys in (
    ("get_crep_state", dict, CREP_KEYS), ...
):
    value = getattr(instance, method)()
    if not isinstance(value, expected_type):
        errors.append(...)
    missing = keys - set(value.keys())
    if missing:
        errors.append(f"{method} missing keys: {sorted(missing)}")
```

Der Validator prüft ausschließlich: (a) Rückgabetyp ist `dict`, (b) die
Schlüssel `{C, R, E, P, Gamma}` sind vorhanden. Keine Wertprüfung, kein
Bezug zu `sigillin_metrics.yaml`, keine Prüfung auf Konstanten oder
Trivialwerte. Ein Paket besteht `validate_diamond_instance` unabhängig
davon, ob `P` aus echten Domänendaten berechnet oder hartkodiert ist.

**Verdikt:** Drei separate, teils widersprüchliche CREP-Bedeutungen
koexistieren im Ökosystem, ohne dass irgendein Mechanismus sie
zusammenhält:
1. Ursprungsgeschichte (Memory `project_crep_origin_story`): Stabilität/
   Reproduktionsfähigkeit/Konnektivität/Kinetik, physikalische Größen.
2. `universal_skeleton_builder.py`: Coherence/Resonance/Emergence/
   Potential, generisches Repo-Qualitäts-Template, explizit
   domänenadaptierbar.
3. Faktische Paket-Implementierungen (`afet-tensions`,
   `resilience-core`): weder (1) noch (2), sondern Wiederverwendung
   vorhandener interner Variablen (teils hartkodierte Konstanten) rein
   um die Schlüsselform des Validators zu erfüllen.

Die Designabsicht (2) ist intakt und sinnvoll. Der Bruch liegt zwischen
(2) und (3): der einzige technisch durchgesetzte Vertrag (der
Validator) prüft nichts von dem, was die Designabsicht eigentlich
verlangt (echte, dokumentierte Anpassung via `sigillin_metrics.yaml`).

## Erwartetes Ergebnis

Kein Paket muss deshalb zwangsläufig umbenannt werden -- das eigentliche
Problem ist eine Lücke im Validierungsvertrag, nicht (nur) einzelne
Paket-Fehler. Ob CREP als Name für (1), (2), (3) oder nur eine
bestimmte davon reserviert bleibt, ist eine Entscheidung, die nur
Johann treffen kann (siehe Rückfrage).

## Nächster Schritt

Zur Entscheidung an Johann vorgelegt (siehe Chat): Soll
`validate_diamond_instance` erweitert werden, um echte semantische
Substanz einzufordern (z.B. Existenz + nicht-generischer Inhalt einer
`sigillin_metrics.yaml`, oder ein Verbot literal hartkodierter
Konstanten in `get_crep_state()`-Werten)? Falls ja, wäre das eine
zentrale Änderung an `diamond_setup` selbst, mit Wirkung auf alle
Pakete, die den Diamond-Vertrag nutzen -- nicht auf einzelne Repos
beschränkbar, daher hier zurückgestellt statt eigenmächtig umgesetzt.

## Alternativen betrachtet

**Die drei CREP-Bedeutungen einfach als "das ist halt so gewachsen"
stehen lassen.** Verworfen: genau das ist der Zustand, den Johanns
Namensdisziplin-Entscheidung (CREP bleibt CREP nur bei gleicher
Bedeutung) beheben sollte -- ohne Klärung, welche der drei Bedeutungen
(oder ob keine) als "die" CREP gilt, lässt sich die Regel nicht
anwenden.
