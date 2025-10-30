import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from load.load_ui_productos import Load_ui_productos
from load.load_ui_clientes import Load_ui_clientes

class Load_ui_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("modelo/ui/ui_menu.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        
        # Conectar botones
        self.boton_clientes.clicked.connect(self.abrir_clientes)
        self.boton_productos.clicked.connect(self.abrir_productos)
        self.boton_salir.clicked.connect(lambda: self.close())
    
    def abrir_clientes(self):
        clientes = Load_ui_clientes()
        clientes.show()
        self.hide()
    
    def abrir_productos(self):
        productos = Load_ui_productos()
        productos.show()
        self.hide()
