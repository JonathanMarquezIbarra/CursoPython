# Modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

correo = Email()

print(correo.enviado)
# Se hace el cambio de función dentro de la clase Email
correo.enviar_correo()
print(correo.enviado)
