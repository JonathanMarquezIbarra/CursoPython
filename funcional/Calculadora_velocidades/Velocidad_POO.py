#! /usr/bin/python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime

# Calculadora de velocidad

# Creación de la función Guardar
def guardar(kilometros,minutos,km_h,m_s):
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    anio = str(now.year)
    fecha = (dia + ' - ' + mes + ' - ' + anio + ':   ')
    
    km = str(kilometros)
    minu = str(minutos)
    
    filename = '/home/excision18/Documentos/Proyectos Python/Proyectos_personales/Bitacora_velocidad.txt'

    with open(filename, 'a') as file_object:
        file_object.write('* ' + fecha + km + ' Kilómetros.'+'\n')
        file_object.write('* ' + fecha + minu + ' minutos.'+'\n')
        file_object.write('* ' + fecha + km_h +' [Km/hora].'+'\n')
        file_object.write('* ' + fecha + m_s +' [metros/segundo].'+'\n'+'\n')


def imprimir(km_h,m_s):
    print('La velocidad es de: ' + km_h + ' [Km/hora].')
    print('Equivalente a: ' + m_s + ' [metros/segundo].')


# Creación de la clase in_data
class In_data():
    def leer(self):
        print('')
        self.km = float(input('Ingrese la distancia recorrida [Km]:         '))
        self.m = float(input('Introduzca el tiempo realizado [minutos]:    '))
        return self.km, self.m
''' La clase In_data guarda los datos ingresados por el usuario mediante el
teclado en las variables self.km y self.m y los retorna como un diccionario'''


# Creación de la clase carrera
class Carrera():
    # Constructor de la clase carrera
    def __init__(self,km,minutos):
        self.km = km
        self.minutos = minutos
    def calcular_km_hora(self):
        # Se hace la conversión de minutos a horas
        horas = (self.minutos/60)
        # Se calcula la velocidad en unidades de km/hora
        velocidad_km_hora = (self.km / horas)
        print('')
        # Se muestra el resultado en pantalla
        return velocidad_km_hora
    def calcular_m_s(self):
        # Se hace la conversión de kilómetros a metros
        metros = self.km * 1000
        # Se hace la conversión de minutos a segundos
        segundos = self.minutos * 60
        # Se calcula la velocidad en unidades de metros/segundo
        velocidad_m_s = metros / segundos
        # Se muestra en pantalla el resultado en metros/segundo
        #print('Equivalente a: ',velocidad_m_s,'[metros/segundo].')
        print('')
        return velocidad_m_s
'''La clase carrera está comprendida por su contructor y los métodos de clase
calcular_km_hora y calcular_m_s. Primero se reciben los parámetros km y minutos,
luego se hace la conversión a las unidades deseadas y se muestran en pantalla'''


# Se crea el objeto leer1 y se indica que es instancia de la clase In_data
leer1 = In_data()
# Se crea la variable datos, que al momento de recibir los valores del método
# leer() se convierte en un diccionario de dos valores, (kilómetros y minutos)
datos = leer1.leer()
# Se crean las variables kilometros y minutos y se le asigna a cada una
# el valor correspondiente que se obtuvo del método leer de la clase In_data
kilometros = datos[0]
minutos = datos[1]


# Se crea el objeto carrera1, que es una instancia de la clase Carrera
# y se le mandan como argumentos las variables kilómetros y minutos
carrera1 = Carrera(kilometros,minutos)
# Se mandan llamar a los métodos de clase del objeto carrera1 que hacen
# los cálculos correspondientes y los muestran en pantalla
km_h = str(carrera1.calcular_km_hora())
m_s = str(carrera1.calcular_m_s())

imprimir(km_h,m_s)
guardar(kilometros,minutos,km_h,m_s)

# El tiempo está en segundos
time.sleep(120)
