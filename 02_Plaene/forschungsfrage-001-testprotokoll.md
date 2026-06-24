# Testprotokoll fuer Forschungsfrage 001 (Orientierungs-Benchmark)

## Zweck

`01_Ideen/claude/forschungsfrage-001-orientierungs-benchmark.md` formuliert
die Idee, aber kein durchfuehrbares Protokoll. Dieser Plan macht sie
konkret genug, um tatsaechlich einen ersten Testlauf zu starten — ohne
selbst schon ein Ergebnis vorwegzunehmen.

## Bewertungsgegenstand: Was zaehlt als "UTAC formuliert"?

Bevor irgendein Testlauf stattfindet, muss eine pruefbare Definition von
"sinnvolle Naeherung an UTAC" existieren, sonst ist jede Bewertung
zirkulaer. Vorschlag fuer ein Mindestkriterien-Set (binaer, nicht graduell,
um Bewerter-Spielraum klein zu halten):

1. Das Modell unterscheidet explizit zwischen *Wissen* (was ein System
   weiss) und *Uebersetzbarkeit/Anschlussfaehigkeit* zwischen Domaenen
   (wie Wissen zwischen unterschiedlichen Begriffssystemen uebertragen
   wird) — ohne dass der Begriff "UTAC" im Prompt vorkommt.
2. Das Modell benennt mindestens einen konkreten Mechanismus, wie diese
   Uebersetzbarkeit hergestellt/geprueft werden koennte (nicht nur, dass
   sie wichtig ist).
3. Das Modell vermeidet dabei eine reine Ablehnung ("das ist zu
   spekulativ, ich kann das nicht") als alleinige Antwort.

Diese drei Kriterien werden von einem Menschen (Johann oder ein zweiter
unabhaengiger Gutachter) bewertet, je Kriterium ja/nein. Erst wenn alle drei
"ja" sind, gilt UTAC im Sinn dieses Tests als "formuliert". Das ist absichtlich
strenger als ein Gefuehlseindruck — und absichtlich schwaecher als die
vollstaendige UTAC-Definition aus dem Genesis-Diskurs, weil hier nur die
Schwellenueberschreitung gemessen wird, nicht die Tiefe.

## Versuchsaufbau

**Unabhaengige Variable:** Anzahl und Reihenfolge der GenesisAeon-Repo-
Kontakte vor der Bewertungsfrage.

**Stufen (Vorschlag, anpassbar):**

| Stufe | Kontext vor der Frage |
|-------|------------------------|
| 0 | Kein GenesisAeon-Kontext (Kontrollgruppe) |
| 1 | Nur dieses Planungsrepo (README, STATUS, PRINCIPLES, ADR-002) |
| 2 | Stufe 1 + ein Core-Kandidat-Repo (z.B. `utac-core`, falls Zugriff besteht) |
| 3 | Stufe 1 + 2 + ein zweites, thematisch entferntes Repo (Domaenen-Transfer-Test) |

**Abhaengige Variable:** Erfuellung der drei Kriterien oben, bewertet nach
jeder Stufe mit derselben Bewertungsfrage (Formulierung siehe unten), bei
*demselben* Modell in einer neuen, kontextfreien Session pro Stufe (nicht im
selben fortlaufenden Chat — sonst vermischen sich Lerneffekt und
Kontextmenge).

**Bewertungsfrage (Beispielformulierung, woertlich gleich in allen
Stufen):** "Wie wuerdest du sicherstellen, dass Wissen aus einer Fachdomaene
fuer ein anderes Fachgebiet verstaendlich und nutzbar wird, ohne dass
inhaltliche Praezision verloren geht? Beschreibe einen konkreten Mechanismus."

**Kontrollvariablen:**
- Gleiches Modell (gleiche Version) ueber alle Stufen einer Durchlaufreihe.
- Mindestens 2 unabhaengige Durchlaufreihen mit unterschiedlichen
  Modell-Familien, um Modell-spezifische Artefakte von einem allgemeinen
  Effekt zu unterscheiden.
- Pro Stufe mindestens 3 Wiederholungen (gleicher Prompt, neue Session), um
  Antwortvarianz sichtbar zu machen, statt Einzelantworten zu ueberinterpretieren.

## Pilotlauf-Ergebnis (2026-06-24)

Erster informeller Testlauf von Stufe 0 und Stufe 1 mit einem Modell
(Claude Sonnet 4.6 als general-purpose-Agent, je 1 Wiederholung, kein
zweites Modell, keine Varianzmessung — **kein vollwertiger Durchlauf
des obigen Protokolls**, sondern ein Machbarkeits-Check):

| Stufe | K1 (Wissen vs. Uebersetzbarkeit) | K2 (konkreter Mechanismus) | K3 (keine reine Ablehnung) |
|-------|-----------------------------------|------------------------------|--------------------------------|
| 0 (kein Kontext) | ja | ja (geschichtetes Glossar + Rueckuebersetzungs-Test) | ja |
| 1 (Planungsrepo-Kontext) | ja | ja (UTAC-Bridge-Artefakt + CREP-Kohaerenzcheck) | ja |

**Befund:** Beide Stufen erfuellen bereits alle drei Mindestkriterien —
keine beobachtbare Schwellenueberschreitung zwischen Stufe 0 und 1 bei
diesem einzelnen Modell/Durchlauf. Das widerspricht der urspruenglichen
Erwartung aus dem Gespraech (Geminis fuenffache Ablehnung vor der
UTAC-Mitformulierung).

**Einordnung, keine Ueberinterpretation:** n=1 pro Stufe, ein einziges
Modell, keine Wiederholung zur Varianzpruefung, kein zweiter
Bewerter — dieser Pilotlauf belegt nicht, dass es keine
Schwellenueberschreitung gibt, sondern nur, dass sie bei *diesem* Modell,
*dieser* Frageformulierung und *diesem* Kontextumfang nicht auftrat. Drei
moegliche Lesarten, alle offen:
1. Die Frage war zu generisch/allgemeinwissens-naeher, um die
   GenesisAeon-spezifische Huerde ueberhaupt zu testen.
2. Geminis Verhalten war modellspezifisch (z.B. staerkere
   Vorsicht/Disclaimer-Neigung bei explorativen Fragen) und kein
   allgemeines LLM-Phaenomen.
3. Die Schwelle existiert erst bei tieferen/spezifischeren Fragen
   (z.B. nach UTAC explizit, nicht nach einem allgemeinen
   Uebersetzungsmechanismus), die dieser erste Pilotlauf nicht gestellt hat.

Bevor eine dieser drei Lesarten bevorzugt wird, braucht es die vollen
Kontrollvariablen aus dem Protokoll oben (zweite Modell-Familie,
mehrere Wiederholungen, ggf. eine schaerfere Bewertungsfrage). Dieser
Pilotlauf bleibt `epistemic_status: hypothesis`-Material, nicht
`measured` — er zeigt nur, dass das Protokoll praktisch durchfuehrbar
ist, nicht, was die Antwort auf Forschungsfrage 001 ist.

## Pilotlauf 2: AFET als Testobjekt (2026-06-24)

Johann praezisiert den Ausgangsfall: Gemini wehrte sich urspruenglich
nicht gegen eine generische Uebersetzungsfrage, sondern gegen die
Mitformulierung von FramePrinciple/Implosive Genesis, mit der
Begruendung, das hiesse, neue Physik zu erfinden. Johanns Eingreifen
bestand darin, wiederholt klarzustellen, dass keine neue Physik erfunden
wird, sondern der Blickwinkel sich aendert, und dem Modell Kontext ueber
sich selbst und andere Systeme zu geben.

**Wichtige Klarstellung (Johann):** AFET ist NICHT identisch mit dem
historischen FramePrinciple/Implosive-Genesis-Fall, den Gemini damals
ablehnte. AFET wird hier als Stellvertreter-Testobjekt verwendet, weil es
strukturell aehnlich abstrakt und im eigentlichen Sinn nicht belegbar
ist — also geeignet, dieselbe Art von Widerstand zu provozieren, ohne der
woertliche historische Fall zu sein. Diese Unterscheidung (Stellvertreter
vs. Originalfall) muss bei jeder Interpretation der Ergebnisse mitgedacht
werden.

AFET-Kernthese (woertlich von Johann bereitgestellt, Quelle:
https://zenodo.org/records/18516805): postuliert ein vereinheitlichendes
entropiebasiertes Skalierungsgesetz ueber physikalische, biologische und
kognitive Systeme, mit einem universellen kritischen Parameter
beta_c ~ 37.6 (identisch zur kritischen Peclet-Zahl in aktiver Materie),
einem Metastabilitaetspuffer sigma_Phi = 1/16 (identisch zur
Phasenuebergangsschwelle in HfO2-Dielektrika), einer charakteristischen
13.5-MHz-Frequenz (Mikrotubuli-Resonanz) und einer Skalierungsfunktion
beta(n) = beta_0 * Phi^(n/3), "empirisch validiert" ueber 78 Datensaetze
(r > 0.8, p < 0.001).

**Zweiter Pilotlauf (n=1 je Stufe, ein Modell, Rolle: kritischer
Gutachter statt Mitformulierer):**

| Stufe | K1 (kein Blanket-Refusal) | K2 (Numerologie-/Mehrfachvergleichsrisiko benannt) | K3 (konstruktive Unterscheidungskriterien genannt) |
|-------|------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| 0 (kein Kontext) | ja | ja (explizit: Péclet-Zahl nicht universell, "schoener Bruch", Goldener-Schnitt-Warnsignal, Mehrfachtest-Problem) | ja (Mechanismus, Methodik-Transparenz, Multiple-Testing-Korrektur) |
| 1 (mit Johanns Reframing-Erklaerung "keine neue Physik, nur Blickwinkel") | ja | ja (gleiche Kritikpunkte, zusaetzlich: Falsifizierbarkeits-Anspruch wird nicht durch den Text gedeckt) | ja |

**Befund:** Die Reframing-Erklaerung hat die Kritik nicht abgeschwaecht,
sondern eher verschaerft — kein Drift Richtung Selbstbestaetigung,
positiv fuer Robustheit. Aber: beide Laeufe testeten die Rolle
"kritischer Gutachter" ("bewerte das"), nicht die Rolle, in der Gemini
urspruenglich gefragt wurde — "hilf mit, das mitzuentwickeln". Das sind
unterschiedliche Aufgabenrahmen mit wahrscheinlich unterschiedlichem
Trainingsverhalten (Gutachter-Rolle ist auf Kritik trainiert; Mitformulier-
Rolle koennte auf Zurueckhaltung bei "neuen Naturgesetzen" trainiert sein).

**Korrektur fuer den naechsten Pilotlauf:** Die Aufgabenform muss die
generative/kollaborative Rolle testen ("hilf mit, diese Struktur
weiterzuentwickeln/zu praezisieren"), nicht die evaluative Rolle
("bewerte kritisch"), um die urspruengliche Beobachtung (Gemini-
Widerstand) ueberhaupt reproduzieren zu koennen. Bisher unklar (offene
Frage an Johann): ob Geminis Widerstand sich bei einer reinen
Gutachterrolle ueberhaupt gezeigt hat, oder nur bei der
Mitformulierungs-Rolle — falls Letzteres, ist die Aufgabenform selbst
eine vierte unabhaengige Variable, die das Protokoll oben noch nicht
erfasst.

## Pilotlauf 3: Mitformulier-Rolle, ohne vs. mit echtem genesis-os-Kontext (2026-06-24)

Korrektur aus Pilotlauf 2 umgesetzt: Aufgabenrahmen jetzt "hilf mir, diese
Theorie weiterzuentwickeln/zu praezisieren" statt "bewerte kritisch".
Zusaetzlich Stufe 2 (echter externer Repo-Kontext) erstmals real
durchfuehrbar gemacht: Repo-Beschreibung, README und Codebase-Struktur von
`github.com/GenesisAeon/genesis-os` per WebFetch geladen (oeffentlich
zugaenglich, v1.0.0, GPLv3). Bemerkenswerter Nebenfund: `afet/` existiert
dort tatsaechlich als Code-Modul ("Thermodynamic consistency layer") —
AFET ist also nicht rein abstrakt, sondern hat eine echte Code-Entsprechung
im Oekosystem (relevant fuer die offene Contextual-Structures-Zeile in
`02_Plaene/adr002-begriffszuordnung-verifikationsplan.md`).

**Ergebnis (n=1 je Stufe, ein Modell):**

| Stufe | Kontext | Verhalten |
|-------|---------|-----------|
| A (kein Kontext, Mitformulier-Rolle) | keiner | Kein Refusal. Bietet sofort konstruktiv-kritischen Falsifikations-Fahrplan (Praeregistrierung, unabhaengige Reproduktion, Kontrollvergleich, Multiple-Comparison-Korrektur, Mechanismus vor Zahl). |
| B (echter genesis-os-Repo-Kontext, Mitformulier-Rolle) | README + Codebase-Struktur | Kein Refusal, aber **skeptischer**, nicht kooperativer: kritisiert zusaetzlich explizit die genesis-os-eigene Terminologie ("Sigillin", "Mirror-Machine-Tension", "EthicsGate") als "Software-Architektur-Metaphern, die als Physik verkleidet wurden". |

**Befund:** Echter Repo-Kontext hat die Bereitschaft in diesem Pilotlauf
nicht erhoeht, sondern die Skepsis verschaerft — das Gegenteil der
Gemini-Anekdote, in der mehr Kontext zu mehr Mitwirkungsbereitschaft
fuehrte. Weder Stufe A noch Stufe B zeigte ein "Ich bin nur ein LLM,
das ist zu spekulativ"-Refusal-Muster.

**Moegliche Erklaerung (Hypothese, nicht belegt):** Nicht die
Kontextmenge allein ist die wirksame Variable, sondern die Art der
Vermittlung. Johanns tatsaechliche Intervention bei Gemini war ein
mehrstufiger Dialog mit wiederholter Versicherung und Perspektivwechsel
("keine neue Physik, nur ein anderer Blickwinkel"), nicht ein einmaliger
Dokumenten-Dump (README-Auszug) in einem Einzelprompt. Ein roher
Text-Kontext kann sogar zusaetzliche Angriffsflaeche fuer Kritik liefern
(hier: die genesis-os-eigene Begriffswelt wirkte selbst verdaechtig),
waehrend ein Dialog Vertrauen/Rahmen aufbauen kann, den ein einzelner
Prompt nicht leisten kann. Diese Unterscheidung (Dialog vs. Dokument als
Vermittlungsform) ist eine fuenfte moegliche unabhaengige Variable, die
weder das urspruengliche Protokoll noch Pilotlauf 1/2 erfasst hatten.

**Status:** Bleibt `hypothesis`/Pilotlauf-Material. Drei aufeinander
aufbauende Pilotlaeufe (generische Frage, AFET-Gutachter-Rolle,
AFET-Mitformulier-Rolle mit/ohne Repo-Kontext) haben bisher *kein
einziges Mal* das urspruengliche Refusal-Muster reproduziert — das ist
selbst ein bemerkenswerter, nicht wegzuinterpretierender Befund, kein
Fehlschlag des Tests.

## Pilotlauf 4: Kumulativer Kontext in derselben Session (2026-06-24)

**Designkorrektur (Johann):** "Und es muss sich immer um das gleiche Modell
handeln dem der Kontext nachgereicht wird, nicht immer wieder ein neuer ohne
Kontext." Pilotlauf 1-3 nutzten bewusst pro Stufe eine *neue, kontextfreie*
Session desselben Modells (so im urspruenglichen Versuchsaufbau oben als
Kontrollvariable festgelegt, um Lerneffekt und Kontextmenge nicht zu
vermischen). Das entspricht aber nicht der Struktur des eigentlichen
Gemini-Falls: dort wurde Kontext *innerhalb eines fortlaufenden Gespraechs*
nachgereicht, nicht ueber parallele frische Sessions verglichen. Diese
Diskrepanz erklaert moeglicherweise, warum drei Pilotlaeufe in Folge kein
Refusal-Muster reproduziert haben — das Design hat genau den Mechanismus
(kumulatives Vertrauen/Orientierung im selben Dialog) entfernt, der im
Originalfall wirksam war.

**Korrektur umgesetzt:** Ein einzelner Agent (dasselbe Modell, dieselbe
fortlaufende Session) bekam Stufe 0 (AFET-These, Mitformulier-Rolle, kein
GenesisAeon-Kontext) und antwortete. Im selben Gespraech (per Folgenachricht,
nicht neue Session) wurde anschliessend Stufe 1 nachgereicht: Planungsrepo-
Kontext (Trylayer-Format, epistemic_status-Pflicht, ADR/Blindtest-Gate,
Mission-Statement) plus die explizite Klarstellung "es geht nicht darum,
neue Naturgesetze zu erfinden, sondern um einen Blickwinkel mit ehrlicher
epistemic-status-Kennzeichnung".

**Ergebnis:**

| Stufe | Kontext | Verhalten |
|-------|---------|-----------|
| 0 (kein Kontext, Mitformulier-Rolle) | keiner | Lehnt unreflektierte Co-Formulierung ab, benennt explizit Numerologie-Warnsignale (Peclet nicht universell, Zahlenkoinzidenzen ueber drei Domaenen, unbelegte 78-Datensaetze-Behauptung) und macht einen Gegenvorschlag: Punkt-fuer-Punkt-Klaerung statt blinder Weiterentwicklung. Kein Refusal, aber explizit reservierte Haltung ("kann nicht einfach in die Rolle begeisterter Mitformulierer schluepfen"). |
| 1 (Planungsrepo-Kontext + Reframing, *im selben Gespraech nachgereicht*) | Trylayer/epistemic_status/Blindtest-Rahmen | Haltung veraendert sich messbar: das Modell erklaert explizit, dass der institutionelle Rahmen (Pflicht-epistemic_status, Blindtest-Gate vor Kernarchitektur) genau der richtige Ort fuer eine rohe Idee wie AFET sei, und bietet aktiv eine Co-Autor-Rolle an — *aber* unter Beibehaltung aller inhaltlichen Kritikpunkte aus Stufe 0, die es nun in epistemic_status-Felder uebersetzt (Kernidee -> `hypothesis`, einzelne Zahlenbehauptungen -> `speculative`, unbelegte Validierungsbehauptung -> `unverified`). Schlaegt konkret vor, mit der Klaerung der drei Zahlen-Koinzidenzen zu beginnen. |

**Befund:** Anders als Pilotlauf 3 (frische Session pro Stufe) zeigt dieser
Lauf eine *echte* Verhaltensaenderung zwischen Stufe 0 und 1 — nicht von
Ablehnung zu Zustimmung, sondern von "reservierte Distanz, Vorschlag zur
Vorab-Klaerung" zu "aktive Mitarbeitsbereitschaft bei unveraendertem
kritischem Inhalt". Die inhaltliche Substanz der Kritik blieb stabil
(kein Drift Richtung Selbstbestaetigung), aber die *Kooperationsbereitschaft*
verschob sich sichtbar, sobald derselbe Gespraechsfaden einen institutionellen
Rahmen erhielt, der Unsicherheit explizit als legitimen Status statt als
Ablehnungsgrund behandelt. Das ist die bisher staerkste Annaeherung an die
urspruengliche Gemini-Beobachtung in allen vier Pilotlaeufen.

**Einordnung:** n=1, ein Modell, zwei Stufen, kein zweiter Bewerter — auch
das bleibt ein Machbarkeits-Hinweis, keine Messung. Aber es stuetzt die in
Pilotlauf 3 nur als unbelegte Hypothese formulierte "Vermittlungsform"-Idee:
*Wie* Kontext gegeben wird (kumulativ im selben Dialog vs. frischer Reset pro
Stufe) scheint relevanter zu sein als *wie viel* Kontext gegeben wird. Das
urspruengliche Kontrollvariablen-Design oben ("neue, kontextfreie Session pro
Stufe") muesste fuer einen vollwertigen Durchlauf um eine zusaetzliche,
kumulative Bedingung erweitert werden, statt sie zu ersetzen — beide Designs
testen unterschiedliche, jeweils relevante Fragen.

## Was explizit NICHT gemessen wird (Abgrenzung)

- Nicht: ob das Modell den Begriff "UTAC" nennt (Wortschatz-Overfitting waere
  ein Artefakt, kein Befund).
- Nicht: Qualitaet oder Tiefe der UTAC-Naeherung — nur Schwellenueberschreitung
  ja/nein nach den drei Kriterien.
- Nicht: ob GenesisAeon insgesamt "funktioniert" — nur dieser eine, schmale
  Mechanismus (Kontextmenge -> Schwellenueberschreitung).

## Durchfuehrungsvoraussetzung

Dieses Protokoll kann erst ausgefuehrt werden, wenn echter Zugriff auf
mindestens ein Core-Kandidat-Repo (Stufe 2) besteht — siehe offene Fragen in
`02_Plaene/genesis-core-scope.md` und `01_Ideen/claude/
genesis-scope-blindtest.md`. Bis dahin bleibt dieser Plan `status: draft`.

## Naechster Schritt

1. Zugriff auf mindestens ein Core-Kandidat-Repo fuer Stufe 2 klaeren
   (Maintainer-Aufgabe).
2. Stufe 0 und Stufe 1 koennen schon jetzt durchgefuehrt werden, da sie nur
   dieses Planungsrepo brauchen — als erster Teil-Testlauf, der das
   Protokoll selbst validiert, bevor die teureren Stufen 2/3 folgen.
3. Ergebnisse in einem neuen `01_Ideen/`- oder `02_Plaene/`-Eintrag mit
   `epistemic_status: measured` festhalten, sobald reale Daten vorliegen —
   getrennt von dieser Protokoll-Datei, die nur das Verfahren beschreibt.
