# fieldtheory (EN, T4) und Feldtheorie (DE, T0) sind keine Duplikate

## Problem

`02_Plaene/genesis-core-scope.md`, Schritt 2, flaggt eine offene Frage:
sind `fieldtheory` (T4, EN) und `Feldtheorie` (T0, DE) tatsächlich
Duplikate? Falls ja, würde die vorgeschlagene Core-Kette kürzer.
Namensähnlichkeit (dieselbe deutsche/englische Übersetzung) allein ist
aber keine Verifikation — das braucht echten Code-/Struktur-Vergleich.

## Vorgehen und Durchführung

Beide Repos liegen lokal vor (`D:\mandala\fieldtheory` und
`D:\mandala\Feldtheorie`) und wurden direkt verglichen: Top-Level-
Struktur, `pyproject.toml` (Name, Version, Beschreibung), README/Scope,
Quellcode-Umfang.

## Ergebnis

**Strukturell und inhaltlich eindeutig keine Duplikate** — zwei
komplett unterschiedliche Artefakte, die nur zufällig denselben
übersetzten Namen tragen:

| | `fieldtheory` (EN) | `Feldtheorie` (DE) |
|---|---|---|
| PyPI-Name | `fieldtheory` | `feldtheorie` |
| Version | 1.0.1 | 6.0.0 (GitHub-Tag: 13.0.0) |
| Umfang | 3 Quelldateien (`core.py`, `cli.py`, `entropy_table_bridge.py`) | Hunderte Analyse-Skripte, riesiger Datenkorpus, `CURRENT_MAP.md` allein >3200 Zeilen |
| Selbstbeschreibung | "The unifying field theory of the GenesisAeon stack" — ein Lagrangian (`L = S_A·S_V/(S_A+S_V) - (1+δ)/t²`) samt Euler-Lagrange-Ableitung | "Reproducibility harness for the Universal Threshold Field programme" |
| Abhängigkeiten | Bridges explizit zu `entropy-table`, `medium-modulation`, `cosmic-moment`, `entropy-governance` (optional via `fieldtheory[stack]`, Fallback auf interne Implementierung sonst) | Eigenständiges, riesiges Forschungslabor mit eigenem `analysis/`/`data/`/`models/`-Baum (138 echte Fit-Ergebnisse, siehe `ecosystem-verifizierbare-daten-audit`) |
| Rolle | Schmales, deterministisches Core-Kandidat-Modul (T4 in der Abhängigkeitskette) | Das ursprüngliche, explorative Forschungslabor selbst (Quelle, nicht Ziel — Regel 9) |

`fieldtheory` (EN) liest sich wie genau das, was dieses Repo mit
Regel 7/9 anstrebt: eine schmale, minimale, deterministische
Destillation EINER spezifischen mathematischen Formulierung (die
S∝A/S∝V-Dualitäts-Lagrangian) aus dem riesigen `Feldtheorie`-Korpus —
nicht eine Kopie davon. Die Namensgleichheit (identisches Wort in zwei
Sprachen) ist die einzige Gemeinsamkeit; sie hat die
Duplikat-Vermutung ausgelöst, ist aber kein inhaltlicher Beleg.

## Erwartetes Ergebnis

Die Core-Kette (`entropy-table` → `implosive-genesis` →
`entropy-governance` → `medium-modulation` → `cosmic-moment` →
`fieldtheory` → `sigillin` → `utac-core`) bleibt in voller Länge
bestehen — `fieldtheory` (EN) ist ein eigenständiges, zu testendes
Kettenglied, keine Dublette von `Feldtheorie` (DE), die man
herausstreichen könnte.

## Nächster Schritt

`fieldtheory` (EN) selbst braucht noch seinen eigenen
Genesis-Blindtest, sobald die Kette bei T4 ankommt (aktuell wird
`entropy-governance`, T1, getestet). `Feldtheorie` (DE) selbst ist
kein Core-Kandidat in dieser Kette (T0, kein Eintrag in
`depends_on`-Ketten der T1-T16-Pakete) — bleibt Quelle/Labor gemäß
Regel 9, nicht Ziel einer eigenen Blindtest-Bewertung im Rahmen dieser
Core-Kette.

## Alternativen betrachtet

**Nur die PyPI-Namen vergleichen (`fieldtheory` vs. `feldtheorie`)
und daraus schließen, es handle sich nicht um Duplikate.** Für sich
genommen zu schwach — zwei unterschiedlich benannte Pakete könnten
trotzdem denselben Code kopiert haben. Deshalb zusätzlich Umfang,
Selbstbeschreibung und Abhängigkeitsstruktur geprüft, nicht nur den
Namen.
