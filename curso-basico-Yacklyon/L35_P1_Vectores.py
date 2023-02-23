# Arreglos

n = int(input('Ingrese el tamaño del arreglo: '))
m = int(input('Ingrese el número de múltiplos: '))
# Definición del arreglo
a = []
for i in range(0,n):
    a.append(i*m)
print(a)
