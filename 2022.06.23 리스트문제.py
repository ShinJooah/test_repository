 #문제1
"""
st =[1,2,3,4,5]

st[1:4] = [3]

 

#문제2

st =[1,2,3,4,5]

st[2:2] = [3,5]

 

#문제3

st =[1,2,3,4,5]

st[1:3] = []

 

#문제4

st = [1,2,3,4,5]

st[0:5] = []

 

 

#문제5

st = [1,2,3,4,5,6,7,8,9,10]

nt = st[0:9:2]

 

 

#문제6

st = [1,2,3,4,5,6,7,8,9,10]

nt = st[1:9:2]

 

#문제 7

str = "Hello"

str += "Python"

print(str)

 

#문제 8

def sum_all(a):

    al = sum(a)

    return al

<풀이>

def sum_all(st):

    sum = 0

    for i in range(len(st)):

        sum += st[i]

    return sum

#문제 9

def show_reverse(b):

    return b.reverse()

 <풀이>

def show_reverse(st):

    for i in range(len(st)):

        print(st[(i+1)*-1],end = ' ')

 
"""