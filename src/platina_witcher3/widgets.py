"""Componentes que respeitam a largura disponível no guia."""
from PySide6.QtCore import Qt, QSize, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QPixmap, QLinearGradient
from PySide6.QtWidgets import (
    QCheckBox, QLabel, QVBoxLayout, QSizePolicy, QStyleOptionButton, QStyle,
    QWidget, QBoxLayout, QFrame,
)


class FuturePanel(QFrame):
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        gradient = QLinearGradient(18, 0, self.width()-18, 0)
        gradient.setColorAt(0, QColor("#37F2FF"))
        gradient.setColorAt(.5, QColor("#877CFF"))
        gradient.setColorAt(1, QColor("#FF4FD8"))
        painter.setPen(QPen(gradient, 2))
        painter.drawLine(18, self.height()-2, self.width()-18, self.height()-2)


class ChecklistBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setObjectName("ChecklistRow")
        self.setAccessibleName(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.caption = QLabel(text, self)
        self.caption.setWordWrap(True)
        self.caption.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(34, 8, 10, 8)
        layout.addWidget(self.caption)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

    def sizeHint(self):
        return self.layout().sizeHint()

    def minimumSizeHint(self):
        return QSize(100, self.layout().minimumSize().height())

    def hitButton(self, pos):
        return self.rect().contains(pos)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.isChecked():
            option = QStyleOptionButton()
            self.initStyleOption(option)
            rect = self.style().subElementRect(QStyle.SubElement.SE_CheckBoxIndicator, option, self)
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setPen(QPen(QColor("#37F2FF"), 2.2))
            painter.drawLine(QPointF(rect.left()+4, rect.center().y()), QPointF(rect.left()+8, rect.bottom()-4))
            painter.drawLine(QPointF(rect.left()+8, rect.bottom()-4), QPointF(rect.right()-3, rect.top()+4))


class GuideImage(QLabel):
    def __init__(self, max_height=260, parent=None):
        super().__init__(parent)
        self._source = QPixmap()
        self._max_height = max_height
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self.setMinimumWidth(0)

    def set_source(self, pixmap):
        self._source = pixmap
        self._fit()

    def _fit(self):
        if not self._source.isNull():
            width = max(80, self.width()-16)
            scaled = self._source.scaled(width, self._max_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.setPixmap(scaled)
            self.setMinimumHeight(scaled.height()+16)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._fit()

    def sizeHint(self):
        return QSize(320, min(200, self._max_height))

    def minimumSizeHint(self):
        return QSize(0, 80)


class ResponsiveHero(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("HeroContent")
        self.row = QBoxLayout(QBoxLayout.Direction.LeftToRight, self)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(22)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        direction = QBoxLayout.Direction.TopToBottom if self.width() < 880 else QBoxLayout.Direction.LeftToRight
        if self.row.direction() != direction:
            self.row.setDirection(direction)
