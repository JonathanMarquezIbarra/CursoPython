#Tabla de multiplicar con funciones

def leer():
    tabla = int(input('¿De qué número quieres conocer su tabla de multiplicar? '))
    print(' ')
    return tabla

def tabla_mul(t):
    for i in range(1,11):
        print(t,' X ',i,' = ',i*t)

tabla_mul(leer())
