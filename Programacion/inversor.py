from inversor_dao import InversorDao
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
    def saldo_cuenta(self):
        return self._saldo_cuenta

    def registrar(self):
        pass

    def verificar_inversor(self, email):
        registros = self._dao.obtener_todos()
        print(registros)
        pass

    def iniciar_sesion(self, contrasena):
        if self._cuenta_bloqueada:
            print("La cuenta está bloqueada.")
            return False
        
        if self._contrasena == contrasena:
            self._intentos_fallidos = 0
            print("Inicio de sesión exitoso.")
            return True
        else:
            self._intentos_fallidos += 1
            if self._intentos_fallidos >= 3:
                self._cuenta_bloqueada = True
                print("Cuenta bloqueada por demasiados intentos fallidos.")
            else:
                print("Contraseña incorrecta.")
            return False

    def mostrar_datos_cuenta(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cuil': self.cuil,
            'saldo_cuenta': self.saldo_cuenta,
            'perfil_inversor': self._perfil_inversor
        }
    
lss = Inversor("Miguel", "ssss","20-20202022-1", "dasdsad", "hola123","dadad", "31211313", "conservador")

print(lss.verificar_inversor("lss"))