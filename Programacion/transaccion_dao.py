from db import ConectorDB
from interfaz_dao import InterfazDao

class TransaccionDao(InterfazDao):
    def __init__(self):
        self.conector = ConectorDB()

    def crear(self, transaccion):
        consulta = """INSERT INTO Transacciones 
                    (id_inversor, id_accion, tipo_transaccion, cantidad, precio, comision) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        parametros = (transaccion.id_inversor, transaccion.id_accion, 
                    transaccion.tipo_transaccion, transaccion.cantidad, 
                    transaccion.precio, transaccion.comision)

        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            print(f"Error al crear la transacción: {e}")
            return False

    def eliminar(self, id):
        consulta = "DELETE FROM Transacciones WHERE id_transaccion = %s"
        parametros = (id,)
        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            print(f"Error al eliminar la transacción: {e}")
            return False

    def modificar(self, transaccion):
        consulta = """
        UPDATE Transacciones
        SET id_inversor = %s, id_accion = %s, tipo_transaccion = %s, cantidad = %s, precio = %s, comision = %s
        WHERE id_transaccion = %s
        """
        parametros = (transaccion.id_inversor, transaccion.id_accion, transaccion.tipo_transaccion, transaccion.cantidad, transaccion.precio, transaccion.comision, transaccion.id_transaccion)
        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            print(f"Error al modificar la transacción: {e}")
            return False

    def obtener(self, id):
        consulta = "SELECT * FROM Transacciones WHERE id_transaccion = %s"
        parametros = (id,)
        return self.conector.obtener_datos(consulta, parametros)
    
    def obtener_todos(self):
        consulta = "SELECT * FROM Transacciones"
        return self.conector.obtener_datos(consulta)

    def consulta_personalizada(self, consulta, parametros=None):
        return self.conector.obtener_datos(consulta,parametros)
