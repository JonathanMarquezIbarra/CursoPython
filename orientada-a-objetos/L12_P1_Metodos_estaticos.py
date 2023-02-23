# Métodos estáticos

import math

class Pastel:
    def __init__(self,ingredientes,tamanio):
        self.ingredientes = ingredientes
        self.tamanio = tamanio
        
    def __repr__(self):
        return(f'Pastel({self.ingredientes}, 'f'{self.tamanio})')
    
    def area(self):
        return self.tamanio_area(self.tamanio)

    @staticmethod
    def tamanio_area(A):
        return A == 2 * math.pi

nuevo_pastel = Pastel(['harina','azucar','leche','crema'],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamanio)
print(nuevo_pastel.tamanio_area(12))

