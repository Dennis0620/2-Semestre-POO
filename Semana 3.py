def datostemperatura():
    "Ingresa las temperaturas diaras"
    temperatura = []
    for dia in range(7):
        tempr = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperatura.append(tempr)
    return temperatura

def calcularpromedio(temperaturas):
    """ Calcular el promedio semanal."""
    return sum(temperaturas) / len(temperaturas)

pirnt = (print("forma tradicional - registro de temperaturas"))
temperatura = datostemperatura()
promedio = calcularpromedio(temperatura)
print(f"Promedio semanal de temperatura es: {promedio}")

