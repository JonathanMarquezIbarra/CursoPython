# Tuplas

# Las tuplas pueden almacenar datos de distinto tipo
tupla = (34,'python',4.6,32,65,71,'pelota','acantilado')
print('La tupla original del ejemplo es: ',tupla)
print(' ')
# En las tuplas también se puede acceder a un dato en específico
# La variable pos indica la posición dentro de la tupla
pos = int(input('Ingrese un número entero del 0 al 7 para indicar la posición: '))
print('La posición ',pos,' hace referencia al dato: ',tupla[pos])
