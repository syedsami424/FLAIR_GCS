from PyQt5.QtWidgets import QDial, QSizePolicy
from PyQt5.QtGui import QPainter, QFont, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect

class CompassDial(QDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(360)
        self.setNotchesVisible(False)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.gps_heading = gps_heading

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        size = min(rect.width(), rect.height())
        circle_rect = QRect(rect.center().x() - size // 2, rect.center().y() - size // 2, size, size)
        painter.setBrush(QBrush(Qt.white))
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(circle_rect)

        directions = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
                      225: "SW", 270: "W", 315: "NW"}
        font = QFont(self.font())
        font.setPointSize(10)
        font.setStyleStrategy(QFont.PreferAntialias) 
        painter.setFont(font)

        for angle, label in directions.items():
            painter.save()
            painter.translate(circle_rect.center())
            painter.rotate(-angle)
            painter.drawText(-10, -circle_rect.height() // 2 + 10, 20, 20, Qt.AlignCenter, label)
            painter.restore()

        # Draw the red needle
        painter.save()
        painter.translate(circle_rect.center())
        painter.rotate(-self.value())
        needle = [QPoint(0, -circle_rect.height() // 2 + 10), QPoint(5, 0), QPoint(-5, 0)]
        painter.setBrush(QBrush(Qt.red))
        painter.drawPolygon(*needle)
        painter.restore()

        # Draw the black needle (opposite to the red needle)
        painter.save()
        painter.translate(circle_rect.center())
        painter.rotate(-self.value() + 180)
        black_needle = [QPoint(0, -circle_rect.height() // 2 + 10), QPoint(5, 0), QPoint(-5, 0)]
        painter.setBrush(QBrush(Qt.black))
        painter.drawPolygon(*black_needle)
        painter.restore()


    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

    def updateHeading(self, gps_heading):
        if gps_heading is not None:
            self.setValue(gps_heading)
            self.update()
        else:
            print("here")
            pass