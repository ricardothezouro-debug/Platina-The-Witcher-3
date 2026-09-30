"""Executa o guia fora do Streamer Sidekick."""
import sys

from PySide6.QtWidgets import QApplication

from . import guide_data
from .page import GuidePage

_THEME = """
QWidget{background:#090C16;color:#F3F6FF;font-family:'Segoe UI';font-size:14px}
QLabel{background:transparent}
QLabel#PageTitle{font-family:'Bahnschrift';font-size:34px;font-weight:700;color:#FFFFFF}
QLabel#CardTitle{font-family:'Bahnschrift';font-size:24px;font-weight:700}
QLabel#SectionTitle{font-size:18px;font-weight:700}
QLabel#Muted{color:#ACB8CA}
QLabel#Kicker{color:#37F2FF;font-family:'Consolas';font-size:14px;font-weight:700}
QLabel#StatusPill{background:#101625;border:1px solid #354056;border-radius:8px;padding:7px 10px;color:#DCE6F2;font-weight:600}
QFrame#NeonPanel{background:#101521;border:1px solid #354056;border-radius:12px}
QFrame#NeonPanel[variant="HeroPanel"]{background:#111827;border:1px solid #37F2FF;border-radius:12px}
QFrame#NeonPanel[variant="ActiveBuildPanel"]{background:#12192B;border:1px solid #FF4FD8;border-radius:12px}
QLineEdit,QComboBox{background:#0B111A;border:1px solid #273140;border-radius:8px;padding:9px 10px;color:#F3F6FF;min-height:20px}
QLineEdit:focus,QComboBox:focus{background:#0D1621;border-color:#37F2FF}
QPushButton{background:#151C2A;border:1px solid #354056;border-radius:8px;padding:10px 14px;color:#F3F6FF;font-weight:600}
QPushButton:hover{background:#151E2C;border-color:#37F2FF;color:#FFFFFF}
QPushButton:pressed{background:#0D121B;border-color:#FF4FD8}
QPushButton:disabled{background:#0D121B;border-color:#202936;color:#687180}
QPushButton#PrimaryButton{background:#123B48;border-color:#37F2FF;color:#FFFFFF}
QPushButton#PrimaryButton:hover{background:#174A52;border-color:#FF4FD8}
QCheckBox{spacing:8px;color:#D9E4EF}
QCheckBox:checked{color:#8E99A8}
QCheckBox::indicator{width:18px;height:18px;border-radius:5px;border:1px solid #596373;background:#0B111A}
QCheckBox::indicator:checked{background:#14383F;border-color:#37F2FF}
QScrollArea{background:transparent;border:0}
QScrollBar:vertical{background:transparent;width:12px;margin:2px}
QScrollBar::handle:vertical{background:#273140;border-radius:5px;min-height:36px}
QScrollBar::handle:vertical:hover{background:#37F2FF}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0;border:0;background:transparent}
"""


def run() -> int:
    app = QApplication(sys.argv)
    app.setStyleSheet(_THEME)
    page = GuidePage()
    page.setWindowTitle(f"{guide_data.GAME_NAME}, guia de platina")
    page.resize(1120, 860)
    page.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(run())
