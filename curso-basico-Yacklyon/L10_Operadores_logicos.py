# Operadores lógicos

''' AND
F AND F = F
F AND T = F
T AND F = F
T AND T = T

    OR
F OR F = F
F OR T = T
T OR F = T
T OR T = T

    NOT
NOT(TRUE) = FALSE
NOT(FALSE) = TRUE
'''
# Ejemplo
# Se declaran las variables a y b y se les asignan valores
a = 3
b = 9
# Se indica en pantalla las operaciones a realizar
print('Sean las variables a = 3 y y = 9: ')
print('Se efectúa la operación anidada de not(a<b and a>b)')
print('a<b = True   y   a>b = False')
print('Así que (a<b and a>b) = False')
print('Entonces el resultado de not(a<b and a>b) = True')
print(' ')
print('A continuación se ejecutará la operación en Python y el resultado es: ')
resultado = not(a<b and a>b)
print(resultado)
