# Braucht Regel 6 eine eigene Form für KI-native Pakete, die erst durch Nutzung befüllt werden?

**Status:** idea · **Epistemic Status:** hypothesis · **Autor:** Claude

## Problem

Der `genesis-scope`-Blindtest (siehe
`01_Ideen/claude/genesis-scope-blindtest`) ist FALSE ausgefallen — und
zwar nicht primär wegen schlechter Dokumentation, sondern weil das
Paket noch nie tatsächlich benutzt wurde: ihm fehlen die Referenzdaten
(reale Sessions, Sigillin-Anker, Concept-Map-Inhalte), die per Design
erst durch spätere KI-Agenten eingespeist werden sollen.

Regel 6 fragt: "Kann eine Person ohne jeden GenesisAeon-Kontext den
Quickstart der README folgen und innerhalb von 5 Minuten ein
sinnvolles, korrektes Ergebnis sehen?" Diese Frage setzt implizit
voraus, dass ein "sinnvolles Ergebnis" durch bessere Doku oder bessere
Quickstart-Gestaltung erreichbar ist. Bei einem Paket, dessen
Sinnhaftigkeit von vorheriger Befüllung abhängt (ein Skelett ohne
Inhalte kann nicht sinnvoll sein, egal wie gut die README ist), kann
der klassische Blindtest strukturell nie TRUE liefern — er misst dann
nicht Doku-Qualität, sondern testet immer wieder denselben Leerzustand.

## Vorschlag

Zwei mögliche Wege, keiner davon bereits entschieden:

- **(a) Vorbedingung**: ein KI-natives, erst durch Nutzung befülltes
  Paket muss vor dem Blindtest mit repräsentativen Beispieldaten/
  Referenzen ausgestattet werden (z.B. eine mitgelieferte
  Demo-Session, ein Beispiel-Sigillin-Anker, eine Beispiel-Concept-Map),
  damit der Quickstart überhaupt etwas zeigen kann, das nicht der
  Default-Leerzustand ist.
- **(b) Eigene Blindtest-Variante**: statt "Verstehst du das Ergebnis
  sofort?" eher "Verstehst du nach dem Quickstart, WAS dieses Paket
  von dir/einer KI noch braucht, um sinnvoll zu werden, und WARUM die
  aktuelle Ausgabe ein Leerzustand ist?" — das wäre ein ehrlicherer,
  erreichbarer Maßstab für Skelett-Pakete, ohne Regel 6 für alle
  anderen Pakete abzuschwächen.

## Warum relevant für dieses Repo

Dieses Repo ist explizit für Mensch-KI-Semantiknavigation gebaut
(ADR-002-Mission-Statement) — es ist plausibel, dass nicht nur
`genesis-scope`, sondern weitere der 48 Ökosystem-Pakete denselben
Charakter haben: erst durch KI-Interaktion über die Zeit sinnvoll.
Wenn Regel 6 das nicht abbildet, droht ein systematisches FALSE für
eine ganze Klasse von Paketen, unabhängig von ihrer tatsächlichen
Architekturqualität.

## Erwartetes Ergebnis

- Eine explizite Entscheidung (Maintainer und/oder neues ADR, da es
  Regel 6 selbst betrifft — Regel 12), ob Regel 6 für KI-native
  Leerpakete eine Variante oder Vorbedingung bekommt.
- Falls ja: nachträgliche Neubewertung von `genesis-scope-blindtest`
  unter der neuen Variante, sobald sie definiert ist — der jetzige
  FALSE-Befund bleibt als historischer Messwert unter der alten
  Definition stehen (Regel 11, kein Löschen).

## Nächster Schritt

Diese Idee dem Maintainer zur Entscheidung vorlegen: Vorbedingung (a),
eigene Blindtest-Variante (b), oder explizit ablehnen mit Begründung
(z.B. "jedes Paket muss auch im Leerzustand minimal verstehbar sein,
sonst ist es kein gutes Paket"). Bei Annahme von (a) oder (b): als
eigenes ADR formulieren, da es Regel 6 selbst ändert (Regel 12).

## Betrachtete Alternativen

- Sofort eine neue Blindtest-Variante als gültig einführen, ohne
  Maintainer-Entscheidung — verworfen: Regel 6 selbst zu ändern ist
  eine Verfassungsänderung (Regel 12), die nicht fallweise per
  ADR-003-Autorität erfolgen darf.
- Den FALSE-Befund von `genesis-scope-blindtest` einfach löschen oder
  überschreiben, statt eine neue, separate Idee zu eröffnen —
  verworfen: widerspricht Regel 11 (Verwerfen ist kein Löschen) und
  würde den ursprünglichen Messwert verdecken.
