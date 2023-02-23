# Módulos

# se importan las funciones desde sus respectivas librerias
from math import pi
from math import factorial
from math import log
from random import choice
from random import randrange
from datetime import date
from fractions import Fraction

p1 = pi
print(p1)

fact = factorial(6)
print(fact)

# el número 10 representa la base
logaritmo = log(8,10)
print(logaritmo)

# selecciona al azar una opcion de los valores dados en la lista
rand = choice(['cara','cruz'])
print(rand)

# selecciona al azar una opción dentro del rango indicado
r_range = randrange(5)
print(r_range)

dia = date(2020,12,11)
print(dia)
# se calculan los días restantes para que termine el año
año = date(2020,12,31)
fin_de_año = (año - dia).days
print(fin_de_año)

# suma de quebrados con Fraction
quebrado = Fraction(2,4)
quebrado2 = Fraction(4,8)
print(Fraction(quebrado+quebrado2))


