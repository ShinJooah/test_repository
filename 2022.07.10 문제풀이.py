#다음 수식의 빈칸에 들어갈 '수'를 찾는 코드를 작성해보자 단 빈칸에 들어갈 수는

#1부터 시작해서 1씩 증가시켜가면서 찾기로 하자.

"""num = 0

r = 0

 

while r != 63:

    num += 1

    r = 3*num/2

print(num)"""

 

#문제 2-1)

#6과 45의 최소공배수를 구하는 코드

"""

lcm = 0

n = 45

while True:

    if n%6==0 and n%45==0:

        lcm = n

        break

    n=n+1
"""
 

#2-2

#최대 공약수
"""

gcm = 0

n=42

while True:

    if 42%n==0and 120%n==0:

        gcm=n

        break

    n-=1

    """

 

#구구단 7단 짝수
"""

for i in range(1,10):

    if(7*i)%2:

        continue

    print(7*i,end=' ')

    
"""
#3-2

#2이상100미만의 정수중 2로도 나누어지지않고 3으로도 나누어지지않는 수를 찾아 출력
"""
num =1

while num<100:

    num+=1

    if num %2 ==0 or num %3 == 0:

        continue

    print(num,end=' ')

 

 

num =1

while num<100:

    num+=1

    if num %2!=0 and num %3 != 0:

        print(num,end=' ')

 
"""
 

#구구단

"""

for i in range(2,10):

    for j in range(1,10):

        print(i*j,end=' ')

    print("\n")
"""