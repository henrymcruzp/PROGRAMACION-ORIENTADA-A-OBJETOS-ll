# Clase que representa una simple calculadora
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1  # Atributo para el primer número
        self.num2 = num2  # Atributo para el segundo número

    def sumar(self):
        return self.num1 + self.num2  # Metodo para sumar los dos números

# Función principal que organiza la lógica
def main():
    print("Calculadora de suma de dos números")  # Mensaje inicial
    numero1 = float(input("Ingresa el primer número: "))  # Pide el primer número
    numero2 = float(input("Ingresa el segundo número: "))  # Pide el segundo número
    calculadora = Calculadora(numero1, numero2)  # Crea un objeto de la clase Calculadora
    resultado = calculadora.sumar()  # Llama al metodo sumar del objeto
    print(f"La suma es: {resultado}")  # Muestra el resultado

# Ejecutar el programa solo si este es el archivo principal
if __name__ == "__main__":
    main()  # Llama a la función principal
