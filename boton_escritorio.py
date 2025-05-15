from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, QTimer, QRect
import sys, random

class BotonCansado(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, 1920, 1080)

        self.button = QPushButton("Haz clic aquí", self)
        self.button.resize(140, 50)
        self.button.move(500, 300)
        self.button.setStyleSheet("""
            font-size: 16px; 
            background-color: #ff7675; 
            color: white; 
            border-radius: 10px;
            padding-right: 25px; /* espacio para la X */
            position: relative;
        """)
        self.button.clicked.connect(self.finalizar)

        self.energy = 10
        self.evadiendo = True
        self.descansando = False

        self.button.installEventFilter(self)

        self.timer_recuperacion = QTimer()
        self.timer_recuperacion.setSingleShot(True)
        self.timer_recuperacion.timeout.connect(self.recuperar_energia)

        # Crear un botón pequeño "X" dentro del botón principal
        self.close_button = QPushButton("×", self.button)
        self.close_button.setGeometry(QRect(self.button.width() - 25, 5, 20, 20))
        self.close_button.setStyleSheet("""
            background-color: #d63031; 
            color: white; 
            border: none; 
            font-weight: bold; 
            border-radius: 10px;
        """)
        self.close_button.hide()
        self.close_button.clicked.connect(self.close)

    def eventFilter(self, obj, event):
        if obj == self.button and event.type() == event.Enter and self.evadiendo and not self.descansando:
            self.energy -= 1
            self.mover_boton()

            if self.energy <= 0:
                self.evadiendo = False
                self.descansando = True
                self.button.setText("... agotado 😩")
                self.timer_recuperacion.start(5000)

        return super().eventFilter(obj, event)

    def mover_boton(self):
        max_x = self.width() - self.button.width()
        max_y = self.height() - self.button.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.button.move(new_x, new_y)

    def recuperar_energia(self):
        self.energy = 10
        self.evadiendo = True
        self.descansando = False
        self.button.setText("Haz clic aquí")
        self.close_button.hide()

    def finalizar(self):
        self.button.setText("¡Lo lograste!")
        self.close_button.show()

app = QApplication(sys.argv)
w = BotonCansado()
w.show()
sys.exit(app.exec_())
