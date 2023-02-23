# La suma de los primeros n números

n = int(input('Introduzca el valor del número hasta el que quiere contar: '))
suma = 0
for i in range(1,n+1):
    suma = suma + i
print('La suma de los n números hasta ',n,' es: ', suma)
