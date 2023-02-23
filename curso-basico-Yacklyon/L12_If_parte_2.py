# Número par o impar

# Petición de un número al usuario y se guarda en la variable n
n = int(input('Ingrese un número entero cualquiera: '))
# Se evalúa la condición de que sea par o impar el número
if n % 2 == 0:
    print('El número {} es un número par'.format(n))
else:
    print(n, 'Es un número impar')
