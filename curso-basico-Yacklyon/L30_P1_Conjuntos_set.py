# Set (conjuntos)

# Un conjunto se define mediante llaves
conjunto = {2,3,4}
print('Se tiene el conjunto: ',conjunto)
print(' ')
# set.add(valor)
conjunto.add(10)
print('set.add(10) le añade el valor de 10: ',conjunto)
print(' ')
# Convertir una lista en un conjunto
a = ['a','b',4,6,7,'z']
print('Dada la lista a = ',a)
print('Se puede convertir en un conjunto mediante: ')
print('set(a) = ',set(a))
print(' ')
# Búsqueda dentro del conjunto
# al realizar una busqueda, arrojará un true o false segun sea el caso
print('Mediante "in conjunto" se realiza una búsqueda en el conjunto')
print('4 in conjunto = ',4 in conjunto)
