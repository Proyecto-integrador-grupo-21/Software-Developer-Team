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
