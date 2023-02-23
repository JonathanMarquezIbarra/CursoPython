# Calcular el número de vocales para una frase

frase = str(input('Ingrese una frase: '))
vocales = 'aeiouAEIOU'
# Contador de vocales
contador = 0

for i in frase:
    if i in vocales:
        contador = contador + 1
print('El número de vocales es: ',contador)
