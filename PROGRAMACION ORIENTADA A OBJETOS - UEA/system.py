import tkinter as tk

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()  # Obtener el texto del campo de entrada
    if dato:
        lista_datos.insert(tk.END, dato)  # Insertar el dato en la lista
        entry.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para limpiar la lista
def limpiar():
    lista_datos.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Establecer un color de fondo para la ventana
ventana.config(bg="#f0f0f0")

# Crear etiqueta con estilo
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 14), bg="#f0f0f0", fg="#333333")
etiqueta.pack(pady=10)  # Agregar un poco de espacio vertical

# Crear campo de texto para ingresar datos con estilo
entry = tk.Entry(ventana, font=("Arial", 12), width=30, bd=2, relief="solid")
entry.pack(pady=5)

# Crear lista para mostrar los datos con estilo
lista_datos = tk.Listbox(ventana, font=("Arial", 12), width=30, height=5, bd=2, relief="solid", bg="#ffffff")
lista_datos.pack(pady=10)

# Crear botón "Agregar" con estilo
btn_agregar = tk.Button(ventana, text="Agregar", font=("Arial", 12), bg="#4CAF50", fg="white", command=agregar_dato, relief="raised")
btn_agregar.pack(pady=5)

# Crear botón "Limpiar" con estilo
btn_limpiar = tk.Button(ventana, text="Limpiar", font=("Arial", 12), bg="#f44336", fg="white", command=limpiar, relief="raised")
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
