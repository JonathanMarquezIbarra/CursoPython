# Serie A B A B A B A ....

# w es la variable que representa al interruptor

n = int(input('Ingrese un número: '))

w = 0

for i in range(1,n + 1):
    if w == 0:
        print('A')
        w == 1
    else:
        print('B')
        w == 0
