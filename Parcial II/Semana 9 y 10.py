class Producto:
    def __init__(self,id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f'{self.nombre},Cantidad: {self.cantidad},Precio: {self.precio}'

class Inventario:
    def __init__(self):
        self.productos = {}
    #Creamos un nuevo objeto para cargar el archivo txt o crearlo y también que seleccione las caracterisitcas de cada producto
    def cargar_inventario(self):
        try:
            with open("inventario.txt", "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    if linea.strip():  # Ignorar líneas vacías
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
                        print("Inventario cargado exitosamente.")
        #Excepcion de errores
        except FileNotFoundError:
            print("Error: No se encontró el archivo de inventario. Se creará uno nuevo.")
        except PermissionError:
            print("Error: No tiene permisos para leer el archivo 'inventario.txt'")

    def guardar_inventario(self):
        try:
            with open("inventario.txt", "w") as archivo:
                for producto in self.productos.values():
                    archivo.write(f"{producto}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo 'inventario.txt'.")

    def agregar_productos(self, producto):
        if producto.id_producto in self.productos:
            print("El Producto ya existe.")
        #Añadimos el producto
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print("Producto agregado exitosamente.")
    def eliminar_productos(self, id_producto):
        if id_producto.id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("El Producto fue eliminado.")
        else:
            print("El Producto no existe.")
    def actualizar_productos(self, id_producto, cantidad = None, precio = None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
            else:
                print("Error: Producto no encontrado.")
    def buscar_producto(self,nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: $"))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_productos(producto)
        elif opcion == '2':
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_productos(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad: ")
            precio = input("Ingrese el nuevo precio: $")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_productos(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()

if __name__ == "__main__":
    menu()