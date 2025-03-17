# Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın
def yas_grubu ( age ):
    if 0 <= age < 13 :
        return print ("Çocuk")
    elif 12 < age < 20 :
        return print ("Genç")
    elif 19 < age < 60 :
        return print ("Yetişkin")
    elif 59 < age :
        return print ("Yaşlı")

count = 5 
while count > 0:   
    age = int(input("Lütfen yaşınızı giriniz: "))
    yas_grubu(age)
    count -= 1 