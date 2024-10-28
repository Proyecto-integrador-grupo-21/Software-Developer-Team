import pytest
from inversor import Inversor
from accion import Accion
from transaccion import Transaccion

# Simulación de un DAO para pruebas
class MockInversorDao:
    def __init__(self):
        self.inversores = {}
    
    def crear(self, inversor):
        if inversor.cuil in self.inversores:
            raise Exception("Inversor ya registrado.")
        self.inversores[inversor.cuil] = inversor

    def consulta_personalizada(self, consulta, parametros):
        if consulta.startswith("SELECT id FROM inversor"):
            if parametros[0] in self.inversores:
                return [1]  # Retorna un ID simulado
            return []
        elif consulta.startswith("SELECT * FROM inversor"):
            if parameters[0] in self.inversores and parameters[1] == self.inversores[parameters[0]].email:
                return [self.inversores[parameters[0]]]
            return []
        return []

# Fixtures de pytest
@pytest.fixture
def mock_dao():
    return MockInversorDao()

@pytest.fixture
def inversor(mock_dao):
    return Inversor(
        nombre="Miguel",
        apellido="Scaccia",
        cuil="20-12335178-9",
        email="miguel1@example.com",
        contrasena="hola123",
        direccion="Direccion",
        telefono="31211313",
        perfil_inversor="conservador",
        saldo_cuenta=1000.00
    )

@pytest.fixture
def accion():
    return Accion(
        simbolo="AAPL",
        nombre_empresa="Apple Inc.",
        ultimo_precio_operado=150.00,
        apertura=148.00,
        minimo_diario=147.50,
        maximo_diario=151.00,
        ultimo_cierre=149.50,
        cantidad_compra_diaria=1000,
        precio_compra=150.00,
        precio_venta=152.00,
        cantidad_venta_diaria=500
    )

def test_registrar_inversor(mock_dao, inversor):
    inversor._dao = mock_dao  # Asignar DAO simulado
    inversor.registrar()  # Registrar al inversor
    assert inversor.verificar_inversor() == True  # Verificar que el inversor esté registrado

def test_registrar_inversor_existente(mock_dao, inversor):
    inversor._dao = mock_dao
    inversor.registrar()
    with pytest.raises(Exception, match="Inversor ya registrado."):
        inversor.registrar()  # Intentar registrar nuevamente debe fallar