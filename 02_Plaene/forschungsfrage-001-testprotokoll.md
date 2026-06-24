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
