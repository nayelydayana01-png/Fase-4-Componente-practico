"""Clase abstracta general del sistema de gestión de reservas."""

from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


class Entidad(ABC):

    def __init__(self, identificacion, nombre):

# Comprueba que la identificacíon no este vacía, osea sin texto
        if not identificacion:
            raise DatoInvalidoError("La identificación es obligatoria.")

# Verifica que se alla ingresado el nombre del cliente 
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")
        
# Pernite guarda los datos como atributos privados 
        self.__identificacion = identificacion
        self.__nombre = nombre.strip()

# Permite consultar la identificación
    @property
    def identificacion(self):
        return self.__identificacion
    
# Permite consultar el nombre 
    @property
    def nombre(self):
        return self.__nombre
    
# Obliga a las clases hijas a mostrar su información 
    @abstractmethod
    def mostrar_informacion(self):
        pass
