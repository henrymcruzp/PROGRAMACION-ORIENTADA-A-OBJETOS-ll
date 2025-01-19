# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.__modelo = modelo  # Atributo privado (encapsulación)

    # Getter para obtener el modelo (acceso al atributo privado)
    def obtener_modelo(self):
        return self.__modelo

    # Método común para todos los vehículos
    def mostrar_info(self):
        return f"Vehículo de marca {self.marca}, modelo {self.obtener_modelo()}"

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.puertas = puertas

    # Sobrescribimos el método mostrar_info para un comportamiento específico
    def mostrar_info(self):
        return f"Coche de marca {self.marca}, modelo {self.obtener_modelo()}, con {self.puertas} puertas"

# Instanciamos un coche
mi_coche = Coche("Toyota", "Corolla", 4)

# Mostramos la información del coche (polimorfismo)
print(mi_coche.mostrar_info())  # El método 'mostrar_info' se comporta de forma diferente


