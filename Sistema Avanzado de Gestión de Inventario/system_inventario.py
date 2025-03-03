
### Paso 1: Definir las clases `Producto` e `Inventario`

import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos de la clase Producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter y setter para cada atributo
    def obtener_id(self):
        return self.id_producto

    def establecer_id(self, id_producto):
        self.id_producto = id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        # metodo para representar al producto como una cadena
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar productos, donde la clave es el ID del producto
        self.productos = {}

    # metodo para añadir un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.obtener_id()] = producto
            print(f"Producto {producto.obtener_nombre()} añadido al inventario.")

    # metodo para eliminar un producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    # metodo para actualizar la cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    # metodo para buscar un producto por nombre
    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.obtener_nombre().lower():
                print(producto)
                return
        print(f"No se encontró ningún producto con el nombre '{nombre}'.")

    # metodo para mostrar todos los productos del inventario
    def mostrar_todos_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    # metodo para guardar el inventario en un archivo JSON
    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            inventario_data = {id_prod: vars(prod) for id_prod, prod in self.productos.items()}
            json.dump(inventario_data, f, indent=4)
            print("Inventario guardado en archivo.")

    # metodo para cargar el inventario desde un archivo JSON
    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                inventario_data = json.load(f)
                self.productos = {id_prod: Producto(id_prod, prod['nombre'], prod['cantidad'], prod['precio'])
                                  for id_prod, prod in inventario_data.items()}
                print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

### Paso 2: Crear la interfaz de usuario

def menu():
    inventario = Inventario()
    archivo = "inventario.json"
    inventario.cargar_inventario(archivo)

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Añadir un producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            # Eliminar un producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            # Actualizar un producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco si no deseas cambiar): ")
            precio = input("Nuevo precio (deja en blanco si no deseas cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            # Buscar producto por nombre
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            # Mostrar todos los productos
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            # Guardar inventario en archivo
            inventario.guardar_inventario(archivo)

        elif opcion == '7':
            # Salir del sistema
            print("Saliendo del sistema...")
            inventario.guardar_inventario(archivo)
            break

        else:
            print("Opción no válida. Intente de nuevo.")

### Paso 3: Ejecutar el programa


if __name__ == "__main__":
    menu()
