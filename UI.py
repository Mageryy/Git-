import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from random import randint
from PyQt6.QtGui import QPainter, QColor


class Oval(QWidget):
    def __init__(self):
        super().__init__()

    def add_oval(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for _ in range(randint(0, 40)):
            d = randint(10, 200)
            x = randint(0, self.width() - d)
            y = randint(0, self.height() - d)
            col1 = randint(0, 255)
            col2 = randint(0, 255)

            painter.setPen(QColor(col1, col2, 0))
            painter.drawEllipse(x, y, d, d)


class ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Git и желтые окружности")
        self.setGeometry(100, 100, 800, 600)

        self.oval = Oval()

        self.add_circle_button = QPushButton("new ovals")
        self.add_circle_button.clicked.connect(self.oval.add_oval)

        layout = QVBoxLayout()
        layout.addWidget(self.add_circle_button)
        layout.addWidget(self.oval)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)