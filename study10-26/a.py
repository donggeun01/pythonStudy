import module1
import time

module1.func1()

module1.func2()

module1.func3()


print(time.asctime())
print(time.localtime())
myTime = time.localtime()
print(myTime[0],'년',myTime[1],'월',myTime[2],'일',myTime[3],'시',myTime[4],'분',myTime[5],'초')

a =['년','월','일','시','분','초']

for i in range(6) :
    print(myTime[i],a[i])


