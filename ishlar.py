




# avtolar = ["audi", "bmw", "volvo", "kia"]
# for avto in avtolar:
#     if avto == 'avto':
#         print(avto.upper())
#     else:
#         print(avto.title())




# ism = input('isminkigzni kiriting\n ')
# if ism.lower() != 'ali':
#     print(f"uzr {ism.title()} biz alini kuyyabmiz")
# else:
#     print("salom Ali")





# son = float(input("12*6 nachaga teng" ))
# if son != 72:
#     print("javob xato")
#

# yosh = int(input("yoshngizni kiriting"))
# if yosh>=18:
#     print('xush kelibsiz')
# else:
#     print('kirish munkin emas')
#
#
# login = input('login kiriting')
# if len(login)<=5:
#     print('siz 5 harfdan kam son kiritingiz')
# else :
#     print('login qabul qilindi')

# yil = int(input('yilingizni kiriting'))
# if 2024-yil<18:
#     print(f"yoshingiz {2024-yil}da ekan")
#     print("kirish munkim emas")
# else:
#     print('hush lelibsiz')
#
#
# yosh = int(input("yoshingiz nechida"))
# if yosh>65: print('siv bergegie')
#
# x,y = 25,50
# print("x>y") if x>y else print("x<y")

# yosh = int(input('yoshinizni kiritin'))
# if yosh <=4:
#     prise = 0
# elif yosh <= 12:
#     prise = 5_000
# elif yosh<65:
#     prise = 10_000
# elif yosh>65:
#     prise = 8000
#
# print(f"siga kirish {prise} so`m")


# kun = input('bugun nima kun')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("bugun dab olish kuni")
# else:
#     print('ish kuni')

# kun = input("bugun nima kun")
# harorat = float(input("havoni horati necha"))
# if kun.lower()=='yakshanba' and harorat>= 30:
#     print("chomilshag ketik")
# elif kun.lower()=='yakshanba' and harorat< 30:
#     print('dam olamiz')
#
#
# narh = 15000
# choy = True
# salat = False
#
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
#
# print(f"jami {narh} som")
#
#
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
#
# if choy:
#     print("mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("mijoz assorti oldi.")
#     narh = narh + 15000
#
#
# print(f"jami { narh} som")
#
#
# menu = ['osh', 'shashlik', 'norin', 'somsa']
# if 'osh' in menu:
#     print('True')
# else:
#     print("False")
#
#
#
# menu = ['osh', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat zakaz qilasiz?')
# if ovqat.lower() not in menu:
#     print("Afsuski bunday taom bizda yo\'q")
# else:
#
#     print('Buyurtma qabul qilindi')
#
#
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'manti', 'shashlik']
#
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#          if taom in menu:
#             print(f"Menuda {taom} bor")
#          else:
#             print(f"Kechirasiz menuda {taom} yo'q")
# else:
#     print("savatcha bosh")
#
#
#
#
# car_0 ={
#     'model': ' feari',
#     'rang': 'qizil',
#     'yil': 2020
#
# }
#
# print(car_0)
#
# talabe_0 = {'ism' : 'murod olimoz',
#             'yosh':20,
#             't_yili': 2000
#             }
# print(f"{talabe_0['ism'].title()},\
# {talabe_0['t_yili']}-yilda tugilgan,\
# {talabe_0['yosh']}-yoshda")
#
# talabe_0 = {'ism' : 'murod olimoz',
#             'yosh':20,
#             't_yili': 2000
#             }
# talabe_0['kurs']= 4
# talabe_0['fokultet'] = 'informatika'
# print(talabe_0)
#
#
# talaba_1 = {}
#
#
# talaba_1['ism'] = 'qobul azadov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
#
# talaba_1['kurs'] = 4
# print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#
# talaba_0 = {'ism':'jalilbek' , 'yosh':'20', 't_yil': 2001}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)
#
#
# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia'
#
#
# }
# print(telefon)
#
# phone= telefon['ali']
# print(f"alida {phone} bor ")
#
# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia'
# }
# print(telefon)
# phone= telefon.get('ali' , 'bumday kry mavjud emas')
# print(phone)


#
# print("salom")
#
# print('salom')
#
# print('men  "lenova" sotib oldim')
#
#
#
#
# print("""odami
# ersang  """)
#
# print(''' odam salom
# nima'''),
#
# print(" salom nima \n nima gap ")
#
#
#
#
# print(2+4*2)
# print(20/5)
# print(25//2)
# print(2**4)
# print(15%2)
#
#
# # qoqizning kvadirati
# print("qoqizning kvadirati", 9**2, "ga teng")
#
#
# # bu uchininig kvadirati
# print('3*3=' , 3*3 )

# # ozgaruvchi
#
# ism = "jalilbek"
# yosh = 14
#
# print(ism)
# print(yosh)
#
#
# ism = "temurbek"
# print(ism)
# ism = "bobur"
# print(ism)








# ozgaruvchilar nomi
#
# ism_jamila = "jalilbek azadov"
# print(ism_jamila)
#
# a = 5
# A = 11
# print(a)
# print(A)
#
# ism_sharf = "jalilbek azadov"
# ismsharf = "jalilbek azadov"
# # paccal case
# IsmSharf = "jalilbek azadov"
# # camel case
# ismSharf = "jalilbek azadov"
#
#
#
# print(ism_sharf)
# print(ismsharf)
# print(IsmSharf)
# print(ismSharf)
#
#
#
# print("salom" )
# print('salom "uzbekiston"')
#
# print("g'anisher")
# print('o\'tkirbekцфв')








# shahar = "urganch"
# viloyat = 'xorazm'
#
# print( shahar)
# print(viloyat)
#
# matn = "men yangi 👌 "
# print(matn)

#
# ism = 'jalilbek'
# print('ismim ' + ism)
#
# ism = 'jalilbek '
# famila = 'azadov'
# print(ism + famila)



# ism = 'jalilbek '
# famila = 'azadov'
# ism_sharf = f" ismmim:{ism} famila:{famila} {88+8}"# print(ism_sharf)

# print( "salom niam")
# print( "salom \tniam")
# print( "salom \nniam")

# ism = 'jalilbek '
# famila = 'azadov'
# ism_sharf = f"{ism} {famila} "
# print("1",ism_sharf.upper())
# print("2",ism_sharf.lower())
# print("3",ism_sharf.title())
# print("4",ism_sharf.capitalize())


# meva = "     olma    "
# print("menda",meva.lstrip(),"yaxshi koraman")
# print("menda",meva.rstrip(),"yaxshi koraman")
# print("menda",meva.strip(),"yaxshi koraman")
# print("menda",meva,"yaxshi koraman")





# ism = input( "ismingizni kiriting")
# famila = input( "famila" )
# print("assalom aleykum", ism , famila)

#
# a = 20
# b = -30
# c = a + b
# print(c)
#
#
# a = 20
# yuzi = a**2

# print(yuzi)
#
# a = -20
# b = 40
# c = b/a
# print(b)
#
#
# aholi_soni = 7_584_000_000
# print("yerda",aholi_soni,"odam yashaydi")
#
# PI = 3.141559
# raduis = 21.2
#
# print(PI , raduis)
#
# x, y, z, w, = 10, -7.25, -30, 5
# print(x,y,z,w)
#
# a = 10
# print(type(a))
# b = "jalilbek"
# print(type(b))
#





# a = 15
# a = float(a)
# print(a)
#
# b = "245"
# b = int(b)
# print(b)
#
# c = 233
# c = str(c)
# print(c)
#
#
# yil = int(input("yilingizni kiriting"))
# yosh = 2024 - yil
#
# print("siz", yosh, "yosh dasiz" )
#
# kocha = "bog`bon"
# mahhala = "sog`bon"
# tuman = "bodomzor"
# viloyat = "Samarqand"
#
# print(kocha,"kochasi,",mahhala,"mahallasi,",tuman,"yumani,",viloyat,"viloyati")
#
#
# kocha = input("kochangizni kiriting")
# mahhala = input("mahalangizni kiriting")
# tuman =input("tumanningizni kiriting")
# viloyat = input("viloyatingizni kiriting")
#
# print(kocha,"kochasi,",mahhala,"mahallasi,",tuman,"yumani,",viloyat,"viloyati")
#
# son = int(input("bita son kiriting"))
# kvadrat =  son**2
# kub = son**3
# print("siz kiritgan sonning kvadirati",kvadrat,"siz kiritgan sonning kubi",kub)
#
# yil = int(input("yilingizni kiriting"))
# yosh = 2024 - yil
#
# print("siz", yosh, "yosh dasiz" )
#
#
#
#
# b_son = int(input("birinch sonni kiriting"))
# i_son = int(input("ikkinchi sonni kiriting"))
# yigindi = b_son + i_son
# ayirma = b_son - i_son
# kopayma = b_son * i_son
# bolinma = b_son / i_son
# print(yigindi ,ayirma,kopayma,bolinma)




# mevalar = ['olam ', 'shaftoli', 'orik', ' anjir']
# narihlar = [12000 , 18000, 10900, 22000]
# sonlar = ['bir' , 'ikki', 3, 4]
# ismlar = []
#
#
#
#
# print(mevalar)
# print(narihlar)
# print(sonlar)
# print(ismlar)
# mevalar = ['olam ', 'shaftoli', 'orik', ' anjir']
# print("birinchi meva", mevalar[0].title())
# print("ikkinchi meva", mevalar[1].upper())


# narihlar = [12000 , 18000, 10900, 22000]
# print(narihlar[2] + narihlar[3])





# narihlar = [12000 , 18000, 10900, 22000]
#
# narihlar[0] = 13000
# narihlar[2] = 11000
# narihlar[3] = narihlar[3] + 2000
#
# print(narihlar)
#
# mevalar = ['olam ', 'shaftoli', 'orik', ' anjir']
# mevalar.append("tarvuz")
# print(mevalar)
#
#
# cars = []
# cars.append("lacetti")
# cars.append("nexia 3 ")
# cars.append("coblt")
#
# print(cars)
#
# cars = ['lacetti', 'nexia 3', 'coblt' ]
# cars.insert(0, 'malubu')
# cars.insert(2, 'damas')
# print(cars)


# mevalar = ['olam ', 'shaftoli', 'orik', ' anjir']
# del mevalar[0]
# print(mevalar)
#
# mevalar = ['olam ', 'shaftoli', 'orik', ' anjir']
# mevalar.remove('shaftoli')
# print(mevalar)

# hayvonlar = ['it', 'mushuk' , 'sigir', 'quyon']
# hayvonlar.remove("mushuk")
# print(hayvonlar)

# bozorlik = ["yog`" ,"un" , "piyoz", "banan","gosht"]
# mahsulot =bozorlik.pop(3)
# print("men", mahsulot,"sotib oldim" )
# print("olinmagan mahsulotlar", bozorlik )









# cars = ["bmw","mers","audi","tesla"]
# cars.sort()
# print(cars)

# mehmonlar = [ "jonibek", "jalilbek  ", " temur", "bekzod", "o`tkir"]
# print("sorted() qatargan royhat", sorted(mehmonlar))
# print("asl  royhat" ,mehmonlar)


# ages = [12,98,56,45,10,45,63]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ["suv","limon","banan","olma",]
# fruits.reverse()
# print(fruits)
#


# fruits = ["suv","limon","banan","olma",]
#
# print("elementlar soni", len(fruits))

# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
#
#
# print("juft sonlar",juft_sonlar)
# print("toq sonlar",toq_sonlar)

# narhlar = [12000,13000,15000,48000,56000,8600]
#
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
#
# print("eng arzon", arzon,"en qimmat", qimmat,"jami",jami)




# cars = ["bmw","mers","audi","tesla", "volvo"]
# my_cars = cars[0:3]
# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])
#
#
# sonlar = [1,2,3,4,5]
# sonlar2 = sonlar
# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar)
# print(sonlar2)




# toys = ("bmw","mers","audi","tesla", "volvo")
# toys = list(toys)
# toys.append("olma")
# toys = tuple(toys)
# print(toys)




# ismlar2 = ["jalilbek", "donyor", "behruz" , "nurhon"]
# for mehmon in ismlar2:
#     print(f"hurmatli {mehmon}, sizni oshga talif qilimaz")
#      print("hurmat bilan")





# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son}, ning kvadirati,{son**2}")


# sonlar = list(range(1100))
# sonlar_kvadirati = [ ]
# for son in sonlar:
#     sonlar_kvadirati.append(son**2)
#
# print(sonlar)
# print(sonlar_kvadirati)


# dostlar = []
# print("5ta dostingizni kiriting")
# for n in range(5):
#     dostlar.append(input(f"{n+1}- dostingizni kiriring "))
#
# print(dostlar)








#
# ismlar2 = ["jalilbek", "donyor", "behruz" , "nurhon" , "temur"]
# for mehmon in ismlar2:
#     print(f"salom  {mehmon}")
#
#
#
#
# toq_sonlar = list(range(11,100,2))
# for n in toq_sonlar:
#     print(f"{n} - kubi ={n**3}")
#
#
#
# kinolar = []
# print("5ta eng sevimli kinoyingizni kiriting ")
# for n in range(5):
#     kinolar.append(input(f"{n+1}- kino kiriting "))
#
# print(kinolar)



























# avtolar = ["audi", "bmw", "volvo", "kia"]
# for avto in avtolar:
#     if avto == 'avto':
#         print(avto.upper())
#     else:
#         print(avto.title())




# ism = input('isminkigzni kiriting\n ')
# if ism.lower() != 'ali':
#     print(f"uzr {ism.title()} biz alini kuyyabmiz")
# else:
#     print("salom Ali")





# son = float(input("12*6 nachaga teng" ))
# if son != 72:
#     print("javob xato")
#

# yosh = int(input("yoshngizni kiriting"))
# if yosh>=18:
#     print('xush kelibsiz')
# else:
#     print('kirish munkin emas')
#
#
# login = input('login kiriting')
# if len(login)<=5:
#     print('siz 5 harfdan kam son kiritingiz')
# else :
#     print('login qabul qilindi')




# yil = int(input('yilingizni kiriting'))
# if 2024-yil<18:
#     print(f"yoshingiz {2024-yil}da ekan")
#     print("kirish munkim emas")
# else:
#     print('hush lelibsiz')
#
#
# yosh = int(input("yoshingiz nechida"))
# if yosh>65: print('siv bergegie')
#
# x,y = 25,50
# print("x>y") if x>y else print("x<y")




# yosh = int(input('yoshinizni kiritin'))
# if yosh <=4:
#     prise = 0
# elif yosh <= 12:
#     prise = 5_000
# elif yosh<65:
#     prise = 10_000
# elif yosh>65:
#     prise = 8000
#
# print(f"siga kirish {prise} so`m")


# kun = input('bugun nima kun')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("bugun dab olish kuni")
# else:
#     print('ish kuni')
#
# kun = input("bugun nima kun")
# harorat = float(input("havoni horati necha"))
# if kun.lower()=='yakshanba' and harorat>= 30:
#     print("chomilshag ketik")
# elif kun.lower()=='yakshanba' and harorat< 30:
#     print('dam olamiz')
#



# narh = 15000
# choy = True
# salat = False
#
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
#
# print(f"jami {narh} som")
#
#
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
#
# if choy:
#     print("mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("mijoz assorti oldi.")
#     narh = narh + 15000
#
#
# print(f"jami { narh} som")
#
#
# menu = ['osh', 'shashlik', 'norin', 'somsa']
# if 'osh' in menu:
#     print('True')
# else:
#     print("False")
#
#
#
# menu = ['osh', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat zakaz qilasiz?')
# if ovqat.lower() not in menu:
#     print("Afsuski bunday taom bizda yo\'q")
# else:
#
#     print('Buyurtma qabul qilindi')
#
#
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'manti', 'shashlik']
#
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#          if taom in menu:
#             print(f"Menuda {taom} bor")
#          else:
#             print(f"Kechirasiz menuda {taom} yo'q")
# else:
#     print("savatcha bosh")
#
#
#
#
# car_0 ={
#     'model': ' feari',
#     'rang': 'qizil',
#     'yil': 2020
#
# }
#
# print(car_0)
#
# talabe_0 = {'ism' : 'murod olimoz',
#             'yosh':20,
#             't_yili': 2000
#             }
# print(f"{talabe_0['ism'].title()},\
# {talabe_0['t_yili']}-yilda tugilgan,\
# {talabe_0['yosh']}-yoshda")
#
# talabe_0 = {'ism' : 'murod olimoz',
#             'yosh':20,
#             't_yili': 2000
#             }
# talabe_0['kurs']= 4
# talabe_0['fokultet'] = 'informatika'
# print(talabe_0)
#
#
# talaba_1 = {}
#
#
# talaba_1['ism'] = 'qobul azadov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
#
# talaba_1['kurs'] = 4
# print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#
# talaba_0 = {'ism':'jalilbek' , 'yosh':'20', 't_yil': 2001}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)
#
#
# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia'
#
#
# }
# print(telefon)
#
# phone= telefon['ali']
# print(f"alida {phone} bor ")
#
# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia'
# }
# print(telefon)
# phone= telefon.get('ali' , 'bumday kry mavjud emas')
# print(phone)





# ismlar = ["Ulliboy ", "Bobur", "Abdirim"]
# print(ismlar)
# #
#
# sonlar = [12,98,56,45,10,45,63 , -12.3 ]
# arzon = min(sonlar)
# qimmat = max(sonlar)
# jami = sum(sonlar)
# sonlar[0] = 13000
# sonlar[2] = 11000
# sonlar[3] = sonlar[3] + 2
# sonlar[4] = sonlar[4] - 5
# sonlar[6] = sonlar[6] * 5
# sonlar[7] = sonlar[7] / 5
# print(sonlar)
# print(arzon)
# print(qimmat)
# print(jami)
#
#
# t_shaxslar = ["amir temur","beruniy ","alisher navoiy","jololiddin"]
# ismlar = t_shaxslar.pop(2)
# print(ismlar)
# print(t_shaxslar)
#
# z_shaxslar = ["Komiljon Murodov","Viktor Khamraev","Dilshodbek Alimov","Abdulaziz Kamilov"]
# z_ismlar = z_shaxslar.pop(2)
# print(z_ismlar)
# print(z_shaxslar)
#
#
#
# mehmonlar = []
# mehmonlar.append("Bobur")
# mehmonlar.append("Ulliboy")
# mehmonlar.append("abdirim")
# mehmonlar.append("alisher")
# mehmonlar.append("jasur")
#
#
# mehmonlar.remove("jasur")
# mehmonlar.remove("alisher")
#
# print(mehmonlar)
#
#
# ismlar2 = ["jalilbek", "donyor", "behruz" , "nurhon"]
# ismlar2.insert(0, 'uliboy')
# ismlar2.insert(4, 'bobur')
# ismlar2.insert(7, 'jasur')
# print(ismlar2)


# sevimli_taom = {
#     'ali': ' osh',
#     'temur':'shashlik',
#     'bobur':'manti',
#     'jalilbek':'somsa'
# }
# print(sevimli_taom)
# ali= sevimli_taom.get('ali' , 'bumday  mavjud emas')
# temur= sevimli_taom.get('temur' , 'bumday  mavjud emas')
# bobur= sevimli_taom.get('bobur' , 'bumday  mavjud emas')
# print(ali)
# print(ali)
# print(ali)


#
#
# sevimli_taom = {
#     'ali': ' osh',
#     'temur':'shashlik',
#     'bobur':'manti',
#     'jalilbek':'somsa'
# }
# print(sevimli_taom)
# ali= sevimli_taom.get('ali' , 'bumday  mavjud emas')
# temur= sevimli_taom.get('temur' , 'bumday  mavjud emas')
# bobur= sevimli_taom.get('bobur' , 'bumday  mavjud emas')
# print(ali)
# print(ali)
# print(ali)
#











# talabe_0 = {
#     'ism': ' Jalilbek',
#     'famila':'azadov',
#     'yoshi':20,
#     'facultet':'kompuyuter',
#     'kurs':2
# }
# print(talabe_0.items())


# talaba_0 = {
#     'ism': ' Jalilbek',
#     'famila':'azadov',
#     'yoshi':20,
#     'facultet':'kompuyuter',
#     'kurs':2
# }
#
# for kalit,qiymat in talaba_0.items():
#     print(f"kalit:{kalit}")
#     print(f"qiymat:{qiymat}")








# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia'
# }
# print('oiuthge')
# for m in telefon.keys():
#     print(m.title())



# telefon = {
#     'ali': 1000,
#     'yemur':3000,
#     'olim':5000,
#     'orif':8000
# }
#
# bozorlik = ['ali','temur','olim']
# for mah in telefon:
#     if mah in bozorlik:
#         print(f"{mah.title()} {telefon[mah]} som")



# telefon = {
#     'ali': 1000,
#     'yemur':3000,
#     'olim':5000,
#     'orif':8000
# }
#
# print("sfgusiegjpw")
# for m in sorted(telefon):
#     print(m.title())




# telefon = {
#     'ali': ' iphone',
#     'yemur':'samsung',
#     'olim':'mi 10 pro',
#     'orif':'nikia',
#     'amir':'nikia'
# }
#
# for tel in set(telefon.values()):
#     print(tel)




# ism0 = {
# 'ism': 'Abu ali inin sinona',
# 'yil': 810,
#  'shahar': 'buxoro',
#  'umir': 60,
#
# }
#
# ism1 = {
# 'ism': 'abdla qodiriy',
# 'yil': 1894,
#  'shahar': 'toshkent',
#  'umir': 44,
#
# }
# ism2 = {
# 'ism': 'alisher',
# 'yil': 1441,
#  'shahar': 'xirotda',
#  'umir': 60,
# }
# cars =[ism0,ism1,ism2]
# for car in cars:
#  print(f"{car['ism'].title()},"
#  f"{car['yil'] }-yilda tugilgan, "
#  f"{car['shahar']}-tugilgan, {car['umir'] }-umir korgan"
#  )



# print("kiriting sonni sgnjk")
# savol = 'istalgan san kiriting'
# savol += 'dasturn tds'
# qiymat = ''
# while qiymat != 'exit':
#  qiymat = input(savol)
#  if qiymat != 'exit':
#   print(float(qiymat)**2)










# sonlar = list(range(1,100000))
# for son in sonlar:
#  if son ==5:
#   break
#  print(f"{son } ning kvadiarat {son**2} ga tre")


# ismlar = []
# print('isminmk joiuh rog')
# n=1
# while True:
#  savol = f"{n} -dosting gizni ismi"
#  ism = input(savol)
#  ismlar.append(ism)
#  javob = input("yana ism qosiiz" )
#  if javob == 'ha':
#   n+=1
#   continue
#  else:
#   break
#
# print("dostlar")
# for ism in ismlar:
#  print(ism.title())


# print('dostingizni yoshni kiriting')
# dostlar = {}
# ishora = True
# while ishora:
#  ism = input('dostingizni ismini kiriting')
#  yosh = input(f"{ism.title()}ning yoshini kiriting")
#  dostlar[ism] = int(yosh)
#
#  javob = input("yana ism qosiiz" )
#  if javob == 'no':
#   ishora = False
#
# for ism,yosh in dostlar.items():
#  print(f"{ism.title()} {yosh} da")

# toys = ["bmw","mers","audi","tesla","tesla", "volvo"]
# while 'tesla' in toys:
#     toys.remove('tesla')
# print(toys)


# talabalar =[ 'jalilbe' , 'husan', 'olim']
# baholangan_ta={}
# while talabalar:
#     talaba =talabalar.pop()
#     baho = input(f"{talaba.title()}nning boaosi kiriting")
#     print(f"{talaba.title()}bahonaldi")
#     baholangan_ta[talaba] = baho
#
# print(baholangan_ta)


# savol = "Sevgan kitobingizni kiriting"
#
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')


#




# def salom_b():
#     print("asalamu alekum")
#
# salom_b()

# def salom_b(ism):
#     print(f"asalamu alekum {ism.title()}")
#
# salom_b('hasan')


# def salom_b(ism):
#     """salomglyglyfutdi"""
#     print(f"asalamu alekum {ism.title()}")
#
#
# salom_b('hasan')
# salom_b('jonimek')
# print(salom_b.__doc__)


# def salom_b(ism , famila):
#     """salomglyglyfutdi"""
#     print(f"fodalanuvchi ism {ism.title()}\n"
#           f"fodalanuvchi famila {famila.title()}")
# salom_b("jalilbek", "azadov")

# def yosh(t_yil,j_y=2024):
#     print(f"siz {j_y-t_yil} yosh")
# yosh(2005)





# def toliq_ism_yasa(ism , famila):
#     toliq_ism = f"{ism} {famila}"
#     return toliq_ism
# print(toliq_ism_yasa('jalilbek', 'azadov'))


# def toliq_ism_yasa(ism , famila):
#     toliq_ism = f"{ism} {famila}"
#     return toliq_ism
#
# talaba1 = toliq_ism_yasa('jalilbek', 'azadov')
# talaba2 = toliq_ism_yasa('jalilbek', 'azadov')
# print(talaba1)
# print(talaba2)


# def toliq_ism_yasa(ism , famila, otasini_ism=''):
#     if otasini_ism:
#         toliq_ism = f"{ism} {otasini_ism} {famila}"
#     else:
#         toliq_ism = f"{ism}  {famila}"
#     return toliq_ism
#
#
#
#
#
#
# talaba1 = toliq_ism_yasa('jalilbek', 'azadov')
# talaba2 = toliq_ism_yasa('jalilbek', 'azadov' ,'jumazarivicj')
# print(f"{talaba1} \n{talaba2}")










#
#
#
# def avto_info(kompaniya, model,rang,korobka,yili,narhi=None):
#     avto ={
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rang,
#         'korobka':korobka,
#         'yili':yili,
#         'narh':narhi
#
#     }
#     return avto
#
#
# avto1 = avto_info('gm','malibu','qora','avtomat','2019')
# avto2 = avto_info('gm','gntira','oq','mehanika','2020','15000')
# avtolar = [avto1,avto2]
# print('onlayn bozorda bor')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "namalum"
#     print(f"{avto['rang']} {avto['model']}. narhi: {narh}")
#
#
#
# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
#
# print(oraliq(5,10))
#
#
# def avto_info(kompaniya, model, rang, korobka, yili, narh=None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rang,
#             'korobka': korobka,
#             'yili': yili,
#             'narhi': narh}
#     return avto
#
#
# print("SAytimizdagi avtolar royxatni shakllantiraamz")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi")
#     model = input("Modeli:")
#     rang = input("Rangi:")
#     korobka = input("Korobka:")
#     yili = input("Yili:")
#     narh = input("Narhi:")
#
#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narh))
#
#     javob = input("Yana avto qoshishni isaysizmi? yes/no")
#     if javob == 'no':
#         break
#
# print(avtolar)
#
#
#
#
#
#
#
# def baholar(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism.title()}ning bahosi")
#         baholar[ism]=baho
#     return baholar
#
#
#
# talabalar = ['ali','vali']
# baholar = baholar(talabalar[:])
# print(baholar)
#
#
#
#
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]= matnlar[i].title()
#     return matnlar
#
# ismlar  = ['ali','vali']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)
#
#
# talabalar  = ['ali','vali']
# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"talaba {ism.title()}ning bahosi")
#         baholar[ism]=baho
#     return baholar
#
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)


