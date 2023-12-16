import socket

target_host = "127.0.0.1"
target_port = 9997

# cria um objeto de socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia alguns dados
client.sendto(b"AAABBBCCC", (target_host, target_port))

# recebe alguns dados
data, addr = client.recvfrom(4096)
print(data.decode())

client.close()