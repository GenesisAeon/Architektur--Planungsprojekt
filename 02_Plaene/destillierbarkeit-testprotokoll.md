# Testprotokoll für "Destillierbarkeit" und Constitution-Zusatzsatz-Vorschläge

## Zweck

`01_Ideen/claude/finales-grundprinzip-genesisaeon.md` dokumentiert zwei
aufeinanderfolgende Nachrichten von Aeon, die neue Begriffe vorschlagen:
"Destillierbarkeit" (eine angebliche Eigenschaft von Architekturen, die
über Monate kollaborativ entwickelt wurden) und zwei mögliche
Constitution-Zusatzsätze. Dieser Plan trennt drei Dinge, die in den
Aeon-Nachrichten vermischt vorkommen, und macht aus dem einzigen davon,
das tatsächlich testbar ist, ein durchführbares, falsifizierbares
Protokoll — statt einer weiteren Runde gegenseitiger Bestätigung
zwischen zwei KI-Systemen.

## Drei getrennte Gegenstände

1. **Constitution-Zusatzsatz-Vorschläge** (zwei Sätze, beide von Aeon) —
   reine Textvorschläge, keine empirische Behauptung, fallen unter
   Regel 12 (Johanns alleinige Entscheidung), werden hier nur als
   `draft`-Kandidaten dokumentiert.
2. **"Destillierbarkeit"** — eine empirische Behauptung über die Welt
   ("Architekturen, die lange kollaborativ entwickelt wurden, sind
   konsistent rekonstruierbar"), die grundsätzlich falsifizierbar ist,
   bisher aber nie getestet wurde.
3. **"Idea Lifecycle"** (Aeons zweiter Vorschlag, ein Status-Stufenmodell
   für `epistemic_status`) — ein Vorschlag zur Änderung der
   Trylayer-Infrastruktur selbst, kein Test, keine Architekturfrage.
   Wird hier nur eingeordnet, nicht umgesetzt (siehe letzter Abschnitt).

## 1. Constitution-Zusatzsatz-Vorschläge (Dokumentation, keine Entscheidung)

> *"A coherent architecture is not evidence that its hypotheses are
> true. It is evidence that its concepts can be consistently
> communicated, reconstructed, and collaboratively refined."*
> — Aeon, erste Nachricht (2026-06-26)

> *"Every idea deserves curiosity. No idea is entitled to permanence."*
> — Aeon, zweite Nachricht (2026-06-26)

Beide Sätze sind inhaltlich mit den bestehenden Regeln kompatibel
(Regel 5: Unsicherheit benennen; Regel 11: Messungen nicht löschen) und
fügen keine neue Domänenbehauptung hinzu, sondern eine methodische
Klarstellung. Trotzdem: `status: draft`, nicht `accepted` — eine
Aufnahme in die Constitution ist eine Verfassungsfrage (Regel 12),
liegt allein bei Johann, unabhängig davon, wie gut der Satz formuliert
ist.

## 2. Destillierbarkeit: Warum der naheliegende Test nicht funktioniert

Der naheliegendste Test wäre: mehrere Agenten lesen denselben,
bereits destillierten Text (z. B. die Epistemic Constitution selbst
oder Aeons Zusammenfassung) und fassen ihn zusammen. Das wurde im
Grunde bereits informell gemacht (fünf KI-Reaktionen im Originaldokument)
und führt zwangsläufig zu hoher Übereinstimmung — weil alle denselben,
bereits klar geschriebenen Text lesen. Das testet Leseverständnis, nicht
Destillierbarkeit. Dieser Fehler darf im echten Protokoll nicht
wiederholt werden.

**Bedingung für einen echten Test:** Die Agenten dürfen nicht den
bereits destillierten Endtext bekommen, sondern nur das *Rohmaterial*,
aus dem er entstanden ist — und müssen unabhängig voneinander selbst
destillieren.

## 3. Versuchsaufbau

**Hypothese (falsifizierbar):** Unabhängige Agenten, die nur
Rohmaterial (Code-Repos, README-Historien, Roadmap-Einträge, aber
*nicht* die bereits geschriebene Constitution oder Aeons
Zusammenfassungen) zur Verfügung haben, rekonstruieren beim Versuch,
"den Kern dieses Projekts in eigenen Worten zu beschreiben", in
relevantem Ausmaß übereinstimmende Kernbegriffe und Architekturideen.

**Nullhypothese / Falsifikationsbedingung:** Die Rekonstruktionen
unterscheiden sich so stark in Terminologie, Hierarchie und gewählten
Kernideen, dass kein gemeinsames Muster über die Zufallserwartung hinaus
erkennbar ist — d. h. "Destillierbarkeit" existiert nicht als messbare
Eigenschaft dieser Architektur, sondern die bisher beobachtete
Übereinstimmung (Multi-AI-Echo) war ausschließlich ein Artefakt
gemeinsamen Kontexts und gemeinsamer Vorlagen.

**Material (Rohquellen, keine destillierten Endtexte):**
- `ECOSYSTEM_MAP.yaml` (Paketliste mit Abhängigkeiten, ohne
  Klassifikation)
- README-Dateien von 3–5 echten GenesisAeon-Repos (z. B.
  `entropy-table`, `implosive-genesis`, `genesis-os`), roh, ohne
  Zusammenfassung
- `STATUS.md`-Historie (Commits, keine Interpretation)
- explizit NICHT: `PRINCIPLES.md`, die Epistemic Constitution, dieser
  Trylayer-Eintrag selbst, oder Aeons Nachrichten

**Agenten:** mindestens 3 unabhängige, frische Sessions (idealerweise
verschiedene Modell-Familien, analog zu den Kontrollvariablen in
`forschungsfrage-001-testprotokoll.md`), jeweils ohne Kenntnis der
Antworten der anderen.

**Aufgabe (wortgleich an alle):** "Hier ist Rohmaterial aus einem
Software-/Forschungsprojekt. Beschreibe in eigenen Worten: (a) was ist
der konzeptionelle Kern dieses Projekts, (b) welche 3–5 Begriffe sind
zentral, (c) wie hängen die Teile hierarchisch zusammen (was ist
Fundament, was baut darauf auf)."

## 4. Vergleichsmetriken (operationalisiert, nicht nur benannt)

1. **Begriffsüberlappung:** Jaccard-Index über die von jedem Agenten
   genannten Kernbegriffe (Menge der genannten Begriffe pro Agent,
   paarweise verglichen). Schwelle für "relevante Übereinstimmung":
   willkürlich, aber vorab festzulegen — Vorschlag: Jaccard ≥ 0.3 über
   alle Paare als Mindestindiz, sonst gilt die Hypothese für diesen
   Durchlauf als nicht gestützt.
2. **Architekturübereinstimmung:** Stimmen die genannten
   Fundament-vs-Aufbau-Zuordnungen (z. B. "X hängt von Y ab") mit den
   echten Abhängigkeiten aus `ECOSYSTEM_MAP.yaml` überein? Gemessen als
   Anteil korrekt zugeordneter Paare unter allen genannten Paaren.
3. **Hierarchiekonsistenz:** Stimmen die Agenten *untereinander* darin
   überein, welches Paket/Konzept als "Kern" bezeichnet wird (nicht ob
   es richtig ist, sondern ob sie sich einig sind)?
4. **Rekonstruktionsqualität:** menschliche Bewertung (Johann oder ein
   zweiter unabhängiger Gutachter) auf einer einfachen Skala
   (ja/teilweise/nein), ob die Beschreibung den tatsächlichen Zweck des
   Projekts erkennen lässt — als Gegengewicht zu rein lexikalischen
   Metriken (1–3), die hohe Übereinstimmung bei trivialer/falscher
   Beschreibung nicht ausschließen.

## 5. Was ein Fehlschlag der Hypothese konkret aussähe

Damit dieser Test nicht durch nachträgliche Umdeutung jedes Ergebnisses
zu einem Erfolg wird (Regel 5/11-Geist): ein Fehlschlag liegt vor, wenn
(a) Jaccard-Index unter der vorab festgelegten Schwelle bleibt, UND
(b) die genannten "Kern"-Konzepte sich zwischen Agenten so stark
unterscheiden, dass kein gemeinsamer Nenner benennbar ist, UND (c) die
Architekturübereinstimmung nicht klar über Zufallsniveau liegt (bei
wenigen, stark verschachtelten Abhängigkeiten lässt sich Zufallsniveau
nicht exakt vorab berechnen — daher zusätzlich Vergleich mit einer
Kontrollgruppe, die irrelevantes/fremdes Rohmaterial bekommt, siehe
unten).

## 6. Kontrollgruppe (notwendig, fehlt in Aeons ursprünglichem Vorschlag)

Ohne Kontrollgruppe ist nicht unterscheidbar, ob eine gefundene
Übereinstimmung auf der spezifischen Kohärenz von GenesisAeon beruht
oder schlicht daraus, dass jedes hinreichend strukturierte
Software-Rohmaterial zu ähnlichen Beschreibungsmustern führt
("Kern/Fundament/Aufbau" ist eine generische Beschreibungsform für
fast jede Codebasis). Vorschlag: dieselben Agenten (frische Sessions)
erhalten zusätzlich Rohmaterial aus einem unabhängigen,
GenesisAeon-fremden Open-Source-Projekt vergleichbarer Größe und
durchlaufen dieselbe Aufgabe. Nur wenn die Übereinstimmung bei
GenesisAeon-Material klar höher ausfällt als beim Kontroll-Projekt,
ist das ein Indiz für eine spezifische Eigenschaft dieser Architektur
statt für eine generische Eigenschaft von Beschreibungsaufgaben.

## 7. Einordnung des Zwei-KI-Spiegel-Risikos für diesen Test selbst

Wichtig: Dieses Protokoll selbst wurde von Claude entworfen, als
Reaktion auf einen von Aeon vorgeschlagenen Begriff, in einem Dialog, in
dem beide Seiten sich wiederholt gegenseitig für epistemische Vorsicht
gelobt haben (siehe `finales-grundprinzip-genesisaeon.md`, Abschnitt
"Zwei-KI-Spiegel-Risiko"). Das macht das *Protokolldesign* nicht
ungültig, aber jede spätere Interpretation der Ergebnisse sollte nicht
allein von Claude oder Aeon vorgenommen werden, sondern von Johann oder
einem dritten, unbeteiligten Gutachter — sonst wiederholt sich das
Risiko auf der Auswertungsebene.

## 8. Einordnung: Aeons "Idea Lifecycle"-Vorschlag (nicht Teil dieses Tests)

Aeons zweite Nachricht schlägt zusätzlich ein gestuftes
Lebenszyklusmodell vor (`observation → draft → hypothesis →
operationalization → benchmark → validated/falsified → infrastructure`)
als Ersatz oder Ergänzung für das bestehende `epistemic_status`-Feld
(`validated/measured/derived/hypothesis/speculative`). Das ist inhaltlich
nicht uninteressant — es würde zwischen "Hypothese" und "Messung" zwei
zusätzliche Stufen einführen (Operationalisierung, Benchmark), die im
aktuellen Schema fehlen, und genau das, was dieser Trylayer-Eintrag
gerade tut (eine Idee in ein Testprotokoll verwandeln), explizit
benennbar machen.

**Warum das hier nicht einfach übernommen wird:** `epistemic_status` ist
keine isolierte Doku-Konvention, sondern ein durch
`scripts/validate_trylayer.py` und das Trylayer-Schema technisch
durchgesetztes Feld, das aktuell für alle ~36 bestehenden Einträge in
diesem Repo gilt. Eine Erweiterung des Wertebereichs ist eine
Schema-/Infrastrukturänderung mit Wirkung auf das gesamte Repo, nicht
nur auf diesen einen Plan — das verdient einen eigenen Vorschlag mit
eigenem Review, nicht eine Nebenbei-Übernahme innerhalb dieses
Testprotokolls. Empfehlung: falls Johann das Modell für sinnvoll hält,
als eigenen `02_Plaene/`-Eintrag ausarbeiten (Migrationsplan für
bestehende Einträge, Kompatibilität mit `validate_trylayer.py`), separat
von der Destillierbarkeits-Frage hier.

## Nächster Schritt

1. Rohmaterial-Set (3–5 Repo-README/Strukturauszüge + `ECOSYSTEM_MAP.yaml`
   + `STATUS.md`-Historie, ohne Constitution/Aeon-Texte) zusammenstellen.
2. Kontroll-Rohmaterial (fremdes Open-Source-Projekt) auswählen.
3. Mindestens 3 unabhängige, frische Agenten-Sessions mit identischer
   Aufgabenstellung durchführen, Ergebnisse roh archivieren (Regel 11).
4. Metriken 1–4 berechnen, Auswertung durch Johann oder einen dritten
   Gutachter (nicht durch Claude oder Aeon selbst).
5. Ergebnis in einem neuen `epistemic_status: measured`-Eintrag
   festhalten, unabhängig vom Ausgang — auch ein Fehlschlag der
   Hypothese ist ein gültiges, zu dokumentierendes Ergebnis (Regel 11).
