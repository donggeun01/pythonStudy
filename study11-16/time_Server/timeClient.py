import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 4444)

sock.connect(address)

print('현재 시각:', sock.recv(1024).decode())