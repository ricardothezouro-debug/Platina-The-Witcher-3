import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from platina_witcher3 import page


def test_page_builds_and_gate_unlocks(monkeypatch):
    app = QApplication.instance() or QApplication([])
    saved = []

    class FakeImageLoader:
        def __init__(self, _parent=None):
            pass

        def load(self, _url, _on_ready):
            return None

        def shutdown(self):
            pass

    monkeypatch.setattr(page, "ImageLoader", FakeImageLoader)
    monkeypatch.setattr(page, "load_progress", lambda: {
        "version": 1,
        "done": [],
        "current_phase": "white_orchard",
        "build_style": "",
    })
    monkeypatch.setattr(page, "save_progress", lambda value: saved.append(value.copy()))
    monkeypatch.setattr(page, "load_ui", lambda: {})
    monkeypatch.setattr(page, "save_ui", lambda _value: None)
    monkeypatch.setattr(page, "guide_dir_label", lambda: "pasta de teste")

    widget = page.GuidePage()
    assert len(widget._phase_combos) >= 2
    # Regioes nao repete os cards de Agora: objetivo de outra fase nao tem
    # caixa de marcar ate a fase dele chegar.
    assert not widget._boxes["task:simulate_letho"]
    status_labels = [
        label for label in widget.stack.widget(1).findChildren(page.QLabel)
        if label.text() in {"FEITO", "PENDENTE"}
    ]
    assert len(status_labels) == len(page.guide_data.TASKS)
    widget._advance_phase()
    assert widget._state["current_phase"] == "vizima"
    assert widget._boxes["task:simulate_letho"]
    assert widget._boxes["gwent:vizima_noble"]
    requirements = [
        widget._boxes["task:start_death_march"][-1],
        widget._boxes["gwent:teacher_white_orchard"][-1],
        widget._boxes["gwent:buy_white_orchard"][-1],
    ]
    audit = widget._boxes["gate:leave_white_orchard"][-1]
    assert not audit.isEnabled()
    for box in requirements:
        box.setChecked(True)
    app.processEvents()
    assert audit.isEnabled()
    audit.setChecked(True)
    app.processEvents()
    app.sendPostedEvents()
    assert "gate:leave_white_orchard" in widget._done
    completed_audit = widget._boxes["gate:leave_white_orchard"][-1]
    completed_audit.setChecked(False)
    app.processEvents()
    app.sendPostedEvents()
    assert "gate:leave_white_orchard" not in widget._done
    # A marcacao feita em Agora aparece no resumo de Regioes
    assert "task:start_death_march" in widget._done
    assert any(
        label.text() == "FEITO"
        for label in widget.stack.widget(1).findChildren(page.QLabel)
    )
    widget._open_phase("skellige")
    assert widget._state["current_phase"] == "skellige"
    assert widget.stack.currentIndex() == 0
    widget._choose_build(page.guide_data.BUILDS[1])
    assert widget._state["build_style"] == "sign_control"
    assert widget.stack.widget(0).findChildren(page.QLabel)
    widget.resize(1120, 860)
    widget.show()
    app.processEvents()
    for section in (0, 1, 2):
        assert any(
            label.pixmap() is not None and not label.pixmap().isNull()
            for label in widget.stack.widget(section).findChildren(page.QLabel)
        )
    assert widget._phase_combos[-1].minimumSizeHint().width() < 500
    assert saved
    widget.close()
