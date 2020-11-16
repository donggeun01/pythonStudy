# 문제를 보고 답을 맞추는 서버프로그램 생성
# 클라이언트에서 답을 잘못 입력한 경우 정답이 아닙니다. 전송
# 5초 초과시 타임 아웃
# q, Q를 입력시 프로그램 종료

import socket

table = {'1':'one','2':'two','3':'three',
         '4':'four','5':'five','6':'six','7':'seven',
         '8':'eight','9':'nine','10':'ten'}

s = socket.socket()
address = ("127.0.0.1", 4444)

s.bind(address)
s.listen()

print('Waiting...')
conn, address = s.accept()
print('Connection from', address)

while True :
    data = conn.recv(1024).decode()
    try :
        resp = table[data]
    except :
        conn.send('정답이 아닙니다.'.encode())
    else :
        conn.send(resp.encode())



