# GenesisAeon Metric Registry

Analog zu `PACKAGE_REGISTRY.md` (Quelle der Wahrheit für P-Nummern) ist
dies die Quelle der Wahrheit für benannte Vier-Buchstaben-Metriken im
GenesisAeon-Ökosystem. Entstanden aus einer Diskussion am 2026-08-05
über CREP-Namensdisziplin (siehe Chat, `01_Ideen/claude/
resilience-core-blindtest.md` und `01_Ideen/claude/
diamond-interface-crep-shape-only-validation-gap.md`).

**Grundregel (Johanns Entscheidung, 2026-08-05):** Ein Metrikname bleibt
nur dann gültig für ein Paket, wenn die Bedeutung mit dem hier
registrierten kanonischen Eintrag übereinstimmt. Verschiebt sich die
Bedeutung in eine andere Domäne, bekommt sie einen eigenen Namen
(Vorbild: `scope-resilience`s `Ρ_sem`, nicht einfach `Ρ`). Die
Vier-Komponenten-**Struktur** ist ein legitim wiederverwendbares Muster
— aber jede inhaltlich eigenständige Instanz braucht einen eigenen
Namen, damit "X wird in N Paketen verwendet" nicht mehr als
Validierungs-Beleg für eine einzelne Metrik missverstanden werden kann.

---

## CREP — kanonisch: Coherence / Resonance / Emergence / Potential

**Status: kanonisch festgelegt, 2026-08-05 (Johann + Gemini).**

CREP ist die **domänenübergreifende Brückenmetrik** — nicht die eigene
interne Größe eines Pakets. Ein Paket rechnet mit seinen eigenen,
domänenpassenden Größen (z.B. Γ, Kopplungslast, Kritikalitätsmarge) und
**übersetzt** diese bei Bedarf für domänenübergreifende Experimente in
die Brücken-Form:

| Buchstabe | Bedeutung |
|---|---|
| C | Coherence |
| R | Resonance |
| E | Emergence |
| P | Potential |
| Gamma | geometrisches Mittel von C·R·E·P (Aggregat) |

**Herkunft:** Eine frühere, unabhängig entstandene CREP-Bedeutung
(Stabilität/Reproduktionsfähigkeit/Konnektivität/Kinetik, physikalische
Größen — siehe Memory `project_crep_origin_story`) gilt als
historische Vorstufe, nicht als konkurrierende aktuelle Definition:
konkrete physikalische Größen wurden zu den allgemeineren
Brücken-Labels abstrahiert, damit CREP überhaupt über wild
unterschiedliche Domänen (Physik, Business, Code-Qualität, Epistemik)
hinweg funktionieren kann. Bestätigt durch echten Code-Fund in
`Feldtheorie/setup/universal_skeleton_builder.py`: dort explizit als
"ADAPT THIS to your project" dokumentiert, mit Alternativ-Templates für
Business (ROI: Profit/Efficiency/Risk/Opportunity) und Engineering
(KPI: Quality/Safety/Testability/Maintainability) — CREP ist eine von
mehreren möglichen Vier-Metrik-Instanzen dieses generischen Templates,
nicht das Template selbst.

**Technische Durchsetzung (seit `diamond-setup` v2.3.0, PR
[#9](https://github.com/GenesisAeon/diamond-setup/pull/9), noch nicht
gemerged/released):** `CREPState.bridge_adapted: bool` (Default
`False`). `True` nur, wenn ein Paket C/R/E/P tatsächlich durch eine
durchdachte Übersetzung seiner eigenen Domänengrößen herleitet — nicht
durch Wiederverwendung vorhandener interner Variablen oder
hartkodierte Konstanten. Additiv, bricht keine bestehende Validierung.

**Bekannte Nicht-Konformität (Bestandsaufnahme, nicht Vorwurf):**
`afet-tensions` (P34, `get_crep_state()["P"] = 0.8` hartkodiert) und
`resilience-core` (P40, `"P" = float(not state.near_collapse)`, ein
wiederverwendetes Flag) — beide bestehen den reinen Form-Validator,
beide haben `bridge_adapted` faktisch nicht (noch nicht existent vor
v2.3.0). Kein sofortiger Umbau nötig (siehe unten, Migrations-Prinzip).

---

## UTAC — Bedeutung noch ungeklärt (offene Frage an Johann)

**Status: zwei widersprüchliche Ausschreibungen gefunden, keine davon
im zentralen `diamond-setup`-Paket selbst verankert.**

- `resilience-core`-README: "UTAC (Universal Tipping Attractor
  Cascade)".
- `Feldtheorie/setup/universal_skeleton_builder.py`-Docstring: "UTAC
  (Universal Threshold Activation-Coupling)".
- `diamond_setup.protocol.UTACState` (die tatsächlich durchgesetzte
  Form: `{H, H_star, K_eff}`) schreibt die Buchstaben nirgends aus —
  strukturell ähnelt es einem logistischen Attraktor-Modell (H nähert
  sich H_star mit effektiver Kapazität K_eff), was eher zu "Threshold
  Activation" als zu "Tipping Attractor Cascade" passt, aber das ist
  Interpretation, keine bestätigte Quelle.

**Noch nicht entschieden.** Braucht dieselbe Klärung wie CREP, bevor
ein kanonischer Eintrag hier stehen kann.

---

## AFET — Allgemeine Feld-Entropie-Theorie

**Status: bestätigt, 2026-08-05, direkter Code-/Doku-Fund.**

`afet_tensions`-README (P34): "Die AFET (Allgemeine Feld-Entropie-
Theorie) sagt voraus: Domänen-spezifische β-Werte erzeugen effektive
Gleichungszustand-Modifikationen, die die beobachteten kosmologischen
Spannungen auflösen." Zentrale Quelle laut `PACKAGE_REGISTRY.md`:
`Feldtheorie` (P70, capital/German), "the central AFET source, 78-system
validation cohort". Kein Konflikt mit einer anderen Bedeutung bisher
gefunden — als kanonisch übernommen, vorbehaltlich weiterer Prüfung
bei zukünftigen Paket-Audits.

---

## Migrations-Tracking (welche Pakete `bridge_adapted` tatsächlich nutzen)

**Prinzip (Johanns Entscheidung, 2026-08-05):** Kein präventiver
Rückbau aller CREP-nutzenden Pakete. Migration passiert opportunistisch
— wenn ein Paket aus irgendeinem Grund ohnehin angefasst wird, wird
`bridge_adapted` dabei gleich mitgelöst. Diese Tabelle verhindert, dass
das vergessen wird.

| Paket | P-Nr | `bridge_adapted` implementiert? | Datum | Notiz |
|---|---|---|---|---|
| afet-tensions | P34 | ⬜ Nein | — | `P=0.8` hartkodiert, bekannter Fall |
| resilience-core | P40 | ⬜ Nein | — | `P` = wiederverwendetes Bool-Flag |
| diamond-setup | P72 | ✅ Feld hinzugefügt | 2026-08-05 | PR #9, noch nicht gemerged/released |

*(Weitere Pakete werden ergänzt, sobald sie im laufenden Audit geprüft
oder aus anderem Anlass angefasst werden.)*

## Maintenance

Neue Metrik gefunden? Erst per echtem Code-Fund verifizieren (nicht aus
dem Namen raten), dann hier eintragen. Neues Paket berührt CREP/UTAC/
AFET? Migrations-Tabelle oben ergänzen — auch wenn `bridge_adapted`
(noch) nicht implementiert wurde, damit der Stand sichtbar bleibt.
