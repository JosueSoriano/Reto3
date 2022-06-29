# RETO 3
# Autor: Josué Soriano
# Año: 2022

"""Se genera la FASE 1 del Reto 3 de Python Basics"""

# Se declaran las variables para cada uno de los billetes
billete_5 = int(5)
billete_10 = int(10)
billete_20 = int(20)
billete_50 = int(50)
billete_100 = int(100)
billete_200 = int(200)
billete_500 = int(500)
# Se declara variable para guardar el precio total
precio_total = int(0)

# Se crean dos arrays, uno con el menú y otro con el precio de cada plato
menu = []
precio_plato = []

"""Se genera la FASE 2 del Reto 3 de Python Basics"""

diccionario_menu = {
    "Gazpacho andaluz" : 4,
    "Ensalada de la casa" : 3,
    "Guisantes con jamón": 4,
    "Pasta carbonara" : 5,
    "Entrecot a la brasa" : 12,
    "Lubina al horno" : 10,
    "Fruta variada" : 3,
    "Flan de la casa" : 4
}
# Se rellenan los arrays con la información del diccionario
for key in diccionario_menu:
    menu.append(key)
    precio_plato.append(diccionario_menu[key])

# Se presenta en pantalla el menu con sus precios
def imprimir_menu(carta, precios):
    print("")
    print("-- CARTA DEL MENÚ --")
    print("")
    idx = 0
    for plato in carta:
        print(f"Plato: {plato} ....... Precio: {precios[idx]} €")
        idx += 1

imprimir_menu(menu,precio_plato)

# Se solicitan los platos que quiere pedir el cliente
lista_platos_pedidos = []
repeticion = True

while repeticion == True:
    plato_elegido = str(input("--> Indique el nombre del plato que desea pedir: "))
    if plato_elegido in menu:
        print(f"Ha seleccionado: {plato_elegido}", end=" ")
        lista_platos_pedidos.append(plato_elegido)
        seleccion_otro_plato = int(input("¿Desea pedir otro plato? Si: 1 , No: 0 :"))
        if seleccion_otro_plato == 1:
            repeticion = True
        else:
            repeticion = False
    else:
        print("Incorrecto, el plato indicado no está en el menú. ")

"""Se genera la FASE 3 del Reto 3 de Python Basics"""

# Se comprueba la lista de platos pedidos con el array de menu

for plato in lista_platos_pedidos:
    if plato not in menu:
        print(f"El plato elegido: {plato} no se encuentra en la carta del menú")
    else:
        indice_plato_menu = menu.index(plato)
        precio_total += precio_plato[indice_plato_menu]

print("--------------------------------------------------")
print(f"Gracias por su pedido, en breve le serviremos:")
print("")
for plato_pedido in lista_platos_pedidos:
    print(plato_pedido)
print("")
print(f"El importe total será de {precio_total} €")
print("Gracias por su pedido.")
print("--------------------------------------------------")
