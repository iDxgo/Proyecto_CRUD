from modelo.producto import Producto
from modelo.conexionbd import ConexionBD

class ProductoDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.producto = Producto()
        
    def listarProductos(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        #for fila in filas:
            #print(fila)
        self.bd.cerrarConexion()
        return filas
            
    def insertarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param = (self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp,param)
        cursor.commit()
        self.bd.cerrarConexion()
        
    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_actualizar_producto] @Clave=?,@Descripcion=?,@Existencia=?,@Precio=?"
        params = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, params)
        self.bd.conexion.commit()
        self.bd.cerrarConexion()

    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_producto] @clave_producto=?"
        params = (self.producto.clave)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        #self.bd.conexion.commit()
        self.bd.cerrarConexion()

    def buscarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_producto] @clave=?"
        param = [self.producto.clave]
        cursor.execute(sp,param)
        filas = cursor.fetchall()
        #for fila in filas:
            #print(fila)
        self.bd.cerrarConexion()
        return filas