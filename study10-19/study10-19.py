class Car :
    color = ""
    speed = 0
    count = 0
    def _init_(self):
        self.speed=0
        Car.count+=1

myCar = Car()
myCar.color = "red"
myCar.speed=10

print('%s자동차의 현재 속도는 %d 생산된 자동차 수 %d'%(myCar.color,myCar.speed,Car.count))

myCar2 = None
myCar2 = Car()
myCar2.color = "black"
myCar2.speed = 60
print('%s 자동차2의 현재속도는 %d 생산된 자동차수는 %d이다.' %(myCar2.color, myCar2.speed, myCar2.count))


class Animal:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
    
    def sound(self):
        pass
    def display(self):
        print("이름:",self.name)
        print("나이:",self.age)
        print("종류:",self.kind.aname)
        self.kind.sound()

class Dog :
    aname="강아지"
    def sound(self):
        print('멍멍')

class Cat :
    aname = '고양이'
    def sound(self):
        print('야옹')

mydog = Animal('콩',5,Dog())
myCat = Animal('냥이',3,Cat());
mydog.display()

'''
class SuperClass :
    def __init__(self):
        self.sound();
    def sound(self):
        print('super haha')

class SubClass(SuperClass) :
    def __init__(self):
        self.sound()
    def sound(self):
        print('sub haha')
    sub = SubClass()

class SuperClass :
    def __init__(self):
        self.sound()
    def sound(self):
        print('super haha')

class SubClass(SuperClass) :
    def __init__(self):
        self.sound()
    def sound(self):
        super().sound()
        print('sub haha')
    sub = SubClass()


class Car() :
    speed = 0
    def speedUp(self, value):
        self.speed += value
        print("슈퍼클래스 속도 %d" %(self.speed))
    
class SubCar(Car) :
    def
 '''

class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        pass
    
class Dog(Animal) :
    aname = '강아지'
    def __init__(self, name, age):
        super().__init__(name,age)
    def display(self):
        print('동물명:',self.aname)
        print('이름:',self.name)
        print('나이:',self.age)
    def sound(self):
        print('멍멍')

mydog = Dog('쫑',5)
mydog.display()
mydog.sound()


class People :
    def __init__(self, age=0, name=None) :
        self_age = age
        self_name = name
    def introMe(self):
        print('Name :', self_name, 'age : ', str(self_age))

class Teacher(People) :
    def __init__(self, age=0, name=None,school=None):
        super.__init__(age, name)
        self.school = school
    def showSchool(self):
        print('MySSchoo is',self.school)