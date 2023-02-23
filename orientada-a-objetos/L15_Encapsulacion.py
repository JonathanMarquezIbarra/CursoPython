# Encapculación

class Cliente:
    def __init__(self):
        self.__codigo = 4321
        
    def __cuenta(self):
        print('Cuenta de procesamiento')
        
    def getcodigo(self):
        return self.__codigo

persona = Cliente()

# Para accede a codigo:     objeto._nombreclase__nombreatributo

print(persona._Cliente__codigo)

# Para acceder a cuenta:

persona._Cliente__cuenta()
