# 문제를 보고 답을 맞추는 서버프로그램 생성
# 클라이언트에서 답을 잘못 입력한 경우 정답이 아닙니다. 전송
# 5초 초과시 타임 아웃
# q, Q를 입력시 프로그램 종료

import socket

i = 0
table = {'one':'1','two':'2','three':'3',
         'four':'4','five':'5'}
a = list(table.keys())


s = socket.socket()
address = ("127.0.0.1", 4444)

s.bind(address)
s.listen()

print('Waiting...')
conn, address = s.accept()
print('Connection from', address)


while True :
    conn.send(a[i].encode())
    data = conn.recv(1024).decode()

    try :
        resp = table[a[i]]
        if resp == data :
            i = i + 1
            conn.send("정답입니다. ".encode())
        else :
            conn.send('정답이 아닙니다.'.encode())
    except :
        conn.send('정답이 아닙니다.'.encode())





