import socket

s = socket.socket()
#s.bind(('localhost', 9999))
s.bind(('192.168.100.101', 9999))
s.listen(1)

sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == 'quit':
        break
    print('Cliente: ', recibido)
    sc.send(recibido)

print('El cliente finalizó la conexión....')
sc.close()
s.close()
