import parkmoudle
print('일반입장권, 자유이용권, 2일 자유이용권, 콤비권')
category = input('입장권을 선택하세요 :')
time = input('주간, 야간을 선택하세요 :')
ageCh = int(input('나이를 입력하세요 :'))


if ageCh <= 10 :
    age = '소인'
else :
    age = '대인'

if category == '일반입장권' :
    print('금액 : ',parkmoudle.cal_fee1(time,age))
elif category == '자유이용권' :
    print('금액 :',parkmoudle.cal_fee2(time, age))
elif category == '2일 자유이용권' :
    print('금액 : ', parkmoudle.cal_fee3(age))
elif category == '콤비권' :
    print('금액 : ',parkmoudle.cal_fee4(age))