import socket

target_host = "www.google.com"
target_port = 80

# cria um objeto de socket
client = socket.socket(socket.AF_INET, socket.SOCK_STRAM)

# conecta o cliente
client.connect((target_host, target_port))

# envia alguns dados
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# recebe alguns dados
response = client.recv(4069)
print(response.decode())

client.close()