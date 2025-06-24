#LE PIDO AL USUARIO QUE INGRESE LOS DOS CONJUNTOS.
def pedir_conjuntos():
    while True:
        dato1 = input("Ingrese números separados por espacios para el primer conjunto de elementos: ")
        dato2 = input("Ingrese números separados por espacios para el segundo conjunto de elementos: ")
        try:
            lista1 = list(map(int, dato1.split()))
            lista2 = list(map(int, dato2.split()))
            return lista1, lista2
        except ValueError:
            print("⚠️ Error: Por favor ingrese solo números separados por espacios. Intente de nuevo.\n")

#OPERACIÓN DE UNIÓN.
def union(lista1, lista2):
    resultado_union = list(set(lista1 + lista2))
    print("\nResultado de la unión:", resultado_union)

#OPERACIÓN DE INTERSECCIÓN.
def interseccion(lista1, lista2):
    resultado_interseccion = list(set(lista1) & set(lista2))
    print("\nResultado de la intersección:", resultado_interseccion)

#OPERACIÓN DE DIFERENCIA.
def diferencia(lista1, lista2):
    resultado_diferencia = list(set(lista1) - set(lista2))
    print("\nResultado de la diferencia (primer conjunto - segundo conjunto):", resultado_diferencia)

#MENÚ.
def mostrar_menu():
    print("\n" + "="*30)
    print("   MENÚ DE OPERACIONES DE CONJUNTOS")
    print("="*30)
    print("1 - Ingresar conjuntos")
    print("2 - Unión (Y)")
    print("3 - Intersección (O)")
    print("4 - Diferencia (-)")
    print("5 - Salir")
    print("="*30)

#FUNCIÓN QUE CONTROLA EL FLUJO DEL PROGRAMA.
def programa():
    lista1, lista2 = [], []
    conjuntos_cargados = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            lista1, lista2 = pedir_conjuntos()
            conjuntos_cargados = True
            print("✅ Conjuntos cargados correctamente.")

        elif opcion == "2":
            if not conjuntos_cargados:
                print("⚠️ Por favor, ingrese primero los conjuntos (opción 1).")
            else:
                union(lista1, lista2)

        elif opcion == "3":
            if not conjuntos_cargados:
                print("⚠️ Por favor, ingrese primero los conjuntos (opción 1).")
            else:
                interseccion(lista1, lista2)

        elif opcion == "4":
            if not conjuntos_cargados:
                print("⚠️ Por favor, ingrese primero los conjuntos (opción 1).")
            else:
                diferencia(lista1, lista2)

        elif opcion == "5":
            print("¡Gracias por usar el programa! 👋")
            break

        else:
            print("⚠️ Opción inválida. Por favor, ingrese un número del 1 al 5.")

programa()







