import socket

s = socket.socket()
#s.connect(('localhost', 9999))
s.connect(('192.168.100.101', 9999))

while True:
    mensaje = input('+> ')    
    s.send(mensaje.encode())
    if mensaje == 'quit':
        break
        print('Conexión finalizada desde el cliente...')
        s.close()

