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
    """Imagem que se ajusta à largura disponível e informa a altura REAL.

    A versão anterior devolvia um sizeHint fixo de 200 px, sem relação com a
    imagem escalada: o layout reservava menos espaço do que a figura ocupava e
    ela invadia o texto seguinte. Agora o widget implementa heightForWidth, que
    é como o Qt pergunta "de quanta altura você precisa nesta largura".
    """

    def __init__(self, max_height=260, parent=None):
        super().__init__(parent)
        self._source = QPixmap()
        self._max_height = max_height
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        policy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)
        self.setMinimumWidth(0)

    def set_source(self, pixmap):
        self._source = pixmap
        self._fit()
        self.updateGeometry()

    def _scaled_size(self, width):
        if self._source.isNull():
            return QSize(0, 0)
        usable = max(80, width - 16)
        return self._source.size().scaled(
            usable, self._max_height, Qt.AspectRatioMode.KeepAspectRatio
        )

    def _fit(self):
        if not self._source.isNull():
            target = self._scaled_size(self.width())
            self.setPixmap(
                self._source.scaled(
                    target, Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.setMinimumHeight(target.height() + 16)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._fit()

    def hasHeightForWidth(self):
        return not self._source.isNull()

    def heightForWidth(self, width):
        return self._scaled_size(width).height() + 16

    def sizeHint(self):
        if self._source.isNull():
            return QSize(320, 0)
        width = self.width() or self._source.width()
        return QSize(self._source.width(), self._scaled_size(width).height() + 16)

    def minimumSizeHint(self):
        return QSize(0, 0 if self._source.isNull() else 80)


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
