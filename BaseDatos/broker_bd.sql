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

INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, direccion, telefono, perfil_inversor, cuenta_bloqueada, saldo_cuenta) VALUES
('Miguel', 'Scaccia', '20-12345678-9', 'miguel@example.com', 'password123', 'Calle Falsa 123', '123456789', 'intermedio', FALSE, 1000.00),
('Ana', 'Gómez', '20-98765432-1', 'ana@example.com', 'password456', 'Avenida Siempre Viva 456', '987654321', 'conservador', FALSE, 5000.00);

SELECT * FROM inversor