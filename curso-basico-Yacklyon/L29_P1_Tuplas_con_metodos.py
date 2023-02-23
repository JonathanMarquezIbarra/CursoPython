# Tuplas con funciones

#sea la tupla
a = (4,6,9,3,6,19)
print('Dada la tupla: ',a)
print('se pueden aplicar algunos métodos como lo son: ')
print(' ')
# tuple(lista) - convierte una tupla a lista
lista = list(a)
print('tuple(lista) ', lista)
# lista(tuple) - convierte una lista en una tupla
lista = tuple(a)
print('lista(tuple) ', lista)
# len(tupla) - mide la longitud de una tupla
print('len(tupla) ',len(a),' elementos')
# max(tupla) - valor máximo de una tupla
print('max(tupla) ',max(a),' es el valor máximo')
# min(tupla) - valor minimo de una tupla
print('min(tupla) ',min(a),' es el valor mínimo')
