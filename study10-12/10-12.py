# 1번 문제
num1 = float(input("실수를 입력하세요 : "))
num2 = float(input("2번째 실수를 입력하세요 : "))
print(num1* num2)

# 2번 문제
min = int(input('분을 입력하세요 :'))
hour = 0
day = 0
if (min >= 60) :
    hour = min // 60
    min = min % 60
if (hour >= 24) :
    day = hour // 24
    hour = hour % 24
print(day,"일",hour,"시간" ,min,"분")

# 3번 문제
score  = [95,100,75,80,90,85,95,60,85,70]
sum = 0
for i in score :
    sum = sum + i
print("평균 : ",sum//len(score))

# 4번 문제
word = 'Python'
print(word[::-1])

#5번 문제
frult = {'peach':6000,'grape':7000,'apple':5500,'banana':3500,'tomato':4000}

#6번 문제
frult_sort = list(frult.items())
frult_sort.sort()
print(frult_sort)

#7번 문제
text = input("이름을 입력하세요 : ")
print(frult.get(text))

#8번 문제
def check_pwd(num) :
    if (num == '1234') :
        return print("성공")
    while(True) :
        num = input("비밀번호가 틀렸습니다 다시 입력하세요 : ")
        if (num == '1234') :
            return print("성공")
check_pwd("1235")

#9번 문제
data = [28,15,10,25,32,17]

for i in range(0,6) :
    k = data[i]
    for j in range(i,6) :
        if data[j] < data[i] :
            data[i] = data[j]
            data[j] = k
            k = data[i]
            print(data)

#10번 문제
star = int(input("3자리 숫자 입력 : "))
num1 = star / 100
num2 = (star-(num1*100)) / 10
num3 = (star-(num1*100)) % 10
for i in range(0,3) :
    for j in range(num1) :
        print('*',end="")
    print("")
    for j in range(0,num2) :
        print('*',end="")
        print("")
    for j in range(0,num3) :
        print('*',end="")


