import json
from pathlib import Path

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_entry_and_icon_are_ready():
    entry = json.loads((ROOT / "platinas-entry.json").read_text(encoding="utf-8"))
    assert entry["id"] == "witcher3-base"
    assert entry["module"] == "platina_witcher3.module"
    icon = QImage(str(ROOT / entry["icon"]))
    assert not icon.isNull()
    assert icon.width() == 256 and icon.height() == 256
    assert icon.hasAlphaChannel()
    assert icon.pixelColor(0, 0).alpha() == 0


def test_local_guide_images_render_without_network():
    app = QApplication.instance() or QApplication([])
    assets = ROOT / "src" / "platina_witcher3" / "assets"
    for filename in ("cover-fallback.svg", "safety-route.svg", "gwent-route.svg"):
        pixmap = QPixmap(str(assets / filename))
        assert not pixmap.isNull(), filename
        assert pixmap.width() >= 800
    assert app is not None
