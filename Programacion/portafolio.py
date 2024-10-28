from transaccion import Transaccion
from accion import Accion
from inversor_dao import InversorDao

class Portafolio:
    def __init__(self, cuil):
        self.inversor_dao = InversorDao()
        self.id_inversor = self.inversor_dao.obtener_id_por_cuil(cuil)
        self.transacciones = Transaccion()
        
        if self.id_inversor is None:
            raise ValueError("No se encontró un inversor con el CUIL proporcionado.")

    def calcular_acciones(self):
        transacciones = self.transacciones.obtener_por_id_inversor(self.id_inversor)
        acciones = {}
        total_invertido = 0 

        for transaccion in transacciones:
            id_accion = transaccion['transaccion'].id_accion
            cantidad = transaccion['transaccion'].cantidad
            tipo_transaccion = transaccion['transaccion'].tipo_transaccion
            precio_compra = transaccion['transaccion'].precio

            if tipo_transaccion.lower() == "compra":
                if id_accion in acciones:
                    acciones[id_accion]['cantidad'] += cantidad
                else:
                    acciones[id_accion] = {'cantidad': cantidad, 'simbolo': transaccion['simbolo_accion'], 'precio_compra': precio_compra}
                total_invertido += cantidad * precio_compra
            elif tipo_transaccion.lower() == "venta":
                if id_accion in acciones:
                    acciones[id_accion]['cantidad'] -= cantidad
                else:
                    acciones[id_accion] = {'cantidad': -cantidad, 'simbolo': transaccion['simbolo_accion'], 'precio_compra': precio_compra}

        acciones_filtradas = {id_accion: datos for id_accion, datos in acciones.items() if datos['cantidad'] > 0}

        total_invertido_actual = sum(datos['cantidad'] * datos['precio_compra'] for id_accion, datos in acciones_filtradas.items())

        for id_accion, datos in acciones_filtradas.items():
            accion = Accion(datos['simbolo'])
            precio_actual = accion.ultimo_precio_operado
            rendimiento = (precio_actual - datos['precio_compra']) * datos['cantidad']
            datos['precio_actual'] = precio_actual
            datos['rendimiento'] = rendimiento

        return acciones_filtradas, total_invertido_actual

    def mostrar_acciones(self):
        acciones, total_invertido = self.calcular_acciones()
        if not acciones:
            print("No hay acciones disponibles.")
        else:
            for id_accion, datos in acciones.items():
                simbolo = datos['simbolo']
                cantidad = datos['cantidad']
                precio_compra = datos['precio_compra']
                precio_actual = datos['precio_actual']
                rendimiento = datos['rendimiento']
                inversion_accion = cantidad * precio_compra
                print(f"Símbolo: {simbolo}, Cantidad: {cantidad}, Precio de compra: {precio_compra}, "
                      f"Precio actual: {precio_actual}, Inversión: {inversion_accion}, Rendimiento: {rendimiento}")

            print(f"\nTotal invertido en acciones que se poseen actualmente: {total_invertido}")

if __name__ == "__main__":
    cuil = "20-12335178-9"
    try:
        portafolio = Portafolio(cuil)
        portafolio.mostrar_acciones()
    except ValueError as e:
        print(e)