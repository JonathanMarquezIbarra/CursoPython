# Tabla de multiplicar del 1 al 10

n = int(input('Ingrese un número entero: '))

print('La tabla del ',n,' es: ')
for i in range(1,11,1):
    print(n,' X ',i, ' = ', n*i)
