class Person:
    def __init__(self, param_name):#클래스가 생성됏을 때 내부 __init__함수가 실행됨
        print("i am created!",self)
        self.name = param_name
    def talk(self):
        print("hi my name is ", self.name,"!")

person_1 = Person('유재석')
print(person_1)
print(person_1.name)
person_1.talk()
person_2 = Person('박명수')
print(person_2)
print(person_2.name)
person_2.talk()

