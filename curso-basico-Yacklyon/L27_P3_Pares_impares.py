# Separar lista en pares e impares

arreglo = [3,7,9,5,8,3,7,12]

def separar(lista):
    lista.sort()
    pares = []
    impares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares,impares = separar(arreglo)

print(pares)
print(impares)

