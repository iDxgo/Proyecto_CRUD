from modelo.clientes import Clientes
from modelo.conexionbd import ConexionBD

class ClientesDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.cliente = Clientes()
        
    def listarProductos(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_clientes]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        #for fila in filas:
            #print(fila)
        self.bd.cerrarConexion()
        return filas
            
    def insertarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_insertar_cliente] @clave=?, @Nombre=?, @Direccion=?, @Telefono=?"
        param = (self.cliente.clave,self.cliente.Nombre,self.cliente.Direccion,self.cliente.Telefono)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp,param)
        cursor.commit()
        self.bd.cerrarConexion()
        
    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_actualizar_cliente] @clave=?,@Nombre=?,@Direccion=?,@Telefono=?"
        params = (self.cliente.clave, self.cliente.Nombre, self.cliente.Direccion, self.cliente.Telefono)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, params)
        self.bd.conexion.commit()
        self.bd.cerrarConexion()

    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_cliente] @clave=?"
        params = (self.cliente.clave)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        #self.bd.conexion.commit()
        self.bd.cerrarConexion()

    def buscarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_cliente] @clave=?"
        param = [self.cliente.clave]
        cursor.execute(sp,param)
        filas = cursor.fetchall()
        #for fila in filas:
            #print(fila)
        self.bd.cerrarConexion()
        return filas