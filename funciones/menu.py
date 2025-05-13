

def menu():

    opciones = 0  # inicializamos opciones

    while opciones != 6:
        print("\n--- Menú de Opciones --- \n1.Cargar vuelos  \n2. Buscar vuelo por código \n3. Mostrar vuelo más caro \n4. Mostrar vuelo más barato \n5. Buscar vuelos con precio mayor a 100000 \n6. Salir \n")

        opcion_input = input("\nIngrese una opción: ")

        if opcion_input.isdigit():  # validamos que sea numero
            opciones = int(opcion_input)
            if 1 <= opciones <= 6:
                return opciones  # retornamos la opcion elegida como int
            else:
                print("Por favor ingrese un número entre 1 y 6.")
        else:
            print("Entrada inválida. Ingrese un número.")
        
    

