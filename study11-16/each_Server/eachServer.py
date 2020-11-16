from socket import *

sock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
address = ('localhost', 4444)
sock.bind(address)
sock.listen(0)

conn, (remotehost, remoteport) = sock.accept()

print('connected by', remotehost, remoteport)

while True :
    try :
        data = conn.recv(1024)
    except Exception as e :
        print("연결이 종료되었습니다.")
        conn.close()
        break
    else :
        print(data.decode())
    try :
        conn.send(data)
    except :
        print('연결이 종료되었습니다.')
        conn.close()
        break
