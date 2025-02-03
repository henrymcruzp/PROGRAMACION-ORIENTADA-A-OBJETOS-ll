import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def gestionar_tareas_programacion():
    print("\n--- Gestión de Tareas de Programación ---")
    print("1. Asignar tarea a desarrollador")
    print("2. Ver estado de tareas")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        print("Asignando tarea a desarrollador...")
    elif opcion == '2':
        print("Mostrando estado de tareas...")
    else:
        print("Saliendo...")


def control_versiones():
    print("\n--- Control de Versiones y Despliegue de Software ---")
    print("1. Ver historial de cambios")
    print("2. Realizar despliegue de nueva versión")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        print("Mostrando historial de cambios...")
    elif opcion == '2':
        print("Desplegando nueva versión...")
    else:
        print("Saliendo...")


def seguimiento_investigacion():
    print("\n--- Seguimiento de Proyectos de Investigación Académica ---")
    print("1. Crear fase de investigación")
    print("2. Asignar tarea de redacción")
    print("3. Ver progreso del proyecto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        print("Creando fase de investigación...")
    elif opcion == '2':
        print("Asignando tarea de redacción...")
    elif opcion == '3':
        print("Mostrando progreso del proyecto...")
    else:
        print("Saliendo...")


def gestion_recursos_humanos():
    print("\n--- Gestión de Recursos Humanos en Proyectos de Desarrollo de Software ---")
    print("1. Asignar tarea según habilidad")
    print("2. Ver estadísticas de rendimiento")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        print("Asignando tarea según habilidad...")
    elif opcion == '2':
        print("Mostrando estadísticas de rendimiento...")
    else:
        print("Saliendo...")


def control_diseno_grafico():
    print("\n--- Control de Proyectos de Diseño Gráfico ---")
    print("1. Crear tarea de diseño")
    print("2. Ver retroalimentación de clientes")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        print("Creando tarea de diseño...")
    elif opcion == '2':
        print("Mostrando retroalimentación de clientes...")
    else:
        print("Saliendo...")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Gestión de Tareas de Programación',
        '2': 'Control de Versiones y Despliegue de Software',
        '3': 'Seguimiento de Proyectos de Investigación Académica',
        '4': 'Gestión de Recursos Humanos en Proyectos de Desarrollo de Software',
        '5': 'Control de Proyectos de Diseño Gráfico',
        '0': 'Salir'
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            break
        elif eleccion == '1':
            gestionar_tareas_programacion()
        elif eleccion == '2':
            control_versiones()
        elif eleccion == '3':
            seguimiento_investigacion()
        elif eleccion == '4':
            gestion_recursos_humanos()
        elif eleccion == '5':
            control_diseno_grafico()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
