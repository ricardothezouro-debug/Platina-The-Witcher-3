"""Redimensiona o ícone-fonte para o PNG usado pelo catálogo."""
from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "icon-source.png"
OUTPUT = ROOT / "assets" / "icon.png"

image = QImage(str(SOURCE))
if image.isNull():
    raise SystemExit(f"não foi possível abrir {SOURCE}")
icon = image.scaled(
    256,
    256,
    Qt.AspectRatioMode.KeepAspectRatio,
    Qt.TransformationMode.SmoothTransformation,
)
if not icon.save(str(OUTPUT), "PNG"):
    raise SystemExit(f"não foi possível salvar {OUTPUT}")

