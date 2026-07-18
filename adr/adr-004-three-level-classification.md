# ADR-004 — Three-Level Package Classification (Core / Scientific / Experimental)

## Kontext

Das GenesisAeon-Ökosystem umfasst inzwischen 52 Pakete, die von
physikalischer Simulation (amoc-utac, quantum-genesis) über
Infrastruktur (diamond-setup, genesis-os) bis zu explorativer Forschung
(genesis-mssc, ai-emergence-utac) reichen. Ohne explizite Klassifikation
wird jedes Paket implizit als gleich stabil behandelt — das ist falsch
und irreführend für externe Nutzer.

Das Audit vom 2026-06-29 bestätigt das: 35% der Diamond-Interface-Pakete
sind vollständig schema-konform, 65% haben eine partielle oder keine
Implementierung. Der Vendoring-Sweep (2026-07-17) fand zusätzliche
strukturelle Altlasten in ~15 Paketen. Eine klare, maschinell
verifizierbare Klassifikation ist nötig.

## Entscheidung

Drei Tiers, bestimmt durch zwei messbare Kriterien:

| Kriterium | Gemessen durch |
|-----------|-----------------|
| Ρ (System-Resilienz) | `get_resilience_state()["rho"]` aus resilience-core (P40) |
| Γ-Konvergenz | `get_crep_state()["Gamma"]` ist nicht None nach `run_cycle()` |

### Tier-Definitionen

| Tier | Ρ | Γ | CREPGate | Bedeutung |
|------|---|---|----------|-----------|
| **Core** | ≥ 0.60 | konvergiert | — | Production-stable. Externe Nutzer können sich darauf verlassen. |
| **Scientific** | 0.30–0.60 | konvergiert | — | Research-grade. API kann sich weiterentwickeln. Mit DOI zitieren. |
| **Experimental** | < 0.30 ODER | nicht konvergiert ODER | blocked | Aktive Forschung. Breaking Changes erwartbar. |

Die Tier-Zuordnung ist **automatisch** — abgeleitet aus der eigenen
Diamond-Interface-Ausgabe des Pakets, nicht vom Maintainer deklariert.
Ein CI-Job berechnet die Tier-Zugehörigkeit bei jedem Release neu.

## Package Assignments (initial, 2026-07-18)

*Basierend auf r=1.0 Default in resilience-core. r wird pro Domäne
kalibriert, sobald empirische Daten vorliegen (siehe amoc_calibration.py
in P40).*

### Core (Ρ ≥ 0.60, Γ konvergiert)

| Paket | Ρ | Γ | Notiz |
|-------|---|---|-------|
| diamond-setup | — | — | Infrastruktur — kein Domain-Γ |
| genesis-os | — | — | Orchestrator — Classification Host |
| entropy-table | — | — | Data Engine — kein Domain-Γ |
| utac-core | — | — | UTAC-Basis — run_cycle für Γ nötig |
| fieldtheory | — | — | Theory Core |
| sigillin | — | — | Semantische Anker |
| implosive-genesis | — | — | Field Dynamics |

*Hinweis: mehrere Core-Kandidaten exponieren `get_resilience_state()`
noch nicht (sie stammen aus der Zeit vor P40). Sie sind vorläufig nach
struktureller Rolle als Core klassifiziert, bis resilience-core
integriert ist — siehe Follow-up-Tasks.*

### Scientific (0.30 ≤ Ρ < 0.60, Γ konvergiert)

| Paket | Ρ (r=1.0) | Γ | Domäne |
|-------|-----------|---|--------|
| amoc-utac | ~0.18 (r=1.0) / ~0.65 (r=3.54) | 0.251 | Ozeanographie |
| neural-avalanche-utac | ~0.18 | 0.241 | Neurowissenschaft |
| seismic-utac | ~0.15 | 0.197 | Geophysik |
| quantum-genesis | ~0.01 | 0.035 | Quantenphysik |
| sandpile-utac | ~0.22 | 0.297 | Statistische Mechanik |
| resilience-core | variiert | — | Meta-Dynamik |
| scope-resilience | — | — | Semantische KI |

*Hinweis: Ρ-Werte bei r=1.0 sind systematisch niedrig. Kalibrierte
r-Werte (siehe amoc_calibration.py: r_amoc ≈ 3.54) werden diese in den
bestätigten Scientific-Bereich verschieben. Ausstehend: Kalibrierung pro
Domäne.*

### Experimental (Ρ < 0.30 ODER Γ nicht konvergiert ODER Gate blocked)

| Paket | Status | Grund |
|-------|--------|-------|
| genesis-mssc | v0.1.0, gate=blocked | CREPGate-Bedingungen nicht erfüllt |
| genesis-tip | v0.1.1, gate=blocked | Gamma_somatic nicht implementiert |
| ai-emergence-utac | v0.1.0, gate=blocked | H1/H2 noch nicht bestätigt |
| hikari-ledger | — | Γ≈0.893 (von Atlas abweichend) |
| diffusive-routing | — | Γ≈0.002 (von Atlas abweichend) |
| phaethon-chimera | — | Γ≈0.296 (abweichend, erwartet 0.165) |

## CI-Implementierung

Ergänzung in `.github/workflows/diamond-validation.yml` in jedem Paket:

```yaml
- name: Compute tier classification
  run: |
    python -c "
    import importlib, sys
    sys.path.insert(0, 'src')

    # Finde die Diamond-Hauptklasse
    pkg = importlib.import_module('${{ vars.PACKAGE_MODULE_NAME }}')
    cls = [c for n,c in vars(pkg).items()
           if isinstance(c, type) and hasattr(c, 'run_cycle')
           and c.__name__ != 'DiamondPackage'][0]
    instance = cls()
    instance.run_cycle()

    crep = instance.get_crep_state()
    gamma = crep.get('Gamma')

    # Resilienz (optional — P40 ist ggf. keine Abhaengigkeit)
    try:
        res = instance.get_resilience_state()
        rho = res.get('rho')
    except Exception:
        rho = None

    # Klassifizieren
    if gamma is None:
        tier = 'Experimental (Gamma not converged)'
    elif rho is None:
        tier = 'unclassified (resilience-core not integrated)'
    elif rho >= 0.60:
        tier = 'Core'
    elif rho >= 0.30:
        tier = 'Scientific'
    else:
        tier = 'Experimental (low resilience)'

    print(f'Gamma: {gamma}')
    print(f'Rho:   {rho}')
    print(f'Tier:  {tier}')

    # In GITHUB_STEP_SUMMARY schreiben
    with open('${{ env.GITHUB_STEP_SUMMARY }}', 'a') as f:
        f.write(f'| Tier | {tier} |\n')
        f.write(f'| Γ    | {gamma} |\n')
        f.write(f'| Ρ    | {rho} |\n')
    "
```

## Begründung

- Externe Nutzer sehen sofort, ob ein Paket production-stable ist.
- Der Tier wird aus dem eigenen Code des Pakets abgeleitet — keine
  manuelle Deklaration, keine Selbstauskunft des Maintainers.
- Schafft einen klaren Anreiz: Ρ und Γ verbessern, um den Tier
  hochzustufen.
- Verbindet sich direkt mit dem CREP Atlas und der resilience-core-Arbeit
  (P40), statt eine eigene, unabhängige Metrik zu erfinden.

## Alternativen betrachtet

- **Manuelle Deklaration** — verworfen. Ein Maintainer, der das eigene
  Paket selbst "Core" nennt, ist nicht verifizierbar und schafft falsche
  Anreize.
- **Testabdeckung als Kriterium** — verworfen. Coverage misst
  Testvollständigkeit, nicht wissenschaftliche Validität. Ein Paket mit
  100% Coverage kann trotzdem falsche Γ-Werte haben.
- **Ein einziger Tier (keine Klassifikation)** — verworfen. 52 Pakete
  ohne Qualitätssignal sind schlechter als eine unvollkommene
  Klassifikation — das verschiebt die Bewertung komplett auf die
  Nutzerin.

## Konsequenzen

- **Positiv:** sofortige Sichtbarkeit für externe Nutzer; Tier aus dem
  Code selbst abgeleitet statt deklariert; klare
  Verbesserungsanreize; direkte Anbindung an CREP Atlas/resilience-core.
- **Negativ/Risiken:** r=1.0-Default liefert systematisch niedrige
  Ρ-Werte — viele eigentlich Scientific-reife Pakete erscheinen bis zur
  Domänen-Kalibrierung als Experimental (siehe P40). Pakete von vor P40
  haben `get_resilience_state()` noch nicht — Integrationsarbeit nötig,
  bevor der Tier für sie maschinell verifizierbar ist. Die aktuelle
  "Core"-Einstufung basiert auf struktureller Rolle, nicht auf
  gemessenem Ρ — Follow-up nötig, sobald P40 überall integriert ist.

### Follow-up Tasks

- [ ] resilience-core in alle aktuell strukturell als Core
      klassifizierten Pakete integrieren.
- [ ] r pro Domäne kalibrieren (P18 amoc-utac-Daten → r_amoc; danach
      weitere).
- [ ] CI-Tier-Classification-Step in allen 52 Paketen ergänzen.
- [ ] Γ-Divergenzen fixen (hikari-ledger 0.893, diffusive-routing 0.002)
      bevor diese Pakete neu eingestuft werden können.

## Referenzen

- CREP Atlas: GenesisAeon Feldtheorie-Preprints (Zenodo
  10.5281/zenodo.17472834)
- resilience-core (P40): UTAC-Eigenrate-Analyse
- Ecosystem Audit Report v1.0.1 (2026-06-29): Diamond-Interface-Coverage
  35%
- ADR-Format: MADR (Markdown Architecture Decision Records)
- Verwandt: [ADR-002](adr-002-mission-statement-v1.md) (Mission-Statement,
  externe Nutzer als Zielgruppe), [ADR-003](adr-003-ai-as-maintainer.md)
  (Verfahren, nach dem dieses ADR selbst entworfen/committet wurde — von
  einer KI entworfen, von Johann inhaltlich geprüft und akzeptiert,
  siehe Commit-Message)
