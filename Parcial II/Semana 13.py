import tkinter as tk
from tkinter import messagebox

def agregar_datos():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")
def limpiar_datos():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de datos")
ventana.geometry("300x300")

# Etiqueta para mensaje
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
tabla_frame = tk.Frame(ventana)
tabla_frame.pack(pady=5)

lista_datos = tk.Listbox(tabla_frame, width=30)
lista_datos.pack()

# Botón para limpiar lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
