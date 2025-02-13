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
    def agregar_productos(self, producto):
        if producto.id_producto in self.productos:
            print("El Producto ya existe.")
        #Añadimos el producto
        else:
            self.productos[producto.id_producto] = producto
    def eliminar_productos(self, id_producto):
        if id_producto.id_producto in self.productos:
            del self.productos[id_producto]
            print("El Producto fue eliminado.")
        else:
            print("El Producto no existe.")
    def actualizar_productos(self, id_producto, cantidad = None, precio = None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
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
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_productos(producto)
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_productos(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad: ")
            precio = input("Ingrese el nuevo precio: ")
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