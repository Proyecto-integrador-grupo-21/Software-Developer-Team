from transaccion_dao import TransaccionDao
from accion_dao import AccionDao
from decimal import Decimal
from accion_dao import AccionDao
from decimal import Decimal

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
        self.comision = (self._cantidad * self._precio) * Decimal("0.015")
        print(f"ID Inversor: {self.id_inversor}, ID Acción: {self.id_accion}, Tipo: {self.tipo_transaccion}, "
              f"Cantidad: {self.cantidad}, Precio: {self.precio}, Comisión: {self.comision}")
        self.comision = (self._cantidad * self._precio) * Decimal("0.015")
        print(f"ID Inversor: {self.id_inversor}, ID Acción: {self.id_accion}, Tipo: {self.tipo_transaccion}, "
              f"Cantidad: {self.cantidad}, Precio: {self.precio}, Comisión: {self.comision}")
        self._dao.crear(self)

    def obtener_simbolo_accion(self, id_accion):
        accion_dao = AccionDao()
        resultado = accion_dao.obtener_id(id_accion)
        
        if resultado and isinstance(resultado, list) and len(resultado) > 0:
            return resultado[0][0]
        
        return None

    def obtener_por_id_inversor(self, id_inversor):
        transacciones = self._dao.obtener(id_inversor)
        transacciones_con_simbolos = []

        for transaccion in transacciones:
            id_transaccion = transaccion[0]
            id_inversor = transaccion[1]
            id_accion = transaccion[2]
            tipo_transaccion = transaccion[3]
            cantidad = transaccion[4]
            precio = transaccion[5]
            comision = transaccion[6]
            fecha_transaccion = transaccion[7]

            transaccion_obj = Transaccion(
                id_transaccion=id_transaccion,
                id_inversor=id_inversor,
                id_accion=id_accion,
                tipo_transaccion=tipo_transaccion,
                cantidad=cantidad,
                precio=precio,
                comision=comision,
                fecha_transaccion=fecha_transaccion
            )
            
            simbolo_accion = self.obtener_simbolo_accion(id_accion)
            transaccion_con_simbolo = {
                'transaccion': transaccion_obj,
                'simbolo_accion': simbolo_accion
            }
            transacciones_con_simbolos.append(transaccion_con_simbolo)

        return transacciones_con_simbolos

    def obtener_por_id(self, id):
        return self._dao.obtener(id)

    def obtener_simbolo_accion(self, id_accion):
        accion_dao = AccionDao()
        resultado = accion_dao.obtener_id(id_accion)
        
        if resultado and isinstance(resultado, list) and len(resultado) > 0:
            return resultado[0][0]
        
        return None

    def obtener_por_id_inversor(self, id_inversor):
        transacciones = self._dao.obtener(id_inversor)
        transacciones_con_simbolos = []

        for transaccion in transacciones:
            id_transaccion = transaccion[0]
            id_inversor = transaccion[1]
            id_accion = transaccion[2]
            tipo_transaccion = transaccion[3]
            cantidad = transaccion[4]
            precio = transaccion[5]
            comision = transaccion[6]
            fecha_transaccion = transaccion[7]

            transaccion_obj = Transaccion(
                id_transaccion=id_transaccion,
                id_inversor=id_inversor,
                id_accion=id_accion,
                tipo_transaccion=tipo_transaccion,
                cantidad=cantidad,
                precio=precio,
                comision=comision,
                fecha_transaccion=fecha_transaccion
            )
            
            simbolo_accion = self.obtener_simbolo_accion(id_accion)
            transaccion_con_simbolo = {
                'transaccion': transaccion_obj,
                'simbolo_accion': simbolo_accion
            }
            transacciones_con_simbolos.append(transaccion_con_simbolo)

        return transacciones_con_simbolos

    def obtener_por_id(self, id):
        return self._dao.obtener(id)

    def todos(self):
        return self._dao.obtener_todos()

    def __str__(self):
        return f"Transacción(id: {self.id_transaccion}, tipo: {self.tipo_transaccion}, cantidad: {self.cantidad}, precio: {self.precio}, comisión: {self.comision})"

if __name__ == "__main__":
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="Compra", cantidad=10, precio=100, comision=Decimal('15.00'))  
    transacciones_con_simbolos = transaccion.obtener_por_id_inversor(1)
    for t in transacciones_con_simbolos:
        print(f"Transacción: {t['transaccion']}, Símbolo: {t['simbolo_accion']}")