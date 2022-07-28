v1= [1,2,3]
v2 =[1,2,3]

print(v1 == v2) #주소 안에있는 내용물이 같음 
print(v1 is v2) #주소가 다름

print(id(v1)) #둘의 주소가 달라
print(id(v2))

#복사
t1 = [1,2,3]
t2 = t1
print(t1 is t2) 