"""Interface do guia de The Witcher 3."""
from __future__ import annotations

import html
import unicodedata
from collections import defaultdict
from pathlib import Path

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from . import guide_data, gwent_catalog, progress, skill_tree, trophies
from .image_loader import ImageLoader
from .paths import guide_dir_label
from .storage import load_progress, load_ui, save_progress, save_ui
from .topbar import InfoCorner, TopBar
from .widgets import ChecklistBox, GuideImage, ResponsiveHero, FuturePanel
from .theme import GUIDE_STYLE
from .walkthroughs import CONTRACT_STARTS, DETAIL_GUIDES, power_stones_by_region

_TIER_COLORS = {
    "bronze": "#CD7F32",
    "prata": "#C0C0C0",
    "ouro": "#FFD700",
    "platina": "#E5E4E2",
}
_TAG_COLORS = {
    "necessária": "#B9FF43",
    "útil": "#7FE7FF",
    "opcional": "#A8B0BC",
    "perdível": "#F87171",
    "spoiler": "#C4A7FF",
    "exploração": "#7FE7FF",
    "pode ignorar": "#A8B0BC",
    "selecionado": "#B9FF43",
    "confirmado": "#B9FF43",
    "fonte única": "#C7A34B",
    "inconsistente": "#F87171",
}
_PROGRESS_QSS = (
    "QProgressBar{background:#0B111A;border:1px solid #273140;border-radius:9px;"
    "min-height:22px;text-align:center;color:#F3F6FF;font-weight:700;padding:0 9px}"
    "QProgressBar::chunk{border-radius:8px;background:qlineargradient("
    "x1:0,y1:0,x2:1,y2:0,stop:0 #37F2FF,stop:0.55 #7C7AFF,stop:1 #FF4FD8)}"
)
_NAV_QSS = (
    "QPushButton#NavButton{background:transparent;border:1px solid #273140;"
    "border-radius:8px;padding:10px 14px;color:#A8B0BC}"
    "QPushButton#NavButton:hover{background:#101722;border-color:#37F2FF;color:#F3F6FF}"
    "QPushButton#NavButton:checked{background:#101B28;border-color:#37F2FF;"
    "color:#FFFFFF;font-weight:700}"
)


def _esc(value: object) -> str:
    return html.escape(str(value or ""))


def _norm(value: object) -> str:
    text = unicodedata.normalize("NFD", str(value or ""))
    return "".join(char for char in text if not unicodedata.combining(char)).lower()


def _label(text: str, object_name: str = "", wrap: bool = True) -> QLabel:
    label = QLabel(text)
    if object_name:
        label.setObjectName(object_name)
    label.setWordWrap(wrap)
    label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    return label


def _pill(text: str) -> QLabel:
    label = _label(text, "StatusPill", False)
    label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
    return label


def _bilingual_title(item: dict) -> str:
    english = str(item.get("en") or "").strip()
    return f"{item['title']} ({english})" if english else str(item["title"])


def _card(name: str = "NeonPanel") -> tuple[QFrame, QVBoxLayout]:
    frame = FuturePanel()
    frame.setObjectName("NeonPanel")
    frame.setProperty("variant", name)
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(18, 16, 18, 16)
    layout.setSpacing(10)
    return frame, layout


def _scroll_page() -> tuple[QScrollArea, QVBoxLayout]:
    body = QWidget()
    body.setObjectName("GuideBody")
    layout = QVBoxLayout(body)
    layout.setContentsMargins(6, 6, 16, 12)
    layout.setSpacing(16)
    scroll = QScrollArea()
    scroll.setObjectName("PageScroll")
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QFrame.Shape.NoFrame)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll.setWidget(body)
    return scroll, layout


class GuidePage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("WitcherGuide")
        self.setStyleSheet(GUIDE_STYLE)
        self._state = load_progress()
        self._done = set(self._state.get("done", []))
        self._image_loader = ImageLoader(self)
        self._boxes: dict[str, list[QCheckBox]] = defaultdict(list)
        self._spoilers: list[tuple[QPushButton, QLabel]] = []
        self._gate_refreshers = []
        self._phase_combos: list[QComboBox] = []
        self._show_all_spoilers = False
        self._nav_buttons: list[QPushButton] = []

        outer = QVBoxLayout(self)
        outer.setContentsMargins(22, 18, 22, 14)
        outer.setSpacing(16)
        self._build_title_and_header()
        self._build_progress()
        self._build_navigation()
        self.top = TopBar(
            self,
            title=self._title_box,
            header=self._header_box,
            progress=self._progress_box,
            nav=self._nav_box,
            bar=self.progress_bar,
            pills=self._progress_pills,
            load_ui=load_ui,
            save_ui=save_ui,
        )
        outer.addWidget(self.top.widget)

        self.stack = QStackedWidget()
        self.stack.addWidget(self._build_now_page())
        self.stack.addWidget(self._build_regions_page())
        self.stack.addWidget(self._build_gwent_page())
        self.stack.addWidget(self._build_trophies_page())
        self.stack.addWidget(self._build_builds_page())
        outer.addWidget(self.stack, 1)
        outer.addWidget(
            InfoCorner(
                f"{guide_data.FOOTER} • progresso salvo em {guide_dir_label()}"
            )
        )
        self._select_section(0)
        self._update_progress()
        app = QApplication.instance()
        if app is not None:
            app.aboutToQuit.connect(self._image_loader.shutdown)

    def closeEvent(self, event):  # noqa: N802
        self._image_loader.shutdown()
        super().closeEvent(event)

    def _build_title_and_header(self) -> None:
        self._title_box = QWidget()
        title_row = QHBoxLayout(self._title_box)
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.addWidget(_label(guide_data.GAME_NAME, "PageTitle", False), 1)

        self._header_box = QWidget()
        header = QVBoxLayout(self._header_box)
        header.setContentsMargins(0, 0, 0, 0)
        header.setSpacing(11)
        header.addWidget(_label(guide_data.INTRO, "Muted"))

        stats = QHBoxLayout()
        stats.setSpacing(8)
        for stat in guide_data.HERO_STATS:
            stats.addWidget(_pill(f"{stat['value']}  {stat['label']}"))
        stats.addStretch(1)
        header.addLayout(stats)

        controls = QHBoxLayout()
        controls.setSpacing(8)
        controls.addWidget(_label("Fase atual", "Kicker", False))
        self.phase_combo = self._new_phase_combo()
        controls.addWidget(self.phase_combo, 1)
        self.spoiler_all_button = QPushButton("Revelar todos os spoilers")
        self.spoiler_all_button.clicked.connect(self._toggle_all_spoilers)
        controls.addWidget(self.spoiler_all_button)
        header.addLayout(controls)

    def _build_progress(self) -> None:
        self._progress_box = QWidget()
        layout = QVBoxLayout(self._progress_box)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(7)
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(_PROGRESS_QSS)
        layout.addWidget(self.progress_bar)
        row = QHBoxLayout()
        row.setSpacing(8)
        self.trophy_pill = _pill("")
        self.safety_pill = _pill("")
        self.gwent_pill = _pill("")
        self._progress_pills = [self.trophy_pill, self.safety_pill, self.gwent_pill]
        for pill in self._progress_pills:
            row.addWidget(pill)
        row.addStretch(1)
        layout.addLayout(row)

    def _build_navigation(self) -> None:
        self._nav_box = QWidget()
        row = QHBoxLayout(self._nav_box)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(7)
        for index, section in enumerate(guide_data.SECTIONS):
            button = QPushButton(section["label"])
            button.setObjectName("NavButton")
            button.setCheckable(True)
            button.clicked.connect(lambda _checked=False, i=index: self._select_section(i))
            self._nav_buttons.append(button)
            row.addWidget(button)
        self._nav_box.setStyleSheet(_NAV_QSS)

    def _select_section(self, index: int) -> None:
        self.stack.setCurrentIndex(index)
        for button_index, button in enumerate(self._nav_buttons):
            button.setChecked(button_index == index)

    def _section_header(self, number: str, title: str, subtitle: str = "") -> QWidget:
        widget = QWidget()
        box = QVBoxLayout(widget)
        box.setContentsMargins(0, 4, 0, 0)
        box.setSpacing(4)
        row = QHBoxLayout()
        row.setSpacing(10)
        number_label = _label(number, "Kicker", False)
        number_label.setStyleSheet("color:#37F2FF;font-family:'Consolas';font-weight:700")
        divider = _label("|", "", False)
        divider.setStyleSheet("color:#FF4FD8;font-size:18px;font-weight:700")
        row.addWidget(number_label)
        row.addWidget(divider)
        row.addWidget(_label(title, "SectionTitle", False))
        row.addStretch(1)
        box.addLayout(row)
        if subtitle:
            box.addWidget(_label(subtitle, "Muted"))
        return widget

    def _new_phase_combo(self) -> QComboBox:
        combo = QComboBox()
        combo.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon
        )
        combo.setMinimumContentsLength(24)
        combo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        for phase in guide_data.PHASES:
            combo.addItem(f"{phase['title']} ({phase['en']})", phase["id"])
        selected = combo.findData(self._state.get("current_phase"))
        combo.setCurrentIndex(max(0, selected))
        combo.currentIndexChanged.connect(
            lambda index, source=combo: self._phase_changed(str(source.itemData(index)))
        )
        self._phase_combos.append(combo)
        return combo

    def _phase_changed(self, phase_id: str) -> None:
        if not phase_id or phase_id == self._state.get("current_phase"):
            return
        self._state["current_phase"] = phase_id
        live_combos = []
        for combo in self._phase_combos:
            try:
                live_combos.append(combo)
                index = combo.findData(phase_id)
                if index >= 0 and combo.currentIndex() != index:
                    combo.blockSignals(True)
                    combo.setCurrentIndex(index)
                    combo.blockSignals(False)
            except RuntimeError:
                continue
        self._phase_combos = live_combos
        self._save_state()
        self._replace_now_page()

    def _advance_phase(self) -> None:
        phase_id = str(self._state.get("current_phase", "white_orchard"))
        index = guide_data.phase_index(phase_id)
        if index + 1 < len(guide_data.PHASES):
            self._phase_changed(guide_data.PHASES[index + 1]["id"])

    def _save_state(self) -> None:
        self._state["done"] = sorted(self._done)
        save_progress(self._state)

    def _replace_now_page(self) -> None:
        if not hasattr(self, "stack") or self.stack.count() == 0:
            return
        old = self.stack.widget(0)
        current = self.stack.currentIndex()
        self.stack.removeWidget(old)
        old.deleteLater()
        self.stack.insertWidget(0, self._build_now_page())
        self._select_section(0 if current == 0 else current)

    def _sync_boxes(self, key: str, checked: bool) -> None:
        live_boxes = []
        for box in self._boxes.get(key, []):
            try:
                live_boxes.append(box)
                if box.isChecked() != checked:
                    box.blockSignals(True)
                    box.setChecked(checked)
                    box.blockSignals(False)
            except RuntimeError:
                continue
        self._boxes[key] = live_boxes

    def _set_done(self, key: str, checked: bool) -> None:
        if checked:
            self._done.add(key)
        else:
            self._done.discard(key)
        self._sync_boxes(key, checked)
        affects_gate = key.startswith("gate:")
        if not checked:
            for gate in guide_data.GATES:
                if key not in gate.get("required", []):
                    continue
                gate_key = progress.gate_key(gate["id"])
                if gate_key in self._done:
                    self._done.discard(gate_key)
                    self._sync_boxes(gate_key, False)
                affects_gate = True
        self._run_refreshers()
        self._save_state()
        self._update_progress()

    def _run_refreshers(self) -> None:
        live_refreshers = []
        for refresh in self._gate_refreshers:
            try:
                refresh()
                live_refreshers.append(refresh)
            except RuntimeError:
                continue
        self._gate_refreshers = live_refreshers
        if affects_gate:
            QTimer.singleShot(0, self._replace_now_page)

    def _reset_checks(self) -> None:
        answer = QMessageBox.question(
            self,
            "Limpar marcações",
            "Deseja desmarcar todos os objetivos, blocos de Gwent, portões e troféus? "
            "A fase atual da história será mantida.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel,
        )
        if answer != QMessageBox.StandardButton.Yes:
            return
        keys = list(self._done)
        self._done.clear()
        for key in keys:
            self._sync_boxes(key, False)
        self._run_refreshers()
        self._save_state()
        self._update_progress()
        self._replace_now_page()

    def _checkbox(self, key: str, text: str) -> QCheckBox:
        box = ChecklistBox(text)
        box.setToolTip(text)
        box.setChecked(key in self._done)
        box.toggled.connect(lambda checked, item_key=key: self._set_done(item_key, checked))
        self._boxes[key].append(box)
        return box

    def _tag(self, text: str) -> QLabel:
        color = _TAG_COLORS.get(text.lower(), "#A8B0BC")
        label = QLabel(text.upper())
        label.setStyleSheet(
            f"color:{color};background:#0A0B12;border:1px solid {color};"
            "border-radius:7px;padding:3px 7px;font-size:10px;font-weight:700;"
        )
        label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        return label

    def _add_spoiler(self, row: QHBoxLayout, layout: QVBoxLayout, text: str) -> None:
        button = QPushButton("SPOILER ▼")
        button.setToolTip("Clique para revelar")
        button.setStyleSheet(
            "QPushButton{color:#C4A7FF;border:1px solid #604D82;padding:3px 8px;"
            "font-size:11px;font-weight:700}"
        )
        button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        spoiler = _label(text, "Muted")
        spoiler.setStyleSheet("background:#11101A;border-left:3px solid #C4A7FF;padding:9px;")
        spoiler.hide()
        button.clicked.connect(lambda: self._toggle_spoiler(button, spoiler))
        row.addWidget(button)
        layout.addWidget(spoiler)
        self._spoilers.append((button, spoiler))

    def _toggle_spoiler(self, button: QPushButton, label: QLabel) -> None:
        visible = label.isHidden()
        label.setVisible(visible)
        button.setText("SPOILER ▲" if visible else "SPOILER ▼")

    def _toggle_all_spoilers(self) -> None:
        self._show_all_spoilers = not self._show_all_spoilers
        live_spoilers = []
        for button, label in self._spoilers:
            try:
                label.setVisible(self._show_all_spoilers)
                button.setText("SPOILER ▲" if self._show_all_spoilers else "SPOILER ▼")
                live_spoilers.append((button, label))
            except RuntimeError:
                continue
        self._spoilers = live_spoilers
        self.spoiler_all_button.setText(
            "Esconder todos os spoilers"
            if self._show_all_spoilers
            else "Revelar todos os spoilers"
        )

    def _item_card(self, item: dict, key: str) -> QFrame:
        frame, layout = _card()
        layout.addWidget(self._checkbox(key, _bilingual_title(item)))
        if item.get("summary"):
            layout.addWidget(_label(item["summary"], "Muted"))
        tags = [tag for tag in item.get("tags", []) if tag != "spoiler"]
        row = QHBoxLayout()
        row.setSpacing(8)
        for tag in tags:
            row.addWidget(self._tag(tag))
        if item.get("spoiler"):
            self._add_spoiler(row, layout, item["spoiler"])
        row.addStretch(1)
        layout.insertLayout(1, row)
        if item.get("detail"):
            detail = _label(item["detail"], "Muted")
            detail.setStyleSheet("color:#D4D9E2")
            detail.hide()
            more = QPushButton("Ver detalhes ▼")
            more.setCheckable(True)
            more.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
            def show_detail(visible: bool) -> None:
                detail.setVisible(visible)
                more.setText("Ocultar detalhes ▲" if visible else "Ver detalhes ▼")
            more.toggled.connect(show_detail)
            layout.addWidget(more)
            layout.addWidget(detail)
        if item["id"] in DETAIL_GUIDES:
            self._add_walkthrough(layout, item["id"])
        return frame

    def _add_walkthrough(self, layout: QVBoxLayout, item_id: str) -> None:
        guide = DETAIL_GUIDES[item_id]
        toggle = QPushButton("Ver mapa e passo a passo ▼")
        toggle.setCheckable(True)
        toggle.setObjectName("PrimaryButton")
        toggle.setProperty("walkthrough", item_id)
        content = QWidget()
        content.setObjectName("GuideBody")
        body = QVBoxLayout(content)
        body.setContentsMargins(0, 12, 0, 0)
        body.setSpacing(12)
        body.addWidget(_label(guide["title"], "SectionTitle"))
        if guide.get("intro"):
            body.addWidget(_label(guide["intro"], "Muted"))
        self._add_diagram(body, guide["visual"], guide["title"], 530)
        # Um passo pode ser texto puro ou um dicionario com foto do local. A foto
        # e o que responde "onde fica", que o esquema sozinho nao resolvia.
        number = 0
        for step in guide["steps"]:
            if isinstance(step, dict) and step.get("heading"):
                body.addWidget(_label(step["heading"], "Kicker"))
                number = 0
                continue
            if isinstance(step, dict):
                number += 1
                body.addWidget(_label(f"{number}. {step['text']}", "Muted"))
                if step.get("image"):
                    # Sem fallback: repetir o esquema inteiro embaixo de cada
                    # passo polui mais do que ajuda. Enquanto a foto nao chega,
                    # o widget fica vazio e discreto.
                    body.addWidget(
                        self._image_widget(
                            step["image"], step["text"][:60], 760, 430, ""
                        )
                    )
            else:
                body.addWidget(_label(step, "Muted"))
        if guide.get("map_url"):
            map_button = QPushButton("Carregar mapa do jogo com as marcações")
            map_button.setCheckable(True)
            map_box = QWidget()
            map_box.setObjectName("GuideBody")
            map_layout = QVBoxLayout(map_box)
            map_layout.setContentsMargins(0, 0, 0, 0)
            map_box.hide()
            loaded = [False]

            def show_map(visible):
                if visible and not loaded[0]:
                    map_layout.addWidget(self._image_widget(guide["map_url"], guide["credit"], 1200, 900, guide["visual"]))
                    credit = _label(f'<a href="{guide["source"]}" style="color:#37F2FF">{guide["credit"]}</a>')
                    credit.setOpenExternalLinks(True)
                    map_layout.addWidget(credit)
                    loaded[0] = True
                map_box.setVisible(visible)

            map_button.toggled.connect(show_map)
            body.addWidget(map_button)
            body.addWidget(map_box)
        content.hide()

        def show_content(visible):
            content.setVisible(visible)
            toggle.setText("Recolher mapa e passo a passo ▲" if visible else "Ver mapa e passo a passo ▼")

        toggle.toggled.connect(show_content)
        layout.addWidget(toggle)
        layout.addWidget(content)

    def _vendor_card(self, item: dict) -> QFrame:
        frame, layout = _card()
        layout.addWidget(
            self._checkbox(
                progress.vendor_key(item["id"]),
                f"{item['title']} ({item['en']})",
            )
        )
        layout.addWidget(
            _label("Abra a loja e compre todas as cartas disponíveis.", "Muted")
        )
        cards = _label(
            "Cartas de referência: " + ", ".join(item["cards"]) + ".",
            "Muted",
        )
        cards.hide()
        toggle = QPushButton(f"Ver cartas desta loja ({len(item['cards'])}) ▼")
        toggle.setCheckable(True)
        toggle.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        def show_cards(visible: bool) -> None:
            cards.setVisible(visible)
            toggle.setText(
                f"Ocultar cartas ({len(item['cards'])}) ▲" if visible
                else f"Ver cartas desta loja ({len(item['cards'])}) ▼"
            )

        toggle.toggled.connect(show_cards)
        layout.addWidget(toggle)
        layout.addWidget(cards)
        return frame

    def _image_widget(
        self, url: str, caption: str, max_w: int = 1040, max_h: int = 260,
        fallback_file: str = "cover-fallback.svg",
    ) -> QLabel:
        holder = GuideImage(max_h)
        if not url:
            return holder
        holder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        holder.setStyleSheet(
            "background:#080B11;border:1px solid #273140;border-radius:10px;padding:8px"
        )
        fallback = QPixmap(str(Path(__file__).resolve().parent / "assets" / fallback_file))
        if not fallback.isNull():
            holder.setText("")
            holder.set_source(fallback)
            holder.setToolTip("Ilustração local exibida até a imagem oficial carregar")
        state = {"loaded": False}

        def show(pixmap: QPixmap) -> None:
            state["loaded"] = True
            holder.setText("")
            holder.set_source(pixmap)
            holder.setToolTip(caption)

        cached = self._image_loader.load(url, show)
        if cached is not None:
            show(cached)
            return holder

        def unavailable() -> None:
            if not state["loaded"] and fallback.isNull():
                holder.setText(
                    f'Imagem indisponível sem conexão. <a href="{_esc(url)}" '
                    f'style="color:{guide_data.ACCENT}">Abrir a fonte oficial</a>'
                )
                holder.setOpenExternalLinks(True)

        QTimer.singleShot(8000, unavailable)
        return holder

    def _add_image(self, layout: QVBoxLayout, url: str, caption: str) -> None:
        layout.addWidget(self._image_widget(url, caption))

    def _add_diagram(self, layout: QVBoxLayout, filename: str, caption: str, height: int = 220) -> None:
        path = Path(__file__).resolve().parent / "assets" / filename
        pixmap = QPixmap(str(path))
        holder = GuideImage(height)
        holder.setAccessibleName(caption)
        if not pixmap.isNull():
            holder.set_source(pixmap)
            holder.setToolTip(caption)
        layout.addWidget(holder)

    def _skippable_card(self, text: str) -> QFrame:
        frame, layout = _card()
        row = QHBoxLayout()
        row.addWidget(self._tag("pode ignorar"))
        row.addStretch(1)
        layout.addLayout(row)
        layout.addWidget(_label(text, "Muted"))
        return frame

    def _build_now_page(self) -> QWidget:
        scroll, layout = _scroll_page()
        phase_id = str(self._state.get("current_phase", "white_orchard"))
        phase = next(item for item in guide_data.PHASES if item["id"] == phase_id)
        current_index = guide_data.phase_index(phase_id)

        intro, intro_layout = _card("HeroPanel")
        hero_widget = ResponsiveHero()
        hero = hero_widget.row
        copy = QVBoxLayout()
        copy.setSpacing(9)
        eyebrow = _label(
            f"FASE {current_index + 1:02d} DE {len(guide_data.PHASES):02d}", "", False
        )
        eyebrow.setStyleSheet(
            "color:#37F2FF;font-family:'Consolas';font-size:11px;font-weight:700"
        )
        copy.addWidget(eyebrow)
        copy.addWidget(_label(phase["title"], "CardTitle"))
        copy.addWidget(_label(f"{phase['en']}  •  {phase['summary']}", "Muted"))
        copy.addSpacing(4)
        copy.addWidget(_label("Onde você está na história", "SectionTitle"))
        copy.addWidget(self._new_phase_combo())
        actions = QHBoxLayout()
        actions.setSpacing(8)
        next_button = QPushButton("Avancei na história")
        next_button.setObjectName("PrimaryButton")
        next_button.setEnabled(current_index + 1 < len(guide_data.PHASES))
        if current_index + 1 == len(guide_data.PHASES):
            next_button.setText("Última fase da campanha")
        next_button.clicked.connect(self._advance_phase)
        reset_button = QPushButton("Limpar marcações")
        reset_button.setToolTip("Desmarcar todo o progresso sem alterar a fase atual")
        reset_button.clicked.connect(self._reset_checks)
        actions.addWidget(next_button)
        actions.addWidget(reset_button)
        actions.addStretch(1)
        copy.addLayout(actions)
        copy.addWidget(
            _label(
                "As caixas registram o que foi feito. A fase só muda quando você escolher "
                "uma nova etapa ou usar o botão de avanço.",
                "Muted",
            )
        )
        hero.addLayout(copy, 3)
        image = self._image_widget(
            guide_data.SECTION_IMAGES["now"],
            "Imagem oficial de The Witcher 3: Wild Hunt Remastered",
            430,
            210,
        )
        hero.addWidget(image, 2)
        intro_layout.addWidget(hero_widget)
        layout.addWidget(intro)

        relevant_gates = [
            gate for gate in guide_data.GATES
            if guide_data.phase_index(gate["phase"]) <= current_index
        ]
        # Um portao so avisa se avisar ANTES. Estes sao os das fases seguintes
        # que ainda estao abertos; aparecem num bloco proprio, sem caixa de
        # auditoria, so para o jogador saber o que vem pela frente.
        upcoming_gates = [
            gate for gate in guide_data.GATES
            if guide_data.phase_index(gate["phase"]) > current_index
            and progress.gate_key(gate["id"]) not in self._done
        ]
        pending_gates = [
            gate for gate in relevant_gates
            if progress.gate_key(gate["id"]) not in self._done and gate["phase"] == phase_id
        ]
        previous_gates = [
            gate for gate in relevant_gates
            if progress.gate_key(gate["id"]) not in self._done and gate["phase"] != phase_id
        ]
        completed_gates = [
            gate for gate in relevant_gates
            if progress.gate_key(gate["id"]) in self._done
        ]
        if pending_gates:
            layout.addWidget(
                self._section_header(
                    "01", "Alertas antes de continuar",
                    "Confira estes riscos antes de avançar na campanha.",
                )
            )
            for gate in pending_gates:
                layout.addWidget(self._gate_card(gate, completed=False))

        if upcoming_gates:
            nearest = upcoming_gates[0]
            phase_title = guide_data.phase_title(nearest["phase"])
            toggle = QPushButton(
                f"Vem por aí: {len(upcoming_gates)} ponto(s) sem volta, o próximo em {phase_title} ▼"
            )
            toggle.setCheckable(True)
            toggle.setObjectName("HistoryToggle")
            upcoming_box = QWidget()
            upcoming_box.setObjectName("GuideBody")
            upcoming_layout = QVBoxLayout(upcoming_box)
            upcoming_layout.setContentsMargins(0, 12, 0, 0)
            upcoming_layout.setSpacing(12)
            for gate in upcoming_gates:
                upcoming_layout.addWidget(self._gate_preview(gate))
            upcoming_box.hide()

            def show_upcoming(visible: bool) -> None:
                upcoming_box.setVisible(visible)
                toggle.setText(
                    f"Ocultar o que vem por aí ▲"
                    if visible
                    else f"Vem por aí: {len(upcoming_gates)} ponto(s) sem volta, o próximo em {phase_title} ▼"
                )

            toggle.toggled.connect(show_upcoming)
            layout.addWidget(toggle)
            layout.addWidget(upcoming_box)

        if previous_gates:
            toggle = QPushButton(f"Revisar {len(previous_gates)} alerta(s) de fases anteriores ▼")
            toggle.setObjectName("HistoryToggle")
            toggle.setCheckable(True)
            history = QWidget()
            history.setObjectName("GuideBody")
            history_layout = QVBoxLayout(history)
            history_layout.setContentsMargins(0, 0, 0, 0)
            history_layout.addWidget(_label(
                "Avançar a fase não conclui objetivos. Confira o que realmente fez no jogo. "
                "Se algum prazo já passou, consulte o item antes de considerar a platina segura.", "Muted"))
            for gate in previous_gates:
                history_layout.addWidget(self._gate_card(gate))
            history.hide()
            toggle.toggled.connect(history.setVisible)
            layout.addWidget(toggle)
            layout.addWidget(history)

        current_tasks = [
            item for item in guide_data.TASKS if item["phase"] == phase_id
        ]
        current_gwent = [
            item for item in guide_data.GWENT_TASKS if item["region"] == phase_id
        ]
        current_vendors = [
            item for item in gwent_catalog.VENDORS if item["region"] == phase_id
        ]

        layout.addWidget(
            self._section_header(
                "02" if pending_gates else "01", "Nesta fase",
                "Marque o que já fez. É aqui que os objetivos são marcados; a aba Regiões só mostra o que existe em cada lugar.",
            )
        )
        if current_tasks or current_gwent or current_vendors:
            required_tasks = [
                item for item in current_tasks if "necessária" in item.get("tags", [])
            ]
            useful_tasks = [
                item for item in current_tasks if "necessária" not in item.get("tags", [])
            ]
            if required_tasks:
                layout.addWidget(_label("OBJETIVOS", "Kicker"))
                for item in required_tasks:
                    layout.addWidget(self._item_card(item, progress.task_key(item["id"])))
            if current_gwent:
                layout.addWidget(_label("GWENT", "Kicker"))
                for item in current_gwent:
                    layout.addWidget(self._item_card(item, progress.gwent_key(item["id"])))
            if current_vendors:
                layout.addWidget(_label("CARTAS À VENDA", "Kicker"))
                for item in current_vendors:
                    layout.addWidget(self._vendor_card(item))
            if useful_tasks:
                layout.addWidget(_label("OPCIONAL E ÚTIL", "Kicker"))
                for item in useful_tasks:
                    layout.addWidget(self._item_card(item, progress.task_key(item["id"])))
        else:
            quiet, quiet_layout = _card()
            quiet_layout.addWidget(_label("Sem objetivos locais nesta fase", "SectionTitle"))
            quiet_layout.addWidget(
                _label("Confira os alertas abaixo e continue a campanha no seu ritmo.", "Muted")
            )
            layout.addWidget(quiet)

        selected_build = next(
            (item for item in guide_data.BUILDS
             if item["id"] == self._state.get("build_style")),
            None,
        )
        if selected_build:
            build_card, build_layout = _card("ActiveBuildPanel")
            build_layout.addWidget(
                _label(f"ESTILO ATIVO · {selected_build['title']}", "Kicker")
            )
            build_layout.addWidget(
                _label("Na Marcha da Morte: " + selected_build["priorities"][0], "Muted")
            )
            layout.addWidget(build_card)

        if completed_gates:
            toggle = QPushButton(f"Revisar concluídos ({len(completed_gates)})  ▼")
            toggle.setCheckable(True)
            completed_box = QWidget()
            completed_layout = QVBoxLayout(completed_box)
            completed_layout.setContentsMargins(0, 0, 0, 0)
            completed_layout.setSpacing(12)
            for gate in completed_gates:
                completed_layout.addWidget(self._gate_card(gate, completed=True))
            completed_box.hide()

            def toggle_completed(visible: bool) -> None:
                completed_box.setVisible(visible)
                toggle.setText(
                    f"Ocultar concluídos ({len(completed_gates)})  ▲"
                    if visible
                    else f"Revisar concluídos ({len(completed_gates)})  ▼"
                )

            toggle.toggled.connect(toggle_completed)
            layout.addWidget(toggle)
            layout.addWidget(completed_box)

        deadline_tasks = [
            item
            for item in guide_data.TASKS
            if item.get("deadline")
            and item["phase"] != phase_id
            and current_index <= guide_data.phase_index(item["deadline"]) <= current_index + 1
            and progress.task_key(item["id"]) not in self._done
        ]
        if deadline_tasks:
            layout.addWidget(
                self._section_header(
                    "03" if pending_gates else "02",
                    "Prazos próximos",
                    "Estas pendências se aproximam do ponto em que podem ser perdidas.",
                )
            )
            for item in deadline_tasks:
                layout.addWidget(self._item_card(item, progress.task_key(item["id"])))
        layout.addStretch(1)
        return scroll

    def _gate_preview(self, gate: dict) -> QFrame:
        """O portao de uma fase futura: so leitura, para planejar a ida."""
        frame, layout = _card()
        header = QHBoxLayout()
        header.setSpacing(10)
        header.addWidget(_label(gate["title"], "SectionTitle"), 1)
        badge = _pill(guide_data.phase_title(gate["phase"]))
        header.addWidget(badge)
        layout.addLayout(header)
        layout.addWidget(_label(gate["summary"], "Muted"))
        for entry in gate.get("fails") or []:
            line = _label(f"• {entry}", "Muted")
            line.setStyleSheet("color:#FF8FA3")
            layout.addWidget(line)
        if gate.get("safe"):
            hint = _label(gate["safe"], "Muted")
            hint.setStyleSheet(
                "color:#C7D0DD;background:#11161F;border-left:3px solid #37F2FF;"
                "border-radius:8px;padding:9px 11px"
            )
            layout.addWidget(hint)
        return frame

    def _gate_card(self, gate: dict, completed: bool = False) -> QFrame:
        frame, layout = _card()
        header = QHBoxLayout()
        header.setSpacing(10)
        header.addWidget(_label(gate["title"], "SectionTitle"), 1)
        status = _pill("CONCLUÍDO" if completed else "PENDENTE")
        status.setStyleSheet(
            "color:#B9FF43;background:#0A0B12;border:1px solid #B9FF43;"
            "border-radius:8px;padding:5px 9px;font-size:10px;font-weight:700"
            if completed
            else "color:#C7A34B;background:#0A0B12;border:1px solid #C7A34B;"
            "border-radius:8px;padding:5px 9px;font-size:10px;font-weight:700"
        )
        header.addWidget(status)
        layout.addLayout(header)
        layout.addWidget(_label(gate["summary"], "Muted"))

        # O que morre neste ponto. Fica sempre visivel, nunca atras de um
        # "ver detalhes": e a informacao que impede o jogador de perder a run.
        fails = gate.get("fails") or []
        if fails:
            layout.addWidget(_label("O QUE SOME SE VOCÊ AVANÇAR", "Kicker"))
            for entry in fails:
                line = _label(f"• {entry}", "Muted")
                line.setStyleSheet("color:#FF8FA3")
                layout.addWidget(line)
        if gate.get("safe"):
            hint = _label(gate["safe"], "Muted")
            hint.setStyleSheet(
                "color:#C7D0DD;background:#11161F;border-left:3px solid #37F2FF;"
                "border-radius:8px;padding:9px 11px"
            )
            layout.addWidget(hint)

        requirement_boxes = []
        for required_key in gate.get("required", []):
            item = guide_data.item_by_key(required_key)
            if item is None:
                continue
            box = self._checkbox(required_key, _bilingual_title(item))
            requirement_boxes.append(box)
            layout.addWidget(box)
        audit = self._checkbox(progress.gate_key(gate["id"]), "Auditoria concluída, é seguro avançar")

        def refresh_audit() -> None:
            pending = sum(1 for box in requirement_boxes if not box.isChecked())
            audit.setEnabled(pending == 0)
            audit.setToolTip(
                "" if pending == 0 else f"Ainda existem {pending} pendência(s) neste portão."
            )

        for box in requirement_boxes:
            box.toggled.connect(refresh_audit)
        self._gate_refreshers.append(refresh_audit)
        refresh_audit()
        layout.addWidget(audit)
        return frame

    def _open_phase(self, phase_id: str) -> None:
        """Leva da aba Regioes para a fase certa da aba Agora."""
        self._phase_changed(phase_id)
        self._select_section(0)

    def _region_tasks_card(self, tasks: list[dict]) -> QFrame:
        """Os objetivos da regiao, so para leitura. Quem marca e a aba Agora.

        Antes o mesmo card aparecia nas duas abas e parecia repeticao. Aqui fica
        uma linha por objetivo, com o estado e o atalho para a fase dele.
        """
        frame, layout = _card()
        layout.addWidget(_label(f"Objetivos desta região ({len(tasks)})", "SectionTitle"))
        layout.addWidget(
            _label(
                "Você marca cada um na aba Agora, na fase em que ele acontece. "
                "O botão leva direto para lá.",
                "Muted",
            )
        )
        for task in tasks:
            row = QHBoxLayout()
            row.setSpacing(10)
            status = QLabel()
            status.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
            row.addWidget(status)
            row.addWidget(_label(_bilingual_title(task)), 1)
            jump = QPushButton(f"Abrir em Agora: {guide_data.phase_title(task['phase'])}")
            jump.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
            jump.clicked.connect(
                lambda _checked=False, phase=task["phase"]: self._open_phase(phase)
            )
            row.addWidget(jump)
            layout.addLayout(row)
            key = progress.task_key(task["id"])

            def refresh(label: QLabel = status, item_key: str = key) -> None:
                done = item_key in self._done
                color = "#B9FF43" if done else "#C7A34B"
                label.setText("FEITO" if done else "PENDENTE")
                label.setStyleSheet(
                    f"color:{color};background:#0A0B12;border:1px solid {color};"
                    "border-radius:7px;padding:3px 7px;font-size:10px;font-weight:700"
                )

            refresh()
            # A mesma lista que os portoes usam: roda a cada marcacao, em
            # qualquer aba, e descarta sozinha os rotulos que ja morreram.
            self._gate_refreshers.append(refresh)
        return frame

    def _region_power_card(self, stones: list[dict]) -> QFrame:
        """Os Locais de Poder da regiao, com foto, carregados so ao abrir."""
        frame, layout = _card()
        toggle = QPushButton(f"Locais de Poder nesta região ({len(stones)}) ▼")
        toggle.setCheckable(True)
        toggle.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        body = QWidget()
        body.setObjectName("GuideBody")
        body_layout = QVBoxLayout(body)
        body_layout.setContentsMargins(0, 8, 0, 0)
        body_layout.setSpacing(12)
        body.hide()
        built = [False]

        def show(visible: bool) -> None:
            if visible and not built[0]:
                built[0] = True
                body_layout.addWidget(
                    _label(
                        "Cada pedra vale um ponto de habilidade. Limpe os inimigos em "
                        "volta antes de absorver.",
                        "Muted",
                    )
                )
                for number, stone in enumerate(stones, 1):
                    body_layout.addWidget(_label(f"{number}. {stone['text']}", "Muted"))
                    body_layout.addWidget(
                        self._image_widget(stone["image"], stone["text"][:60], 760, 430, "")
                    )
            body.setVisible(visible)
            toggle.setText(
                f"Ocultar Locais de Poder ({len(stones)}) ▲" if visible
                else f"Locais de Poder nesta região ({len(stones)}) ▼"
            )

        toggle.toggled.connect(show)
        layout.addWidget(toggle)
        layout.addWidget(body)
        return frame

    def _build_regions_page(self) -> QWidget:
        scroll, layout = _scroll_page()
        self._add_diagram(layout, "safety-route.svg", "Rota de segurança da platina")
        intro, intro_layout = _card()
        intro_layout.addWidget(_label("O que existe em cada região", "SectionTitle"))
        intro_layout.addWidget(
            _label(
                "Esta aba é o mapa: contratos, Locais de Poder com foto e o que dá para "
                "ignorar. O que fazer agora e o que não pode perder fica na aba Agora.",
                "Muted",
            )
        )
        layout.addWidget(intro)
        root_layout = layout
        picker = QComboBox()
        picker.setAccessibleName("Filtrar por região")
        picker.addItem("Todas as regiões", "")
        root_layout.addWidget(picker)
        groups = []
        tasks_by_region: dict[str, list[dict]] = defaultdict(list)
        for task in guide_data.TASKS:
            tasks_by_region[task["region"]].append(task)
        stones_by_region = power_stones_by_region()
        for region in guide_data.REGIONS:
            tasks = tasks_by_region.get(region["id"], [])
            contracts = [
                item for item in guide_data.CONTRACTS if item["region"] == region["id"]
            ]
            stones = stones_by_region.get(region["id"], [])
            if not tasks and not contracts and not stones:
                continue
            group = QWidget()
            group.setObjectName("GuideBody")
            layout = QVBoxLayout(group)
            layout.setContentsMargins(0, 8, 0, 0)
            layout.setSpacing(16)
            root_layout.addWidget(group)
            groups.append((region["id"], group))
            picker.addItem(f"{region['title']} ({region['en']})", region["id"])
            layout.addWidget(_label(f"{region['title']} ({region['en']})", "SectionTitle"))
            if contracts:
                contract_card, contract_layout = _card()
                contract_layout.addWidget(
                    _label(
                        f"Contratos para Geralt: bruxo profissional ({len(contracts)} nesta região)",
                        "SectionTitle",
                    )
                )
                contract_layout.addWidget(
                    _label(
                        "Marque os contratos concluídos. Os nomes em inglês identificam cada "
                        "missão; o nome no diário pode variar conforme a edição.",
                        "Muted",
                    )
                )
                for item in contracts:
                    contract_layout.addWidget(
                        self._checkbox(
                            progress.contract_key(item["id"]),
                            f"Contrato: {item['en']}",
                        )
                    )
                    contract_layout.addWidget(_label("Onde começar: " + CONTRACT_STARTS[item["id"]], "Muted"))
                layout.addWidget(contract_card)
            if stones:
                layout.addWidget(self._region_power_card(stones))
            if tasks:
                layout.addWidget(self._region_tasks_card(tasks))
            skippable = guide_data.SKIPPABLE_BY_REGION.get(region["id"])
            if skippable:
                layout.addWidget(self._skippable_card(skippable))
        picker.currentIndexChanged.connect(lambda _: [group.setVisible(not picker.currentData() or region_id == picker.currentData()) for region_id, group in groups])
        root_layout.addStretch(1)
        return scroll

    def _build_gwent_page(self) -> QWidget:
        scroll, layout = _scroll_page()
        self._add_diagram(layout, "gwent-route.svg", "Fontes da coleção de Gwent")
        notice, notice_layout = _card()
        notice_layout.addWidget(_label("Regra simples para não perder cartas", "SectionTitle"))
        notice_layout.addWidget(
            _label(
                "Compre cartas sempre que um comerciante vender, jogue contra cada adversário "
                "novo e conclua torneios e missões assim que aparecerem. Use o Guia Milagroso "
                "de Gwent para conferir a quantidade restante.",
                "Muted",
            )
        )
        notice_layout.addWidget(_label("Se você nunca jogou Gwent", "SectionTitle"))
        for index, tip in enumerate(guide_data.GWENT_PRIMER, 1):
            notice_layout.addWidget(_label(f"{index}. {tip}", "Muted"))
        layout.addWidget(notice)

        # Perdeu a primeira chance? Estas ainda têm resgate. As sete sem resgate
        # ficam nos portões, porque lá o aviso chega antes do corte.
        rescue, rescue_box = _card()
        rescue_box.addWidget(_label("Perdeu a carta? Estas ainda dá para recuperar", "SectionTitle"))
        rescue_box.addWidget(
            _label(
                "Sete cartas do jogo base não têm segunda chance e estão nos alertas da "
                "aba Agora. As de baixo têm. Mesmo assim, ganhe na primeira oportunidade: "
                "onde a fonte é única ou os relatos divergem, o resgate é sorte, não plano.",
                "Muted",
            )
        )
        for entry in gwent_catalog.GWENT_FALLBACKS:
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(_label(f"<b>{_esc(entry['card'])}</b>"), 1)
            head.addWidget(self._tag(entry["confianca"]))
            rescue_box.addLayout(head)
            rescue_box.addWidget(_label(f"Ganhe assim: {entry['win']}", "Muted"))
            rescue_box.addWidget(_label(f"Prazo: {entry['deadline']}", "Muted"))
            where = _label(f"Se perdeu: {entry['fallback']}", "Muted")
            where.setStyleSheet(
                "color:#C7D0DD;background:#11161F;border-left:3px solid #37F2FF;"
                "border-radius:8px;padding:8px 10px"
            )
            rescue_box.addWidget(where)
        layout.addWidget(rescue)
        root_layout = layout
        picker = QComboBox()
        picker.setAccessibleName("Filtrar Gwent por região")
        picker.addItem("Todas as regiões e objetivos globais", "")
        root_layout.addWidget(picker)
        groups = []
        items_by_region: dict[str, list[dict]] = defaultdict(list)
        for item in guide_data.GWENT_TASKS:
            items_by_region[item["region"]].append(item)
        for region in guide_data.REGIONS:
            items = items_by_region.get(region["id"], [])
            vendors = [
                item for item in gwent_catalog.VENDORS if item["region"] == region["id"]
            ]
            if not items and not vendors:
                continue
            group = QWidget()
            group.setObjectName("GuideBody")
            layout = QVBoxLayout(group)
            layout.setContentsMargins(0, 8, 0, 0)
            layout.setSpacing(16)
            root_layout.addWidget(group)
            groups.append((region["id"], group))
            picker.addItem(f"{region['title']} ({region['en']})", region["id"])
            layout.addWidget(_label(f"{region['title']} ({region['en']})", "SectionTitle"))
            for item in items:
                layout.addWidget(self._item_card(item, progress.gwent_key(item["id"])))
            if vendors:
                layout.addWidget(_label("VENDEDORES DE CARTAS", "Kicker"))
                for item in vendors:
                    layout.addWidget(self._vendor_card(item))
        picker.currentIndexChanged.connect(lambda _: [group.setVisible(not picker.currentData() or region_id == picker.currentData()) for region_id, group in groups])
        root_layout.addStretch(1)
        return scroll

    def _build_trophies_page(self) -> QWidget:
        page = QWidget()
        outer = QVBoxLayout(page)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(10)
        controls = QHBoxLayout()
        self.trophy_search = QLineEdit()
        self.trophy_search.setPlaceholderText("Buscar troféu, categoria ou condição...")
        self.trophy_filter = QComboBox()
        self.trophy_filter.addItem("Todas as categorias", "")
        for category in sorted({item["category"] for item in trophies.TROPHIES}):
            self.trophy_filter.addItem(category.title(), category)
        controls.addWidget(self.trophy_search, 1)
        controls.addWidget(self.trophy_filter)
        outer.addLayout(controls)

        image_box = QVBoxLayout()
        self._add_image(
            image_box,
            guide_data.SECTION_IMAGES["trophies"],
            "Imagem oficial de The Witcher 3",
        )
        outer.addLayout(image_box)

        scroll, list_layout = _scroll_page()
        self._trophy_rows: list[tuple[QWidget, str, str]] = []
        for item in trophies.TROPHIES:
            frame, layout = _card()
            title = f"{item['pt']} ({item['en']})"
            layout.addWidget(self._checkbox(progress.trophy_key(item["id"]), title))
            tags = QHBoxLayout()
            tier = QLabel(item["tier"].upper())
            tier.setStyleSheet(
                f"color:{_TIER_COLORS[item['tier']]};font-size:11px;font-weight:700;"
            )
            tags.addWidget(tier)
            tags.addWidget(self._tag(item["category"]))
            if item.get("missable"):
                tags.addWidget(self._tag("perdível"))
            tags.addStretch(1)
            layout.addLayout(tags)
            layout.addWidget(_label(item["description"], "Muted"))
            tip = trophies.TROPHY_TIPS[item["id"]]
            layout.addWidget(_label(f"<b>Como obter:</b> {_esc(tip)}"))
            visual_id = {"power_overwhelming": "white_orchard_power", "pest_control": "skellige_nests", "armed_dangerous": "witcher_gear_set"}.get(item["id"])
            if visual_id:
                self._add_walkthrough(layout, visual_id)
            haystack = _norm(f"{title} {item['description']} {item['category']} {tip}")
            self._trophy_rows.append((frame, haystack, item["category"]))
            list_layout.addWidget(frame)
        list_layout.addStretch(1)
        outer.addWidget(scroll, 1)
        self.trophy_search.textChanged.connect(self._filter_trophies)
        self.trophy_filter.currentIndexChanged.connect(self._filter_trophies)
        return page

    def _filter_trophies(self) -> None:
        query = _norm(self.trophy_search.text())
        category = str(self.trophy_filter.currentData())
        for widget, haystack, item_category in self._trophy_rows:
            widget.setVisible(query in haystack and (not category or category == item_category))

    def _build_builds_page(self) -> QWidget:
        scroll, layout = _scroll_page()
        self._add_image(
            layout,
            guide_data.SECTION_IMAGES["builds"],
            "Imagem oficial do sistema de habilidades Remastered",
        )
        warning, warning_layout = _card()
        warning_layout.addWidget(_label("Escolha seu estilo para Marcha da Morte", "SectionTitle"))
        warning_layout.addWidget(
            _label(
                "Clique em Usar este estilo para salvar uma preferência. Ela aparecerá na aba Agora. "
                "Isso não muda o jogo nem marca troféus. Você pode trocar de estilo a qualquer momento.",
                "Muted",
            )
        )
        layout.addWidget(warning)

        # O jogador chega aqui vindo de guia escrito para a versao antiga, entao
        # a primeira coisa da aba e o que o patch 5.0 mudou.
        changes, changes_box = _card()
        changes_box.addWidget(_label("O que o Remastered mudou", "SectionTitle"))
        changes_box.addWidget(_label(guide_data.REMASTER_OPEN, "Muted"))
        for change in guide_data.REMASTER_CHANGES:
            changes_box.addWidget(_label(f"<b>{_esc(change['title'])}</b>"))
            changes_box.addWidget(_label(change["detail"], "Muted"))
            impact = _label(change["impact"], "Muted")
            impact.setStyleSheet(
                "color:#C7D0DD;background:#11161F;border-left:3px solid #37F2FF;"
                "border-radius:8px;padding:8px 10px"
            )
            changes_box.addWidget(impact)
        layout.addWidget(changes)

        for build in guide_data.BUILDS:
            layout.addWidget(self._build_card(build))
        layout.addStretch(1)
        return scroll

    def _build_card(self, build: dict) -> QFrame:
        selected = self._state.get("build_style") == build["id"]
        frame, box = _card("ActiveBuildPanel" if selected else "NeonPanel")
        heading = QHBoxLayout()
        heading.setSpacing(8)
        heading.addWidget(_label(build["title"], "SectionTitle"), 1)
        heading.addWidget(self._tag(build["confidence"]))
        if selected:
            heading.addWidget(self._tag("selecionado"))
        box.addLayout(heading)
        box.addWidget(_label(build["best_for"], "Muted"))

        box.addWidget(_label("COMO JOGAR NA MARCHA DA MORTE", "Kicker"))
        box.addWidget(_label("<br>".join(f"• {_esc(value)}" for value in build["priorities"])))
        box.addWidget(_label(build["note"], "Muted"))

        box.addWidget(_label("EQUIPAMENTO", "Kicker"))
        box.addWidget(_label(f"<b>Armadura:</b> {_esc(build['set'])}"))
        box.addWidget(_label(f"<b>Mutagênicos:</b> {_esc(build['mutagens'])}"))
        box.addWidget(_label(f"<b>Mutação:</b> {_esc(build['mutation'])}", "Muted"))

        # As 12 equipadas, por arvore, com o nome que aparece na tela do jogo.
        box.addWidget(_label("AS 12 HABILIDADES PARA DEIXAR EQUIPADAS", "Kicker"))
        by_tree: dict[str, list[str]] = defaultdict(list)
        for name in build["equip"]:
            by_tree[skill_tree.tree_of(name)].append(name)
        for tree in skill_tree.TREE_ORDER:
            if by_tree.get(tree):
                box.addWidget(_label(f"<b>{tree}:</b> {_esc(', '.join(by_tree[tree]))}"))

        # O caminho: sai da arvore, nao de uma lista escrita a mao.
        path = skill_tree.unlock_order(build["equip"])
        equipped = set(build["equip"])
        toggle = QPushButton(f"Ver a ordem de compra ({len(path)} habilidades) ▼")
        toggle.setCheckable(True)
        toggle.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        lines = []
        for number, name in enumerate(path, 1):
            links = skill_tree.links_of(name)
            suffix = f" · pede {', '.join(links)}" if links else " · livre desde o começo"
            mark = "<b>EQUIPAR</b> " if name in equipped else ""
            lines.append(
                f"{number}. {mark}{_esc(name)} <span style='color:#7D8796'>"
                f"({skill_tree.tree_of(name)}{_esc(suffix)})</span>"
            )
        order = _label(
            "Pior caso, contando que o jogo peça todas as ligações. Se a tela já liberar "
            "uma habilidade antes, pule o que faltar. Os níveis 2 e 3 custam pontos a "
            "mais: dê prioridade às marcadas como EQUIPAR.<br><br>" + "<br>".join(lines)
        )
        order.hide()

        def show_order(visible: bool) -> None:
            order.setVisible(visible)
            toggle.setText(
                f"Ocultar a ordem de compra ▲" if visible
                else f"Ver a ordem de compra ({len(path)} habilidades) ▼"
            )

        toggle.toggled.connect(show_order)
        box.addWidget(toggle)
        box.addWidget(order)

        button = QPushButton("Estilo ativo" if selected else "Usar este estilo")
        button.setObjectName("PrimaryButton" if selected else "")
        button.setEnabled(not selected)
        button.clicked.connect(lambda _checked=False, item=build: self._choose_build(item))
        box.addWidget(button)
        return frame

    def _choose_build(self, build: dict) -> None:
        self._state["build_style"] = build["id"]
        self._save_state()
        self._replace_now_page()
        old = self.stack.widget(4)
        self.stack.removeWidget(old)
        old.deleteLater()
        self.stack.insertWidget(4, self._build_builds_page())
        self._select_section(4)

    def _update_progress(self) -> None:
        trophy_keys = progress.trophy_keys()
        task_keys = progress.task_keys()
        gwent_keys = progress.gwent_keys()
        contract_keys = progress.contract_keys()
        vendor_keys = progress.vendor_keys()
        tracked = trophy_keys + task_keys + gwent_keys + contract_keys + vendor_keys
        complete = sum(1 for key in tracked if key in self._done)
        self.progress_bar.setRange(0, max(1, len(tracked)))
        self.progress_bar.setValue(complete)
        self.progress_bar.setFormat(f"{complete}/{len(tracked)} itens acompanhados")
        trophy_done = sum(1 for key in trophy_keys if key in self._done)
        task_done = sum(1 for key in task_keys if key in self._done)
        gwent_done = sum(1 for key in gwent_keys if key in self._done)
        contract_done = sum(1 for key in contract_keys if key in self._done)
        vendor_done = sum(1 for key in vendor_keys if key in self._done)
        self.trophy_pill.setText(f"{trophy_done}/{len(trophy_keys)} troféus")
        self.safety_pill.setText(
            f"{task_done}/{len(task_keys)} objetivos · "
            f"{contract_done}/{len(contract_keys)} contratos"
        )
        self.gwent_pill.setText(
            f"{gwent_done}/{len(gwent_keys)} blocos de Gwent · "
            f"{vendor_done}/{len(vendor_keys)} lojas"
        )
        if hasattr(self, "top"):
            self.top.sync()
