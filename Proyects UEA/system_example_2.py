import threading
barrera = threading.Barrier(2)

def tarea():
    print("Hilo esperando en la barrera")
    barrera.wait()
    print("Hilo continuando después de la barrera")

hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Programa terminado")
