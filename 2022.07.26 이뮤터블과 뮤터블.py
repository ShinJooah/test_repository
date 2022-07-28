"""
수정이 가능한 객체와 수정이 불가능한 객체

 

수정이 불가능한 객체(이뮤터블,immutable):문자열,튜플

수정이 가능한 객체(뮤터블,mutable):리스트

 

a = [1,5,3,7,33,11,7,0,99,5,7,3]

a.sort() : 오름차순으로 정렬 

 

#sort() 예제

I = [3,1,5,4,7,6]

 

def min_max(a):

    a.sort()

    print(" 가장 작은 수 : ",a[0],"\n","가장 작은 수 : ",a[-1])

    

min_max(I)

 
#원본의 숫자가 바뀜
I = [3,1,5,4,7,6]
 
def min_max(a):
    a.sort()
    print(" 가장 작은 수 : ",a[0],"\n","가장 작은 수 : ",a[-1])
 
print(I)
min_max(I)
print(I)
 
 
#원본 숫자 바뀌지 않는 방법 : 복사해서 사용
I = [3,1,5,4,7,6]

def min_max(a):
    a = list(a)
    a.sort()
    print(" 가장 작은 수 : ",a[0],"\n","가장 작은 수 : ",a[-1])

print(I)
min_max(I)
print(I)

#튜플로 작업 가능gka
c = (3,1,5,4,7,6)
min_max(c)
print(c)
"""