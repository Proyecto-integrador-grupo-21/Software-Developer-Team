from db import ConectorDB

class InversorDao():
    def __init__(self):
        self.conector = ConectorDB()

    def crear(self, inversor):
        consulta = """
        INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, direccion, telefono, perfil_inversor, cuenta_bloqueada, saldo_cuenta)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        parametros = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.direccion, inversor.telefono, inversor.perfil_inversor, inversor.cuenta_bloqueada, inversor.saldo_cuenta)
        self.conector.ejecutar_consulta(consulta, parametros)

    def eliminar(self, id):
        consulta = "DELETE FROM inversor WHERE id = %s"
        parametros = (id,)
        self.conector.ejecutar_consulta(consulta, parametros)

    def modificar(self, inversor):
        consulta = """
        UPDATE inversor
        SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s, direccion = %s, telefono = %s, perfil_inversor = %s, cuenta_bloqueada = %s, saldo_cuenta = %s
        WHERE id = %s
        """
        parametros = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.direccion, inversor.telefono, inversor.perfil_inversor, inversor.cuenta_bloqueada, inversor.saldo_cuenta, inversor.id)
        self.conector.ejecutar_consulta(consulta, parametros)

    def obtener(self, id):
        consulta = "SELECT * FROM inversor WHERE id = %s"
        parametros = (id,)
        return self.conector.obtener_datos(consulta, parametros)

    def obtener_todos(self):
            consulta = "SELECT * FROM inversor"
            return self.conector.obtener_datos(consulta)
    
    def consulta_personalizada(self, consulta, parametros=None):
        return self.conector.obtener_datos(consulta,parametros)
         
if __name__ == "__main__":
    lel = InversorDao()

    print(lel.obtener_todos())