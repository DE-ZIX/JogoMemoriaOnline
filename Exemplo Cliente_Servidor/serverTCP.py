import socket
import threading

bind_ip = 'localhost'  # IP em que o servidor estará rodando
bind_port = 80         # PORTA em que o servidor estará rodando

# SOCK_STREAM informa que estamos usando o Protocolo ITCP e AF_INET que estamos usando IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# ouve um total de até 5 conexões simultâneas
server.listen(5)

print('[*] Escutando %s:%d' % (bind_ip, bind_port))

# Função que chama o Laço Infinito
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print('[*] Recebido: %s' %request)
    print('----------------')
    client_socket.send(' Mensagem destianda ao cliente: %s' %addr[0])
    client_socket.send(' ACK! Recebido pelo servidor!')
    client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Conexão aceita de; %s:%d' %(addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()
