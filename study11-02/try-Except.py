from builtins import print, range

# 예외 처리 학습
'''
num = int(input("숫자를 넣으세요 :"))
try :
    a = 1 / num
except ZeroDivisionError :
    print("0으로 나올 수 없습니다.")
else :
    print(a)


import sys
try :
    fp = open("t.txt")
    sl = fp.readline()
    sl = int(fp.readline())
    value = sl.strip()
except OSError as err:
    print("OS오류")
except ValueError :
    print("정수로 변화 불능")
except :
    print("알수 없는 예외")
else :
    print(value)

def isEven(n) :
    if n%2 == 0 :
        return True
    else :
        return False
assert isEven(8)
print('Even')


data = {'Sun':0,'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6}


while True :
    try :
        text = input("문자열을 입력하세요 : ")
        print('값 : ',data[text])

    except :
        print('data 없음')
        print('프로그램을 종료합니다.')
        break
'''

'''
# 파일 입출력 학습

# 파일 입력
outfile = None
instr = ""
outfile = open('test03.text','w',encoding='utf-8') #파일 쓰기

while True :
    instr = input("내용입력 : ")
    if instr != '' :
        outfile.write(instr + '\n')

    else :
        break;
outfile.close()


# 파일 출력
infile,outfile = None,None
instr =""
infile = open('filetest01.py','r',encoding='utf-8') # 파일 읽기

while True :
    instr = infile.read()
    if instr != ""  :
        print(instr + '\n')

    else :
        break


# 파일 입력 및 출력
infile,outfile = None,None
instr =""
infile = open('filetest01.py','r',encoding='utf-8')  # 파일 읽기
outfile = open('filetest01.py','w',encoding='utf-8') # 파일 쓰기

# while True : 
#    instr = infile.read()
#    if instr != "" :
#        outfile.write(instr + '\n')
        
#    else : 
#       break

for i in instr :
    outfile.write(i)

infile.close()
outfile.close()
'''

'''
# 파일 읽기 연습
filein = open('test03.text','r',encoding='utf-8')
# readall = filein.read() # 파일 전체 읽기
# readall = filein.read(7) # 파일 문자 7개 읽기
# readall = filein.readline() # 한줄 읽기
readall = filein.readlines() # 파일 전체를 한줄씩 읽어 리스트에 저장
print(readall)
filein.close()


# 연습문제
infile = None
instr = ''
infile  = open('e://파이썬//t1.txt','r',encoding='utf-8')
for i in range(len(instr)) :
    print(i+1,''.instr[i], sep="")
infile.close()

infile = None
instr = ''
fname = input("파일명을 입력하세요")
try :
    infile = open(fname,'r',encoding='utf-8')

except FileNotFoundError :
    print('파일이 존재하지 않습니다.')

else :
    instr = infile.readlines()
    for i in range(len(instr)) :
        print(i+1,'.',instr[i],sep="")
    infile.close()

with open('./phones1.txt','w',encoding='utf-8') as fileout :
    fileout.write('성춘향 010-2345-6789\n')
    fileout.write('이몽룡 010-2345-6789\n')
    fileout.write('변학도 010-2345-6789\n')
    fileout.write('장금이 010-2345-6789\n')


inFp, outFp = None, None
inStr = ''
inFp = open('./test01.png','rb')
outFp = open('./test02.png','wb')

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)

    inFp.close()
    outFp.close()
    print('image file copied.')


print(chr(97)) # a
print(ord(122)) # z

for i in range(ord('a'), ord('z')) :
    print(chr(i))
'''


k = int(input('1. 암호화 2. 복호 : '))
text = input("입력 파일명 :")

if k == 1 :
    print('파일 암호화')
    print('출력 파일명 : ',end="")
    for i in text :
        print(chr(ord(i) + 200), end="")

else :
    print('파일 복호화')
    print('출력 파일명 : ',end="")
    for i in text:
        print(chr(ord(i) - 200), end="")

