from abc import ABC, abstractmethod

class InterfazDao (ABC):
    @abstractmethod
    def crear(self, obj):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

    @abstractmethod
    def modificar(self, obj):
        pass

    @abstractmethod
    def obtener(self, id):
        pass