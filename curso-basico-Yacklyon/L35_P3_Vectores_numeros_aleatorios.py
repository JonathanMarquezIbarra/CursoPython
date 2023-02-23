# Arreglos - Calcular 10 números aleatorios

# mediante import se llama a la función externa random
import random
# se cra una función
def vector_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(0,10)
    return vector

print('Ingrese cuantos número aleatorios desea obtener: ')
n = int(input())

aleatorio = vector_aleatorio(n)
print(aleatorio)        
