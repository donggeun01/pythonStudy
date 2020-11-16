# 번호 입력시 정답 리턴 받아 출력
import socket
address = ("localhost", 4444)

s = socket.socket()

s.connect(address)

while True :
    msg = input("Message to send : ")
    try :
        n = s.send(msg.encode())
    except :
        print("송신 연결이 종료되었습니다.")
        rety = input("계속(y/n)")

        if rety == 'n' :
            s.close()
            break
        else :
            continue

    else :
        print("{} bytes sent" .format(n))
    s.settimeout(5.0)
    try :
        data = s.recv(1024)
        if not data :
            break
        if msg == 'q' or msg == 'Q' :
            break
    except :
        print("수신 연결이 종료되었습니다.")
        s.close()
        break
    else :
        print("Received message: %s" %data.decode())