# Uso de sentencias If y Else anidados

# Se le pide al usuario que ingrese un número
n = int(input('Ingrese un número entero cualquiera: '))
# Se evalúa si el número es negativo, neutro o positivo
if n<0:
    print('El número es negativo')
else:
    if n==0:
        print('El número es = 0')
    else:
        print('El número es positivo')
