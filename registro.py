"""Registro de eventos y errores del sistema de gestión de reservas."""

from datetime import datetime


# Guarda las acciones que se realizan correctamente.
def registrar_evento(mensaje):
    fecha = datetime.now()

 # Agrega el evento al archivo de registros.
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] EVENTO: {mensaje}\n")


# Guarda los errores que ocurren durante el programa.
def registrar_error(mensaje):
    fecha = datetime.now()

# Agrega el error al archivo de registros.
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] ERROR: {mensaje}\n")