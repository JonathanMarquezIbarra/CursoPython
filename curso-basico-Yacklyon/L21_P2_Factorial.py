# Encontrar el factorial de un número

n = int(input('Introduzca el número del que quiere conocer el factorial: '))
fact = 1

for i in range(1,n+1):
    fact = fact * i
print('El factorial de ',n,'! es = ', fact)
