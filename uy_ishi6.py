
class Person:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.__yosh = yosh

    def get_name(self):
        return self.ism

    def set_name(self, ism):
        self.ism = ism

    def get_age(self):
        return self.__yosh


    def set_age(self, yosh):
        if yosh > 0:
            self.__yosh = yosh
        else:
            print("Yosh musbat butun son bo'lishi kerak.")


shaxs = Person("Ali", 25)
print(shaxs.get_name())  # Ali
print(shaxs.get_age())   # 25

shaxs.set_name("Vali")
shaxs.set_age(30)
print(shaxs.get_name())  # Vali
print(shaxs.get_age())


class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} mablag' qo'shildi. Joriy balans: {self.__balance}")
        else:
            print("Qo'shiladigan mablag' musbat son bo'lishi kerak.")


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} mablag' yechildi. Joriy balans: {self.__balance}")
        else:
            print("Yetarli mablag' mavjud emas yoki kiritilgan qiymat noto'g'ri.")


    def check_balance(self):
        return self.__balance


hisob = Account(100)
hisob.deposit(50)
hisob.withdraw(30)





