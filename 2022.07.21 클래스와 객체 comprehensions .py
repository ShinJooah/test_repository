#인터넷 찾아본 리스트 comprehensions

"""

squarel = []

for x in range(0,10):

squarel.append(x*x)

 

==

 

[x*x for x in range(0,10)]

 

이렇게 줄여서 쓸 수 있다.

 

eve_number = list()

for x in range(20):

if x%2 ==0:

even_number.append(i)

 

==

 

even_number_compre = [x for x in range(20) if x % 2 == 0]

 

 

 

 

 

 

 

객체 = 인스턴스

 

인스턴스 변수 : 인스턴스(객체) 안에 존재하는 변수

인스턴스 안에 존재하는 변수 - 아빠 문제의 age 느낌 

 

인스턴스 메소드 : 인스턴스(객체) 안에 존재하는 메소드(함수)

- def up_age(self):

- def get_age(self):

 

 

 

#family_age3.py

class AgeInfo:

    def up_age(self):

        self.age +=1

    def get_age(self):

        return self.age

 

def main():

    fa = AgeInfo()

    mo = AgeInfo()

    me = AgeInfo()

    fa.age = 20

    mo.age = 20

    me.age = 9

    sum = fa.get_age() +mo.get_age() + me.get_age()

    print("가족 나이 합 :",sum)

    fa.up_age()

    mo.up_age()

    me.up_age()

    sum = fa.get_age() +mo.get_age() + me.get_age()

    print("가족 나이 합 :",sum)

    print(fa.age)    

    

 
#직접적으로
class AgeInfo:
 
    def up_age(self):
 
        self.age +=1
 
    def get_age(self):
 
        return self.age
 
def main():
    fa = AgeInfo()
    fa.age = 20
    fa.up_age()
 
    AgeInfo.up_age(fa) #직접적 안좋음
 
    print(fa.get_age())
    print(AgeInfo.get_age(fa))
 
main()
 
 
 
#매개변수 age와 파이썬이 만들어준 age는 다름. 그래서 구분 가능해야 함.
class AgeInfo:
 
    def up_age(self):
        self.age +=1
 
    def get_age(self):
        return self.age
 
    def set_age(self,age):
        self.age = age
 
def main():
    fa = AgeInfo()
    fa.set_age(20)
    fa.up_age()
    print("1년 후 아빠 나이 :",fa.get_age())
    
    
 
main()
 
 
 
#constructor ( java ,c# ,c++) -> 생성자
#Initializer, generator -> 초기화 함수, 생성자
constructor 과 generator은 성격이 매우 다름
constructor 과 initializer 은 비슷함
따라서 constructor = initializer 생성자로 동일.
 
 
 
 
#ctor1.py
class Const:
    def __init__(self):
        print("new~")
 
def main():
    o1 = Const()
    o2 = Const()
 
main()
 
// init 안에 있는 함수가 실행이 되었다는 것을 알 수 있다.
 
 
#이때까지 변수를 초기화 시켜줄려면 두줄이 필요했는데 생성자를 통해 하나로 가능하게 만들었다.
 
 
#ctor2.py
class Const:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def show_data(self):
        print(self.n1, self.n2)
 
def main():
    o1 = Const(1,2)
    o2 = Const(3,4)
    o1.show_data()
    o2.show_data()
 
main()
 
 
 
 
 
#파이썬의 모든 값은 객체
n = 1000
n.bit_length()
10
 
f = 3.14
f.is_interger()
False
 
 
 
 
 
hyh6269@naver.com
jihun0831
 
 
 
 
 
 
#숙제 1
class Freind:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        print(self.name)
    def get_phone(self):
        print(self.phone)
    def set_phone(self,phone):
        self.phone = phone
    def show_info(self):
        print(self.name,self.phone)
 
def main():
    f = Freind('허지훈','010 2228 4517') 
    f.get_name()
    f.get_phone()
    f.set_phone('010 4545 1212')
    f.show_info()
 
main()
 
 
 
#숙제 2
class Freind:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        print(self.name)
    def get_phone(self):
        print(self.phone)
    def set_phone(self,phone):
        self.phone = phone
    def show_info(self):
        print(self.name,self.phone)
 
friend_list.append(Friend('허현욱','010-9876-5432'))
friend_list.append(Friend('이선준','010-7410-0258'))
friend_list.append(Friend('장지우','010-9630-0258'))
friend_list.append(Friend('허진욱','010-4321-1234'))
 
for i in friend_list:
    i.show_info()
 
 
#숙제 3
 
for i in friend_list:
    if i.get_name().startswith('허'):
        i.show_info()
 
#숙제 4

for i in friend_list:
    if i.get_name() == '장지우':
        i.set_phone('010-8520-0147')

        
for i in friend_list:
    if i.get_name() =='장지우':
        i.show_info()

        
장지우 010-8520-0147





 
클래스 : 데이타와 기능(메소드)을 기반으로 만들어진 일종의 틀.
객체 : 클래스라는 틀을 기반으로 만들어 낸 메모리에 존재하는 실제 대상
 
객체 생성 시 데이타와 기능이 함께 채워져서 만들어진다.
그러나... 사실은 객체 속 테이타는 나중에 채워진다. 
"""