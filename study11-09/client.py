import socket
ip = '127.0.0.1'
port = 4444


# 클라이언트 소켓 생성
client = socket.socket()

client.connect((ip,port))
print('Server connect...')

client.sendall(b'send MSG from client')
print('send msg')

msg = client.recv(1024)
print('...msg receive')
print(msg)

client.close()

