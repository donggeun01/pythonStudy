def cal_fee1(day, age) :
    money = 0
    if age == '대인' :
        if day == '주간' :
            money = 26000
        else :
            money = 21000
    else :
        if day == '주간' :
            money = 19000
        else :
            money = 16000
    return money

def cal_fee2(day, age) :
    money = 0
    if age == '대인':
        if day == '주간':
            money = 33000
        else:
            money = 28000
    else:
        if day == '주간':
            money = 24000
        else:
            money = 21000
    return money

def cal_fee3(age) :
    money = 0
    if age == '대인' :
        money = 55000
    else :
        money = 40000
    return money 

def cal_fee4(age) :
    money = 0
    if age == '대인':
        money = 54000
    else:
        money = 40000
    return money