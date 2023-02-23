#Tabla de multiplicar con funciones

# Se pide al usuario que ingrese el valor de la tabla que quiere
tabla = int(input('¿De qué número quieres conocer su tabla de multiplicar? '))
print(' ')
# Se crea la función que efectuará las multiplicaciones
# en base al número que indicó el usuario
def tabla_mul(t):
    for i in range(1,11):
        print(t,' X ',i,' = ',i*t)
# Se manda a llamar la función, enviándole como parámetro
# el número que introdujo el usuario
tabla_mul(tabla)
