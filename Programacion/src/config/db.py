import mysql.connector
from mysql.connector import Error

class ConectorDB:
    def __init__(self, host="localhost", user="root", password="", database="ARGBrokerDB"):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._conexion = None

    def conexion_db(self):
        if self._conexion is None or not self._conexion.is_connected():
            try:
                self._conexion = mysql.connector.connect(
                    host=self._host,
                    user=self._user,
                    password=self._password,
                    database=self._database
                )
            except Error as error:
                raise Exception(f"Error al conectarse a la base de datos: {error}")
        return self._conexion

    def desconectar(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()

    def ejecutar_consulta(self, consulta, parametros=None):
        conexion = self.conexion_db()
        try:
            with conexion.cursor() as cursor:
                if parametros:
                    cursor.execute(consulta, parametros)
                else:
                    cursor.execute(consulta)
                conexion.commit()
        except Error as error:
            raise Exception(f"Error al ejecutar la consulta: {error}")

    def obtener_datos(self, consulta, parametros=None):
        conexion = self.conexion_db()
        try:
            with conexion.cursor() as cursor:
                if parametros:
                    cursor.execute(consulta, parametros)
                else:
                    cursor.execute(consulta)
                resultados = cursor.fetchall()
                return resultados
        except Error as error:
            raise Exception(f"Error al obtener los datos: {error}")
