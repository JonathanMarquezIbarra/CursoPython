# Método contructor

class Persona:
    # Pass significa que por el momento está vacío pero se va a llenar
    pass
    def __init__(self,nombre,anio):
        self.nombre = nombre
        self.anio = anio        
    def descripcion(self):
        return ' {} tiene {} años '.format(self.nombre,self.anio)
    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('José',26)

print(doctor.descripcion())
print(doctor.comentario('hola que tal '))
