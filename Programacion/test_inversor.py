import pytest
from inversor import Inversor
from inversor_dao import InversorDao

@pytest.fixture
def inversor_dao():
    return InversorDao()

@pytest.fixture
def inversor_prueba():
    return Inversor(
        nombre="Miguel",
        apellido="Scaccia",
        cuil="20-12345678-9",
        email="miguel@example.com",
        contrasena="password123",
        direccion="Calle Falsa 123",
        telefono="123456789",
        perfil_inversor="intermedio"
    )

def test_registrar_inversor(inversor_dao, inversor_prueba):
    inversor_prueba.registrar()
    assert inversor_dao.obtener_todos()

def test_verificar_inversor(inversor_dao, inversor_prueba):
    inversor_prueba.registrar()
    assert inversor_prueba.verificar_inversor() is True

def test_verificar_contrasena(inversor_dao, inversor_prueba):
    inversor_prueba.registrar()
    assert inversor_prueba.verificar_contrasena(inversor_prueba.cuil, inversor_prueba.contrasena) is True

def test_iniciar_sesion(inversor_dao, inversor_prueba):
    inversor_prueba.registrar()
    assert inversor_prueba.iniciar_sesion(inversor_prueba.cuil, inversor_prueba.contrasena) is True

def test_bloquear_cuenta(inversor_dao, inversor_prueba):
    inversor_prueba.registrar()
    for _ in range(3):
        inversor_prueba.iniciar_sesion(inversor_prueba.cuil, "wrong_password")
    assert inversor_prueba.cuenta_bloqueada is True 