# Programa para calcular el área de un círculo y verificar si excede un umbral

import math  # Importamos el módulo math para acceder a la constante pi


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo

    Retorna:
    float: El área calculada
    """
    return math.pi * (radio ** 2)


# Entrada del usuario para el radio del círculo
radio_circulo = float(input("Introduce el radio del círculo (en unidades): "))

# Cálculo del área utilizando la función
area_circulo = calcular_area_circulo(radio_circulo)

# Mostrar el área calculada
print(f"El área del círculo con radio {radio_circulo} es: {area_circulo:.2f} unidades cuadradas")

# Umbral para comparación
umbral_area = 50.0  # El umbral es un número flotante

# Verificación si el área es mayor al umbral
es_mayor_que_umbral = area_circulo > umbral_area  # Variable booleana

# Mostrar si el área es mayor que el umbral
if es_mayor_que_umbral:
    print(f"El área del círculo es mayor que el umbral de {umbral_area}.")
else:
    print(f"El área del círculo no supera el umbral de {umbral_area}.")
