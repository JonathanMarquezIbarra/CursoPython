# Funcionamiento de continue

n = int(input('Ingrese un número: '))
for i in range(1,n+1):
    if i % 2 == 0:
        continue# Salta a la siguiente instrucción (no sea par)
        print(i)
    else:
        print(i)
