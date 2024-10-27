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

        self.conector.ejecutar_consulta(consulta, parametros)

    def eliminar(self, id):
        consulta = "DELETE FROM Transacciones WHERE id_transaccion = %s"
        parametros = (id,)
        self.conector.ejecutar_consulta(consulta, parametros)

    def modificar(self, transaccion):
        consulta = """
        UPDATE Transacciones
        SET id_inversor = %s, id_accion = %s, tipo_transaccion = %s, cantidad = %s, precio = %s, comision = %s
        WHERE id_transaccion = %s
        """
        parametros = (transaccion.id_inversor, transaccion.id_accion, transaccion.tipo_transaccion, transaccion.cantidad, transaccion.precio, transaccion.comision, transaccion.id_transaccion)
        self.conector.ejecutar_consulta(consulta, parametros)

    def obtener(self, id):
        consulta = "SELECT * FROM Transacciones WHERE id_transaccion = %s"
        parametros = (id,)
        return self.conector.obtener_datos(consulta, parametros)
    
    def obtener_todos(self):
            consulta = "SELECT * FROM Transacciones"
            return self.conector.obtener_datos(consulta)

    def consulta_personalizada(self, consulta, parametros=None):
        return self.conector.obtener_datos(consulta,parametros)