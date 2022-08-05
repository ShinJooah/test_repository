#객체가 아닌 것 : 함수
x = 3.0
print(type(x))

#소수점 값이 존재하나?(1)
print(x.is_integer())

#소수점 값이 존재하나?(2)
def func1(n):
    return n

def func2():
    print("HI")

print(type(func1))
print(type(func2))      #function 이라는 타입

print(func1(10))
print(func2()) #함수도 객체다 -> 매개변수(인자) 넣을 수 있나?

def say1():
    print("Hola")
def say2():
    print("Adios")

def caller(fct):
    fct()

caller(say1)
caller(say2)

def fac_fac(n):
    def exp(x):
        return x**n
    return exp

f1 = fac_fac(2)
f2 = fac_fac(3)
print(f1(4)) #4의 거듭제곱은?
print(f2(3))

#람다 
#이름 없는 함수 만들기
def show(s):
    print(s)

ref = show
ref("Adios~")   #레퍼런스 카운터가 두개가 됨

#람다로 정의
ref = lambda n: print(n*2)
ref("adios~") 

f1 = lambda n1, n2 : n1+n2
print(f1(10,3))

def ref1(s):
    return s
print(ref1("HI"))
#람다와는 다르게 ''의 문자열이 출력됨

ref = lambda s: s
print(ref('HI'))
#둘이 똑같음 = lambda s : return s

f2 = lambda s : len(s)
print(f2("adios~"))

#매개변수 없는 lambda
f3 = lambda : print("냠냠")
print(f3())

def fac_fac(n):
    return lambda x: x**n


f1 = fac_fac(2)
f2 = fac_fac(3)
print(f1(4)) #4의 거듭제곱은?
print(f2(3))