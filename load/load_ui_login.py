import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from modelo.logindao import LoginDAO
from load.load_ui_menu import Load_ui_menu

class Load_ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("modelo/ui/ui_login.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        
        # Conectar botones
        self.boton_login.clicked.connect(self.validar_login)
        self.boton_salir.clicked.connect(lambda: self.close())

    
    def validar_login(self):
        usuario = self.usuario_login.text().strip()
        contraseña = self.password_login.text()
        
        if not usuario or not contraseña:
            self.label_login.setText("Complete todos los campos")
            return
        
        logindao = LoginDAO()
        if logindao.validar_login(usuario, contraseña):
            self.label_login.setText(f"Bienvenido {usuario}")
            self.abrir_menu()
        else:
            self.label_login.setText("Usuario o contraseña incorrectos")
            self.password_login.clear()
            self.password_login.setFocus()
            
    def abrir_menu(self):
        menu = Load_ui_menu()
        menu.show()
        self.hide()