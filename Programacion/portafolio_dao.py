from db import ConectorDB  # Asegúrate de que esto apunte correctamente a tu archivo
from interfaz_dao import InterfazDao

class PortafolioDao(InterfazDao):
    def __init__(self):
        self.conector = ConectorDB()

    def crear(self, portafolio) -> bool:
        consulta = """
        INSERT INTO Portafolio (id_inversor, id_accion, cantidad_acciones, valor_invertido, rendimiento)
        VALUES (%s, %s, %s, %s, %s)
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_invertido, portafolio.rendimiento)
        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            raise Exception(f"Error al crear el portafolio: {e}")

    def eliminar(self, id: int) -> bool:
        consulta = "DELETE FROM Portafolio WHERE id_portafolio = %s"
        parametros = (id,)
        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            raise Exception(f"Error al eliminar el portafolio: {e}")

    def modificar(self, portafolio) -> bool:
        consulta = """
        UPDATE Portafolio
        SET id_inversor = %s, id_accion = %s, cantidad_acciones = %s, valor_invertido = %s, rendimiento = %s
        WHERE id_portafolio = %s
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_invertido, portafolio.rendimiento, portafolio.id_portafolio)
        try:
            self.conector.ejecutar_consulta(consulta, parametros)
            return True
        except Exception as e:
            raise Exception(f"Error al modificar el portafolio: {e}")

    def obtener(self, id: int):
        consulta = "SELECT * FROM Portafolio WHERE id_portafolio = %s"
        parametros = (id,)
        try:
            return self.conector.obtener_datos(consulta, parametros)
        except Exception as e:
            raise Exception(f"Error al obtener el portafolio: {e}")

    def obtener_todos(self):
        consulta = "SELECT * FROM Portafolio"
        try:
            return self.conector.obtener_datos(consulta)
        except Exception as e:
            raise Exception(f"Error al obtener todos los portafolios: {e}")

if __name__ == "__main__":
    portafolio_dao = PortafolioDao()
    print(portafolio_dao.obtener_todos())
