# 번호 입력시 정답 리턴 받아 출력
import socket
address = ("localhost", 4444)

s = socket.socket()

s.connect(address)

while True :
    qu = s.recv(1024)
    print("종료를 하길 원하시면 q 를 눌러주세요.")
    msg = input("문제 %s : " %qu.decode())
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