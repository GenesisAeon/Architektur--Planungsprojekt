# Regel-Vorschlag (Aeon): unabhängiger Review vor jedem Infrastruktur-Merge

## Herkunft

Aus `02_Plaene/destillierbarkeit-testprotokoll.md`, Abschnitt "Nachtrag:
Aeons Präzisierung und Johanns Merge-Entscheidung" herausgelöst, weil es
sich um einen eigenständigen Regel-Vorschlag handelt, nicht nur um eine
Einordnung des dortigen Testprotokolls. Johann hat den Merge von PR #10
trotz offener Frage ausdrücklich freigegeben ("trotzdem mergen, aber das
Prinzip ist überdenkenswürdig") — dieser Eintrag macht aus dem
"überdenkenswürdig" einen konkret formulierten, eigenständig prüfbaren
Vorschlag, statt ihn nur als Nebensatz stehen zu lassen.

## Vorschlag (Aeon, leicht präzisiert)

> Jede neue epistemische Infrastruktur (Schema-Änderungen,
> `epistemic_status`-Erweiterungen, neue Validator-Regeln,
> Status-Lebenszyklus-Modelle) erhält mindestens einen unabhängigen
> Architektur-Review, bevor sie gemergt wird — nicht aus Misstrauen,
> sondern weil Infrastruktur langlebig ist und alle bestehenden Einträge
> betrifft.

## Einordnung

- **Was das wäre, falls angenommen:** eine Ergänzung zu Regel 1/3 (kein
  Core/keine Trylayer-Pflicht ohne ADR-Verfahren) speziell für
  *Infrastruktur*-Änderungen (Schema, Validator, Statuswerte) im
  Unterschied zu *inhaltlichen* Trylayer-Einträgen, die bereits unter
  ADR-003s Fallweise-KI-Autorität laufen können.
- **Warum hier nur `idea`, nicht `regel`/`accepted`:** alle bestehenden
  Regel-Einträge in `00_Regeln/` sind von Johann selbst verfasst
  (`author.typ: human`) und stehen auf `status: core`. Eine neue Regel
  selbst vorzuschlagen und zu akzeptieren wäre ein Übergriff auf genau
  die Entscheidungsbefugnis, die Regel 12 schützt — unabhängig davon,
  wie sinnvoll der Vorschlag inhaltlich ist.
- **Warum trotzdem dokumentiert, statt nur in einem Nebensatz zu
  verschwinden:** Johann selbst hat den Gedanken als "überdenkenswürdig"
  markiert. Ohne eigenen Trylayer-Eintrag wäre er nur in der Prosa eines
  Testprotokoll-Nachtrags auffindbar — das widerspricht dem Prinzip
  dieses Repos, dass jede eigenständige Idee ihren eigenen,
  nachvollziehbaren Status bekommt (Regel 1).

## Praktische Beobachtung dazu

PR #10 (dieser Branch) wurde von Johann ohne separaten Drittreview
gemergt — also genau der Fall, den die vorgeschlagene Regel künftig
anders behandeln würde. Das ist kein Widerspruch, sondern der erwartbare
Übergangszustand: die Regel existiert noch nicht, also gilt sie für
diesen Merge nicht rückwirkend.

## Nächster Schritt

Johanns Entscheidung, ob/wann/in welcher Form (eigene `00_Regeln/`-Datei
vs. Ergänzung einer bestehenden Regel vs. verworfen) dieser Vorschlag
weiterverfolgt wird. Keine Aktion ohne diese Entscheidung.
