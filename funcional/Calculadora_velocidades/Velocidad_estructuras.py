# Calculadora de velocidad

# Definicion de variables
dist_km = 0.0
tiempo_minutos = 0.0

# Leer distancia
def leer_dist():
    print('')
    dist = float(input('Introduzca la distancia recorrida en [Km]: '))
    return dist
# Se le asigna el valor obtenido mediante la función leer
# a la variable dist_km
dist_km = leer_dist()

# Leer tiempo
def leer_tiempo():
    tiempo = float(input('Introduzca el tiempo realizado en [minutos]: '))
    print('')
    return tiempo
# Se le asigna el valor a la variable tiempo_minutos
tiempo_minutos = leer_tiempo()

# Conversión
def conversion(dist_km,tiempo_minutos):
    m = (dist_km * 1000)
    s = (tiempo_minutos * 60)
    return m,s
# Se crean las variables metros y segundos, y se les asignan
# los valores retornados por la función conversión
metros , segundos = conversion(dist_km,tiempo_minutos)

# Calcular velocidad en metros / segundo
def calc_velocidad(metros,segundos):
    m_s = (metros / segundos)
    return m_s

# Se muestra en pantalla la velocidad en metros / segundo
vel_m_s = calc_velocidad(metros,segundos)
print('Velocidad = ',vel_m_s,' m/s.')
print('')

# Calcular la velocidad en kilómetros / hora
def calc_km_h(vel_m_s):
    km_h = vel_m_s*(3600/1000)
    return km_h

#Se muestra en pantalla la velocidad en kilómetros / hora
vel_km_h = calc_km_h(vel_m_s)
print('Equivalente a: ',vel_km_h,' km/h.')
print('')
