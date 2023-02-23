# Diccionario

# Se define el diccionario edades
edades = {'david':30,'carlos':60,'victor':34,'hector':30}
# Se muestra el conjunto
print(edades)
print(' ')
# Para acceder a un elemento en específico, se busca
# por medio de su clave
print('Victor tiene: ',edades['victor'],' años')
print(' ')
# Modificar el valor de una clave
print('Modificando la edad de Victor:')
edades['victor'] = 37
print('Ahora victor tiene: ',edades['victor'])
print(' ')
# Mostrar las edades mediante el uso del key y el valor
for i in edades:
    print(i,edades[i])
