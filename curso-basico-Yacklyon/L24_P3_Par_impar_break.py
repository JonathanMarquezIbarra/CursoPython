# Seleccionar impares y terminar al econtrar el primer divisible entre 6

n = int(input('Ingrese un número '))
for i in range(1,n+1):
    if not(i % 2) & (i % 6):
        continue
    if i % 6 == 0:
        break
    print(i)
