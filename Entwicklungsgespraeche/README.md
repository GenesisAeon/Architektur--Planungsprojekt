# Entwicklungsgespraeche

Rohprotokolle laufender Multi-AI-Diskurse (Claude, ChatGPT, Grok, Gemini,
MSCopilot, Johann), die zu einer konkreten Entscheidung gefuehrt haben oder
fuehren sollen. Anders als `Planungsdiskurse/` (read-only Archiv des
*urspruenglichen* Gruendungsdiskurses) ist dieser Ordner fuer **laufende**
Gespraeche gedacht, die noch nach diesem Repo verarbeitet werden.

Format: ein Rohtext/Markdown-Dump pro Gespraech, kein Trylayer-Tripel (das
ist hier bewusst nicht erforderlich, siehe `AGENTS.md`, Abschnitt "Rohformat
fuer externe Einreichungen" — diese Dateien sind die Eingabe, nicht das
Ergebnis). Wird ein Gespraech in eine Entscheidung umgesetzt, entsteht daraus
ein Trylayer-Eintrag (`01_Ideen/`, `02_Plaene/`, `adr/`, ...), der per
`derived_from`/`related_adr` auf die Datei hier zurueckverweist.

Namenskonvention: `<YYYY-MM-DD>-<kurzer-slug>.md`.
