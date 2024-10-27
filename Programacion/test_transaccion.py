import pytest
from transaccion import Transaccion
from transaccion_dao import TransaccionDao

@pytest.fixture
def transaccion_dao():
    return TransaccionDao()

def test_crear_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10, precio=150.75)
    assert transaccion_dao.crear(transaccion) is True

def test_obtener_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10, precio=150.75)
    transaccion_dao.crear(transaccion)
    resultado = transaccion_dao.obtener(1)  # Asumiendo que el ID es 1
    assert resultado is not None
    assert resultado[0][2] == "compra"  # Verifica el tipo de transacción

def test_modificar_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10, precio=150.75)
    transaccion_dao.crear(transaccion)
    
    transaccion_modificada = Transaccion(id_transaccion=1, id_inversor=1, id_accion=1, tipo_transaccion="venta", cantidad=5, precio=155.00)
    assert transaccion_dao.modificar(transaccion_modificada) is True

def test_eliminar_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10, precio=150.75)
    transaccion_dao.crear(transaccion)
    
    assert transaccion_dao.eliminar(1) is True  # Elimina la transacción con ID 1
