# ARGBroker

## Descripcion
ARGBrokers es una aplicación de consola diseñada para facilitar la gestión de inversiones en el mercado bursátil. Los usuarios pueden registrarse, iniciar sesión, consultar su portafolio de acciones y realizar operaciones de compra y venta de manera simple y eficiente. La aplicación se enfoca en proporcionar una experiencia clara y funcional, con un diseño basado en principios de modularidad, bajo acoplamiento y alta cohesión.

Además, la arquitectura del sistema implementa una base de datos para registrar todas las transacciones y el historial de cotizaciones de las acciones, asegurando precisión y consistencia en los datos. Se utiliza el patrón de diseño DAO (Data Access Object) para desacoplar la lógica de negocio del acceso a datos, mejorando la escalabilidad y mantenibilidad del proyecto.
## Contexto
Este proyecto es parte de la formación de programadores, integrando múltiples módulos, como diseño de sistemas, bases de datos, programación orientada a objetos y principios de diseño simple. La aplicación fue desarrollada por el equipo de ISPC Cba, en respuesta a los requerimientos funcionales para actuar como intermediarios entre los inversores y la Bolsa de Valores de Buenos Aires.

## Alcance
La primera etapa del proyecto es una versión demo que simula la compra y venta de acciones. Incluye las siguientes funcionalidades clave:
- Registro e inicio de sesión de inversores.
- Consulta de cotizaciones de acciones de empresas argentinas.
- Compra y venta de acciones a precio del mercado.
- Visualización del portafolio del usuario, con detalles de saldo, total invertido, acciones y rendimiento.
- Cálculo automático de comisiones (1.5% por operación).

## Usos
1. Regístrate como inversor proporcionando nombre, apellido, cuil, email y contraseña.
2. Inicia sesión en la plataforma.
3. Accede al panel de cotizaciones para consultar las acciones disponibles y sus precios.
4. Realiza operaciones de compra y venta de acciones desde el panel de operaciones.
5. Consulta tu portafolio personal para visualizar tu saldo y el rendimiento de tus inversiones.

## Nomenclatura

### Archivos y Directorios
- **Archivos Python**: `snake_case` en minúsculas. Ejemplo: `main.py`, `registro_usuario.py`.
- **Directorios**: Nombres en minúsculas sin espacios ni caracteres especiales. Ejemplo: `docs`, `src`.

### Clases
- Nombres de clases: `PascalCase`. Ejemplo: `Usuario`, `GestorDeInversiones`.

### Métodos y Funciones
- Nombres de funciones y métodos: `snake_case`, comenzando con un verbo en infinitivo. Ejemplo: `registrar_usuario`, `obtener_cotizaciones`.

### Variables
- Nombres de variables: `snake_case`. Ejemplo: `saldo_inicial`, `acciones_compradas`.

### Constantes
- Nombres de constantes: `MAYÚSCULAS_CON_GUIONES`. Ejemplo: `MAX_INTENTOS`, `COMISION_BROKER`.

## Base de Datos
- La base de datos está diseñada para registrar todas las operaciones de compra y venta de acciones, así como para mantener un registro histórico de las cotizaciones.
- La estructura está normalizada hasta la Tercera Forma Normal (3FN).
- Script SQL para la creacion y modificacion de las tablas.

### Entidades Principales
1. **Usuarios**
2. **Acciones**
3. **Transacciones**
4. **Portafolio**

## Autores
- Rojas Rodrigo Walter
- Miguel Ivan Scaccia
- Agustin Rizzo
