# fonksiyonlar-methodlar

#kodun yeniden kullanılabilirliğini arttırmak ve bakımını kolaylaştırmak için kullanılır

price = 100
total_prize = price + (price*0.2)
price(total_prize)

# fonksiyon tanımlamak 
#parametre => fonksiyona çağırılma aşamasında verilen ver,

# default parameter => rate gönderilirse gönderilen değeri, gönderilmezse 20'yi kullan.
# required parameter , default parameter
# default parameter , required parameter bu sırayla yazamayız bi üstteki gibi yazabiliriz 

def calculate_tax(price , rate=20): # void -> dönüş tipi olmayan # return -> dönüş tipi (int,str)
    return price + (price * (rate / 100))

print("***********")
price1 =calculate_tax(100) # print
price2 =calculate_tax(200) # toplam fiyat alıp başka bir değerle (kargo fyatı) ile topla
price3 =calculate_tax(500)
price4 =calculate_tax(100,10)
price5 =calculate_tax(1000,10)

print(price1)
print(price2+50)

def sum(*args): # sayılar #*args bi tuple dır değişmeyen liste bu örnekte istediğimiz kadar sayı yazabiliriz
    if len(args) <= 0:
        raise ArithmeticError("En az 1 argüman zorunludur")# hata yönetimi
    sonuc = 0 
    for sayi in args:
        sonuc+=sayi
    return sonuc

print(sum (1,2,3,4,5,6,7,8,9,10))
print(sum (5,10))
print(sum(5))
print(sum())

# ** kwargs 
def selamla(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Fonksiyona anahtar kelime argümanları gönderelim
selamla(ad="Ahmet", soyad="Yılmaz", yas=25)


def kullanici_bilgisi(isim, **bilgiler):
    print(f"İsim: {isim}")
    for key, value in bilgiler.items():
        print(f"{key}: {value}")

kullanici_bilgisi("Mehmet", yas=30, sehir="İstanbul", meslek="Mühendis")


# lamdba fonksiyonları: 
# tek satırlık fonksiyonları kısaca tanımlama yöntemi

topla = lambda a,b: a+b

def topla2(a,b):
    return a+b

selamla = lambda isim: print(f"Merhaba,{isim}")

print(topla(3,5))
selamla("Halit")


