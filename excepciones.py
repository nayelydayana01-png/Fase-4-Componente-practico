
"""Excepciones personalizadas del sistema de gestión de reservas."""

# Error general del sistema
class ErrorSistema(Exception):
    pass

# Se utiliza cuando un dato no cumple con las condiciones
class DatoInvalidoError(ErrorSistema):
    pass

# Se utiliza cuando la información de un cliente es incorrecta
class ClienteInvalidoError(DatoInvalidoError):
    pass

# Se utiliza cuando se intenta usar un servicio no disponible
class ServicioNoDisponibleError(ErrorSistema):
    pass

# Se utiliza cuando una reserva tiene algún problema
class ReservaInvalidaError(ErrorSistema): 
    pass

# Se utiliza cuando falta información necesaria
class DatosFaltantesError(ErrorSistema):
    pass

