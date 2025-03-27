from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import os
import winsound

class ShowStringGUI(QDialog):
    """
    Interfaz gráfica que tiene como fin únicamente mostrar la orden para la adquisición de datos 
    de entrenamiento para el clasificador
    """
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'ShowStringGUI.ui')
        uic.loadUi(ui_path, self)
        screen_resolution = QApplication.desktop().screenGeometry()
        self.width, self.height = screen_resolution.width(), screen_resolution.height()
        # Establecer las dimensiones de la ventana
        self.setGeometry(0, 0, self.width, self.height)
        self.order.center()
        self.message.center()
        self.message.desplazar(0, -100)

    def updateOrder(self, text:str = "", fontsize:int = 36, background = None, border = "1px", font_color = "black", fade = None, fadeTime:float = 2):
        self.order.setText(text)
        self.order.format(fontsize = fontsize, background = background, border = border, font_color = font_color)
        if fade:
            self.order.fade(fade, time = fadeTime)
    
    def updateMessage(self, text:str = "", fontsize:int = 36, background = None, border = "1px", font_color = "black", fade = None, fadeTime:float = 2):
        self.message.setText(text)
        self.message.format(fontsize = fontsize, background = background, border = border, font_color = font_color)
        if fade:
            self.message.fade(fade, time = fadeTime)

# if __name__ == "__main__":
app = QApplication(sys.argv)
_ventana = ShowStringGUI()
_ventana.show()
_ventana.updateOrder(text = 'a', fade = 'OUT', fadeTime = 5)
app.exec_()