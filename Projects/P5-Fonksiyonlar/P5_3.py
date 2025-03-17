# Kullanıcının yaşını girerek kaç yıl sonra 100 yaşına ulaşacağını hesaplayan bir fonksiyon yazın.
from datetime import datetime
def how_many_years(age):
    year1 = 100 - age
    bugün = datetime.now().year
    tarih = bugün + year1
    print(f"{year1} yıl sonra {tarih}'de 100 yaşında olucaksın :( ")

for i in range (0,5):
    age = int(input("Lütfen yaşınızı giriniz: "))
    how_many_years(age)