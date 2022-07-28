# 1. 처리 가능

# 1)

# lit = [1,2,3] 

# lst[int(input("0~2사이"))]

# Traceback (most recent call last):

#   File "<pyshell#35>", line 1, in <module>

#     lst[3]

# IndexError: list index out of range

 

# 2)

# def main():

#     print("안녕하세요.")

#     age = int(input("나이를 입력하세요:"))

#     print("입력하신 나이는 다음과 같습니다.:",age)

#     print("만나서 반가웠습니다.")

 

    

# main()

# 안녕하세요.

# 나이를 입력하세요:스물

# Traceback (most recent call last):

#   File "<pyshell#45>", line 1, in <module>

#     main()

#   File "<pyshell#44>", line 3, in main

#     age = int(input("나이를 입력하세요:"))

# ValueError: invalid literal for int() with base 10: '스물'

 

 

 

# 2. 처리 불가능

 

# 1)

#  lit = [1,2,3] 

# lst[3]

# Traceback (most recent call last):

#   File "<pyshell#35>", line 1, in <module>

#     lst[3]

# IndexError: list index out of range

 

# 2)

# 3+"coffee"

# Traceback (most recent call last):

#   File "<pyshell#37>", line 1, in <module>

#     3+"coffee"

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

 

# 3)

# 3/0

# Traceback (most recent call last):

#   File "<pyshell#38>", line 1, in <module>

#     3/0

# ZeroDivisionError: division by zero

 

 

 

# #예외 처리

# try:

#     try 영역

# except ValueError:

#     except 영역

 

 

# #age_expt.py

 

# def main():

#     print("안녕하세요")

 

#     try:

#         age = int(input("나이를 입력하세요 :"))

#         print("입력하신 나이는 다음과 같습니다:",age)

#     except ValueError:

#         print("입력이 잘못되었습니다.")

 

#     print("만나서 반가웠습니다.")

    

# main()

 

# #age_expt_conti.py

# def main():

#     print("안녕하세요")

#     while True:

        

#         try:

#             age = int(input("나이를 입력하세요 :"))

#             print("입력하신 나이는 다음과 같습니다:",age)

#             break

#         except:

#             print("입력이 잘못되었습니다.")

    

 

#     print("만나서 반가웠습니다.")

    

# main()


# #예외처리 문제
# def main():

#     bread = 10

#     try :

#         people = int(input("몇 명?"))

#         print("1인당 빵의 수 :", bread / people)

#         print("맛있게 드세요.")

 

#     except ValueError as msg:

#         print("입력이 잘못되었습니다.")

#         print(msg)

#     except ZeroDivisionError as msg:

#         print("0으로 나눌 수 없습니다.")

#         print(msg)

# main()

 

 

 

# finally : 무조건 실행하는 명령어 

 

#  def main():

#     bread = 10

#     try :

#         people = int(input("몇 명?"))

#         print("1인당 빵의 수 :", bread / people)

#         print("맛있게 드세요.")

 

#     except ValueError as msg:

#         print("입력이 잘못되었습니다.")

#         print(msg)

#     except ZeroDivisionError as msg:

#         print("0으로 나눌 수 없습니다.")

#         print(msg)

#     finally:

#         print("어쨌든 프로그램은 종료합니다.")

# main()

 

 

 

# #모든 예외 무시

# def main():

#     bread = 10

#     try :

#         people = int(input("몇 명?"))

#         print("1인당 빵의 수 :", bread / people)

#         print("맛있게 드세요.")

 

#     except :

#         print("뭔지는 몰라도 예외가 발생했군요.")

   

# main()
