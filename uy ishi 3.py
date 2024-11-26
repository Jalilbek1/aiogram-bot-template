
class user:
    """talaba"""
    def __init__(self,ism,famila,e_mail):

        """talabalar"""
        self.ism = ism
        self.famila = famila
        self.e_mail = e_mail
    def get_name(self):
        """dfgkieuiyfdk"""
        return self.ism

    def get_lastname(self):
        return self.famila

    def fullnema(self):
        """rfweuhf"""
        return f"{self.ism} {self.famila}"






    def hamma(self):
        print(f"ismin {self.ism} famila {self.famila} email:{self.e_mail} ")


user11 = user("jalilbek","azadov", "jack.com12j@gmail.com")
print(user11.ism)
print(user11.famila)





print(user11.hamma())
print(user11.get_name())
print(user11.get_lastname())
print(user11.fullnema())