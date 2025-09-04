
def inicializar_matriz(cantidad_filas, cantidad_columnas = 3):

    matriz = []
    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]

    return matriz

def cargar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input("Agregar valor: ")


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])
        print()
        
def buscar_vuelo_por_codigo(matriz, numero_buscado):
    posiciones = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero_buscado == matriz[i][j]:
                posiciones += [matriz[i]]
    
    if posiciones == []:
        return "El numero no se encuentr en la matriz"
    else:
        return posiciones


def valor_maximo_matriz(matriz):
    maximo = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
    return maximo

def valor_minimo_matriz(matriz):
    minimo = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
    return minimo

def vuelo_mayor_cienmil(matriz):
    vuelo_ = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 100000:
                maximo = matriz[i][j]
    return maximo