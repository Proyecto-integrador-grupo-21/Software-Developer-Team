from transaccion_dao import TransaccionDao

class Transaccion:
    def __init__(self, id_transaccion=None, id_inversor=None, id_accion=None, tipo_transaccion=None, cantidad=None, precio=None, comision=None, fecha_transaccion=None):
        self._id_transaccion = id_transaccion
        self._id_inversor = id_inversor
        self._id_accion = id_accion
        self._tipo_transaccion = tipo_transaccion
        self._cantidad = cantidad
        self._precio = precio
        self._comision = comision
        self._fecha_transaccion = fecha_transaccion
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

    @property
    def fecha_transaccion(self):
        return self._fecha_transaccion

    @comision.setter
    def comision(self, valor):
        if valor < 0:
            raise ValueError("La comisión no puede ser negativa.")
        self._comision = valor

    def crear_transaccion(self):
        self.comision = (self._cantidad * self._precio) * 0.015
        self._dao.crear(self)

    def todos(self):
        return self._dao.obtener_todos()

    def __str__(self):
        return (f"Transaccion(id_transaccion={self._id_transaccion}, id_inversor={self._id_inversor}, "
                f"id_accion={self._id_accion}, tipo_transaccion='{self._tipo_transaccion}', "
                f"cantidad={self._cantidad}, precio={self._precio}, comision={self.comision}, "
                f"fecha_transaccion={self._fecha_transaccion})")

if __name__ == "__main__":
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="Compra", cantidad=10, precio=100)
    transaccion.crear_transaccion()
    print(transaccion.todos())
