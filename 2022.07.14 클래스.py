"""
fa_age = 20

def up_fa_age():

    global fa_age

    fa_age +=1

def get_fa_age():

    return fa_age

 

def main():

    print("2022년...")

    print("아빠 :", get_fa_age())

    print("2023년...")

    up_fa_age()

    print("아빠 :", get_fa_age())

 

main()





class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    fa.age = 20
    print("현재 아빠 나이...")
    print("아빠:",fa.get_age())
    print("1년 뒤...")
    fa.up_age()
    print("아빠:",fa.get_age())
"""