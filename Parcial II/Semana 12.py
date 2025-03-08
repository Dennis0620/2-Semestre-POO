class Libros:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = (titulo,)
        self.autor = (autor,)
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_regristrados = set()

    def registrar_usuario(self, usuario):
        #Una condicional para verificar si el usuario ya esta regristado o no
        if usuario.id_usuario in self.usuarios_regristrados:
            print(f"El usuario con ID {usuario.id_usuario} ya esta registrado")
        else:
            self.usuarios_regristrados.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} regristado con exito")

    def regristar_libro(self, libro):
        #Una condicional para verificar si el usuario ya esta regristado o no
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya esta registrado")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo[0]}' Agregado a la biblioteca")

    def quitar_libro(self, isbn):
        #Una condicional para verificar si el libro existe o no para poder eliminarlo
        if isbn in self.libros_disponibles:
            libro_removido = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro_removido.titulo[0]}' eliminado a la biblioteca")
        else:
            print(f"No se encontro el libro con ISBN {isbn} en la biblioteca")

    def prestar_libro(self, isbn, usuario):
        #Aqui usamos if y elif para verificar si el usuario esta regristado o no y para prestar el libro
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} ya esta registrado")
        elif usuario.id_usuario not in self.usuarios_regristrados:
            print(f"El usuario con ID {usuario.id_usuario} no esta registrado")
        else:
            libro = self.libros_disponibles[isbn]
            usuario.libros_prestados.append(libro)
            print(f"El libro '{libro.titulo[0]}' fue prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn,usuario):
        #Dentro del ciclo for verificamos si el libro esta prestado o no y de que usuario lo devuelve
        # Verificar que el libro esté en la lista de libros prestados del usuario
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)  # Remover el libro de la lista de usuarios
                self.libros_disponibles[isbn] = libro  # Agregar el libro de vuelta a la biblioteca
                print(f"El libro '{libro.titulo[0]}' fue devuelto a la biblioteca por {usuario.nombre}.")
                return

    def buscar_libros(self, criterio, valor):
        #Con el ciclo for buscamos en la lista los libros que desea el usuario buscar
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.titulo[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor[0].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print(f"Se encontraron {len(resultados)} libro(s) que coinciden con el criterio '{criterio}':")
            for libro in resultados:
                print(f"- {libro.titulo[0]} por {libro.autor[0]} (Categoría: {libro.categoria}, ISBN: {libro.isbn})")
        else:
            print(f"No se encontraron libros para el criterio '{criterio}' con el valor '{valor}'.")

    def lista_libros_prestados(self, usuario):
        #Métodos anteriores omitidos para mayor claridad
        if not usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro.titulo[0]} por {libro.autor[0]} (ISBN: {libro.isbn})")
                # Crear la biblioteca, un usuario y algunos libros

def mostrar_menu():
    print("\n----- Menú de Biblioteca -----")
    print("1. Registrar usuario")
    print("2. Registrar libro")
    print("3. Quitar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Buscar libros")
    print("7. Listar libros prestados")
    print("8. Salir")
    print("--------------------------------")

mi_biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = int(input("Ingrese el ID único del usuario: "))
        usuario = Usuario(nombre, id_usuario)
        mi_biblioteca.registrar_usuario(usuario)

    elif opcion == "2":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libros(titulo, autor, categoria, isbn)
        mi_biblioteca.regristar_libro(libro)

    elif opcion == "3":
        isbn = input("Ingrese el ISBN del libro a quitar: ")
        mi_biblioteca.quitar_libro(isbn)

    elif opcion == "4":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        usuario_encontrado = None
        for id_registrado in mi_biblioteca.usuarios_regristrados:
            if id_registrado == id_usuario:
                usuario_encontrado = Usuario("Temporal", id_usuario)  # Usuario temporal
                break
        if usuario_encontrado:
            mi_biblioteca.prestar_libro(isbn, usuario_encontrado)
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    elif opcion == "5":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        usuario_encontrado = None
        for id_registrado in mi_biblioteca.usuarios_regristrados:
            if id_registrado == id_usuario:
                usuario_encontrado = Usuario("Temporal", id_usuario)  # Usuario temporal
                break
        if usuario_encontrado:
            mi_biblioteca.devolver_libro(isbn, usuario_encontrado)
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    elif opcion == "6":
        criterio = input("Ingrese el criterio de búsqueda (titulo, autor, categoria): ").lower()
        valor = input("Ingrese el valor a buscar: ")
        mi_biblioteca.buscar_libros(criterio, valor)

    elif opcion == "7":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        usuario_encontrado = None
        for id_registrado in mi_biblioteca.usuarios_regristrados:
            if id_registrado == id_usuario:
                usuario_encontrado = Usuario("Temporal", id_usuario)  # Usuario temporal
                break
        if usuario_encontrado:
            mi_biblioteca.lista_libros_prestados(usuario_encontrado)
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    elif opcion == "8":
        print("¡Gracias por usar el sistema de gestión de biblioteca!")
        break

    else:
        print("Opción no válida, por favor intente nuevamente.")

