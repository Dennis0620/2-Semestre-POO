import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()
    #Una condicional para verificar si los campos estan llenos o no
    if fecha and hora and descripcion:
        tabla.insert("", tk.END, values=(fecha, hora, descripcion))
        entrada_fecha.set_date('')
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")

def eliminar_evento():
    seleccionado = tabla.selection()
    #Condicional para verificar si el usuario quiere eliminar un evento de la tabla
    if seleccionado:
        confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")
        if confirmacion:
            tabla.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Frame para la entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
lbl_fecha = tk.Label(frame_entrada, text="Fecha:")
lbl_fecha.grid(row=0, column=0, padx=5, pady=5)
entrada_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

lbl_hora = tk.Label(frame_entrada, text="Hora:")
lbl_hora.grid(row=1, column=0, padx=5, pady=5)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=5, pady=5)

lbl_descripcion = tk.Label(frame_entrada, text="Descripción:")
lbl_descripcion.grid(row=2, column=0, padx=5, pady=5)
entrada_descripcion = tk.Entry(frame_entrada, width=40)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame para la tabla de eventos
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

# Configuración del Treeview para mostrar eventos
tabla = ttk.Treeview(frame_tabla, columns=("Fecha", "Hora", "Descripción"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripción", text="Descripción")
tabla.pack()

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar la aplicación
ventana.mainloop()
