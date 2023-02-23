# Palabras reservadas Del e In

# del : borra elementos dentro de una lista
curso = 'python'
# se creó la variable curso que es de tipo cadena
lista_nueva = list(curso)
# se convirtió la variable curso en la lista lista_nueva
print(lista_nueva)
# se borra la 'p' mediante del
del lista_nueva[0]
print(lista_nueva)
# in : verifica si un elemento es parte de una lista
print('y' in curso)

if 'y' in lista_nueva:
    print('t es parte de la lista')
