# Programa en Python que utiliza constructores (__init__) y destructores (__del__)

class Persona:
    """
    Clase que representa a una persona.
    """

    def __init__(self, nombre, edad):
        """
        Constructor que inicializa los atributos de la persona.
        :param nombre: Nombre de la persona.
        :param edad: Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años.")

    def __del__(self):
        """
        Destructor que se llama cuando el objeto es eliminado.
        """
        print(f"Persona eliminada: {self.nombre}.")

# Demostración del uso de la clase Persona
def main():
    # Crear un objeto de la clase Persona
    persona = Persona("Dennis", 19)
    print(f"Hola, soy {persona.nombre} y tengo {persona.edad} años.")

    # El destructor se llama automáticamente al finalizar el programa o
    # cuando el objeto se elimina..

if __name__ == "__main__":
    main()
