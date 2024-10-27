from portafolio_dao import PortafolioDao
class Portafolio:
    def __init__(self, id_inversor):
        self._id_inversor = id_inversor
        self._acciones = [] 

    @property
    def id_inversor(self):
        return self._id_inversor

    @property
    def acciones(self):
        return self._acciones

    def agregar_accion(self, accion, cantidad, valor_invertido, rendimiento=0.00):
        self._acciones.append({
            'accion': accion,
            'cantidad': cantidad,
            'valor_invertido': valor_invertido,
            'rendimiento': rendimiento
        })

    def calcular_valor_total_invertido(self):
        return sum(a['valor_invertido'] for a in self._acciones)

    def calcular_rendimiento_total(self):
        return sum(a['rendimiento'] for a in self._acciones)

    def obtener_detalle_portafolio(self):
        detalle = []
        for a in self._acciones:
            detalle.append({
                'simbolo': a['accion'].simbolo,
                'nombre_empresa': a['accion'].nombre_empresa,
                'cantidad': a['cantidad'],
                'valor_invertido': a['valor_invertido'],
                'rendimiento': a['rendimiento']
            })
        return detalle

    def __str__(self):
        detalles = "\n".join(
            f"Acción: {a['accion'].simbolo} - {a['accion'].nombre_empresa}\n"
            f"Cantidad: {a['cantidad']}\n"
            f"Valor Invertido: {a['valor_invertido']}\n"
            f"Rendimiento: {a['rendimiento']}\n"
            for a in self._acciones
        )
        return (f"Portafolio del Inversor {self.id_inversor}:\n"
                f"Valor Total Invertido: {self.calcular_valor_total_invertido()}\n"
                f"Rendimiento Total: {self.calcular_rendimiento_total()}\n\n"
                f"{detalles}")