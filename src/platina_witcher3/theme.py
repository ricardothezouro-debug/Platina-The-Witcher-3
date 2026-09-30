"""Acentos future funk, restritos à página do guia."""
GUIDE_STYLE = """
QWidget#WitcherGuide { background:#0A0B12; }
QWidget#HeroContent, QWidget#GuideBody { background:transparent; }
QFrame#NeonPanel { background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #142030,stop:0.55 #121827,stop:1 #23172D); border:1px solid #3E4263; border-radius:16px; }
QFrame#NeonPanel[variant="HeroPanel"] { border:1px solid #37F2FF; background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #12323D,stop:0.55 #171F38,stop:1 #3A1C42); }
QCheckBox#ChecklistRow { background:transparent; border:1px solid transparent; border-radius:9px; spacing:10px; color:#E1E8F3; }
QCheckBox#ChecklistRow:hover { background:rgba(55,242,255,12); border-color:#36515D; }
QCheckBox#ChecklistRow:checked { background:rgba(55,242,255,7); }
QCheckBox#ChecklistRow QLabel { background:transparent; color:#E1E8F3; }
QCheckBox#ChecklistRow:disabled QLabel { color:#77859B; }
QCheckBox#ChecklistRow::indicator { width:19px; height:19px; margin-left:3px; border:1px solid #60748F; border-radius:6px; background:#0C1521; }
QCheckBox#ChecklistRow::indicator:checked { background:#123641; border-color:#37F2FF; }
QPushButton#PrimaryButton:disabled { color:#8491A6; background:#1B2230; border-color:#3A4254; }
QLabel#PageTitle { font-size:30px; }
QLabel#Kicker { font-size:12px; }
QLabel#StatusPill { background:#131B2C; border:1px solid #43415F; border-radius:10px; padding:7px 10px; }
QPushButton#HistoryToggle { background:#211A31; border:1px solid #75518C; color:#DEC4F2; text-align:left; }
"""
