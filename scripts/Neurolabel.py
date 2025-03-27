from PyQt5.QtWidgets import QLabel, QApplication, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtGui import QFont

class Neurolabel(QLabel):

    def __init__(self, parent = None):
        super().__init__(parent)
        screen_resolution = QApplication.desktop().screenGeometry()
        self.width, self.height = screen_resolution.width(), screen_resolution.height()
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1.0)  # Opacidad inicial (1.0 = completamente visible)
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    
    def fade(self, type = 'IN', time:float = 2):
        time_ms = time*1000
        if type == 'IN':
            self.animation.setDuration(time_ms)  # Duración en milisegundos
            self.animation.setStartValue(0.0)  # Opacidad inicial
            self.animation.setEndValue(1.0)  # Opacidad final (1.0 = completamente visible)
            self.animation.start()
        elif type == 'OUT':
            self.animation.setDuration(time_ms)  # Duración en milisegundos
            self.animation.setStartValue(1.0)  # Opacidad inicial
            self.animation.setEndValue(0.0)  # Opacidad final (0.0 = completamente transparente)
            self.animation.start()

    def center(self):
        """
        Centra el objeto (widget) en la pantalla
        """
        self.setGeometry(int(self.width/2 - self.width/2), int(self.height/2 - self.height/2), 
                           int(self.width),int(self.height))
        
    def mover_a_posicion(self, x, y):
        """Mueve el widget a una posición absoluta (x, y)."""
        self.move(x, y)

    def desplazar(self, dx, dy):
        """Desplaza el widget desde su posición actual."""
        posicion_actual = self.pos()
        nueva_posicion = QPoint(posicion_actual.x() + dx, posicion_actual.y() + dy)
        self.move(nueva_posicion)

    def format(self, fontsize:int = 36, background = None, border = "1px", font_color = "black"):
        self.setFont(QFont('Berlin Sans', fontsize))
        if background:
            self.setStyleSheet(f"background-color: {background};border: {border} solid black;color: {font_color}")
        # else:
        #     self.setStyleSheet(f"border: 0px solid black;color: {font_color}")

if __name__ == "__main__":
    neurolabel = Neurolabel()