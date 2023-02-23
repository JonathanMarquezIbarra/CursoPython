# Mayor que el anterior

valor = int(input('¿Cuántos valores va a introducir? '))
if valor<1:
    print('Ingrese un número positivo diferente de cero')
else:
    primero = int(input('Escriba un número '))
    for i in range(valor-1):
        numero = int(input('Escriba un número mas grande que {primero} '))
        if numero <= primero:
            print('{número} no es mayor que {primero}')
    print('Gracias por su colaboración')
        
