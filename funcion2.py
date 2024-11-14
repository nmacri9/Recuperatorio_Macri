import math
#Generar una función que calcule la media geométrica de filas o columnas de una matriz cuadrada.
def media_geometrica(matriz, tipo, indice):
    filas = len(matriz)
    for fila in matriz:
        if len(fila) != filas:
            print ('La matriz no es cuadrada')
            return None
        
    producto = 1
    n = filas
    
    if tipo == 'fila':
        for j in range (filas):
            producto *= matriz[indice][j]
    elif tipo == 'columna':
        for i in range(filas):
            producto *= matriz [i][indice]
    else: 
        print('Invalido. Debe ser fila o columna:')
        return None
    
    media = producto ** (1 / n)
    return media

#2 Generar una función que calcule la suma de las diagonales principal y secundaria de una matriz.
def suma_diagonales (matriz):

    filas = len(matriz)
    for fila in matriz:
        if len(fila) != filas:
            print('La matriz no es cuadrada.')
            return None
    suma_p = 0
    suma_s = 0

    for i in range(filas):
        suma_p += matriz[i][i]
        suma_s += matriz[i][filas - i - 1]

        return suma_p + suma_s
    
#3 calcular traspuesta

def calcular_transpuesta (matriz):
    filas = len(matriz)

    for fila in matriz:
        if len(fila)!= filas:
            print('La matriz no es cuadrada.')
            return None
        
    transpuesta = []

    for i in range(filas):
        fila_transpuesta = []
        for j in range (filas):
            fila_transpuesta.append(matriz[j][i])
        transpuesta.append(fila_transpuesta)
    return transpuesta

#4 A la función del ejercicio 2 agregar un parámetro que permita seleccionar si lo que se
# pretende recibir como retorno es la suma de ambas diagonales, solo la de la diagonal
# principal o solo la de la diagonal secundaria.

def sumar_diagonales(matriz , diagonal = 'ambas diagonales'):
    filas = len(matriz)
    
    for fila in matriz:
        if len(fila) != filas:
            print('La matriz no es cuadrada.')
            return None 
    
    suma_p = 0
    suma_s = 0
    for i in range(filas):
        suma_p += matriz[i][i]
        suma_s += matriz[i][filas - i - 1]

    if diagonal == 'ambas':
        return {suma_s + suma_p}
    elif diagonal == 'principal':
        return (f'La suma de la principal es: {suma_p}')
    elif diagonal == 'secundaria':
        return (f'La suma de la secundaria es {suma_s}')
    else:
        print('Diagonal invalida.')
        return None
    
#verificacion
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

resultado_ambas = sumar_diagonales (matriz , diagonal = 'ambas')
print(f'suma de ambas diagonales: {resultado_ambas}')
resultado_secundaria = sumar_diagonales (matriz , diagonal = 'secundaria')
print(f'suma de diagonal secundaria: {resultado_secundaria}')
resultado_principal = sumar_diagonales (matriz , diagonal = 'principal')
print(f'suma de diagonal principal : {resultado_principal}')