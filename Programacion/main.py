from dao.inversor import Inversor
# from src.model.accion import Accion
# from src.model.transaccion import Transaccion
# from src.model.portafolio import Portafolio

# El resto del código permanece igual


# Crear instancias de los DAOs
# inversor_dao = InversorDao()
# accion_dao = AccionDao()
# transaccion_dao = TransaccionDao()
# portafolio_dao = PortafolioDao()

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Gestión de Inversores")
    print("2. Gestión de Acciones")
    print("3. Gestión de Transacciones")
    print("4. Gestión de Portafolio")
    print("5. Salir")

def menu_inversor():
    print("\nGestión de Inversores")
    print("1. Agregar inversor")
    print("2. Modificar inversor")
    print("3. Eliminar inversor")
    print("4. Consultar inversor")
    print("5. Volver al menú principal")

def menu_accion():
    print("\nGestión de Acciones")
    print("1. Agregar acción")
    print("2. Modificar acción")
    print("3. Eliminar acción")
    print("4. Consultar acción")
    print("5. Volver al menú principal")

def menu_transaccion():
    print("\nGestión de Transacciones")
    print("1. Registrar transacción")
    print("2. Consultar transacción")
    print("3. Volver al menú principal")

def menu_portafolio():
    print("\nGestión de Portafolio")
    print("1. Agregar al portafolio")
    print("2. Consultar portafolio")
    print("3. Volver al menú principal")

def agregar_inversor():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cuil = input("CUIL: ")
    email = input("Email: ")
    contrasena = input("Contraseña: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    perfil = input("Perfil Inversor (conservador/intermedio/agresivo): ")
    cuenta_bloqueada = input("Cuenta bloqueada (True/False): ") == "True"
    saldo_cuenta = float(input("Saldo de cuenta inicial: "))

    inversor = Inversor(
        nombre=nombre, apellido=apellido, cuil=cuil, email=email,
        contrasena=contrasena, direccion=direccion, telefono=telefono,
        perfil_inversor=perfil, cuenta_bloqueada=cuenta_bloqueada, saldo_cuenta=saldo_cuenta
    )
    # inversor_dao.crear(inversor)
    print("Inversor agregado exitosamente.")

# Similar a agregar_inversor, agrega funciones para `modificar`, `eliminar` y `consultar`

# Menú de operaciones
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_inversor()
            opcion_inversor = input("Seleccione una opción de inversores: ")
            if opcion_inversor == "1":
                agregar_inversor()
            # Agregar llamadas para modificar, eliminar y consultar inversores
            
        elif opcion == "2":
            menu_accion()
            opcion_accion = input("Seleccione una opción de acciones: ")
            if opcion_accion == "1":
                # Llamar a función para agregar acción
                pass
            # Agregar llamadas para modificar, eliminar y consultar acciones
        
        elif opcion == "3":
            menu_transaccion()
            opcion_transaccion = input("Seleccione una opción de transacciones: ")
            if opcion_transaccion == "1":
                # Llamar a función para registrar transacción
                pass
            # Agregar llamada para consultar transacciones
            
        elif opcion == "4":
            menu_portafolio()
            opcion_portafolio = input("Seleccione una opción de portafolio: ")
            if opcion_portafolio == "1":
                # Llamar a función para agregar al portafolio
                pass
            # Agregar llamada para consultar portafolio
            
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar()
