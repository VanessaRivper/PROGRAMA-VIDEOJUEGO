from archivos import *
from analisis import *

datos = cargar_datos()

while True:
    print("\n---- MENÚ ----")
    print("1. Buscar")
    print("2. Estadísticas") 
    print("3. Filtrar")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        entrada = input("Ingrese búsqueda: ")
        resultados = buscar(datos, entrada)
        guardar_hist(entrada, len(resultados))
        guardar = input("¿Desea guardar los resultados? (s/n): ")

        if guardar == "s":
            guardar_csv("Busqueda.csv", resultados)
        
    elif opcion == "2":
        estadisticas(datos)
        guardar_hist("estadísticas", 1)
        
    elif opcion == "3":
        resultados = filtrar(datos)
        guardar_hist("filtro", len(resultados))
                          
    elif opcion == "4":
        print("¡Adiós! El programa ha finalizado")  
        break
    else:
        print("Opción inválida")
        
