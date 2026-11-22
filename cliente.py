"""Clase Cliente del sistema Software FJ."""

import re
from entidades import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)

        self.__correo = None
        self.__telefono = None

        self.correo = correo
        self.telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str):
            raise ClienteInvalidoError("El correo debe ser texto.")

        patron = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron, nuevo_correo.strip()):
            raise ClienteInvalidoError("El correo electrónico no es válido.")

        self.__correo = nuevo_correo.strip().lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not isinstance(nuevo_telefono, str):
            raise ClienteInvalidoError("El teléfono debe ingresarse como texto.")

        telefono_limpio = nuevo_telefono.strip()

        if not re.fullmatch(r"\+?\d{7,15}", telefono_limpio):
            raise ClienteInvalidoError("El teléfono debe tener entre 7 y 15 dígitos.")

        self.__telefono = telefono_limpio

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
