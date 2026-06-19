#!/usr/bin/env python3
"""Erzwingt die Trylayer-Regeln aus PRINCIPLES.md.

Laeuft als pre-commit-Hook und in CI. Exit-Code != 0 bei jeder Verletzung.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

FOLDER_RULES: dict[str, tuple[str, set[str]]] = {
    "00_Regeln": ("regel", {"core"}),
    "01_Ideen": ("idee", {"idea", "draft"}),
    "02_Plaene": ("plan", {"draft", "review"}),
    "03_Architektur": ("architektur", {"accepted", "core"}),
    "04_Programme": ("programm", {"accepted", "core"}),
    "05_Hilfsprogramme": ("hilfsprogramm", {"accepted", "core"}),
    "06_Sprachen": ("sprache", {"accepted", "core"}),
    "adr": ("adr", {"accepted"}),
}

STATUS_RANK = {
    "idea": 0,
    "draft": 1,
    "review": 2,
    "accepted": 3,
    "core": 4,
}

ADR_REQUIRED_KATEGORIEN = {"architektur", "programm", "hilfsprogramm"}


@dataclass
class Entry:
    slug: str
    folder: str
    meta: dict


def find_trylayer_dirs() -> list[Path]:
    return [ROOT / name for name in FOLDER_RULES if (ROOT / name).is_dir()]


def collect_entries(errors: list[str]) -> list[Entry]:
    entries: list[Entry] = []
    for folder in find_trylayer_dirs():
        folder_name = folder.name
        yaml_files = sorted(folder.rglob("*.yaml"))
        for yaml_path in yaml_files:
            slug = yaml_path.stem
            json_path = yaml_path.with_name(f"{slug}.ai.json")
            md_path = yaml_path.with_name(f"{slug}.md")

            missing = [str(p.name) for p in (json_path, md_path) if not p.exists()]
            if missing:
                errors.append(
                    f"[{folder_name}] Unvollstaendiges Trylayer-Tripel fuer '{slug}': "
                    f"fehlt {', '.join(missing)} (Regel 1)"
                )
                continue

            try:
                meta = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError as exc:
                errors.append(f"[{folder_name}] '{slug}.yaml' ist kein gueltiges YAML: {exc}")
                continue

            try:
                ai_doc = json.loads(json_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"[{folder_name}] '{slug}.ai.json' ist kein gueltiges JSON: {exc}")
                continue

            if ai_doc.get("id") != meta.get("id"):
                errors.append(
                    f"[{folder_name}] '{slug}': id in .yaml ('{meta.get('id')}') und "
                    f".ai.json ('{ai_doc.get('id')}') stimmen nicht ueberein"
                )

            entries.append(Entry(slug=slug, folder=folder_name, meta=meta))
    return entries


def check_required_fields(entry: Entry, errors: list[str]) -> None:
    required = ("id", "title", "kategorie", "status", "epistemic_status", "created", "author")
    for field in required:
        if field not in entry.meta:
            errors.append(
                f"[{entry.folder}] '{entry.slug}': Pflichtfeld '{field}' fehlt (Schema)"
            )


def check_folder_rules(entry: Entry, errors: list[str]) -> None:
    expected_kategorie, allowed_status = FOLDER_RULES[entry.folder]
    kategorie = entry.meta.get("kategorie")
    status = entry.meta.get("status")

    if kategorie != expected_kategorie:
        errors.append(
            f"[{entry.folder}] '{entry.slug}': kategorie '{kategorie}' passt nicht zu "
            f"Ordner (erwartet '{expected_kategorie}') (Regel 2)"
        )

    if status not in allowed_status and status not in ("deprecated", "archived"):
        errors.append(
            f"[{entry.folder}] '{entry.slug}': status '{status}' nicht erlaubt in diesem "
            f"Ordner (erlaubt: {sorted(allowed_status)}) (Regel 2)"
        )


def check_adr_required(entry: Entry, errors: list[str]) -> None:
    kategorie = entry.meta.get("kategorie")
    status = entry.meta.get("status")
    if kategorie in ADR_REQUIRED_KATEGORIEN and status in ("accepted", "core"):
        related_adr = entry.meta.get("related_adr") or []
        if not related_adr:
            errors.append(
                f"[{entry.folder}] '{entry.slug}': status='{status}' ohne related_adr "
                f"(Regel 3 — kein Core ohne ADR)"
            )


def check_blindtest(entry: Entry, errors: list[str]) -> None:
    kategorie = entry.meta.get("kategorie")
    status = entry.meta.get("status")
    if kategorie in ("architektur", "programm") and status == "accepted":
        if entry.meta.get("blindtest_passed") is not True:
            errors.append(
                f"[{entry.folder}] '{entry.slug}': status='accepted' aber "
                f"blindtest_passed != true (Regel 6)"
            )


def check_dependency_rank(entries: list[Entry], errors: list[str]) -> None:
    by_id = {e.meta.get("id"): e for e in entries if e.meta.get("id")}
    for entry in entries:
        own_status = entry.meta.get("status")
        own_rank = STATUS_RANK.get(own_status)
        if own_rank is None:
            continue
        for dep_id in entry.meta.get("depends_on") or []:
            dep = by_id.get(dep_id)
            if dep is None:
                errors.append(
                    f"[{entry.folder}] '{entry.slug}': depends_on unbekannte id '{dep_id}'"
                )
                continue
            dep_rank = STATUS_RANK.get(dep.meta.get("status"))
            if dep_rank is None:
                continue
            if dep_rank < own_rank:
                errors.append(
                    f"[{entry.folder}] '{entry.slug}' (status={own_status}) haengt von "
                    f"'{dep_id}' (status={dep.meta.get('status')}) ab — Reife darf nicht "
                    f"von Unreife abhaengen (Regel 4)"
                )


def main() -> int:
    errors: list[str] = []
    entries = collect_entries(errors)

    for entry in entries:
        check_required_fields(entry, errors)
        check_folder_rules(entry, errors)
        check_adr_required(entry, errors)
        check_blindtest(entry, errors)

    check_dependency_rank(entries, errors)

    if errors:
        print(f"Trylayer-Validierung fehlgeschlagen ({len(errors)} Verstoss/Verstoesse):\n")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"Trylayer-Validierung ok ({len(entries)} Eintraege geprueft).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
