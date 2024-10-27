from transaccion_dao import TransaccionDao
from decimal import Decimal

class Transaccion:
    def __init__(self, id_transaccion=None, id_inversor=None, id_accion=None, tipo_transaccion=None, cantidad=None, precio=None):
        self._id_transaccion = id_transaccion
        self._id_inversor = id_inversor
        self._id_accion = id_accion
        self._tipo_transaccion = tipo_transaccion
        self._cantidad = cantidad
        self._precio = precio
        self._comision = None  # Esta se calculará más tarde
        self._dao = TransaccionDao()

    @property
    def id_transaccion(self):
        return self._id_transaccion

    @property
    def id_inversor(self):
        return self._id_inversor

    @property
    def id_accion(self):
        return self._id_accion

    @property
    def tipo_transaccion(self):
        return self._tipo_transaccion

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    @property
    def comision(self):
        return self._comision

    def crear_transaccion(self):
        self.comision = (self._cantidad * self._precio) * Decimal("0.015")  # Calcular comisión
        self._dao.crear(self)  # Inserta la transacción en la base de datos

    def __str__(self):
        return (f"Transaccion(ID: {self._id_transaccion}, ID Inversor: {self._id_inversor}, "
                f"ID Acción: {self._id_accion}, Tipo: '{self._tipo_transaccion}', "
                f"Cantidad: {self._cantidad}, Precio: {self._precio}, Comisión: {self.comision})")

if __name__ == "__main__":
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="Compra", cantidad=10, precio=100)
    transaccion.crear_transaccion()
