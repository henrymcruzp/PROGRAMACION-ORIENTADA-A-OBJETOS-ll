import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar  # Importa el widget de calendario

# Funciones para manejar los eventos
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        # Agregar el evento a la lista
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

def eliminar_evento():
    # Eliminar el evento seleccionado
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)
    else:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione un evento para eliminar.")

def salir():
    # Confirmación de salida
    respuesta = messagebox.askyesno("Confirmar salida", "¿Seguro que quieres salir?")
    if respuesta:
        root.quit()

def seleccionar_fecha(event):
    # Obtener la fecha seleccionada del calendario
    selected_date = calendario.get_date()
    entry_fecha.delete(0, tk.END)
    entry_fecha.insert(0, selected_date)

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")  # Tamaño de la ventana

# Colores y estilo
root.config(bg="lightblue")

# Crear los contenedores (Frames)
frame_lista = tk.Frame(root, bg="lightblue")
frame_lista.pack(padx=10, pady=10)

frame_entrada = tk.Frame(root, bg="lightblue")
frame_entrada.pack(padx=10, pady=10)

frame_botones = tk.Frame(root, bg="lightblue")
frame_botones.pack(padx=10, pady=10)

# Crear la TreeView (para mostrar los eventos)
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Crear los campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha:", bg="lightblue")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):", bg="lightblue")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:", bg="lightblue")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Crear el calendario (DatePicker)
calendario = Calendar(frame_entrada, selectmode="day", date_pattern="yyyy-mm-dd")
calendario.grid(row=0, column=2, padx=10, pady=10)

# Vincular el calendario con la entrada de fecha
calendario.bind("<<CalendarSelected>>", seleccionar_fecha)

# Crear los botones con colores
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="lightgreen", fg="black")
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="lightcoral", fg="black")
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir, bg="lightsalmon", fg="black")
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Ejecutar la ventana
root.mainloop()
