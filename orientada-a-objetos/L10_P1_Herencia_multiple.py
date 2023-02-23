# Herencia múltiple

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('Ocupado...')

class Camara:
    def __init__(self):
        pass
    def foto(self):
        print('Tomando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def musica(self):
        print('Reproduciendo música...')
    def video(self):
        print('Reproduciendo video...')

class Smartphone(Telefono,Camara,Reproduccion):
    # Así como con __init__ se indica el constructor_
    #_con __del__ se indica que es un deconstructor
    def __del__(self):
        print('Teléfono apagado...')


movil = Smartphone()
# Mediante la sentencia dir se obtiene un directorio de los métodos_
#_que puedne ser aplicados al objeto que se le mande como argumento

print(dir(movil))

print(movil.llamar)
