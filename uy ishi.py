







#            1




def royhat_info(ismi, famila, t_yili, t_joyi, e_mail=None, t_raqami=None):
    royhat = {'ismi': ismi,
            'famila': famila,
            't_yili': t_yili,
            't_joyi': t_joyi,
            'e_mail': e_mail,
            't_raqam': t_raqami}
    return royhat


print("royhattan oting")
rohatlar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting")
    ismi = input("ismmingizni kiriting")
    famila = input("familangizni kiriting")
    t_yili = input("tugilgan yilingizni kiriting")
    t_joyi = input("tugilgan joyingizni kiriting")
    e_mail = input("emailingizni kiriting")
    t_raqam = input("telefon raqamingizni kiriting")

    rohatlar.append(royhat_info(ismi, famila, t_yili, t_joyi, e_mail, t_raqam))



    javob = input("Yana royhat qoshishni isaysizmi? yes/no")
    if javob == 'no':
        break



print(rohatlar)

          # 2
mijozlar = []  # Mijozlar ro'yxatini yaratamiz

while True:
    ismi = input("Mijozning ismini kiriting (to'xtatish uchun 'exit' deb yozing): ")
    if ismi.lower() == 'exit':
        break  # Agar foydalanuvchi 'exit' yozsa, siklni to'xtatamiz
    yoshi = input("Mijozning yoshini kiriting: ")

    mijozlar.append({'ismi': ismi, 'yoshi': yoshi})  # Mijoz ma'lumotlarini ro'yxatga qo'shamiz

# Mijozlar ro'yxatini konsolga chiqaramiz
print("\nMijozlar ro'yxati:")
for mijoz in mijozlar:
    print(f"Ismi: {mijoz['ismi']}, Yoshi: {mijoz['yoshi']}")


        # 3
def eng_katta_son(a, b, c):
    return max(a, b, c)  # Uchta son ichidan eng kattasini qaytaradi

# Funksiyani chaqirish misoli
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))

kattasi = eng_katta_son(son1, son2, son3)
print(f"Eng katta son: {kattasi}")


#         4


def aylana_hisobla(radius):
    diameter = 2 * radius
    perimeter = 2 * 3.14159 * radius  # Pi ning taxminiy qiymati
    area = 3.14159 * radius ** 2

    return {
        'radius': radius,
        'diameter': diameter,
        'perimeter': perimeter,
        'area': area
    }


# Foydalanuvchidan radiusni kiritishni so'raymiz
radius = float(input("Aylaning radiusini kiriting: "))

# Funksiyani chaqiramiz
natija = aylana_hisobla(radius)

# Natijani konsolga chiqaramiz
print("Aylaning ma'lumotlari:")
print(f"Radius: {natija['radius']}")
print(f"Diametr: {natija['diameter']}")
print(f"Perimetri: {natija['perimeter']}")
print(f"Yuzi: {natija['area']}")
