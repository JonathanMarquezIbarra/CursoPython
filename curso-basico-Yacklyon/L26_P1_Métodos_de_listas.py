lista = [2,7,8,14,8,12,6]
# Encontrar el mayor de los números mediante métodos
print('Sea la lista: ',lista)
print(' ')
# Método max: muestra el elemento con el valor máximo de la lista
print('Método max: ',max(lista))
# Método min: muestra el elemento con el valor mínimo de la lista
print('Método min: ',min(lista))
# Método len: muestra la cantidad de elementos que conforman la lista
print('Método len: ',len(lista))
print(' ')
# Método append: añade elementos a la lista indicada
lista.append(100)
print('Método append: ',lista,' añadió el valor 100')
# Método count: cuenta los elementos repetidos de una lista
print('Método count: el elemento de valor 8 se repite: count ',lista.count(8),' veces')
# Método sort: ordena los elementos de manera ascendente
lista.sort()
print('Método sort: ',lista)
# Método reverse: invierte el orden original de los elemenos de la lista
lista.reverse()
print('Método reverse: ',lista)
