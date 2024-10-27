from abc import ABC, abstractmethod

class InterfazDao(ABC):
    @abstractmethod
    def crear(self, obj) -> bool:
        """
        Crea un nuevo registro en la base de datos.
        :param obj: El objeto que se va a insertar.
        :return: True si la creación fue exitosa, False en caso contrario.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int) -> bool:
        """
        Elimina un registro de la base de datos por su ID.
        :param id: El ID del registro a eliminar.
        :return: True si la eliminación fue exitosa, False en caso contrario.
        """
        pass

    @abstractmethod
    def modificar(self, obj) -> bool:
        """
        Modifica un registro existente en la base de datos.
        :param obj: El objeto con los nuevos datos.
        :return: True si la modificación fue exitosa, False en caso contrario.
        """
        pass

    @abstractmethod
    def obtener(self, id: int):
        """
        Obtiene un registro de la base de datos por su ID.
        :param id: El ID del registro a obtener.
        :return: El objeto correspondiente al registro, o None si no se encuentra.
        """
        pass

    @abstractmethod
    def obtener_todos(self):
        """
        Obtiene todos los registros de la base de datos.
        :return: Una lista de todos los objetos.
        """
        pass
