"""Persistência do progresso e das preferências de interface."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .paths import guide_dir

_STATE_VERSION = 1


def default_progress() -> dict[str, Any]:
    return {
        "version": _STATE_VERSION,
        "done": [],
        "current_phase": "white_orchard",
        "build_style": "",
    }


def _read_json(path: Path, fallback: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return fallback


def _write_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    try:
        temporary.write_text(
            json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        temporary.replace(path)
    except OSError:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def load_progress() -> dict[str, Any]:
    raw = _read_json(guide_dir() / "progress.json", default_progress())
    if isinstance(raw, list):
        state = default_progress()
        state["done"] = [str(key) for key in raw]
        return state
    if not isinstance(raw, dict):
        return default_progress()
    state = default_progress()
    state.update(raw)
    done = state.get("done", [])
    state["done"] = sorted({str(key) for key in done}) if isinstance(done, list) else []
    return state


def save_progress(state: dict[str, Any]) -> None:
    clean = default_progress()
    clean.update(state)
    clean["done"] = sorted({str(key) for key in clean.get("done", [])})
    _write_json(guide_dir() / "progress.json", clean)


def load_ui() -> dict[str, Any]:
    raw = _read_json(guide_dir() / "ui.json", {})
    return raw if isinstance(raw, dict) else {}


def save_ui(prefs: dict[str, Any]) -> None:
    _write_json(guide_dir() / "ui.json", prefs)

