# Métodos

class Matematica:
    # Nota: Mediante self se hace referencia a un objeto que_
    #_aún no ha sido creado
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()

s.suma()
print(s.n1 + s.n2)
