import json

from platina_witcher3 import storage


def test_progress_roundtrip_and_deduplication(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "guide_dir", lambda: tmp_path)
    storage.save_progress(
        {
            "done": ["task:a", "task:a", "trophy:b"],
            "current_phase": "novigrad",
            "build_style": "sign_control",
        }
    )
    loaded = storage.load_progress()
    assert loaded["done"] == ["task:a", "trophy:b"]
    assert loaded["current_phase"] == "novigrad"
    assert loaded["build_style"] == "sign_control"


def test_legacy_list_progress_is_migrated(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "guide_dir", lambda: tmp_path)
    (tmp_path / "progress.json").write_text(
        json.dumps(["task:a", "trophy:b"]), encoding="utf-8"
    )
    loaded = storage.load_progress()
    assert loaded["done"] == ["task:a", "trophy:b"]
    assert loaded["current_phase"] == "white_orchard"

