print("Problemas - Arreglos")
print("Bienvenido a mis ejercicios - Autor: Cristian Ballesteros")
a = 1

while(a <= 10):
    a += 1
    print("\n")
    opcion = int(input("Digite el numero del problema que desea revisar: "))
    print("\n")
    print(f"Problema {opcion}\n")


    def Problema1():
        arr = [1, 2 , 3 , -4, 5]
        suma = 0        
        for i in arr:
            suma += i
            promedio = suma / len(arr)
        print(f"la lista del arreglo es: {arr}")
        print(f"El promedio del arreglo es: {promedio}\n")


    def Problema2():
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
        arr10 = [2, 4 , 6 , 8, 10]
        arr20 = [1, 3 , 5 , 7, 9]
        resultado = []
        print("La lista del primer arreglo es: ", arr10)
        print("La lista del segundo arreglo es: ", arr20)
        
        for z in range(len(arr10)):
            resultado.append(arr10[z] * arr20[z])
        print(f"La lista de resultados es: {resultado}")
    
    def Problema4():
        arrA = [-8 , 10, 4 , 3, -1, 5]
        ORDarray = sorted(arrA)
        print(f"La lista array es: {arrA}")
        print(f"La lista array ordenada es: {ORDarray}")
        m = len(ORDarray)
        if m % 2 == 1:
            mediana = ORDarray[m//2]
        else:
            mediana = (ORDarray[m//2-1])
        print(f"La mediana de la lista array ordenada es: {mediana}")
    
    def Problema5():
        arrB =[1, 0, 2, 3, 0, 0, 0]
        resultado = [x for x in arrB if x != 0]  
        ceros = [0] * arrB.count(0)               
        print(f"El array original es: {arrB}")
        print(f"El array modificado es: {(resultado + ceros)}")
        
    def Problema6():
        matriz = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],            
        ]
        print(f"Tu matriz es: {matriz}\n")
        def matrizmagica(matriz):
            n = len(matriz)            
        
            for fila in matriz:
                if len(fila) != n:
                    return False

            suma_objetivo = sum(matriz[0])
            
            for fila in matriz:
                if sum(fila) != suma_objetivo:
                    return False
            
            for col in range(n):
                suma_col = sum(matriz[fila][col] for fila in range(n))
                if suma_col != suma_objetivo:
                    return False
            
            suma_diag_principal = sum(matriz[i][i] for i in range(n))
            if suma_diag_principal != suma_objetivo:
                return False
            
            suma_diag_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
            if suma_diag_secundaria != suma_objetivo:
                return False
            
            return True
        
        if(matrizmagica(matriz) == True):
            print(f"La matriz: {matriz} es magica :D!")
        else: 
            print(f"La matriz: {matriz} no es magica :(")

        
    if(opcion == 1):
        Problema1()
    elif(opcion == 2):
        Problema2()
    elif(opcion == 3):
        Problema3()
    elif(opcion == 4):
        Problema4()
    elif(opcion == 5):
        Problema5()
    elif(opcion == 6):
        Problema6()
    else:
        print("Opcion no valida")


    