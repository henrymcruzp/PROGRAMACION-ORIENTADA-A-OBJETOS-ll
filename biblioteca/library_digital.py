class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.usuario_id}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs únicos de usuarios
        self.usuarios = {}  # Diccionario con ID como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.usuario_id)
            self.usuarios[usuario.usuario_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            del self.usuarios[usuario_id]
            self.usuarios_registrados.remove(usuario_id)
            print(f"Usuario con ID {usuario_id} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[usuario_id]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("No se pudo realizar el préstamo. Verifique el usuario y el ISBN.")

    def devolver_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios:
            usuario = self.usuarios[usuario_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene ese libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros_disponibles.values():
            if all(getattr(libro, key, None) == value for key, value in criterios.items()):
                resultados.append(str(libro))
        return resultados if resultados else "No se encontraron libros."

    def listar_libros_prestados(self, usuario_id):
        if usuario_id in self.usuarios:
            usuario = self.usuarios[usuario_id]
            return [str(libro) for libro in
                    usuario.libros_prestados] if usuario.libros_prestados else "No tiene libros prestados."
        return "Usuario no encontrado."


# Pruebas del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Distopía", "123456789")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "987654321")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María Gómez", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "123456789")
biblioteca.devolver_libro("U001", "123456789")

# Búsqueda de libros
print(biblioteca.buscar_libro(categoria="Distopía"))

# Listar libros prestados
print(biblioteca.listar_libros_prestados("U001"))
