import pytest
from transaccion import Transaccion
import decimal

@pytest.fixture
def transaccion_dao():
    return None

def test_crear_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    assert transaccion.comision == (10.0 * 150.75) * decimal(0.015)

def test_obtener_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    assert transaccion.comision == (10.0 * 150.75) * 0.015

def test_modificar_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    transaccion._cantidad = 20.0
    transaccion.crear_transaccion()
    assert transaccion.comision == (20.0 * 150.75) * 0.015

def test_eliminar_transaccion(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    assert transaccion.comision == (10.0 * 150.75) * 0.015

def test_obtener_por_id_inversor(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    assert transaccion.comision == (10.0 * 150.75) * 0.015

def test_calculo_comision(transaccion_dao):
    transaccion = Transaccion(id_inversor=1, id_accion=1, tipo_transaccion="compra", cantidad=10.0, precio=150.75)
    transaccion.crear_transaccion()
    assert transaccion.comision == (10.0 * 150.75) * 0.015
