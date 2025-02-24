# Clase Producto: Representa un producto con ID, nombre, cantidad y precio
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad  # Actualiza la cantidad del producto

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # Actualiza el precio del producto

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_string(self):
        """Convierte un producto a formato de texto para almacenamiento en archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

# Clase Inventario: Maneja una lista de productos y operaciones sobre ellos
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []  # Lista para almacenar los productos
        self.archivo = archivo  # Ruta del archivo de inventario
        self.cargar_inventario()  # Cargar productos desde el archivo al iniciar el programa

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar."""
        try:
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    id_producto, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, "w") as archivo:
                for producto in self.productos:
                    archivo.write(producto.to_string() + "\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error de permisos: No se pudo escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añadir un producto al inventario y al archivo."""
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto por ID y actualizar el archivo."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_inventario()
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar un producto existente y reflejar los cambios en el archivo."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.actualizar_cantidad(cantidad)
                if precio is not None:
                    producto.actualizar_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre y mostrarlos."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        for p in encontrados:
            print(p)
        if not encontrados:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Mostrar todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Función de menú interactivo en la consola
def menu():
    inventario = Inventario()  # Se crea un objeto de Inventario
    while True:
        # Muestra las opciones del menú
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Captura los datos del nuevo producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            # Captura el ID del producto a eliminar
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            # Captura el ID y los valores a actualizar
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            # Captura el nombre del producto a buscar
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            # Muestra el inventario completo
            inventario.mostrar_productos()
        elif opcion == "6":
            # Sale del programa
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
