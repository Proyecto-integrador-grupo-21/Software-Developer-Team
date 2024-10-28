from inversor import Inversor
from accion import Accion
from portafolio import Portafolio
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
    inversor = Inversor(nombre="", apellido="", cuil=cuil, email="", contrasena=contrasena, direccion="", telefono="", perfil_inversor="", saldo_cuenta=1000000)
    
    try:
        if inversor.iniciar_sesion(cuil, contrasena):
            print("\nInicio de sesión exitoso. Bienvenido.")
            mostrar_menu_principal(inversor)
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

def mostrar_menu_principal(inversor):
    while True:
        print("\nMenú Principal")
        print("1. Gestión de Acciones")
        print("2. Registro de Transacciones")
        print("3. Portafolio")
        print("4. Datos Personales")
        print("5. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_accion(inversor)
        elif opcion == "2":
            registrar_transacciones(inversor)
        elif opcion == "3":
            menu_portafolio(inversor)
        elif opcion == "4":
            print("Sesión cerrada. Regresando al menú de bienvenida.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_accion(inversor):
    while True:
        print("\nGestión de Acciones")
        print("1. Ver todas las acciones")
        print("2. Comprar acción")
        print("3. Vender acción")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            acciones = Accion("AAPL")
            print(acciones.ver_todo())
        elif opcion == "2":
            comprar_accion(inversor)
        elif opcion == "3":
            vender_accion(inversor)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def comprar_accion(inversor):
    simbolo_accion = input("Ingrese el símbolo de la acción que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    
    try:
        inversor.operacion(simbolo_accion, cantidad, "Compra")
    except Exception as e:
        print(f"Error en la compra: {e}")

def vender_accion(inversor):
    simbolo_accion = input("Ingrese el símbolo de la acción que desea vender: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    
    try:
        inversor.operacion(simbolo_accion, cantidad, "Venta")
    except Exception as e:
        print(f"Error en la venta: {e}")

def registrar_transacciones(inversor):
    print("\nRegistro de Transacciones")
    consultar_transacciones(inversor) 

def menu_portafolio(inversor):
    print("\nPortafolio")
    portafolio = Portafolio(inversor.cuil)
    portafolio.mostrar_acciones()


def consultar_transacciones(inversor):
    print("\nConsultar Transacciones")
    try:
        transacciones_con_simbolos = inversor.registro_transaccion()
        
        if transacciones_con_simbolos:
            print("\n{:<10} {:<10} {:<15} {:<10} {:<15} {:<15}".format(
                "ID", "Tipo", "Símbolo", "Cantidad", "Precio", "Comisión"))
            print("-" * 80)

            for item in transacciones_con_simbolos:
                print("{:<10} {:<10} {:<15} {:<10} {:<15} {:<15}".format(
                    item['id'], 
                    item['tipo'], 
                    item['simbolo_accion'],
                    item['cantidad'], 
                    item['precio'], 
                    item.get('comision', 'No disponible')))
        else:
            print("No hay transacciones registradas.")
    except Exception as e:
        print(f"Error al consultar transacciones: {e}")

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
