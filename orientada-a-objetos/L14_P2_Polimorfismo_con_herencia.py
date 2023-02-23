# Polimorfismo con herencia

class Aves:
    def volar(self):
        print('Algunas vuelan y otras no')

class Aguila(Aves):
    def volar(self):
        print('Las águilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('Las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()
