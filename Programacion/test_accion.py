import pytest
from accion import Accion
from accion_dao import AccionDao

@pytest.fixture
def accion_prueba():
    return Accion("APBR")

def test_atributos_accion(accion_prueba):
    assert accion_prueba.simbolo == "APBR"
    assert accion_prueba.nombre_empresa == "Petrobras Argentina"
    assert accion_prueba.ultimo_precio_operado == 150.75

def test_obtener_simbolo_y_nombre(accion_prueba):
    assert accion_prueba.obtener_simbolo_y_nombre() == ("APBR", "Petrobras Argentina")

def test_obtener_accion(mocker, accion_prueba):
    mocker.patch.object(AccionDao, 'consulta_personalizada', return_value=[(1, "APBR", "Petrobras Argentina", 150.75, 148.00, 145.50, 155.00, 148.50, 500, 149.50, 151.00, 300)])
    resultado = accion_prueba.obtener_accion("APBR")
    assert resultado is not None
