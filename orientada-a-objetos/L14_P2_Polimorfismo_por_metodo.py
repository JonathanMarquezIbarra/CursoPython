class Colombia:
    def capital(self):
        print('Bogotá')

    def idioma(self):
        print('Español')

class Francia:
    def capital(self):
        print('París')

    def idioma(self):
        print('Francés')


colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()
