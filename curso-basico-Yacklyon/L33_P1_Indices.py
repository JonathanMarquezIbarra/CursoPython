# Indices


# En python nos podemos referir a un elemento de una cadena de caracteres
# mediante su posición, como si fuera una lista
curso = 'python'

print(curso[0])
print(curso[1])
print(curso[2])
print(curso[3])
print(curso[4])
print(curso[5])
print('')
# También se pueden imprimir solamente un rango específico
# NOTA: el último valor del parámetro indicado no se mostrará
print(curso[2:5])
print('')
# Se puede omitir el valor de inicio
print(curso[:3])
print('')
# Se puede también indicar a partir de qué valor muestre sus elementos
print(curso[3:])
print('')
# Dada a la cadena de la variable var1, se transforma a una lista "vocales"
var1 = 'aeiou'
vocales = list(var1)
# Para referirse a posiciones específicas dentro de la lista
# lo podemos realizar mediante index, lo que devolverá un número
# que representa a la posición del elemento
print(vocales.index('o'))
