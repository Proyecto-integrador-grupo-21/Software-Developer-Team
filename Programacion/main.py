from inversor import Inversor
from transaccion import Transaccion
from accion import Accion
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
            mostrar_menu_principal(inversor)  # Pasar el inversor para usarlo en las opciones
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
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_accion(inversor)  # Pasar inversor
        elif opcion == "2":
            menu_transaccion(inversor)  # Pasar inversor
        elif opcion == "3":
            menu_portafolio(inversor)  # Pasar inversor
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
            # Lógica para ver todas las acciones
            acciones = Accion.obtener_todas_las_acciones()  # Asegúrate de que esta función exista
            for accion in acciones:
                print(f"Símbolo: {accion.simbolo}, Empresa: {accion.nombre_empresa}, Último Precio: {accion.ultimo_precio_operado}")
        elif opcion == "2":
            simbolo = input("Ingrese el símbolo de la acción a comprar: ")
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            try:
                transaccion = Transaccion(id_inversor=inversor.id, id_accion=simbolo, tipo_transaccion='compra', cantidad=cantidad, precio=0.0, comision=0.0)
                transaccion.comprar()  # Implementa esta lógica en la clase Transaccion
                print("Compra realizada exitosamente.")
            except Exception as e:
                print(f"Error en la compra: {e}")
        elif opcion == "3":
            simbolo = input("Ingrese el símbolo de la acción a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            try:
                transaccion = Transaccion(id_inversor=inversor.id, id_accion=simbolo, tipo_transaccion='venta', cantidad=cantidad, precio=0.0, comision=0.0)
                transaccion.vender()  # Implementa esta lógica en la clase Transaccion
                print("Venta realizada exitosamente.")
            except Exception as e:
                print(f"Error en la venta: {e}")
        elif opcion == "4":
            mostrar_menu_principal(inversor)
            break
        else:
            print("Opción no válida.")

def menu_transaccion(inversor):
    while True:
        print("\nRegistro de Transacciones")
        print("1. Consultar transacciones")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            transacciones = Transaccion.obtener_transacciones_por_inversor(inversor.id)  # Implementa esta función
            for transaccion in transacciones:
                print(f"ID: {transaccion.id_transaccion}, Tipo: {transaccion.tipo_transaccion}, Cantidad: {transaccion.cantidad}, Precio: {transaccion.precio}")
        elif opcion == "2":
            mostrar_menu_principal(inversor)
            break
        else:
            print("Opción no válida.")

def menu_portafolio(inversor):
    while True:
        print("\nPortafolio")
        print("1. Consultar portafolio")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            portafolio = inversor.consultar_portafolio()  # Implementa esta función en la clase Inversor
            for accion in portafolio:
                print(f"Símbolo: {accion.simbolo}, Cantidad: {accion.cantidad_acciones}, Valor Invertido: {accion.valor_invertido}")
        elif opcion == "2":
            mostrar_menu_principal(inversor)
            break
        else:
            print("Opción no válida.")

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
