import threading
contador_global = 0
mutex = threading.Lock()

def incrementar():
    global contador_global
    with mutex:  # Se usa with para manejar el bloqueo automáticamente
        contador_global += 1

def tarea():
    for _ in range(10):
        incrementar()

hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("El valor final del contador global es:", contador_global)
