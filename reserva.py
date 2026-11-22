"""Clase Reserva del sistema de gestión de reservas."""

from excepciones import ReservaInvalidaError, DatosFaltantesError
from registro import registrar_evento

# Representación de las reservas realizadas por los clientes
class Reserva:
    """Representa una reserva realizada por un cliente."""

    def __init__(self, identificacion, cliente, servicio, duracion):

#Comprueba que la reserva tenga una identificación
        if not identificacion:
            raise DatosFaltantesError("La identificación de la reserva es obligatoria.")

# Verifica que se hayan seleccionado un cliente y un servicio
        if cliente is None or servicio is None:
            raise DatosFaltantesError("La reserva debe tener un cliente y un servicio.")

# Sirve para comprobar que la duración sea valida
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ReservaInvalidaError("La duración debe ser mayor que cero.")

# Sirve para verificar que el servicio pueda utilizarse durante ese tiempo
        servicio.validar_parametros(duracion)

# Guarda la información de la reserva 
        self.__identificacion = identificacion
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__total = 0

        registrar_evento(f"Reserva {identificacion} creada correctamente.")

# Permiten consultar los datos de la reserva
    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def total(self):
        return self.__total

# Sirve para cambiar el estado de la reserva a confirmada
    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError("Solo se pueden confirmar reservas pendientes.")

        self.__estado = "Confirmada"

        registrar_evento(f"Reserva {self.__identificacion} confirmada.")

        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        if self.__estado in ("Cancelada", "Procesada"):
            raise ReservaInvalidaError("No se puede cancelar esta reserva.")

        self.__estado = "Cancelada"

        registrar_evento(f"Reserva {self.__identificacion} cancelada.")

        return "La reserva fue cancelada."

# Calcula el costo y finalización del proceso de la reserva
    def procesar(self, impuesto=0, descuento=0):
        if self.__estado != "Confirmada":
            raise ReservaInvalidaError("Primero debe confirmar la reserva.")

        self.__total = self.__servicio.calcular_costo(
            self.__duracion, impuesto, descuento
        )

        self.__estado = "Procesada"

        registrar_evento(
            f"Reserva {self.__identificacion} procesada. "
            f"Total: ${self.__total:,.2f}"
        )

        return self.__total

# Muestra los datos y el estado actual de la reserva
    def mostrar_informacion(self):
        return (
            f"Reserva: {self.__identificacion}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Total: ${self.__total:,.2f}"
        )
