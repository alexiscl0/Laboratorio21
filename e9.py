import threading
import time
import random

def consultar_bd(numero):
    print(f"Consulta {numero} iniciada")
    tiempo = random.randint(1, 5)
    time.sleep(tiempo)
    
    print(f"Consulta {numero} terminada ({tiempo}s)")

print("SIN CONCURRENCIA")
inicio = time.time()
for i in range(3):
    consultar_bd(i + 1)
tiempo_secuencial = time.time() - inicio
print(f"Tiempo total: {tiempo_secuencial:.1f}s\n")

print("CON CONCURRENCIA")
inicio = time.time()

hilos = []
for i in range(3):
    hilo = threading.Thread(target=consultar_bd, args=(i + 1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

tiempo_concurrente = time.time() - inicio
print(f"Tiempo total: {tiempo_concurrente:.1f}s")

mejora = tiempo_secuencial - tiempo_concurrente
print(f"\nMejora: {mejora:.1f}s más rápido")