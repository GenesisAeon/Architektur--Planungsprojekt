# ADR-003 — KI als Maintainer fuer Status-Entscheidungen (fallweise, begruendungspflichtig)

## Kontext

`AGENTS.md` (Abschnitt "Was dieses Repo NICHT ist") und `PRINCIPLES.md`
legten bisher fest, dass ausschliesslich der menschliche Maintainer
(Johann) `status: accepted/core/archived/deprecated` vergibt; KI-Systeme
reichen nur Vorschlaege mit `status: idea/draft` ein.

Anlass fuer die Revision: bei der Bearbeitung des
ADR-002-Verifikationsplans (siehe
`01_Ideen/claude/cartography-pheromones-drift-ecosystem-map-befund`)
stellte sich heraus, dass genau diese Trennung den naechsten Schritt
blockiert — die KI durfte den eigenen, recherchierten Befund (Begriff
nicht auffindbar) nicht selbst zu einer `archive/`-Entscheidung
weiterfuehren, sondern musste auf eine separate Maintainer-Pruefung
warten, obwohl die Pruefung bereits im Befund enthalten war. Johann
(2026-06-24, im Chat) entscheidet, diese Rolle gezielt zu erweitern, mit
Sicherheitsventil per Begruendungspflicht statt vollstaendiger Aufhebung
der Trennung.

## Entscheidung

Eine KI darf ab sofort fallweise auch `status: accepted`, `core`,
`deprecated` oder `archived` selbst vergeben (nicht nur
`idea`/`draft`/`review` vorschlagen) — vorausgesetzt, jede solche
Entscheidung wird im selben Commit explizit begruendet (im
Trylayer-Eintrag selbst, z.B. `content.begruendung`, UND in der
Commit-Message), so dass Johann sie jederzeit per Diff nachvollziehen
und per Revert zuruecknehmen kann.

Es gibt **keine pauschale Vorab-Freigabe** fuer ganze Kategorien — die KI
bewertet pro Einzelfall, ob sie selbst entscheidet oder eine Frage an
Johann stellt, wenn die Faktenlage mehrdeutig oder die Tragweite gross
ist.

## Scope-Praezisierung

- Betrifft alle Trylayer-Kategorien, nicht nur `archive/`-Verschiebungen.
- Regel 3 (ADR-Pflicht vor Core), Regel 5 (epistemic_status ehrlich),
  Regel 6 (Genesis-Blindtest vor `accepted`) und Regel 9/11
  (Unified-Mandala ist Quelle, Verwerfen ist kein Loeschen) bleiben
  unveraendert in Kraft — die KI vergibt Status nach denselben
  inhaltlichen Kriterien wie bisher der Mensch, nicht nach laxeren.
- Die Begruendungspflicht ist keine Formalitaet: ein Trylayer-Eintrag,
  dessen Statuswechsel nicht im `content`-Feld begruendet ist, gilt als
  unvollstaendig im Sinne dieses ADR (auch wenn
  `scripts/validate_trylayer.py` das technisch nicht prueft).
- **ADR-Eintraege selbst (`kategorie: adr`) bleiben ausschliesslich von
  Johann verfasst/verantwortet**, da sie Aenderungen der Verfassung
  dokumentieren (Regel 12) — eine KI kann ein ADR vorschlagen/entwerfen,
  aber nicht selbst mit `author.typ: ai` und `status: accepted`
  versehen.

## Begruendung

- Die bisherige strikte Trennung erzeugte unnoetigen Leerlauf genau dort,
  wo die KI die fuer eine Entscheidung notwendige Recherche bereits
  selbst durchgefuehrt hatte — das widerspricht dem Mission-Statement
  (ADR-002), das Menschen als Curators/Researchers/Architects vorsieht,
  aber nicht als alleinige Ausfuehrende jeder einzelnen Statuspruefung.
- Eine Begruendungspflicht statt Vorab-Freigabe erhaelt die
  Nachvollziehbarkeit (Regel 11 bleibt strikt), verschiebt aber die
  Kontrolle von "vorher fragen" zu "jederzeit nachpruefbar und
  revertierbar" — passend zu einem Git-Repo, in dem jede Aenderung
  ohnehin als Diff sichtbar ist.
- Fallweise statt pauschal vermeidet, dass die KI sich selbst eine
  Blanko-Vollmacht fuer `kategorie: adr` oder fuer folgenreiche
  Core-Entscheidungen gibt; bei echter Unsicherheit bleibt die
  Eskalation an Johann der Normalfall, nicht die Ausnahme.

## Alternativen betrachtet

- **Volle Gleichstellung** (KI vergibt auch `status: accepted` fuer
  `kategorie: adr` selbst) — verworfen (Johann, explizit): ADRs aendern
  die Verfassung selbst (Regel 12), das bleibt zu folgenreich fuer eine
  fallweise Delegation.
- **Nur `archive/`-Entscheidungen delegieren**, alles andere bei Johann
  lassen — verworfen: das haette das urspruengliche Problem (Leerlauf
  bei bereits recherchierten Befunden) nur fuer einen Teilbereich
  geloest.
- **Direkte Anpassung von `PRINCIPLES.md`/`AGENTS.md` ohne eigenes ADR**
  — verworfen (Johann, explizit): Regel 12 verlangt ein ADR vor jeder
  Verfassungsaenderung; ein Praezedenzfall ohne ADR haette die eigene
  Kernregel sofort unterlaufen, die dieses ADR gerade staerken soll.

## Konsequenzen

- `AGENTS.md`, Abschnitt "Was dieses Repo NICHT ist", wird praezisiert
  (nicht ersatzlos gestrichen): fallweise erlaubt, mit
  Begruendungspflicht, ADRs ausgenommen.
- `PRINCIPLES.md` braucht keine neue Regel-Nummer, aber einen Verweis auf
  ADR-003 dort, wo bisher implizit "nur der Mensch" stand.
- Der konkrete Anlassfall
  (`cartography-pheromones-drift-ecosystem-map-befund`) wird im selben
  Arbeitsschritt wie dieses ADR nach diesem neuen Verfahren
  weiterbearbeitet — das ist der erste Anwendungsfall, nicht nur die
  Begruendung.
- Jede kuenftige Statusentscheidung durch eine KI sollte auf dieses ADR
  verweisen, solange keine weitere Praezisierung erfolgt ist.
