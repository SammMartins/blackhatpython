import socket

target_host = "127.0.0.1"
target_port = 9998

# cria um objeto de socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta o cliente
client.connect((target_host, target_port))

# envia alguns dados
client.send(b"ABCDEF")

# recebe alguns dados
response = client.recv(4096)
print(response.decode())

client.close()