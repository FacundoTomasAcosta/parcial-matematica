#LE PIDO AL USUARIO QUE INGRESE LOS DOS CONJUNTOS.
def pedir_conjuntos():
    while True:
        dato1 = input("Ingrese números separados por espacios para el primer conjunto de elementos: ")
        dato2 = input("Ingrese números separados por espacios para el segundo conjunto de elementos: ")
        try:
            #INTENTAMOS CONVERTIR PARA VALIDAR QUE SEAN NÚMEROS
            lista1 = list(map(int, dato1.split()))
            lista2 = list(map(int, dato2.split()))
            return lista1, lista2
        except ValueError:
            print("Error: Por favor ingrese solo números separados por espacios. Intente de nuevo.")

#LE PIDO AL USUARIO QUÉ OPERACIÓN VA A REALIZAR.
def pedir_operacion():
    while True:
        operacion = input("Ingrese la operación que quiera realizar con los conjuntos elegidos, puede ser Y (unión), O (intersección), - (diferencia): ").upper()
        if operacion in ["Y", "O", "-"]:
            return operacion
        else:
            print("Operación no válida. Por favor ingrese Y, O o -.")


#OPERACIÓN DE UNIÓN.
def union(lista1, lista2):
  resultado_union = list(set(lista1 + lista2))
  print("El resultado de la unión entre los dos conjuntos es: ", resultado_union)
  return resultado_union

#OPERACIÓN DE INTERSECCIÓN.
def interseccion(lista1, lista2):
  resultado_interseccion = list(set(lista1) & set(lista2))
  print("El resultado de la intersección entre los dos conjuntos es: ", resultado_interseccion)
  return resultado_interseccion

#OPERACIÓN DE DIFERENCIA.
def diferencia(lista1, lista2):
  resultado_diferencia = list(set(lista1) - set(lista2))
  print("El resultado de la diferencia entre los dos conjuntos es: ", resultado_diferencia)
  return resultado_diferencia

#FUNCIÓN QUE LLAMA A LA OPERACIÓN CORRESPONDIENTE SEGÚN LA OPCIÓN DE USUARIO.
def operaciones(operacion, lista1, lista2):
  if operacion == "Y":
    return union(lista1, lista2)
  elif operacion == "O":
    return interseccion(lista1, lista2)
  elif operacion == "-":
    return diferencia(lista1, lista2)



#FUNCIÓN PRINCIAPAL QUE CONTROLA EL FLUJO DEL PROGRAMA.
def programa():
  lista1, lista2 = pedir_conjuntos()
  operacion = pedir_operacion()
  operaciones(operacion, lista1, lista2)

programa()