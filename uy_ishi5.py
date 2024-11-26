class Bank:

    def __init__(self,ism,passport,id_raqam):
        self.ism = ism
        self.passport = passport
        self.id_raqam = id_raqam

    def get_info(self):
        info = f"{self.ism}  id: {self.id_raqam}"
        info += f" passport:{self.passport}"
        return info





inson =Bank("jalilbek","1253", "8600")
print(f"{inson.get_info()} " )

class Manzil(Bank):
    def __init__(self,ism,passport,id_raqam,manzil):
        super().__init__(ism, id_raqam, passport, )
        self.manzil = manzil

    def get_man(self):
        return f"Shu yerda turadi {self.manzil}"



manzil1 =Manzil("jalilbek","5454", "8600","xorazm")
print(f"{manzil1.get_man()} ")