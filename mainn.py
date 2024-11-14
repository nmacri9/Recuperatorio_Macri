from funcion import *

depositos = ["Tierra del Fuego, Tucumán, Mendoza, Bs As, Misiones y Santa Fé."]
equipos = ["Barcelona, Inter Miami, PSG, Manchester City y Real Madrid."]


menu1 = """1 _ Obtener existencias:
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas:
Seleccione una opcion: """
res = 's'
while res == 's':


    menu = input(menu1)
    
    match menu:
        case "1":
            print(crear_matriz(5,6,matriz))
            pass
        case "2":
            pass
            pass
        case "3":
            print('Mostrar equipos que hay en stock más de 5.000 camisetas.')
            pass
        case "4":
            print('máxima cantidad de camisetas de cada equipo.')
            pass
        case "5":
            print('Cargar ventas:')
            pass
        case " ":
            print('Por favor, ingrese un numero valido')