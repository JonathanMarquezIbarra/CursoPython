# Identificar pares e impares

n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese un número mayor o igual que el primero: '))

if n2 < n1:
    print('Ingrese un número mayor o igual que el primero: ')
else:
    for i in range(n1,n2 + 1):
        if i % 2 == 0:
            print('El número ', i, ' es par')
        else:
            print('El número ', i, ' es impar')
