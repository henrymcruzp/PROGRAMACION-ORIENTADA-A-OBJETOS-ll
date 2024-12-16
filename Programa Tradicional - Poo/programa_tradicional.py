# Función para pedir un número al usuario
def pedir_numero():
    numero = float(input("Ingresa un número: "))  # Pide un número
    return numero  # Devuelve el número ingresado

# Función para calcular la suma de dos números
def sumar(num1, num2):
    return num1 + num2  # Devuelve la suma de los dos números

# Función principal que organiza la lógica
def main():
    print("Calculadora de suma de dos números")  # Mensaje inicial
    numero1 = pedir_numero()  # Pide el primer número
    numero2 = pedir_numero()  # Pide el segundo número
    resultado = sumar(numero1, numero2)  # Calcula la suma
    print(f"La suma es: {resultado}")  # Muestra el resultado

# Ejecutar el programa solo si este es el archivo principal
if __name__ == "__main__":
    main()  # Llama a la función principal
