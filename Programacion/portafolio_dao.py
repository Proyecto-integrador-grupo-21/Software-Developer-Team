from config.db import ConectorDB
from interfaz_dao import InterfazDao

class PortafolioDao(InterfazDao):
    def __init__(self):
        self.conector = ConectorDB()

    def crear(self, portafolio):
        consulta = """
        INSERT INTO Portafolio (id_inversor, id_accion, cantidad_acciones, valor_invertido, rendimiento)
        VALUES (%s, %s, %s, %s, %s)
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_invertido, portafolio.rendimiento)
        self.conector.ejecutar_consulta(consulta, parametros)

    def eliminar(self, id):
        consulta = "DELETE FROM Portafolio WHERE id_portafolio = %s"
        parametros = (id,)
        self.conector.ejecutar_consulta(consulta, parametros)

    def modificar(self, portafolio):
        consulta = """
        UPDATE Portafolio
        SET id_inversor = %s, id_accion = %s, cantidad_acciones = %s, valor_invertido = %s, rendimiento = %s
        WHERE id_portafolio = %s
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_invertido, portafolio.rendimiento, portafolio.id_portafolio)
        self.conector.ejecutar_consulta(consulta, parametros)

    def obtener(self, id):
        consulta = "SELECT * FROM Portafolio WHERE id_portafolio = %s"
        parametros = (id,)
        return self.conector.obtener_datos(consulta, parametros)

    def obtener_todos(self):
        consulta = "SELECT * FROM Portafolio"
        return self.conector.obtener_datos(consulta)
