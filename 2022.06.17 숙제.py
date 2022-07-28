
"""
#1,3,5,7,9의 합을 계산해서 결과를 출력하는 코드를 for루프를 기반으로 작성해봅시다.

sum = 0

for i in[1,3,5,7,9]:

    sum = sum +i

print(sum)

 

#1부터 10까지의 곱의 결과를 계산해서 그 결과를 출력하는 코드를 for 루프를 기반으로 작성.

sum = 1

for i in range(1,11):

    sum = sum *i

print(sum)

 

#구구단에서 7단 전부를 출력하는 코드

for i in range(1,10):

    print("7 *",i,"=",7*i)

 

# 구구단 7단 전부 출력하되 거꾸로

for i in [9,8,7,6,5,4,3,2,1]:

    print("7 *",i,"=",7*i)

 

숙제
#안녕하세요 5회 출력
for i in range(5):
    print("안녕하세요")

#구구단에서 7단 전부를 출력하는 코드

for i in range(1,10):

    print("7 *",i,"=",7*i)

#제곱 구하는 함수

def exp(x,y):
    return x**y
print(exp(2,3))


def exp(x,y):
    a=1
    for i in range(y):
        a = a*x
    print(a)

#반갑습니다 출력

def greet():
    n = int(input("인사를 몇번할지 입력하세요 :"))
    for i in range(n):
        print("반갑습니다.")

#구구단 2~9

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)

    print("\n")
   

"""

