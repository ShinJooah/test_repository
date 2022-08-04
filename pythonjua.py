H2022 = ["허지훈",('남자','한국'),["잘생김",20]]
import copy
H2023 = copy.deepcopy(H2022)
print(H2023)
H2023[2][1] += 1
print(H2023)

print((H2022[0] is H2023[0])and (H2022[1] is H2023[1]))
print(H2022[2]is H2023)

#빈 리스트 r1을 만들고, 리스트에 내용을 1~10 까지 체워주세요. 
#그 다음에 리스트에 저장된 내용을 2배씩 증가시키는 코드를 작성해주세요
def main():
    r1 = []
    r1 = [i+1 for i in range(10)]
    r2 = [x*2 for x in r1]
    print(r2)

main()

#홀수만 출력
def main():
    r1 = []
    r1 = [i+1 for i in range(10)]
    r2 = [x*2 for x in r1 if x %2 == 1]
    print(r2)

main()