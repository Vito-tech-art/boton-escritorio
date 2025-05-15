import sys
import random
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt

class Escurridizo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, 1920, 1080)  # Ajusta a tu resolución

        self.button = QPushButton("Haz clic aquí", self)
        self.button.resize(140, 50)
        self.button.move(500, 300)
        self.button.setStyleSheet("font-size: 16px; background-color: #ff7675; color: white; border-radius: 10px;")

        self.button.installEventFilter(self)
        self.button.clicked.connect(lambda: self.button.setText("¡Lo lograste!"))

    def eventFilter(self, obj, event):
        if obj == self.button and event.type() == event.Enter:
            self.mover_boton()
        return super().eventFilter(obj, event)

    def mover_boton(self):
        max_x = self.width() - self.button.width()
        max_y = self.height() - self.button.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.button.move(new_x, new_y)

app = QApplication(sys.argv)
w = Escurridizo()
w.show()
sys.exit(app.exec_())
