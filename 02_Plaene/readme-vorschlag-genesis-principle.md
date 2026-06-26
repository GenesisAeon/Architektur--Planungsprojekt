# Vorschlag: Genesis Principle / Architectural Principle als README-Einleitung für das zukünftige Genesis-Core-Monorepo

**Status:** draft · **Epistemic Status:** derived · **Autor:** Claude

## Problem

Johann hat in `FinalesGrundpriniziepGenesisAeon.txt` formulierte
Abschnitte ("Genesis Principle", "Architectural Principle", "Long-Term
Vision") als geeigneten Marketing-/Onboarding-Text für kontextfreie
Leser eingeordnet — nicht als Verfassungsänderung (Regel 12 betrifft das
nicht), sondern als Pitch für das zukünftige Genesis-Core-Monorepo
(siehe `02_Plaene/genesis-core-scope.md`). Aktuell existiert dafür noch
kein konkreter Textvorschlag in Trylayer-Form.

## Vorschlag

Eine kurze README-Einleitung, die den Text fast wörtlich übernimmt,
aber an zwei Stellen präzisiert:

1. explizit als Beschreibung gelebter Praxis kennzeichnen, nicht als
   bindendes Regelwerk — die eigentlichen Regeln stehen in
   `PRINCIPLES.md`/`00_Regeln`;
2. den Bezug zum bereits etablierten Trylayer-/Blindtest-/
   epistemic_status-Apparat herstellen, damit der Pitch nicht als reine
   Behauptung wirkt, sondern als Zusammenfassung von etwas, das durch
   Tooling (`validate_trylayer.py`, Genesis-Blindtest) tatsächlich
   durchgesetzt wird.

## Textvorschlag (DE)

> ## Wofür dieses Projekt steht
>
> Bring deine schärfste Kritik mit.
>
> Wir bauen den Raum so, dass er unser gemeinsames Verstehen verbessert.
>
> Meinungsverschiedenheit ist kein Scheitern der Zusammenarbeit. Mit
> intellektueller Ehrlichkeit und gegenseitigem Respekt erforscht, wird
> sie zu einer der wertvollsten Ressourcen.
>
> GenesisAeon ist so angelegt, dass
>
> - Kritik bewahrt statt unterdrückt wird (siehe Regel 11: keine
>   Löschung dokumentierter Messungen);
> - Unsicherheit dokumentiert statt versteckt wird (siehe
>   epistemic_status-Feld: validated/measured/derived/hypothesis/
>   speculative);
> - Hypothesen falsifizierbar bleiben (siehe Genesis-Blindtest, Regel 6);
> - jeder Beitrag das gemeinsame Modell verbessern kann.
>
> Das System optimiert nicht auf Konsens. Es optimiert auf
> kontinuierliche Verbesserung des gemeinsamen Verstehens.
>
> Das ist kein Versprechen, sondern eine Beschreibung der Werkzeuge, die
> das hier tatsächlich durchsetzen.

## Textvorschlag (EN)

> ## What this project stands for
>
> Bring your strongest criticism.
>
> We build the space so that it improves our shared understanding.
>
> Disagreement is not a failure of collaboration. Explored with
> intellectual honesty and mutual respect, it becomes one of the most
> valuable resources we have.
>
> GenesisAeon is designed so that
>
> - criticism is preserved rather than suppressed (see Rule 11: recorded
>   measurements are never deleted);
> - uncertainty is documented rather than hidden (see the
>   epistemic_status field: validated/measured/derived/hypothesis/
>   speculative);
> - hypotheses remain falsifiable (see the Genesis Blindtest, Rule 6);
> - every contribution may improve the shared model.
>
> The system does not optimize for consensus. It optimizes for
> continuous improvement of shared understanding.
>
> This is not a promise — it describes tooling that actually enforces
> it.

## Einordnung

`status: draft` (nicht `accepted`), weil Platzierung und finaler
Wortlaut noch Johanns Entscheidung sind. `epistemic_status: derived`,
weil der Text direkt aus `FinalesGrundpriniziepGenesisAeon.txt`
abgeleitet ist, mit Präzisierungen, die auf bereits etablierten
Repo-Mechanismen (Regel 11, epistemic_status, Genesis-Blindtest)
beruhen — keine neue empirische Behauptung.

## Nächster Schritt

Johann entscheidet, ob/wann/wo (dieses Planungsrepo vs. zukünftiges
Genesis-Core-Monorepo-README) der Text übernommen wird; bei Bedarf
Feinschliff am Wortlaut.
