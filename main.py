import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Circle(QWidget):
    def __init__(self):
        super(Circle, self).__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)

        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor('yellow'))
        r = randrange(1, 300)
        qp.drawEllipse(0, 0, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Circle()
    win.show()
    sys.exit(app.exec())
