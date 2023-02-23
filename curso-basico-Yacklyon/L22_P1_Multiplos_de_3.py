# Generar los múltiplos de 3

n = int(input('Ingrese un número: '))
# m es la variable intorruptor
m = 3

for i in range (1,n+1):
    print(m, end=' - ')
    m = m + 3
    
