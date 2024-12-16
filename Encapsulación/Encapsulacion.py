# Definimos la clase CuentaBancaria
class CuentaBancaria:
    # El constructor __init__ inicializa el saldo de la cuenta
    def __init__(self, saldo_inicial):
        # La variable __saldo es privada, no puede accederse directamente desde fuera de la clase
        self.__saldo = saldo_inicial

    # Método para depositar dinero en la cuenta
    def depositar(self, monto):
        # Verifica que el monto a depositar sea positivo
        if monto > 0:
            # Si es válido, suma el monto al saldo
            self.__saldo += monto

    # Método para consultar el saldo de la cuenta
    def consultar_saldo(self):
        # Devuelve el saldo actual de la cuenta
        return self.__saldo

# Crear una instancia de la clase CuentaBancaria con un saldo inicial de 1000
mi_cuenta = CuentaBancaria(1000)
# Depositar 500 en la cuenta
mi_cuenta.depositar(500)
# Consultar el saldo actual y mostrarlo
print(mi_cuenta.consultar_saldo())  # Salida: 1500
