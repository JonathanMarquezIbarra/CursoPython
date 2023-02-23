# Funciones para atributos

# Se declara la clase
class Persona:
    edad = 27
    nombre = "Victor"
    apellido = "Pérez"
    pais = "Colombia"
# Se declara el objeto, relacionándolo con la clase Persona
doctor = Persona()
# Se hace referencia a un atributo de la clase Persona
print("La edad es: ",doctor.edad)
# Otra manera es:
print("La edad es: ", getattr(doctor,'edad'))

# con hasattr devuelve un true o false si el atributo existe
print('El doctor tiene una edad? ', hasattr(doctor,'edad'))

# Con setattr se cambia el valor de un atributo de la clase_
#_en este caso cambia Pérez por Ramírez
setattr(doctor,'apellido', 'Ramírez')
# La sintaxis es: (objeto,'atributo', 'nuevo valor') NOTA: se usan comillas
#_simples
print(doctor.apellido)

# Con delattr se borra un atributo
print(doctor.pais)
# La sintaxis es (clase, 'atributo a borrar')
delattr(Persona,'pais')


