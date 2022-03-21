from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainterPath


class QNavigationWidget(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.backgroundColor = '#E4E4E4'
        self.selectedColor = "#2CA7F8"
        self.hoveredColor = "#BBBBBB"
        self.rowHeight = 40
        self.currentIndex = 0
        self.currentHoverIdx = None
        self.listItem = []

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        # font.setBold(True)
        self.setFont(font)

        self.setMouseTracking(True)
        self.setFixedWidth(150)
        pass

    def addItem(self, title):
        self.listItem.append(title)
        self.update()
        pass

    def setWidth(self, width):
        self.setFixedWidth(width)
        pass

    def setBackgroundColor(self, color):
        self.backgroundColor = color
        self.update()
        pass

    def setSelectedColor(self, color):
        self.selectedColor = color
        self.update()
        pass

    def setRowHeight(self, height):
        self.rowHeight = height
        self.update()
        pass

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtWidgets.QStylePainter(self)
        painter.setRenderHint(QtWidgets.QStylePainter.Antialiasing, True)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QColor(self.backgroundColor))
        painter.drawRect(self.rect())

        count = 0
        for str in self.listItem:
            itemPath = QPainterPath()
            itemPath.addRect(QtCore.QRectF(0, count * self.rowHeight, self.width(), self.rowHeight))

            if self.currentIndex == count:
                painter.setPen(QColor("#FFFFFF"))
                painter.fillPath(itemPath, QColor(self.selectedColor))
                pass
            elif self.currentHoverIdx == count:
                painter.setPen(QColor("#202020"))
                painter.fillPath(itemPath, QColor(self.hoveredColor))
                pass
            else:
                painter.setPen(QColor("#202020"))
                painter.fillPath(itemPath, QColor(self.backgroundColor))
                pass

            painter.drawText(QtCore.QRect(0, count * self.rowHeight, self.width(), self.rowHeight),
                             QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter, str)

            count += 1
            pass
        pass

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.y() / self.rowHeight < len(self.listItem):
            self.currentHoverIdx = a0.y() // self.rowHeight
            pass
        else:
            self.currentHoverIdx = None
            pass
        self.update()
        pass

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.y() / self.rowHeight < len(self.listItem):
            self.currentIndex = a0.y() // self.rowHeight
            self.signal.emit(self.currentIndex)
            self.update()
            pass
        pass

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        pass
