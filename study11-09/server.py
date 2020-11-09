import socket

server = socket.socket()
server.bind(('127.0.0.1',4444))

server.listen(1)
print('Server read...')

while True :
    # 클라이언트 접속 수락, 연결
    client, addr = server.accept()
    print('...Client is connect')

    # 메세지 수신
    print('나는 서버입니다.')
    while True :
        msg = client.recv(1024)
        print('클라이언트 메세지 수신 : ', repr(msg.decode()))
    # 메세지 송신
        print('클라이언트 메세지 송신', addr)
        if msg:
            client.sendall('안녕 나는 서버야'.encode())
            print('메세지를 보냈습니다.')

        else:
            print('no Date', addr)

        break
    client.close()
    server.close()

'''
client, addr = server.accept()
print('...Client is connect')
msg = client.recv(1024)
print('msg received')
print(msg)

client.sendall(b'server message\n')
client.sendall(b'send MSG from server')

print('msg send')
client.close()
server.close()
'''