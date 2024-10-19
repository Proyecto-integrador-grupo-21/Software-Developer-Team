CREATE TABLE inversor (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cuil VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    perfil_inversor ENUM('conservador', 'medio', 'agresivo') NOT NULL, 
    saldo_cuenta DECIMAL(12, 2) DEFAULT 0.00 
);
