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
import random

count = 0
ballList = []
num = random.randrange(0,10)


# 중복 없는 난수 생성
for i in range(4) :
    while num in ballList :
        num = random.randrange(0,10)
    ballList.append(num)

for i in range(4) :
    ballList[i] = str(ballList[i])

ballNumber = tuple(ballList)

s = socket.socket()
address = ("127.0.0.1", 4444)

s.bind(address)
s.listen()

print('접속을 기다리고 있습니다.')
conn, address = s.accept()
print('사용자가 접속했습니다.', address)
print(ballNumber)

while True :
    try :
        strike = 0
        ball = 0
        data = conn.recv(1024).decode()
        resp = list(data)

        for i in range(4) :
            if resp[i] == ballNumber[i] :
                strike = strike + 1
            elif resp[i] in ballNumber :
                ball = ball + 1
    except :
        s.close()
        print("프로그램 종료")
        break;

    else :
        count = count + 1
        print("스트라이크 : ", strike)
        print("볼 : " , ball)
        conn.send(str(count).encode())
        conn.send(str(strike).encode())
        conn.send(str(ball).encode())



