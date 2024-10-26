# src/model/transaccion.py
class Transaccion:
    def __init__(self, id_transaccion=None, id_inversor=None, id_accion=None, tipo_transaccion=None, cantidad=None, precio=None, comision=None, fecha_transaccion=None):
        self.id_transaccion = id_transaccion
        self.id_inversor = id_inversor
        self.id_accion = id_accion
        self.tipo_transaccion = tipo_transaccion
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision
        self.fecha_transaccion = fecha_transaccion

    def __str__(self):
        return (f"Transaccion(id_transaccion={self.id_transaccion}, id_inversor={self.id_inversor}, "
                f"id_accion={self.id_accion}, tipo_transaccion='{self.tipo_transaccion}', "
                f"cantidad={self.cantidad}, precio={self.precio}, comision={self.comision}, "
                f"fecha_transaccion={self.fecha_transaccion})")
