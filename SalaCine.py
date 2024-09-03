from colorama import init, Fore, Style
matrizSala = []
def crearSala(f, c):
    #global matrizSala  # Usamos la matriz global
    cont = 0 #contador
    for i in range(f):#filas
        matrizSala.append([])
        for j in range(c):#columnas
            cont += 1
            matrizSala[i].append(cont)          
    return f, c, matrizSala

#Imprime la matriz.
init()  # Inicializamos la biblioteca colorama
def presentarSala(matrizSala):
    for fila in matrizSala:  # Iteramos sobre cada fila de la matriz
        for elemento in fila:  # Iteramos sobre cada elemento de la fila
            if elemento == 'X':
                print(Fore.BLUE + "🟣" + Style.RESET_ALL, end='\t')#imprime en punto azul
            else:
                print(elemento, end="\t") # Imprime el numero
        print()
    return matrizSala

#funcion asignar puesto
def asig_Puesto(matrizSala):
    presentarSala(matrizSala)#3x3=9 casillas 1 al 9
    try:
        fila = int(input("Ingrese la fila donde desea asignar el puesto: ")) 
        columna = int(input("Ingrese la columna donde desea asignar el puesto: ")) 
        
        if (0 <= fila < len(matrizSala)) and (0 <= columna < len(matrizSala[0])):
            if matrizSala[fila][columna] != 'X':
                matrizSala[fila][columna] = 'X'
                print("Puesto reservado!")
            else:
                print("Puesto ya reservado")
        else:
            print("Puesto fuera de rango")
    except ValueError:
        print("Error, ingrese un dato numerico entero")
                
def main():
    matrizSala = None
    while True:
        print("\nMenú de principal\n")
        print("1. Crear sala")
        print("2. Ver sala")
        print("3. Reservar")
        print("4. Cargar sala")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione la opción deseada (1-5): "))
        except ValueError:
            print("Error, ingrese un dato numerico entero ")
            continue
        
        if opcion == 1:
            try:
                n = int(input("Ingrese el número de filas: "))
                m = int(input("Ingrese el número de columnas: "))
                if n > 0 and m > 0:
                    f, c, matrizSala = crearSala(n, m)
                    print(f"La sala de cine de {n}x{m}, ha sido creada exitosamente!")
                else:
                    print("Error, ingrese un número entero positivo")
            except ValueError:
                print("Error, ingrese un número entero")
                
        elif opcion == 2:
            if matrizSala:
                presentarSala(matrizSala)
            else:
                print("ERROR, Debes crear una sala")
                
        elif opcion == 3:
            if matrizSala:
                asig_Puesto(matrizSala)
            else:
                print("ERROR, Debes crear una sala")
                
        elif opcion == 4:
            if matrizSala:
                presentarSala(matrizSala)
            else:
                print("ERROR, Debes crear una sala") 
                
        elif opcion == 5:
            print("Adiós!")
            break
            
        else:
            print("Opción no válida, debe estar en el rango de 1-5")

if __name__ == "__main__":
    main()