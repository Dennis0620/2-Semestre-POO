def datostemperatura(): #Definimos una funcion para la parte de regristar las temperaturas diaras
    "Ingresa las temperaturas diaras"
    temperatura = []
    for dia in range(7): #Con este blucle for hacemos que repita la pregunta 7 veces que son los dias de la semana
        tempr = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperatura.append(tempr)
    return temperatura

def calcularpromedio(temperaturas): #Aqui con esta funcion vamos a hacer la operacion para calcular el promedio
    """ Calcular el promedio semanal."""
    return sum(temperaturas) / len(temperaturas)

print("forma tradicional - registro de temperaturas")
temperatura = datostemperatura()
promedio = calcularpromedio(temperatura)
print(f"Promedio semanal de temperatura es: {promedio}")

