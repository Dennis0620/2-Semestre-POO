class clima: #creamos una clase para abarcar todas las fuciones necesarias para el proceso de agregar y promediar las temperaturas
    def __init__(self):
        self.temperatura = []
    def agregartemperatura(self, temperatura):
        "Agrega una temperatura a la lista"
        self.temperatura.append(temperatura)
    def calcularpromedio(self):
        if len(self.temperatura) == 0:
            return 0
        return sum(self.temperatura) / len(self.temperatura)

print("Forma POO - Registro de temperaturas")
clima = clima()

for dia in range(7):
    temp = float(input(f"Ingresa la temperatura del dia {dia + 1}: "))
    clima.agregartemperatura(temp)

promedio = clima.calcularpromedio()
print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")
