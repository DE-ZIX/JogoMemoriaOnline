import socket


alvo = 'localhost'
porta = 3000

# Criar um cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar o cliente
cliente.connect((alvo, porta))

# Enviar requisição
cliente.send('Estamos conectados')

# Receber dados
r = cliente.recv(1024)
print (r)