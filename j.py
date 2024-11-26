# def summa(*sonlar):
#     """jwhigfiuoa"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi +=son
#     return yigindi
#
# print(summa(1,2,))
# print(summa(1,2,5,4,7,8,9))
import fusiya
# def summa(*sonlar):
#
#     return sum(sonlar)
#
# print(summa(1, 2))
# print(summa(1, 2, 5, 4, 7, 8, 9))





# def summa(x,y,*sonlar):
#     """hgsfiuhjas"""
#
#     return x+y+sum(sonlar)
#
#
# print(summa(1, 2, 5, 4, 7, 8, 9))





# def avto_info(kompaniya,model,**malumot):
#     """houdfsjh"""
#
#     malumot["kompaniya"] = kompaniya
#     malumot["model"] = model
#     return malumot
#
#
#
# avto1 = avto_info("gm","malibu", rang="qora", yil=2024)
# avto2 = avto_info("kia","k5", rang="qora", yil=2024)
#
# print(avto1)
# print(avto2)











# import fusiya
#
# avto2 = fusiya.avto_info("gm","malibu", "qora","avto", 2000 )
#




#
# from fusiya import avto_info
# avto3 = avto_info("gm","malibu", "qora","avto" ,2000 )
#







# from fusiya import *
# avto4 = avto_info("gm","malibu", "qora","avto",2000  )



# kompaniya, model, rangi, korobka, yili, narhi=None

from fusiya import avto_info as ak,info_print as ip
avto5 = ak("gm","malibu", "qora","avto",2020)
ip(avto5)





#
# import fusiya as fm
# avto1 = fm.avto_info("gm","malibu", "qora","avto" ,2000 )
# fm.info_print(avto1)
#








