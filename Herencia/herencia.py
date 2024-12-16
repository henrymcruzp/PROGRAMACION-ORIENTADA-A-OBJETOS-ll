# Definimos una clase base llamada Animal
class Animal:
    # Método hacer_sonido para la clase Animal
    def hacer_sonido(self):
        # Imprime un sonido genérico
        print("Sonido genérico")

# Definimos una clase derivada llamada Perro que hereda de Animal
class Perro(Animal):
    # Sobrescribimos el método hacer_sonido de la clase base
    def hacer_sonido(self):
        # Imprime el sonido específico de un perro
        print("Guau")

# Crear un objeto (instancia) de la clase Perro
mi_perro = Perro()
# Llamamos al método hacer_sonido, el cual ha sido sobrescrito en la clase Perro
mi_perro.hacer_sonido()  # Salida: Guau
