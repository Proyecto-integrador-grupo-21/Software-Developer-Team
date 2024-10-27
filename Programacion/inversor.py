from inversor_dao import InversorDao
from transaccion import Transaccion
from accion import Accion

class Inversor:
    def __init__(self, nombre, apellido, cuil, email, contrasena, direccion, telefono, perfil_inversor, saldo_cuenta=0.00):
        self._nombre = nombre
        self._apellido = apellido
        self._cuil = cuil
        self._email = email
        self._contrasena = contrasena
        self._direccion = direccion
        self._telefono = telefono
        self._perfil_inversor = perfil_inversor
        self._cuenta_bloqueada = False
        self._saldo_cuenta = saldo_cuenta
        self._intentos_fallidos = 0 
        self._dao = InversorDao()

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def cuil(self):
        return self._cuil

    @property
    def email(self):
        return self._email
    
    @property
    def contrasena(self):
        return self._contrasena

    @property
    def direccion(self):
        return self._direccion
    
    @property
    def telefono(self):
        return self._telefono
    
    @property
    def perfil_inversor(self):
        return self._perfil_inversor
    
    @property
    def cuenta_bloqueada(self):
        return self._cuenta_bloqueada
    
    @property
    def saldo_cuenta(self):
        return self._saldo_cuenta
    
    def buscar_id(self):
        consulta = "SELECT id FROM inversor WHERE cuil = %s"
        parametros = (self._cuil,)
        try:
            resultado = self._dao.consulta_personalizada(consulta, parametros)
            if resultado:
                return resultado[0][0]
            else:
                raise ValueError("Inversor no encontrado.")
        except Exception as e:
            raise Exception(f"Error al buscar el ID del inversor: {e}")

    def registrar(self):
        if self.verificar_inversor():
            return f"El inversor con CUIL {self._cuil} ya tiene una cuenta registrada."
        else:
            try:
                self._dao.crear(self)
                print("Registro exitoso.")
            except Exception as e:
                raise Exception(f"Error al registrar el inversor: {e}")

    def verificar_inversor(self):
        consulta = "SELECT * FROM inversor WHERE cuil = %s AND email = %s"
        parametros = (self._cuil, self._email)
        try:
            registro = self._dao.consulta_personalizada(consulta, parametros)
            print(f"Resultado de verificación: {registro}")
            return bool(registro)
        except Exception as e:
            raise Exception(f"Error en la verificación del inversor: {e}")  

    def verificar_contrasena(self, cuil, contrasena):
        consulta = "SELECT cuil FROM inversor WHERE cuil = %s AND contrasena = %s"
        parametros = (cuil, contrasena)
        try:
            registro = self._dao.consulta_personalizada(consulta, parametros)
            return bool(registro)
        except Exception as e:
            raise Exception(f"Error al verificar la contraseña: {e}")

    def iniciar_sesion(self, cuil, contrasena):
        if self._cuenta_bloqueada:
            print("La cuenta está bloqueada.")
            return False
        
        if self.verificar_contrasena(cuil, contrasena):
            self._intentos_fallidos = 0
            print("Inicio de sesión exitoso.")
            return True
        else:
            self._intentos_fallidos += 1
            if self._intentos_fallidos >= 3:
                self._cuenta_bloqueada = True
                print("Cuenta bloqueada por demasiados intentos fallidos.")
            else:
                print("CUIL o contraseña incorrectos.")
            return False
        
    def operacion(self, simbolo_accion, cantidad: int, tipo: str):
        accion = Accion(simbolo_accion)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        id_inversor = self.buscar_id()

        if tipo == "Compra":
            total_operacion = cantidad * accion.precio_compra
            if total_operacion > self._saldo_cuenta:
                raise Exception("Saldo insuficiente para realizar la compra.")
            self._saldo_cuenta -= total_operacion
            
            transaccion = Transaccion(id_inversor=id_inversor, id_accion=accion.id, tipo_transaccion="Compra", cantidad=cantidad, precio=accion.precio_compra)
            transaccion.crear_transaccion()
            print(f"Compra exitosa: {cantidad} acciones de {accion.simbolo} por un total de {total_operacion:.2f}.")

        elif tipo == "Venta":
            total_operacion = cantidad * accion.precio_venta
            
            transaccion = Transaccion(id_inversor=id_inversor, id_accion=accion.id, tipo_transaccion="Venta", cantidad=cantidad, precio=accion.precio_venta)
            transaccion.crear_transaccion()
            self._saldo_cuenta += total_operacion
            print(f"Venta exitosa: {cantidad} acciones de {accion.simbolo} por un total de {total_operacion:.2f}.")
        else:
            raise ValueError("Tipo de operación no válido. Debe ser 'Compra' o 'Venta'.")

    def mostrar_datos_cuenta(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cuil': self.cuil,
            'saldo_cuenta': self.saldo_cuenta,
            'perfil_inversor': self._perfil_inversor
        }

if __name__ == "__main__":
    test = Inversor("Miguel", "Scaccia", "20-12335178-9", "miguel1@example.com", "hola123", "Direccion", "31211313", "conservador", 100000)
    print(test.operacion("AAPL", 3, "Compra"))
