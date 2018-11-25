import socket
import sys
from JogoDaMemoria import EstadoJogo

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('Conectando ao servidor {} na porta {}'.format(server_address[0], server_address[1]))
sock.connect(server_address)

# Cria um tabuleiro de jogo vazio
estado = EstadoJogo()


try:

    while True:
        # Recebe a jogada do servidor
        data = sock.recv(1024)



finally:
    print('Encerrando o cliente')
    sock.close()