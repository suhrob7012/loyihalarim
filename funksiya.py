
# import random
# print("\n\nAssolomu alaykum \nBu komputer bilan qaechi, qohoz, quduq oeni")
# print("Oyinni boshlash uchun bittasini tanlang:\n")
# tanlov = ['qaychi', 'quduq', 'qohoz']
# k = 0
# f = 0
# d = 0
# for i in range(5):
#     komp = random.choice(tanlov)
#     men = input(f"Tanlov qiling: {tanlov}\n>>> ")
#     if komp == "quduq" and men == "qaychi" or komp == "qpohoz" and men == "quduq" or men == "qaychi" and men == "qohoz":
#         print("Komputer yutdi")
#         k += 1
#     elif komp == men:
#         print("DURRANG")
#         d += 1 
#     else:
#         print("Siz uytdingiz")
#         f += 1
#     print(f"(komputer) {komp}:{men} (Oenchi)\n ")
# print(f"Hisoblar: (komputer){k}:{f} (Oenchi)\nDuranglar soni {d}")


# print("***🏨ASSOLOMU ALAYKUM MEHMONXONA DASTURIGA XUSH KELIBSIZ🏨***")
# def menu():
#     oyin = True
#     while True:
#         if oyin:
#             print("\n\tdastur ishga tushish uchun korsatilgan ammalrdan birini tanlang")
#             tanlov = int(input("""\n\t\tMehmonxonani menusi kerakli menuni tanlang:
#             1.Hona bron qilish,
#             2.Mehmonxona haqida malumot olish,
#             3.Admin kabinetiga kirish,
#             4.Dasturni toxtatish,
#             kriting>>>"""))
#         else:
#             tanlov = input("Xato 1 va 4 sonlarni ichidagi sonlarni kiriting. ")
#             continue

#         for j in range(1):
       
#             if tanlov == 1:
#                 print("Siz xona bron qilish tanladingiz ")
#                 tanlov = int(input("""
#                 Xonalardan birini tanlang,
#                 1.Luks xona,
#                 2.Standart xona,
#                 3.Ortga
#                 kiriting>>> """))