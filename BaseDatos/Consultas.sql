SET SQL_SAFE_UPDATES = 0;

-- Consulta 1: Inversores con saldo mayor a 2000.00
SELECT nombre, apellido, saldo_cuenta
FROM inversor
WHERE saldo_cuenta > 2000.00;

-- Consulta 2: Lista de acciones disponibles con su último precio operado
SELECT simbolo, nombre_empresa, ultimo_precio_operado
FROM Acciones;

-- Consulta 3: Transacciones de compra realizadas por un inversor específico
SELECT t.id_transaccion, t.tipo_transaccion, t.cantidad, t.precio, t.fecha_transaccion
FROM Transacciones t
JOIN inversor i ON t.id_inversor = i.id
WHERE i.cuil = '20-12345678-9' AND t.tipo_transaccion = 'compra';

-- Consulta 4: Portafolio de un inversor específico
SELECT a.simbolo, p.cantidad_acciones, p.valor_invertido
FROM Portafolio p
JOIN inversor i ON p.id_inversor = i.id
JOIN Acciones a ON p.id_accion = a.id_accion
WHERE i.nombre = 'Ana' AND i.apellido = 'Gómez';

-- Consulta 5: Transacciones con comisiones mayores a 2.00
SELECT t.id_transaccion, t.tipo_transaccion, t.cantidad, t.precio, c.monto_comision
FROM Transacciones t
JOIN Comisiones c ON t.id_transaccion = c.id_transaccion
WHERE c.monto_comision > 2.00;


-- Consultas UPDATE
-- ----------------

-- 1. Actualizar el saldo de un inversor específico
UPDATE inversor
SET saldo_cuenta = saldo_cuenta + 500.00
WHERE nombre = 'Miguel' AND apellido = 'Scaccia';

-- 2. Bloquear la cuenta de un inversor por intentos fallidos
UPDATE inversor
SET cuenta_bloqueada = TRUE
WHERE cuil = '20-98765432-1';

-- 3. Modificar el último precio operado de una acción específica
UPDATE Acciones
SET ultimo_precio_operado = 250.75
WHERE simbolo = 'ALUA';

-- 4. Actualizar el rendimiento en el portafolio de un inversor
UPDATE Portafolio
SET rendimiento = rendimiento + 100.00
WHERE id_inversor = (SELECT id FROM inversor WHERE nombre = 'Ana' AND apellido = 'Gómez');

-- 5. Modificar el porcentaje de comisión en una transacción específica
UPDATE Comisiones
SET porcentaje = 2.00
WHERE id_transaccion = 1;


-- Consultas Multitabla
-- ---------------------

-- 1. Obtener el saldo de cuenta y el portafolio de cada inversor
SELECT i.nombre, i.apellido, i.saldo_cuenta, a.nombre_empresa, p.cantidad_acciones, p.valor_invertido
FROM inversor i
JOIN Portafolio p ON i.id = p.id_inversor
JOIN Acciones a ON p.id_accion = a.id_accion;

-- 2. Consultar todas las transacciones de un inversor específico, con los detalles de las acciones involucradas
SELECT i.nombre, i.apellido, t.tipo_transaccion, a.nombre_empresa, t.cantidad, t.precio, t.fecha_transaccion
FROM Transacciones t
JOIN inversor i ON t.id_inversor = i.id
JOIN Acciones a ON t.id_accion = a.id_accion
WHERE i.cuil = '20-12345678-9';

-- 3. Calcular las comisiones totales generadas por cada inversor
SELECT i.nombre, i.apellido, SUM(c.monto_comision) AS total_comisiones
FROM inversor i
JOIN Transacciones t ON i.id = t.id_inversor
JOIN Comisiones c ON t.id_transaccion = c.id_transaccion
GROUP BY i.id;
