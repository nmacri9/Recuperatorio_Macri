matriz = []

def crear_matriz( fila: int , columnas: int , matriz):
    matriz = []
    fila = [0] * columnas
    matriz_nueva = matriz.append(fila)
    return matriz_nueva



"""
1_Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
"""
"""def obtener_existencias (lista1: list, lista2: list , existencia) -> list:
    for i in range(len(matriz)):
                print(f'Deposito: {depositos[i]}')
                for j in range(len(equipos)):
                    print(f'{equipos[j]} : {existencia[i][j]} camisetas')
    """

"2_ Mostrar depósitos que tienen en stock más de 10.000 camisetas."
"""def mostrar_depo_10mil (existencia: list , depositos: list)-> list:
    depositos = ["Tierra del Fuego, Tucumán, Mendoza, Bs As, Misiones y Santa Fé."]
    print('Depositos con +10.000 camisetas : ')
    for i in range(len(depositos)):
        suma_depositos = 0
        for j in range(len(existencia[i])):
            suma_depositos += existencia[i][j]
            
        if suma_depositos > 10000:
            print(f'Deposito: {depositos[i]}.')"""

"3_Mostrar equipos que hay en stock más de 5.000 camisetas."

