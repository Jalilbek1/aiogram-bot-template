# def summa(*sonlar):
#     """jwhigfiuoa"""
#     yigindi = 1
#     for son in sonlar:
#         yigindi *=son
#     return yigindi
#
# print(summa(1,2,))
# print(summa(1,2,5,4,7,8,9))

#
#
# def kvadratlar(a, b, c, *sonlar):
#     kvadratlar_royhati = [a**2, b**2, c**2]  # Majburiy parametrlar kvadratlari
#     for son in sonlar:
#         kvadratlar_royhati.append(son**2)  # Qo'shimcha sonlarning kvadratlari
#     return kvadratlar_royhati
#
# # Misol uchun chaqirish
# natija = kvadratlar(2, 3, 4, 5, 6, 7)
# print(natija)
#




# def talabalar_malumotlari(isim, familiya, **malumotlar):
#     talabalar_lugati = {
#         'isim': isim,
#         'familiya': familiya,
#     }
#     talabalar_lugati.update(malumotlar)  # Ixtiyoriy malumotlarni qoshish
#     return talabalar_lugati
#
# # Misol uchun chaqirish
# talaba = talabalar_malumotlari('Ali', 'Valiyev', yosh=20, fakultet='Matematika', )
# print(talaba)










