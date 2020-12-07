'''
숫자 야구 게임
1. 서버 구동 후 client 접속 대기
2. 숫자야구 번호 생성 (튜플? 리스트)
3. client 접속
4. client 메세지 수신
5. 정답 여부 및 힌트 송신
6. 오답 시 계속, 정답 시 프로그램 종료
'''

import socket
address = ("localhost", 4444)

s = socket.socket()

s.connect(address)
print('게임을 시작합니다.')
while True :
    answer = input("정답 : ")

    try :
        n = s.send(answer.encode())
    except :
        print("연결이 끊어졌습니다.")
        rety = input("계속(y/n) : ")

        if rety == 'n' :
            s.close()
            break
        else :
            continue
    try :
        count = s.recv(1024)
        strike = s.recv(1024)
        ball = s.recv(1024)
        if (strike.decode() == '0' and ball.decode() == '0'):
            print("아웃입니다.")
        elif strike.decode() == '4' :
            print("정답입니다.")
            print("%s번에 맞추셨습니다." %count.decode())
            print("프로그램을 종료합니다.")
            s.close()
            break
    except :
        print("수신 연결이 종료되었습니다.")
        s.close()
        break
    else :
        print("%s번 시도" % count.decode())
        print("%s 스트라이크 %s 볼" %(strike.decode(), ball.decode()))