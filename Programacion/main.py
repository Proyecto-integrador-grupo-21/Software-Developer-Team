from inversor import Inversor
import re

def mostrar_bienvenida():
    print("\nBienvenido al Broker")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")

def validar_cuil(cuil):
    patron = r'^\d{2}-\d{8}-\d$'
    return re.match(patron, cuil) is not None

def iniciar_sesion():
    print("\nIniciar Sesión")
    cuil = input("Ingrese su CUIL (formato XX-XXXXXXXX-X): ")
    
    if not validar_cuil(cuil):
        print("Formato de CUIL inválido. Debe ser XX-XXXXXXXX-X.")
        return
    
    contrasena = input("Ingrese su contraseña: ")
    inversor = Inversor(nombre="", apellido="", cuil=cuil, email="", contrasena=contrasena, direccion="", telefono="", perfil_inversor="")
    
    try:
        if inversor.iniciar_sesion(cuil, contrasena):
            print("\nInicio de sesión exitoso. Bienvenido.")
            mostrar_menu_principal()
        else:
            print("CUIL o contraseña incorrectos. Intente nuevamente.")
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")

def registrar_usuario():
    print("\nRegistro de Nuevo Usuario")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    cuil = input("CUIL (formato XX-XXXXXXXX-X): ")
    if not validar_cuil(cuil):
        print("Formato de CUIL inválido. Debe ser XX-XXXXXXXX-X.")
        return

    email = input("Email: ")
    contrasena = input("Contraseña: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    perfil = input("Perfil Inversor (conservador/intermedio/agresivo): ")
    saldo_cuenta = 1000000

    nuevo_inversor = Inversor(
        nombre=nombre, apellido=apellido, cuil=cuil, email=email,
        contrasena=contrasena, direccion=direccion, telefono=telefono,
        perfil_inversor=perfil, saldo_cuenta=saldo_cuenta
    )
    
    try:
        if not nuevo_inversor.verificar_inversor():
            nuevo_inversor.registrar()
            print("Registro exitoso. Ya puede iniciar sesión.")
        else:
            print("Ya existe un inversor con este CUIL. Intente iniciar sesión.")
    except Exception as e:
        print(f"Error al registrar usuario: {e}")

def mostrar_menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Gestión de Acciones")
        print("2. Registro de Transacciones")
        print("3. Portafolio")
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_accion()
        elif opcion == "2":
            menu_transaccion()
        elif opcion == "3":
            menu_portafolio()
        elif opcion == "4":
            print("Sesión cerrada. Regresando al menú de bienvenida.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_accion():
    print("\nGestión de Acciones")
    print("1. Ver todas las acciónes")
    print("2. Comprar acción")
    print("3. Vender acción")
    print("4. Volver al menú principal")

def menu_transaccion():
    print("\Registro de Transacciones")
    print("1. Consultar transacciónes")
    print("2. Volver al menú principal")

def menu_portafolio():
    print("\nPortafolio")
    print("1. Consultar portafolio")
    print("2. Volver al menú principal")

# Inicio de la aplicación
def ejecutar():
    while True:
        mostrar_bienvenida()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Gracias por utilizar el Broker. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar()
