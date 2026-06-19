# adr — Architecture Decision Records

Format: Trylayer-Tripel `<slug>.{yaml,ai.json,md}` mit `kategorie: adr`,
`status: accepted`. Slug ist ein normaler lowercase-Slug
(z.B. `adr-001-warum-monorepo.yaml`); das Pflichtfeld `adr_number`
(`ADR-001`) ist die Referenz, ueber die andere Eintraege per
`related_adr` auf dieses ADR verweisen (siehe PRINCIPLES.md, Regel 3).

Jede groessere Architekturentscheidung bekommt ein ADR, bevor sie in
`03_Architektur/`, `04_Programme/` oder `05_Hilfsprogramme/` als
`accepted` landen kann. Niemals nachtraeglich inhaltlich aendern — eine
neue Entscheidung bekommt ein neues ADR mit `supersedes` auf das alte.
