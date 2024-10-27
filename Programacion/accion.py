from accion_dao import AccionDao
class Accion:
    def __init__(self, simbolo, nombre_empresa, ultimo_precio_operado, apertura, minimo_diario, maximo_diario, ultimo_cierre, cantidad_compra_diaria, precio_compra, precio_venta, cantidad_venta_diaria):
        self._simbolo = simbolo
        self._nombre_empresa = nombre_empresa
        self._ultimo_precio_operado = ultimo_precio_operado
        self._apertura = apertura
        self._minimo_diario = minimo_diario
        self._maximo_diario = maximo_diario
        self._ultimo_cierre = ultimo_cierre
        self._cantidad_compra_diaria = cantidad_compra_diaria
        self._precio_compra = precio_compra
        self._precio_venta = precio_venta
        self._cantidad_venta_diaria = cantidad_venta_diaria
        self._dao = AccionDao()

    @property
    def simbolo(self):
        return self._simbolo

    @property
    def nombre_empresa(self):
        return self._nombre_empresa

    @property
    def ultimo_precio_operado(self):
        return self._ultimo_precio_operado

    @property
    def apertura(self):
        return self._apertura

    @property
    def minimo_diario(self):
        return self._minimo_diario

    @property
    def maximo_diario(self):
        return self._maximo_diario

    @property
    def ultimo_cierre(self):
        return self._ultimo_cierre

    @property
    def cantidad_compra_diaria(self):
        return self._cantidad_compra_diaria

    @property
    def precio_compra(self):
        return self._precio_compra

    @property
    def precio_venta(self):
        return self._precio_venta

    @property
    def cantidad_venta_diaria(self):
        return self._cantidad_venta_diaria

    def obtener_todos(self):
            registros = self._dao.obtener_todos()
            print(registros)
    def __str__(self):
        return (f"Acción: {self.simbolo} - {self.nombre_empresa}\n"
                f"Último Precio: {self.ultimo_precio_operado}\n"
                f"Apertura: {self.apertura}\n"
                f"Mínimo Diario: {self.minimo_diario}\n"
                f"Máximo Diario: {self.maximo_diario}\n"
                f"Último Cierre: {self.ultimo_cierre}\n"
                f"Cantidad Compra Diaria: {self.cantidad_compra_diaria}\n"
                f"Precio Compra: {self.precio_compra}\n"
                f"Precio Venta: {self.precio_venta}\n"
                f"Cantidad Venta Diaria: {self.cantidad_venta_diaria}")

lett = Accion()
print(lett.obtener_todos())