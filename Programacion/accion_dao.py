from accion import Accion
from db import ConectorDB
from interfaz_dao import InterfazDao

class AccionDao(InterfazDao):
    def __init__(self):
        self.conector = ConectorDB()

    def crear(self, accion):
        consulta = """
        INSERT INTO Acciones (simbolo, nombre_empresa, ultimo_precio_operado, apertura, minimo_diario, maximo_diario, ultimo_cierre, cantidad_compra_diaria, precio_compra, precio_venta, cantidad_venta_diaria)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        parametros = (
            accion.simbolo, accion.nombre_empresa, accion.ultimo_precio_operado, accion.apertura,
            accion.minimo_diario, accion.maximo_diario, accion.ultimo_cierre,
            accion.cantidad_compra_diaria, accion.precio_compra, accion.precio_venta,
            accion.cantidad_venta_diaria
        )
        self.conector.ejecutar_consulta(consulta, parametros)

    def eliminar(self, simbolo):
        consulta = "DELETE FROM Acciones WHERE simbolo = %s"
        parametros = (simbolo,)
        self.conector.ejecutar_consulta(consulta, parametros)

    def modificar(self, accion):
        consulta = """
        UPDATE Acciones SET nombre_empresa = %s, ultimo_precio_operado = %s, apertura = %s, minimo_diario = %s,
        maximo_diario = %s, ultimo_cierre = %s, cantidad_compra_diaria = %s, precio_compra = %s, precio_venta = %s,
        cantidad_venta_diaria = %s WHERE simbolo = %s
        """
        parametros = (
            accion.nombre_empresa, accion.ultimo_precio_operado, accion.apertura, accion.minimo_diario,
            accion.maximo_diario, accion.ultimo_cierre, accion.cantidad_compra_diaria, accion.precio_compra,
            accion.precio_venta, accion.cantidad_venta_diaria, accion.simbolo
        )
        self.conector.ejecutar_consulta(consulta, parametros)

    def obtener(self, simbolo):
        consulta = "SELECT * FROM Acciones WHERE simbolo = %s"
        parametros = (simbolo,)
        resultado = self.conector.obtener_datos(consulta, parametros)
        
        if resultado:
            return Accion(*resultado[0])
        return None
    
    def obtener_todos(self):
            consulta = "SELECT * FROM Acciones"
            return self.conector.obtener_datos(consulta)