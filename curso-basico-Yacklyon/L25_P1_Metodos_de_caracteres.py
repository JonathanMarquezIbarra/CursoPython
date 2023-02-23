# Métodos

# La variable p representa una cadena de caracteres
p = 'Mensaje para comprobar los métodos de python'
print('Este es el mensaje original: ',p)
print(' ')
# Método lower: Convierte los caracteres en minúsculas
print('Método lower: ', p.lower())
# Método upper: Convierte los caracteres en Mayúsuclas
print('Método upper: ', p.upper())
# Método swapcase: Convierte los caracteres de mayor a menos y viceversa
print('Método swapcase: ', p.swapcase())
# Método count: Cuenta los elementos indicados dentro del paréntesis
print('Método count: ', p.count('a'), ' letras "a"')
# Método replace: Reemplaza un elemento por otro
print('Método replace: ', p.replace('a','A'))
# Método capitalize: Cambia el primer caracter en mayúscula
# y las demás en minúsculas
print('Método capitalize: ', p.capitalize())
# Método find: Enumera los caracteres y espacios
# necesarios para llegar hasta la palabra dentro del paréntesis
print('Método find: ', p.find('métodos'),' hasta la palabra "métodos"')
