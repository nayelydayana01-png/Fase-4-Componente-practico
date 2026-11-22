import tkinter as tk
from tkinter import messagebox

def registrar_cliente():
    messagebox.showinfo(
        "Registro de Cliente",
        "Funcionalidad de registro de clientes disponible."
    )

def crear_reserva():
    messagebox.showinfo(
        "Crear Reserva",
        "Funcionalidad de creación de reservas disponible."
    )

def ver_reservas():
    messagebox.showinfo(
        "Reservas",
        "Consulta de reservas disponible."
    )

ventana = tk.Tk()

ventana.title("Software FJ")
ventana.geometry("650x500")
ventana.resizable(False, False)
ventana.config(bg="#E8EEF7")


titulo = tk.Label(
    ventana,
    text="SOFTWARE FJ",
    font=("Arial", 22, "bold"),
    bg="#E8EEF7",
    fg="#003366"
)

titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Sistema de Gestión de Clientes, Servicios y Reservas",
    font=("Arial", 14),
    bg="#E8EEF7",
    fg="#333333"
)

subtitulo.pack(pady=5)

frame_botones = tk.Frame(
    ventana,
    bg="#E8EEF7"
)

frame_botones.pack(pady=30)


btn_cliente = tk.Button(
    frame_botones,
    text="Registrar Cliente",
    width=30,
    height=2,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=registrar_cliente
)

btn_cliente.pack(pady=10)

btn_reserva = tk.Button(
    frame_botones,
    text="Crear Reserva",
    width=30,
    height=2,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    command=crear_reserva
)

btn_reserva.pack(pady=10)

btn_consultar = tk.Button(
    frame_botones,
    text="Ver Reservas",
    width=30,
    height=2,
    bg="#FF9800",
    fg="white",
    font=("Arial", 11, "bold"),
    command=ver_reservas
)

btn_consultar.pack(pady=10)

btn_salir = tk.Button(
    frame_botones,
    text="Salir",
    width=30,
    height=2,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold"),
    command=ventana.destroy
)

btn_salir.pack(pady=10)

pie = tk.Label(
    ventana,
    text="Proyecto POO - Gestión de Reservas | Software FJ",
    font=("Arial", 10, "italic"),
    bg="#E8EEF7",
    fg="#666666"
)

pie.pack(side="bottom", pady=20)

ventana.mainloop()