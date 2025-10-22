

print("Problemas - Arreglos")
print("Bienvenido a mis ejercicios - Autor: Cristian Ballesteros")
a = 1

while(a <= 10):
    a += 1
    print("\n")
    opcion = int(input("Digite el numero del problema que desea revisar: "))
    print("\n")


    def Problema1():
        print(f"Problema {opcion}\n")
        arr = [1, 2 , 3 , -4, 5]
        suma = 0        
        for i in arr:
            suma += i
            promedio = suma / len(arr)
        print(f"la lista del arreglo es: {arr}")
        print(f"El promedio del arreglo es: {promedio}\n")


    def Problema2():
        print(f"Problema {opcion}\n")
        arr1 = [1, 2 , 3 , 4, 5]
        arr2 = [6, 7 , 8 , 9, 10]
        resultado = []
        total = 0
        print("La lista del primer arreglo es: ", arr1)
        print("La lista del segundo arreglo es: ", arr2)
    
        for i in range(len(arr1)):
            resultado.append(arr1[i] * arr2[i])
        print(f"La lista de resultados es: {resultado}")
        
        for a in range(len(resultado)):
            total += resultado[a]
        print(f"La suma total de los resultados es: {total}")
        print("\n")
        
    def Problema3():
        print(f"Problema {opcion}\n")
        arr10 = [2, 4 , 6 , 8, 10]
        arr20 = [1, 3 , 5 , 7, 9]
        resultado = []
        print("La lista del primer arreglo es: ", arr10)
        print("La lista del segundo arreglo es: ", arr20)
        
        for z in range(len(arr10)):
            resultado.append(arr10[z] * arr20[z])
        print(f"La lista de resultados es: {resultado}")
        













    if(opcion == 1):
        Problema1()
    elif(opcion == 2):
        Problema2()
    elif(opcion == 3):
        Problema3()
    else:
        print("Opcion no valida")


    