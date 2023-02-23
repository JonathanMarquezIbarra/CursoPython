# serie 4, 3, 2, 1, 4, 3, 2, 1

n = int(input('Ingrese un número: '))
# la variable c representa el controlador
c = 0
# la variable w es un interruptor
w = 4

while c < n:
    print(w)
    if w > 1:
        w = w - 1
    else:
        w = 4
    c = c + 1
