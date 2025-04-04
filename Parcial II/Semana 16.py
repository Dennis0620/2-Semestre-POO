import tkinter as tk
from tkinter import messagebox

class ListaTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas
        self.tareas = []

        # Campo de entrada
        self.entry_tareas = tk.Entry(root, width=40)
        self.entry_tareas.grid(row=0, column=0, padx=10, pady=10)
        self.entry_tareas.bind("<Return>", self.agregar_tarea)  # Añadir tarea con Enter

        # Botones
        btn_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=1, padx=10, pady=10)

        btn_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completado)
        btn_completar.grid(row=1, column=0, padx=10, pady=10)

        btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.grid(row=1, column=1, padx=10, pady=10)

        # Listbox para mostrar las tareas
        self.listbox_tareas = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox_tareas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        #Atajos teclado
        # Atajos de teclado corregidos
        root.bind('<Escape>', lambda e: root.quit())
        root.bind('c', lambda e: self.marcar_completado())  # Tecla 'C' para marcar como completada
        root.bind('d', lambda e: self.eliminar_tarea())  # Tecla 'Delete' para eliminar
        root.bind('<Return>', lambda e: self.marcar_completado() if self.listbox_tareas.curselection() else self.agregar_tarea())

    def agregar_tarea(self, event=None):
        """Añadir una nueva tarea a la lista"""
        tarea = self.entry_tareas.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})  # Clave corregida
            self.listbox_tareas.insert(tk.END, tarea)
            self.entry_tareas.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escriba una tarea antes de agregarla.")

    def marcar_completado(self):
        """Marcar la tarea seleccionada como completada"""
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            tarea_texto = self.tareas[indice]["texto"] + " (Completada)"
            self.listbox_tareas.delete(indice)
            self.listbox_tareas.insert(indice, tarea_texto)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")  # Mensaje corregido

    def eliminar_tarea(self):
        """Eliminar la tarea seleccionada"""
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas.pop(indice)
            self.listbox_tareas.delete(indice)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()