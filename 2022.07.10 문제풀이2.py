#튜플을 리스트로
"""
def to_list(t):

    st = []

    for i in t:

        st.append(i)

    return st
"""
 

#구구단 7단 거꾸로
"""
for i in range(9,0,-1):

    print(7*i,end=' ')

 

tp = tuple(range(1,100))+tuple(range(100,0,-1))

 

 

for i in range(3):

    print(i+1,i+2,i+3,sep=',')

 

    

def add1(li):

    for i in range(len(li)):

        li[i]+=1
"""