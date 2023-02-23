# Ejemplo del uso de elif con calificaciones

# Se le pide al usuario que ingrese su calificación
n = float(input('Introduzca su calificación: '))

# Se evaluará la calificación mediante el uso de elif
if n>=0 and n<=5:
    print('Mejor dedícate a otra cosa, estás pelas !!')
elif n>=6 and n<=8:
    print('Buen trabajo, estás aprobado !!')
elif n>=9 and n<=10:
    print('Eres un genio !!, has de estudiar en la ESIME Zacatenco!!')
else:
    print('Introduce una calificación válida')
