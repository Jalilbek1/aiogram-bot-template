class Avto:
    def __init__(self,model,rang,narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.km = 3

    def get_info(self):
        return f"modeli-{self.model} rangi-{self.rang} narh-{self.narh} {self.km} - km yurgan"
    # def set_km(self.km):
    #     self.km = km
    def update_km(self):
        self.km += 1

avto1 = Avto('nexia 2','oq','10000$')
print(avto1.get_info())


avto1.update_km()
print(avto1.get_info())

avto1.update_km()
print(avto1.get_info())


class Avtosalon:
    def __init__(self,salon_nomi,manzili,s_avtomobillar):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.s_avtomobilllar = s_avtomobillar




class Avto:
    def __init__(self, model, rang, narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.km = 8

    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Narh: {self.narh}, {self.km} km yurgan"

    def set_km(self, km):

        if km >= self.km:
            self.km = km
        else:
            print("Yangi kilometraj eski kilometrajdan katta bo'lishi kerak.")

    def update_km(self):

        self.km += 1


