class ConexiónBaseDatos:
    def __init__(self, host, usuario, contrasena, base_datos):
        """
        Constructor que inicializa la conexión a la base de datos.
        Recibe como parámetros el host, usuario, contraseña y el nombre de la base de datos.
        """
        self.host = host
        self.usuario = usuario
        self.contrasena = contrasena
        self.base_datos = base_datos

        # Simulamos la conexión a la base de datos (en un caso real, se usaría una librería como psycopg2 o sqlite3)
        self.conexion = f"Conectando a la base de datos {self.base_datos} en {self.host} con usuario {self.usuario}"
        print(self.conexion)

    def realizar_consulta(self, consulta):
        """
        Simula la realización de una consulta en la base de datos.
        """
        print(f"Ejecutando consulta: {consulta}")

    def __del__(self):
        """
        Destructor que se ejecuta cuando el objeto es destruido.
        Simula el cierre de la conexión a la base de datos.
        """
        print(f"Cerrando conexión a la base de datos {self.base_datos}")
        self.conexion = None


# Ejemplo de uso de la clase ConexiónBaseDatos
db = ConexiónBaseDatos("localhost", "admin", "1234", "mi_base_de_datos")
db.realizar_consulta("SELECT * FROM empleados")

# El destructor se ejecutará automáticamente al finalizar el programa o cuando se elimine el objeto.
del db  # Llamada explícita para eliminar el objeto y ejecutar el destructor
