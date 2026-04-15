archivo = open("videojuegos50registros.csv", "r", encoding="latin-1")
print("Archivo abierto correctamente\n")

for i in range(5):
    print(archivo.readline())

archivo.close()
