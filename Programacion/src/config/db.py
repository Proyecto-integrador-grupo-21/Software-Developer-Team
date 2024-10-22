import mysql.connector
from mysql.connector import Error

# En rasgos generales esta armado la clase Conector, queda a revisar y gestionar mejoras
class ConectorDB:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "ARGBrokerDB"
        self.conexion = None

    def conexion_db(self):
        if self.conexion is None or not self.conexion.is_connected():
            try:
                self.conexion = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            except Error as error:
                raise Exception(f"Error al conectarse a la base de datos: {error}")
        return self.conexion

    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()

    def ejecutar_consulta(self, consulta, parametros=None):
        conexion = self.conexion_db()
        try:
            cursor = conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            conexion.commit()
            return cursor
        except Error as error:
            raise Exception(f"Error al ejecutar la consulta: {error}")
        finally:
            cursor.close()
\
    def obtener_datos(self, consulta, parametros=None):
        conexion = self.conexion_db()
        try:
            cursor = conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
        except Error as error:
            raise Exception(f"Error al obtener los datos: {error}")
        finally:
            cursor.close()