# Herencia, ejemplo práctico

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    def leer(self):
        self.datos = [int(input('Ingresar datos '+str(i+1)+' = ')) for i in range(self.n)]


# La clase op_basicas hereda atributos desde la clase Calculadora
class op_basicas(Calculadora):
    def __init__(self):
        # con la siguiente linea se restringe a solamente dos parámetros
        #_en este caso numeros, de la clase padre Calculadora
        Calculadora.__init__(self,2)
        # los parámetros a receibir son a y b de la clase suma


    def suma(self):
         a,b, = self.datos
         s = a + b
         print('El resultado es: ',s)
         
    def resta(self):
         a,b, = self.datos
         r = a - b
         print('El resultado es: ',r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es: ',math.sqrt(a))

ejemplo = op_basicas()
print(ejemplo.leer())
print(ejemplo.suma())

ejemplo = raiz()
print(ejemplo.leer())
print(ejemplo.cuadrada())
