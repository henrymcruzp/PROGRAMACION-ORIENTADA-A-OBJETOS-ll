import threading
import time

evento = threading.Event()

def esperar_evento():
    print("Esperando al evento...")
    evento.wait()
    print("El evento ha sido activado!")

hilo = threading.Thread(target=esperar_evento)
hilo.start()

time.sleep(3)  # Simula una espera antes de activar el evento
evento.set()

hilo.join()
print("Programa terminado")
