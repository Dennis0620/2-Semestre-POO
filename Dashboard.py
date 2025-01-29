import os
from colorama import Fore, Style

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    # Pausa para que el usuario pueda leer el código antes de volver al menú
    input(Fore.YELLOW + "\nPresiona Enter para volver al menú..." + Style.RESET_ALL)


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    print(Fore.CYAN + """ 
        ===============================
          Bienvenido al Dashboard
          Gestiona tus proyectos fácilmente
        ===============================
        """ + Style.RESET_ALL)

    opciones = {
        '1': 'Semana 2.py',
        '2': 'Semana 3.py',
        '3': 'Semana 4.py',
        '4': 'Semana 5.py',
        '5': 'Semana 6.py',
        '6': 'Semana 7.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()