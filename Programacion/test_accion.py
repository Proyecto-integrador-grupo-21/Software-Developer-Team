import pytest
from accion import Accion
from accion_dao import AccionDao

# Asegúrate de que tu base de datos esté configurada y contenga los datos necesarios antes de ejecutar los tests

def test_atributos_accion():
    accion_aapl = Accion("AAPL")

    # Validamos los atributos
    assert accion_aapl.simbolo == "AAPL"
    assert accion_aapl.nombre_empresa == "Apple Inc."
    assert accion_aapl.ultimo_precio_operado == 150.50
    assert accion_aapl.apertura == 148.00
    assert accion_aapl.minimo_diario == 147.50
    assert float(accion_aapl.maximo_diario) == 151.20
    assert accion_aapl.ultimo_cierre == 149.00
    assert accion_aapl.cantidad_compra_diaria == 500
    assert accion_aapl.precio_compra == 150.00
    assert accion_aapl.precio_venta == 151.00
    assert accion_aapl.cantidad_venta_diaria == 400
def test_ver_todo(capfd):
    accion_aapl = Accion("AAPL")
    
    accion_aapl.ver_todo()

    captured = capfd.readouterr()
    assert "AAPL" in captured.out 
    assert "Apple Inc." in captured.out

def test_cargar_datos():
    accion_aapl = Accion("AAPL")
    
    assert accion_aapl.simbolo == "AAPL"
    
    try:
        accion_aapl.cargar_datos()
    except ValueError as e:
        pytest.fail(f"Unexpected error: {e}")
