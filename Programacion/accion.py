from accion_dao import AccionDao

class Accion:
    def __init__(self, simbolo):
        self._simbolo = simbolo
        self._dao = AccionDao()
        self.cargar_datos()

    def cargar_datos(self):
        consulta = "SELECT * FROM Acciones WHERE simbolo = %s"
        parametros = (self._simbolo,)
        try:
            registro = self._dao.consulta_personalizada(consulta, parametros)
            print("Registro devuelto:", registro)
            if registro:
                (self._id, self._simbolo, self._nombre_empresa, self._ultimo_precio_operado,
                 self._apertura, self._minimo_diario, self._maximo_diario,
                 self._ultimo_cierre, self._cantidad_compra_diaria,
                 self._precio_compra, self._precio_venta, 
                 self._cantidad_venta_diaria) = registro[0]
            else:
                raise ValueError("No se encontró la acción con el símbolo proporcionado.")
        except Exception as e:
            raise Exception(f"Error al cargar los datos de la acción: {e}")

    @property
    def id(self):
        return self._id

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
    
    def obtener_simbolo_y_nombre(self):
        return self.simbolo, self.nombre_empresa

    def obtener_accion(self, simbolo):
        return self._dao.obtener(simbolo)  # Llamada al DAO para obtener la acción por símbolo

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

if __name__ == "__main__":
    accion_aapl = Accion("AAPL")
    print(accion_aapl)
