"""Programa principal del sistema de gestion de reservas."""

# Sirve para importar las clases necesarias para poder realizar las operaciones
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteInvalidoError, DatosFaltantesError
from registro import registrar_evento, registrar_error

# Estas son las listas donde se guardan los datos durante la ejecución
clientes = []
servicios = []
reservas = []

# Ejecuta cada operación y controla los errores que puedan llegar a presentarse
def ejecutar_operacion(numero, descripcion, accion):
    """Ejecuta una operación y controla cualquier error."""

    print(f"\n--- OPERACIÓN {numero}: {descripcion} ---")

    try:
        accion()

    except Exception as error:
        print(f"Error controlado: {error}")
        registrar_error(f"Operación {numero}: {descripcion}. Error: {error}")

    else:
        print("Operación realizada correctamente.")
        registrar_evento(f"Operación {numero}: {descripcion} realizada correctamente.")

    finally:
        print(f"Se finalizó la operación {numero}.")

# Registra un cliente con sus datos personales
def crear_cliente():
    cliente = Cliente("1001", "Carlos Pérez", "carlos@gmail.com", "3001234567")

    clientes.append(cliente)
    print(cliente.mostrar_informacion())

# Prueba el registro de un cliente con un correo incorrecto
def cliente_correo_invalido():
    Cliente("1002", "Ana López", "correo_incorrecto", "3001234568")

# Prueba la validación del número telefonico
def cliente_telefono_invalido():
    Cliente("1003", "Pedro Gómez", "pedro@gmail.com", "123")

# Registra un servicio de una reserva de sala
def crear_servicio_sala():
    servicio = ReservaSala("S001", "Sala de reuniones", 50000)

    servicios.append(servicio)
    print(servicio.describir_servicio())

# Registra un servicio de alquiler de equipos
def crear_servicio_equipo():
    servicio = AlquilerEquipo("S002", "Computador portátil", 30000)

    servicios.append(servicio)
    print(servicio.describir_servicio())

# Registra un servicio de asesoria especializada
def crear_servicio_asesoria():
    servicio = AsesoriaEspecializada("S003", "Asesoría tecnológica", 40000)

    servicios.append(servicio)
    print(servicio.describir_servicio())

# Comprueba la validación de la tarifa de un servicio
def crear_servicio_invalido():
    ReservaSala("S004", "Sala no válida", -50000)

# Crea una reserva, la confirma y calcula su costo
def reserva_exitosa():
    reserva = Reserva("R001", clientes[0], servicios[0], 2)

    reservas.append(reserva)

    print(reserva.confirmar())

    total = reserva.procesar(impuesto=19, descuento=10)

    print(f"Total de la reserva: ${total:,.2f}")
    print(reserva.mostrar_informacion())


# Intenta realizar una reserva de un servicio ocupado
def reserva_no_disponible():
    servicio = ReservaSala("S005", "Sala ocupada", 50000, disponible=False)

    servicios.append(servicio)

    Reserva("R002", clientes[0], servicio, 2)


# Sirve para realizar la cancelación de una reserva
def reserva_cancelada():
    reserva = Reserva("R003", clientes[0], servicios[1], 1)

    reservas.append(reserva)

    print(reserva.cancelar())
    print(reserva.mostrar_informacion())


# Sirve para intentar procesar una reserva que sigue sin confirmar o pendiente
def reserva_sin_confirmar():
    reserva = Reserva("R004", clientes[0], servicios[2], 1)

    reservas.append(reserva)
    reserva.procesar()


# Comprueba el amnejo de errores relacionados entre si
def error_encadenado():
    try:
        Cliente("1004", "María Ruiz", "correo_mal_escrito", "3001234569")

    except ClienteInvalidoError as error:
        raise DatosFaltantesError(
            "No fue posible registrar el cliente debido a sus datos."
        ) from error


# Comprueba los calculos con impuestos y descuentos
def probar_calculo_costos():
    servicio = servicios[0]

    costo_normal = servicio.calcular_costo(2)

    costo_con_impuesto = servicio.calcular_costo(2, 19)

    costo_con_impuesto_descuento = servicio.calcular_costo(2, 19, 10)

    print(f"Costo normal: ${costo_normal:,.2f}")
    print(f"Costo con impuesto: ${costo_con_impuesto:,.2f}")
    print(f"Costo con impuesto y descuento: ${costo_con_impuesto_descuento:,.2f}")


print("======================================")
print(" SISTEMA DE GESTIÓN DE RESERVAS")
print("======================================")

ejecutar_operacion(1, "Registro válido de cliente", crear_cliente)
ejecutar_operacion(2, "Registro con correo inválido", cliente_correo_invalido)
ejecutar_operacion(3, "Registro con teléfono inválido", cliente_telefono_invalido)
ejecutar_operacion(4, "Creación de reserva de sala", crear_servicio_sala)
ejecutar_operacion(5, "Creación de alquiler de equipo", crear_servicio_equipo)
ejecutar_operacion(6, "Creación de asesoría especializada", crear_servicio_asesoria)
ejecutar_operacion(
    7, "Creación de servicio con tarifa incorrecta", crear_servicio_invalido
)
ejecutar_operacion(8, "Reserva exitosa", reserva_exitosa)
ejecutar_operacion(9, "Reserva con servicio no disponible", reserva_no_disponible)
ejecutar_operacion(10, "Cancelación de reserva", reserva_cancelada)
ejecutar_operacion(11, "Procesamiento sin confirmar", reserva_sin_confirmar)
ejecutar_operacion(12, "Prueba de excepción encadenada", error_encadenado)
ejecutar_operacion(
    13, "Prueba de variantes del cálculo de costos", probar_calculo_costos
)

print("\n===== RESUMEN DE LAS LISTAS =====")
print(f"Clientes registrados: {len(clientes)}")
print(f"Servicios registrados: {len(servicios)}")
print(f"Reservas registradas: {len(reservas)}")

print("\n======================================")
print(" FIN DE LAS PRUEBAS DEL SISTEMA")
print("======================================")
