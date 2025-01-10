class Habitacion: #Aqui creamos una clase para hacer las funciones de la reserva de una habitacion
    def __init__(self, numero, tipo, precio):#creamos la funcion principal donde estaran las varaibles que vamos a usar
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self): #Aqui creamos la funcion reservar, y usamos el if para que cuando una habitacion este ocupada diga que esta reservada o este disponible
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self): #aqui en esta funciones hacemos con el if para saber si una habitacion sera libre para que este disponible para otro cliente
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ha sido liberada.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    def mostrar_informacion(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"\n{self.nombre} - Lista de Habitaciones")
        for habitacion in self.habitaciones:
            habitacion.mostrar_informacion()

    def buscar_habitacion_disponible(self, tipo):
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and not habitacion.ocupada:
                return habitacion
        return None

    def reservar_habitacion(self, tipo):
        habitacion = self.buscar_habitacion_disponible(tipo)
        if habitacion:
            habitacion.reservar()
        else:
            print(f"No hay habitaciones disponibles de tipo {tipo}.")


# instancias de las habitaciones
habitacion1 = Habitacion(101, "Simple", 50)
habitacion2 = Habitacion(102, "Doble", 80)
habitacion3 = Habitacion(103, "Suite", 150)

# instancias del hotel y agregar habitaciones
mi_hotel = Hotel("Hotel Paraíso")
mi_hotel.agregar_habitacion(habitacion1)
mi_hotel.agregar_habitacion(habitacion2)
mi_hotel.agregar_habitacion(habitacion3)

# Interacciones
mi_hotel.mostrar_habitaciones()

print("\nIntentando reservar una habitación doble...")
mi_hotel.reservar_habitacion("Doble")

mi_hotel.mostrar_habitaciones()

print("\nLiberando una habitación...")
habitacion2.liberar()

mi_hotel.mostrar_habitaciones()
