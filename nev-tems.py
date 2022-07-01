# def my_func(ism, familiya, yoshi=25):
# """ Bu func ismini toliq qaytaradi """
# full_name = f"{ism} {familiya} {yoshi}"
# return full_name

# ism1 = my_func(familiya="Mardonov", ism="Ochil,")
# print(ism1)

# def moshinlar(modeli, yili, narxi, rangi):
    # if moshinlar:
        #  moshina = f" {modeli} {yili} {narxi} {rangi} "
    # else:
        # moshina = f" {modeli} {yili} {narxi} "
        # return moshina

# moshina1 = moshinlar("modeli":"KIA", "yili":2022, "Narxi":495000, "Rangi":"KO'K")
# moshina2 = moshinlar("modeli":"TESLA", "Yili":2019, "Narxi":145000)

# print(f"Elektocar emas: {moshina1}")
# print(f"Elektocar:{moshina2}") 


# def malumot(familiyasi, ism, tugilgan_joyi, yashash_joyi, telefon_raqami, yoshi, tugilgan_yili):
#     odam = {
#         'familiyasi':familiyasi,
#         'ism':ism,
#         'tugilgan_joyi':tugilgan_joyi,
#         'yashash_joyi':yashash_joyi,
#         'telefon_raqami':telefon_raqami,
#         'yoshi':yoshi,
#         'tugilgan_yili':tugilgan_yili
#     }
#     return odam

# odam1 = malumot("Dilmurodov", "Joxongir", 'Samarqand', 'Toshkent', 904502112, 31, 1991)
# odam2 = malumot("Alisher", "Murodov", 'Samarqand', 'Toshkent', 304502112, 31, 1991)
# print(odam1)
# print(odam2)

# while True:
#     def malumot(familiyasi, ism, tugilgan_joyi, yashash_joyi, telefon_raqami, yoshi, tugilgan_yili):
#         odam = {
#             'familiyasi':familiyasi,
#             'ism':ism,
#             'tugilgan_joyi':tugilgan_joyi,
#             'yashash_joyi':yashash_joyi,
#             'telefon_raqami':telefon_raqami,
#             'yoshi':yoshi,
#             'tugilgan_yili':tugilgan_yili
#         }
#         return odam
    
#     odam1 = malumot("Dilmurodov", "Joxongir", 'Samarqand', 'Toshkent', 904502112, 31, 1991)
#     odam2 = malumot("Alisher", "Murodov", 'Samarqand', 'Toshkent', 304502112, 31, 1991)
#     print(odam1)
#     print(odam2)
#     break

# def my_func(name):
#     print(f"Assolomu alaykum {name.title()} ")
# print('olim')

# """ REGESTRATION IN PROGRAMS """
# user = [
#     {"username":'test', "id":'82845', "password":'120021'}
# ]
# print("\n\nAssolomu alaykum royxatdan otish bolimiga hush kelibsiz\nMenu'dan kerakli bolimini tanlang: ")

# def main():
#     def login():
#         username = input("Foydalanuvchini nomi: ")
#         username = input("Foydalanuvchini kodi: ")
#         for users in user:
#             if user['username'] == username and users['password'] == password:
#                 print("Tabriklaymiz siz akkauntga kirdingiz! ")
#                 break
#             else:
#                 print("Xato login va parol oylab va qayta kiriting ")
#                 login()
#     def creats():
#         username = input("Yangi login kiriting: ")
#         password = input("Yangi parol kiriting: ")
#         id_raqam = input("Yangi id  kiriting: ")

#         new_user = {"username":username, "id":id_raqam, "password":password}
#         user.append(new_user)
#         print(user)
#         print("Siz royxatdan otdingiz")
#         login()

#     print("1-kirish: ")
#     print("2-royxatdan otish: ")
#     javob = int(input("KIRITING>>>"))
    
#     if javob == 1:
#         login()
#     elif javob == 2:
#         creats()

# main()

# def dasturchi(ism, **dev):
#     dev['ism'] = ism
#     return dev

# moshina1 = dasturchi("Jasur", fam='Sobirov', yoshi=20, sohasi="backend")
# print(moshina1)

# from math import sqrt

# numbers = list(range(1, 111))

# ildiz = list(map(sqrt, numbers))
# print(numbers)
# print(ildiz)

# class Phone:
#     def __init__(self, name, model, rangi, yili):
#         self.name = name
#         self.model = model
#         self.rangi = rangi
#         self.yili = yili
# phone = Phone("samsung", "S-23 ultra", "ko'k", 2022)
# phone2 = Phone("apple", "i[hone-12", "oq", 2021)
# print("-=-BIRINCHI TELEFON📱-=-")
# print("ismi",phone.name)
# print("modeli",phone.model)
# print("rangi",phone.rangi)
# print("yili",phone.yili)
# print("-=-IKINCHI TELEFON📱-=-")
# print("ismi",phone2.name)
# print("modeli",phone2.model)
# print("rangi",phone2.rangi)
# print("yili",phone2.yili)

# class Dasturchi:
#     def __init__(self, ismi, familiyasi, yoshi, fakulteti):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.yoshi = yoshi
#         self.fakulteti = fakulteti

#     def get_ismi(self):
#         return self.ismi

#     def get_familiyasi(self):
#         return self.familiyasi

#     def get_yoshi(self):
#         return self.yoshi

#     def get_fakulteti(self):
#         return self.fakulteti

#     def new_info(self):
#         print(f"Dasturchini ismi: {self.ismi} familiyasi {self.familiyasi} yoshi {self.yoshi} va fakulteti {self.fakulteti}")

# Birinchi_dasturchi = Dasturchi("Suhrob", "Ergashev", 15, "IT")
# print("Ismi", Birinchi_dasturchi.get_ismi(),"familiyasi", Birinchi_dasturchi.get_familiyasi(),"yoshi", Birinchi_dasturchi.get_yoshi(), "fakulteti", Birinchi_dasturchi.get_fakulteti())

# from distutils.log import info
# from mimetypes import init


# class Moshina:
#     def __init__(self, nomi, modeli, rangi, yili, narhi):
#         self.nomi = nomi
#         self.modeli = modeli
#         self.rangi = rangi
#         self.yili = yili
#         self.narhi = narhi
#     def get_info(self):
#         info = f"Nomi:{self.nomi}, Modeli:{self.modeli}, Rangi:{self.rangi}. "
#         info += f"Yili:{self.yili}, Narhi:{self.narhi}. "
#         return info

# car1 = Moshina("GM", "Gentra", "Oq", 2021, 12000)
# car2 = Moshina("Opel", "cls", "qora", 2019, 24510)
# print(car1.get_nomi())
# print(car2.get_nomi())




# # voris klass
# class New_Car(Moshina):
#     def __init__(self, nomi, modeli, rangi, yili, narhi, lyuk):
#         super().__init__(nomi, modeli, rangi, yili, narhi)
#         self.lyuk = lyuk

#         def get_info(self):
#             info = f"Nomi:{self.nomi}, Modeli:{self.modeli}, Rangi:{self.rangi}. "
#             info += f"Yili:{self.yili}, Narhi:{self.narhi}, Luyk:{self.lyuk}. "
#             return info

# car3 = New_Car("Mercedes-B", "G63", "Oq", 2021, 145000)
# print(f"{car3.get_nomi()} ")

# class Moshina:
#     def __init__(self, nomi, modeli, rang, narh, yili=0):
#         self.nomi = nomi
#         self.modeli = modeli
#         self.rang = rang
#         self.narh = narh
#         self._yil = yili

#     def get_yil(self):
#         return self._yil

#     def __repr__(self):
#         return f"Moshina: {self.nomi}, "

# moshina1 = Moshina("HUYNDAI", "Tukson", "Qora", 47600, 2022)
# print(moshina1.modeli)
# print(moshina1.narh)
# print("Inkap: ", moshina1.get_yil())

# from distutils.log import info


# class Tanish_Bilish:
#     def __init__(self, ismi, familiyasi, nechi_yoshi, qaerda_ishlidi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.nechi_yoshi = nechi_yoshi
#         self.qaerda_ishlidi = qaerda_ishlidi
#     def get_info(self):
#         info = f"Ismi:{self.ismi}, Familiyasi:{self.familiyasi}, Nechi_yosh:{self.nechi_yoshi}."
#         info += f"Qaerda_ishlidi:{self.qaerda_ishlidi}."
#         return info