# Ciclo While

# Se efectuará una suma del número 1 al 6
# se define n como la cantidad de números a sumar
n = int(input('Ingrese un número entero positivo: '))
suma = 0
i = 1

while i <= n:
    suma = suma + i
    i = i + 1
print('La suma de los números hasta ',n,' es: ',suma)
