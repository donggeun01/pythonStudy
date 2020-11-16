import socket
address = ('localhost', 4444)

s = socket.socket()
s.connect(address)

while True :
    msg = input("Message to send")
    try :
        n = s.send(msg.encode())
    except :
        print('송신 연결이 종료되었습니다.')
        rety = input("계속(y/n)")
        if rety == 'n' :
            s.close()
            break
        else :
            continue
    else :
        print("{} bytes sort : " .format(n))
