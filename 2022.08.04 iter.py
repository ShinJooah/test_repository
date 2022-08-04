#리스트에서 값을 빼는 방법
ds = [1,2,3,4]
for i in ds:
    print(i)

#객체를 얻어내는 함수
#리모컨 다음버튼
ir = iter(ds)
print(next(ir)) #1
print(next(ir)) #2
print(next(ir)) #3
print(next(ir)) #4
#next(ir) #stoplteration 예외처리가 됨.
#ir와 next는 객체에 속해있는 함수

#파이썬이 실제 처리하는 코드!
ds = [1,2,3]
ir = ds.__iter__()
print(ir.__next__())
#스페셜 메소드! #__init__와 비슷함!
#스페셜 메소드 : 파이썬 인터프리터에 의해서 호출되는 메소드

st = 'abcdefg'
sr = iter(st)
print(next(sr))


tp = (1,2,3,4,5)
tr = iter(tp)
print(next(tr))
#iterable 객체 : iter함수에 인자로 전달이 가능한 객체
#iterator 객체 : iter함수가 생성해서 반환하는 객체

#iterable 객체를 대상으로 iter함수를 호출해서 lterator 객체를 만든다.
#iterator 객체를 생성할 수 있는 대상이 되는것이 lterable 객체이다.


r1 = [1,2,3]
print(dir(r1))  #r1에 있는 함수 출력

#실제 for루프의 구조.
for i in [1,2,3]:
    print(i,end=' ')

ir = iter([1,2,3])
while True:
    try:
        i = next(ir)
        print(i,end=" ")
    except StopIteration:
        break

for i in [1,2,3]:
    print(i,end=' ')

ir = iter([1,2,3])
while True:
    try:
        i = next(ir)
        print(i,end=" ")
    except StopIteration:
        ir = iter([1,2,3])
        continue