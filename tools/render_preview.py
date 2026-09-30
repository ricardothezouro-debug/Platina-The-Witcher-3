"""Gera uma captura local da tela inicial para revisão visual."""
from __future__ import annotations

import os
import sys
import argparse
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QPushButton, QScrollArea

from platina_witcher3 import page
from platina_witcher3.__main__ import _THEME


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("phase", nargs="?", default="white_orchard")
    parser.add_argument("section", nargs="?", type=int, default=0)
    parser.add_argument("--width", type=int, default=1120)
    parser.add_argument("--height", type=int, default=860)
    parser.add_argument("--detail")
    args = parser.parse_args()
    output = Path(args.output).resolve()
    phase = args.phase
    section = args.section
    output.parent.mkdir(parents=True, exist_ok=True)

    page.load_progress = lambda: {
        "version": 1,
        "done": [],
        "current_phase": phase,
        "build_style": "sign_control",
    }
    page.save_progress = lambda _value: None
    page.load_ui = lambda: {"level": 1}
    page.save_ui = lambda _value: None
    page.guide_dir_label = lambda: "pasta de dados do Streamer Sidekick"

    app = QApplication.instance() or QApplication([])
    windows_font = Path("C:/Windows/Fonts/segoeui.ttf")
    if windows_font.exists():
        QFontDatabase.addApplicationFont(str(windows_font))
    app.setStyleSheet(_THEME)
    widget = page.GuidePage()
    widget.resize(args.width, args.height)
    widget.show()
    widget._select_section(section)
    app.processEvents()
    if args.detail:
        target_page = widget.stack.widget(section)
        for button in target_page.findChildren(QPushButton):
            if button.property("walkthrough") == args.detail:
                button.setChecked(True)
                app.processEvents()
                scroll = target_page if isinstance(target_page, QScrollArea) else target_page.findChild(QScrollArea)
                scroll.verticalScrollBar().setValue(button.mapTo(scroll.widget(), button.rect().topLeft()).y()-40)
                app.processEvents()
                break
    success = widget.grab().save(str(output), "PNG")
    widget.close()
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
