# Funciones aplicadas a diccionarios

# Dado el diccionario:
notas = {'david':85,'carlos':60,'victor':98,'hector':75}
# str(diccionario) - convierte el diccionario en cadena
# type(variable) - regresa el tipo de variables
# diccionario.clear() - remueve todos los elementos del diccionario
notas_1 = {'david':85,'carlos':60,'victor':98,'hector':75}
print('El resultado de notas.clear es: ',notas_1.clear())
# diccionario.copy() - copia el diccionario en otra variable
notas_2 = notas.copy()
print('El contenido de la variable notas_2 es: ',notas_2)
# diccionario.fromkeys(lista,valor) - crea un nuevo diccionario,
# a partir de una lista, y se le añade la key indicada
# a todos y cada uno de los elementos del nuevo diccionario
listanotas = dict.fromkeys(['david','carlos','victor','hector'],100)
print('La variable listanotas contiene al nuevo diccionario: ',listanotas)
# diccionario.get(clave) - regresa el valor de la clave que se indica
v_obtenido = notas.get('victor')
print('La función notas.get("victor") devuelve: ',v_obtenido)
# diccionario.items() - regresa una lista de pares (claves,valor)
items = notas.items()
print('La función notas.items() devuelve: ',items)
# diccionario.keys() - regresa una lista con las claves (keys) del diccionario
keys = notas.keys()
print('La función notas.keys() devuelve: ',keys)
# diccionario1.update(diccionario2) - añade los pares clave-valor
# de diccionario 1 a diccinoario 2
dict1={'a':1,'b':2,'c':3,'d':4}
dict2={'d':5,'e':6,'f':7,'g':8}
dict1.update(dict2)
print('Ĺa función dict1.update(dict2) devuelve: ',dict1)
# diccionario.value() - regresa una lista con los valores de un diccionario
value = notas.values()
print('La función notas.values() devuelve: ',value)
# diccionario.pop(clave) - borra un elemento específico del diccionario
pop = dict2.pop('f')
# si se imprime la variable, muestra el valor del elemento borrado
print('El elemento borrado de dict2 es "f" y su valor es: ',pop)
print('El diccionario después de pop queda como: ',dict2)


