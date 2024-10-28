DROP DATABASE IF EXISTS ARGBrokerDB;

-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS ARGBrokerDB;
USE ARGBrokerDB;

-- Tabla Inversores
CREATE TABLE IF NOT EXISTS inversor (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cuil VARCHAR(13) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    perfil_inversor ENUM('conservador', 'intermedio', 'agresivo') NOT NULL, 
    cuenta_bloqueada BOOLEAN DEFAULT FALSE,
    saldo_cuenta DECIMAL(12, 2) DEFAULT 0.00 
);

-- Creación de la tabla Acciones
CREATE TABLE IF NOT EXISTS Acciones (
  id_accion BIGINT PRIMARY KEY AUTO_INCREMENT,
  simbolo VARCHAR(10) NOT NULL,
  nombre_empresa VARCHAR(255) NOT NULL,
  ultimo_precio_operado DECIMAL(10, 2),
  apertura DECIMAL(10, 2),
  minimo_diario DECIMAL(10, 2),
  maximo_diario DECIMAL(10, 2),
  ultimo_cierre DECIMAL(10, 2),
  cantidad_compra_diaria INT,
  precio_compra DECIMAL(10, 2),
  precio_venta DECIMAL(10, 2),
  cantidad_venta_diaria INT
);

-- Creación de la tabla Transacciones
CREATE TABLE IF NOT EXISTS Transacciones (
  id_transaccion BIGINT PRIMARY KEY AUTO_INCREMENT,
  id_inversor INT,
  id_accion BIGINT,
  tipo_transaccion ENUM('compra', 'venta') NOT NULL,
  cantidad INT NOT NULL,
  precio DECIMAL(10, 2) NOT NULL,
  comision DECIMAL(5, 2) DEFAULT 1.50,
  fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_inversor) REFERENCES inversor(id),
  FOREIGN KEY (id_accion) REFERENCES Acciones(id_accion)
);

-- Creación de la tabla Portafolio
CREATE TABLE IF NOT EXISTS Portafolio (
  id_portafolio BIGINT PRIMARY KEY AUTO_INCREMENT,
  id_inversor INT, 
  id_accion BIGINT,
  cantidad_acciones INT NOT NULL,
  valor_invertido DECIMAL(15, 2) NOT NULL,
  rendimiento DECIMAL(15, 2),
  FOREIGN KEY (id_inversor) REFERENCES inversor(id),
  FOREIGN KEY (id_accion) REFERENCES Acciones(id_accion)
);

INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, direccion, telefono, perfil_inversor, saldo_cuenta)
VALUES 
('Juan', 'Pérez', '20-12345678-9', 'juan.perez@example.com', 'password123', 'Calle Falsa 123', '1234567890', 'conservador', 50000.00),
('María', 'Gómez', '20-87654321-0', 'maria.gomez@example.com', 'mypassword456', 'Avenida Siempre Viva 456', '0987654321', 'intermedio', 100000.00),
('Carlos', 'López', '20-13579246-8', 'carlos.lopez@example.com', 'securepass789', 'Boulevard de los Sueños 789', '1122334455', 'agresivo', 250000.00);


INSERT INTO Acciones (simbolo, nombre_empresa, ultimo_precio_operado, apertura, minimo_diario, maximo_diario, ultimo_cierre, cantidad_compra_diaria, precio_compra, precio_venta, cantidad_venta_diaria)
VALUES 
('AAPL', 'Apple Inc.', 150.00, 148.50, 147.00, 151.00, 149.00, 10000, 148.00, 150.50, 8000),
('MSFT', 'Microsoft Corp.', 300.00, 295.00, 290.00, 302.00, 298.00, 12000, 294.00, 299.50, 10000),
('TSLA', 'Tesla Inc.', 700.00, 680.00, 675.00, 710.00, 690.00, 9000, 678.00, 702.00, 7500);


INSERT INTO Transacciones (id_inversor, id_accion, tipo_transaccion, cantidad, precio, comision)
VALUES 
(1, 1, 'compra', 10, 150.00, 1.50),
(1, 2, 'venta', 5, 300.00, 1.50),
(2, 3, 'compra', 2, 700.00, 1.50);

INSERT INTO Portafolio (id_inversor, id_accion, cantidad_acciones, valor_invertido, rendimiento)
VALUES 
(1, 1, 10, 1500.00, 200.00),
(2, 2, 5, 1500.00, 300.00),
(3, 3, 2, 1400.00, 500.00);
