# Clase base para representar un Animal
class Animal:
    def __init__(self, nombre, sonido):
        """
        Inicializa un objeto Animal.

        Parámetros:
        nombre (str): Nombre del animal
        sonido (str): Sonido que hace el animal
        """
        self.nombre = nombre
        self._sonido = sonido  # Encapsulamos el sonido del animal

    # Metodo para hacer que el animal emita su sonido
    def emitir_sonido(self):
        return f"{self.nombre} dice: {self._sonido}"


# Clase derivada para representar un Perro
class Perro(Animal):
    def __init__(self, nombre, raza):
        """
        Inicializa un objeto Perro, derivado de Animal.

        Parámetros:
        raza (str): Raza del perro
        """
        super().__init__(nombre, "Guau")  # Todos los perros hacen "Guau"
        self.raza = raza

    #  sobrescrito para agregar más detalles
    def emitir_sonido(self):
        return f"{self.nombre} (de raza {self.raza}) ladra: {self._sonido}"


# Clase derivada para representar un Gato
class Gato(Animal):
    def __init__(self, nombre, color):
        """
        Inicializa un objeto Gato, derivado de Animal.

        Parámetros:
        color (str): Color del gato
        """
        super().__init__(nombre, "Miau")  # Todos los gatos hacen "Miau"
        self.color = color

    #  sobrescrito para agregar más detalles
    def emitir_sonido(self):
        return f"{self.nombre}, un gato de color {self.color}, dice: {self._sonido}"


# Ejecución del programa
# Creamos instancias de las clases
mi_perro = Perro("Max", "Labrador")
mi_gato = Gato("Luna", "Blanco")

# Mostramos los sonidos de los animales
print("Sonidos de los animales:")
print(mi_perro.emitir_sonido())
print(mi_gato.emitir_sonido())
