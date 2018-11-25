import socket

# estabelecer Host e Porta
myHost = 'localhost'
myPort = 3000

# Criar o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((myHost, myPort))  # esperar conexão
server.listen(5)  # o servidor pode lidar com até 5 conexões ao mesmo tempo

print('[*] Escutando %s:%d' % (myHost, myPort))
# Configurar conexões
while True:
    conexao, endereco = server.accept()
    print('[*] Servidor conectado por', endereco)

    while True:

        data = conexao.recv(1024)
        if not data: break
        conexao.send(b'[*]Recebido pelo servidor: ' + data)


    conexao.close()

