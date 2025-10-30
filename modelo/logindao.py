from modelo.conexionbd import ConexionBD
from modelo.login import Login

class LoginDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.usuario = Login()
    
    def validar_login(self, usuario, contraseña):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "EXEC sp_validar_login @usuario=?, @contraseña=?"
        params = (usuario, contraseña)
        
        try:
            cursor.execute(sp, params)
            resultado = cursor.fetchone()
            
            if resultado:
                self.usuario.usuario = resultado[0]
                return True
            return False
            
        except Exception as e:
            print(f"Error en login: {e}")
            return False
        finally:
            self.bd.cerrarConexion()