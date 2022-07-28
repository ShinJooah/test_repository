"""
객체(Object) : 데이터와 값과 기능을 한번에 모아둠

#객체 안에 있는 함수

1)리스트(list)

st = [1,2,3]

st.remove(2) : 리스트에서 2를 찾아서 삭제

st.append(4) : st 끝에 4 추가

st.extend([5,6]) : st의 끝에 [5,6]의 내용 추가

st.insert(2,3) : 인덱스 값 2의 위치에 3 저장

st.clear() :리스트 내용 전부 삭제

st.pop(0) : 인덱스 값 0의 위치에 저장된 데이터 꺼낸 후 리스트 안에서 삭제

st.count(1) : '1'이 몇 번 등장하는지 세어라.

st.index(2) : 처음 2가 등장하는 위치의 인덱스 값은?

 

del st[:] : 오른쪽에 지정된 만큼 삭제

del st : 리스트 자체를 삭제

 

 

2)문자열(str)

#문자열은 원래 값은 그대로 두고 새로운 문자열을 반환함

 

str = "HeoHyunWook"

str.count("H") : "H"가 몇 번 등장?

.lower()/ .upper() : 모든 문자를 소문자/대문자로 바꿔서 반환

>>>org = "Heo"

>>>lcp = org.lower()

>>>ucp = org.upper()

>>>org

Heo

>>>lcp

heo

>>>ucp

HEO

 

.lstrip()/.rstrip() : (.strip :공백 제거) 앞쪽(왼쪽)/뒤쪽(오른쪽)에 있는 공백 제거

.replace("oo","ee") : "oo" 를 전부 "ee" 로 교체

.replace("oo","ee",1) : 왼쪽에서부터 한 개의"oo" 를 "ee" 로 교체

.split('_') : '_'기준으로 문자열 쪼개서 리스트에

>>>org = "ab_cd_ef:

>>>ret = org.split("_")

>>>ret

['ab','cd','ef']

 

.find("is") : "is"가 있는 위치의 인덱스 값은? //패턴이 존재하지 않을 경우 -1 반환

.rfind("is" : 마지막 "is"가 있는 위치의 인덱스 값은?

 

 

리스트와 문자열의 차이점

-리스트는 값 수정 가능/문자열은 값 수정 불가능

 

 

 

#객체 밖에 있는 함수

1)리스트(list)

len() : 리스트가 몇 개 인지 
"""