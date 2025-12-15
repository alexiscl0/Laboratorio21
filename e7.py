def copiar_texto(origen, destino):
    with open(origen, 'r', encoding='utf-8') as archivo_origen:
        contenido = archivo_origen.read()
    
    with open(destino, 'w', encoding='utf-8') as archivo_destino:
        archivo_destino.write(contenido)
    
    print(f"Copiado: {origen} -> {destino}")

def copiar_binario(origen, destino):
    with open(origen, 'rb') as archivo_origen:
        contenido = archivo_origen.read()
    
    with open(destino, 'wb') as archivo_destino:
        archivo_destino.write(contenido)
    
    print(f"Copiado: {origen} -> {destino}")


with open("prueba.txt", "w", encoding='utf-8') as f:
    f.write("Hola mundo")

with open("prueba.dat", "wb") as f:
    f.write(bytes([1, 2, 3, 4, 5]))

copiar_texto("prueba.txt", "copia.txt")
copiar_binario("prueba.dat", "copia.dat")