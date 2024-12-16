
# Definimos una clase llamada Coche
class Coche:
    # El constructor __init__ se ejecuta al crear un objeto de la clase Coche
    def __init__(self, marca, modelo):
        # Inicializa los atributos marca y modelo del coche
        self.marca = marca
        self.modelo = modelo

    # Definimos un método llamado encender que imprime un mensaje
    def encender(self):
        # Imprime que el coche está encendido
        print(f"El coche {self.marca} {self.modelo} está encendido.")

# Crear un objeto (instancia) de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
# Llamamos al método encender, el cual imprime un mensaje con el estado del coche
mi_coche.encender()
