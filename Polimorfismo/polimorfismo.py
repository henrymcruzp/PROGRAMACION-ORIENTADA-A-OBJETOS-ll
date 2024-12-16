# Definimos una clase Gato
class Gato:
    # Método hacer_sonido para la clase Gato
    def hacer_sonido(self):
        # Imprime el sonido específico de un gato
        print("Miau")

# Definimos una clase Vaca
class Vaca:
    # Método hacer_sonido para la clase Vaca
    def hacer_sonido(self):
        # Imprime el sonido específico de una vaca
        print("Muu")

# Función que recibe un animal y llama a su método hacer_sonido
def hacer_sonido_del_animal(animal):
    # Llama al método hacer_sonido del objeto animal
    animal.hacer_sonido()

# Crear instancias de las clases Gato y Vaca
mi_gato = Gato()
mi_vaca = Vaca()

# Llamamos a la función hacer_sonido_del_animal con el gato y la vaca
hacer_sonido_del_animal(mi_gato)  # Salida: Miau
hacer_sonido_del_animal(mi_vaca)  # Salida: Muu
