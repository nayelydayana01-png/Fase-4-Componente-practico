"""Servicios especializados de gestión de reservas."""

from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import DatoInvalidoError,ServicioNoDisponibleError


class Servicio(Entidad, ABC):
    """Clase abstracta para los servicios de la empresa."""

    def __init__(self, identificacion, nombre, tarifa, disponible=True):
        super().__init__(identificacion, nombre)

# Comprubea que la tarifa sea un valor mayor a cero
        if (
            not isinstance(tarifa, (int, float))
            or isinstance(tarifa, bool)
            or tarifa <= 0
        ):
            raise DatoInvalidoError("La tarifa debe ser un número mayor a cero.")

# Verifica que la disponibilidad sea verdadera o falsa
        if not isinstance(disponible, bool):
            raise DatoInvalidoError("La disponibilidad debe ser verdadera o falsa.")

# Guarda la tarifa y el estado del servicio
        self.__tarifa = tarifa
        self.__disponible = disponible

# Permite consultar la tarifa y la disponibilidad
    @property
    def tarifa(self):
        return self.__tarifa

    @property
    def disponible(self):
        return self.__disponible

# Comprueba que la duración sea válida y que el servicio esté disponible 
    def _validar_duracion(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise DatoInvalidoError("La duración debe ser un número mayor a cero.")

        if not self.__disponible:
            raise ServicioNoDisponibleError("El servicio no está disponible.")

# Sirve para establecer los métodos que deben tener los servicios especializados
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

# Muestra los datos generales del servicio
    def mostrar_informacion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Tarifa por hora: ${self.tarifa:,.2f}\n"
            f"Disponible: {self.disponible}"
        )


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

# Sirve para comprobar la duración de la reserva sea correcta
    def validar_parametros(self, duracion):
        self._validar_duracion(duracion)

# Calcula el costo de la sala con impuesto y despcuento opcionales
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100

        return round(total, 2)

# Devuelve una descripción de la sala 
    def describir_servicio(self):
        return (
            f"Reserva de sala: {self.nombre}. "
            "Espacio disponible para reuniones y actividades."
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

# Sirve para comprobar la duración del alquiler sea correcta
    def validar_parametros(self, duracion):
        self._validar_duracion(duracion)

# Clacula el costo del equipo incluyendo un recargo del 10%
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        subtotal = self.tarifa * duracion
        recargo = subtotal * 0.10
        subtotal += recargo

        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100

        return round(total, 2)

# Su función es devolver una descripción del equipo
    def describir_servicio(self):
        return (
            f"Alquiler de equipo: {self.nombre}. "
            "Equipo tecnológico disponible para alquiler."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría tecnológica especializada."""

# Comprueba que la duración de la asesoria sea correcta
    def validar_parametros(self, duracion):
        self._validar_duracion(duracion)

# Sirve para calcular el costo de la asesoria incluyendo un recargo del 15%
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        subtotal = self.tarifa * duracion
        recargo = subtotal * 0.15
        subtotal += recargo

        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100

        return round(total, 2)

# Devulve una descripción de la asesoria 
    def describir_servicio(self):
        return (
            f"Asesoría especializada: {self.nombre}. "
            "Orientación y acompañamiento tecnológico."
        )
