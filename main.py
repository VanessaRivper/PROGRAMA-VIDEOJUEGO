def cargar_datos():
    archivo = open("videojuegos.csv", "r", encoding="utf-8")
    datos = archivo.readlines()
    archivo.close()
    return datos


def buscar(datos, termino):
    contador = 0

    for linea in datos:
        if termino.lower() in linea.lower():
            partes = linea.strip().split(",")

            try:
                nombre = partes[0]
                plataforma = partes[1]
                genero = partes[2]
                ventas = partes[6]

                print("Juego:", nombre, "| Plataforma:", plataforma, "| Ventas:", ventas)
                contador += 1
            except:
                continue

    print("\nSe encontraron", contador, "resultados")


def estadisticas_ventas(datos):
    ventas = []

    for linea in datos[1:]:
        partes = linea.strip().split(",")

        try:
            venta = float(partes[6])
            ventas.append(venta)
        except:
            continue

    print("Máximo:", max(ventas))
    print("Mínimo:", min(ventas))
    print("Promedio:", sum(ventas)/len(ventas))


def filtrar_ventas(datos, limite):
    for linea in datos[1:]:
        partes = linea.strip().split(",")

        try:
            venta = float(partes[6])
            if venta > limite:
                print(linea)
        except:
            continue


def menu():
    datos = cargar_datos()

    while True:
        print("\n1. Buscar")
        print("2. Estadísticas")
        print("3. Filtrar por ventas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            termino = input("Ingrese término: ")
            buscar(datos, termino)

        elif opcion == "2":
            estadisticas_ventas(datos)

        elif opcion == "3":
            limite = float(input("Ventas mayores a: "))
            filtrar_ventas(datos, limite)

        elif opcion == "4":
            break

menu()