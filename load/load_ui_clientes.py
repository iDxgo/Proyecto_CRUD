#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from modelo.clientesdao import ClientesDAO

#2.- Cargar archivo .ui
class Load_ui_clientes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("modelo/ui/ui_clientes.ui", self)
        self.show()
        self.clientedao = ClientesDAO()
        
#3.- Configurar contenedores
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Cerrar ventana
        self.boton_salir.clicked.connect(lambda: self.close())
        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        #menu lateral
        self.boton_menu.clicked.connect(self.mover_menu)
        #Fijar ancho columnas
        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

#4.- Conectar botones a funciones
#Botones para cambiar de página
        self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

        #Botones para guardar, buscar, eliminar, eliminar y salir
        self.buscar_eliminar.clicked.connect(self.buscar_producto_eliminar)
        self.buscar_actualizar.clicked.connect(self.buscar_producto_actualizar)
        self.buscar_buscar.clicked.connect(self.buscar_producto_buscar)
        self.accion_guardar.clicked.connect(self.guardar_producto)
        self.accion_eliminar.clicked.connect(self.eliminar_producto)
        self.accion_actualizar.clicked.connect(self.actualizar_producto)
        self.accion_limpiar.clicked.connect(self.limpiar_producto)
        self.boton_refresh.clicked.connect(self.actualizar_tabla)
        
#5.- Operaciones con el modelo de datos            
    def guardar_producto(self): #Bien
        self.clientedao.cliente.clave = self.sku_agregar.text()
        self.clientedao.cliente.Nombre = self.descripcion_agregar.text()
        self.clientedao.cliente.Direccion = int(self.existencia_agregar.text())
        self.clientedao.cliente.Telefono = float(self.precio_agregar.text())
        self.clientedao.insertarProducto()
        self.label.setText(f"Cliente Agregado")


    def limpiar_producto(self): #Bien
        self.sku_buscar.clear()
        self.descripcion_buscar.clear()
        self.existencia_buscar.clear()
        self.precio_buscar.clear()

    def actualizar_producto(self): #Bien
        self.clientedao.cliente.clave = self.sku_actualizar.text()
        self.clientedao.cliente.Nombre = self.descripcion_actualizar.text()
        self.clientedao.cliente.Direccion = int(self.existencia_actualizar.text())
        self.clientedao.cliente.Telefono = float(self.precio_actualizar.text())
        self.clientedao.actualizarProducto()
        self.label.setText(f"Cliente '{self.clientedao.cliente.Nombre}' actualizado")


    def eliminar_producto(self): #Bien
        self.clientedao.cliente.clave = self.sku_eliminar.text()
        self.clientedao.eliminarProducto()
        self.label.setText(f"Producto Eliminado")

    def buscar_producto_eliminar(self):
        sku = self.sku_eliminar.text().strip()
        
        if not sku:
            self.label.setText("Error: Ingrese un SKU para buscar")
            return
        
        self.clientedao.cliente.clave = sku
        datos = self.clientedao.buscarProducto()
        
        if datos and len(datos) > 0:
            cliente = datos[0]
            self.descripcion_eliminar.setText(str(cliente[1]))
            self.existencia_eliminar.setText(str(cliente[2]))
            self.precio_eliminar.setText(str(cliente[3]))

    def buscar_producto_actualizar(self):
        sku = self.sku_actualizar.text().strip()
        
        if not sku:
            self.label.setText("Error: Ingrese un SKU para buscar")
            return
        
        self.clientedao.cliente.clave = sku
        datos = self.clientedao.buscarProducto()
        
        if datos and len(datos) > 0:
            cliente = datos[0]
            self.descripcion_actualizar.setText(str(cliente[1]))
            self.existencia_actualizar.setText(str(cliente[2]))
            self.precio_actualizar.setText(str(cliente[3]))

    def buscar_producto_buscar(self): #Mas o menos
        sku = self.sku_buscar.text().strip()
        
        if not sku:
            self.label.setText("Error: Ingrese un SKU para buscar")
            return
        
        self.clientedao.cliente.clave = sku
        datos = self.clientedao.buscarProducto()
        
        if datos and len(datos) > 0:
            cliente = datos[0]
            self.descripcion_buscar.setText(str(cliente[1]))
            self.existencia_buscar.setText(str(cliente[2]))
            self.precio_buscar.setText(str(cliente[3]))
    
    def actualizar_tabla(self): #Bien
        datos = self.clientedao.listarProductos()
        self.tabla_consulta.setRowCount(len(datos))
        fila = 0
        for item in datos:
            self.tabla_consulta.setItem(fila,0,QtWidgets.QTableWidgetItem(str(item[1])))
            self.tabla_consulta.setItem(fila,1,QtWidgets.QTableWidgetItem(str(item[2])))
            self.tabla_consulta.setItem(fila,2,QtWidgets.QTableWidgetItem(str(item[3])))
            self.tabla_consulta.setItem(fila,3,QtWidgets.QTableWidgetItem(str(item[4])))
            fila+=1


    # 6.- mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

#7.- Mover menú
    def mover_menu(self):
        if True:			
            width = self.frame_lateral.width()
            widthb = self.boton_menu.width()
            normal = 0
            if width==0:
                extender = 200
                self.boton_menu.setText("Menú")
            else:
                extender = normal
                self.boton_menu.setText("")
                
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            
            self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
        
            self.animacionb.setStartValue(width)
            self.animacionb.setEndValue(extender)
            self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacionb.start()