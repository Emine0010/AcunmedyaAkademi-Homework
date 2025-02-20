print ("Kodlamio")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double
aylikÖdeme = 200.50

#bool, boolean => True veya False
yukselisteMi = False

#Matematiksel Operatörler
# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade - 12)
print(vade - ekVade)
print(36-6)

# * 
print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10*10)

# / (bölme işleminde dönen değer float değerdir)
print(5/5)
print( vade / 2)
print(vade / ekVade)
print(10/2)

yeniVade = vade/ 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod Operatörü
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(10 % 10)

#Mantıksal Operatörler
print(1 == 1)
print( 1 == 2)

#CTRL K + CTRL C (seçilen satırların hepsini yorum yapmak için )veya CTRL ö (hem hepsini yorum yapar hem de normale döndürür)
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)


# or and 
# or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and  5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

# Karar Yapıları
# if else
sayi1 = 10
sayi2 = 15
# sayi1 sayi2 den büyükse ekrana sayi1 daha büyüktür yazdır

#indent = boşluk
if sayi1 > sayi2:
    print("sayi1 sayi2 den büyüktür")
    print("Hala if bloğunun içindeyim")
#Eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("iki sayi eşittir")
else:
    print("sayi1 sayi2 den küçüktür")
print("Burası if bloğunun dışıdır")

print("***********************************")

if sayi1 <= sayi2:
    print("sayi1 sayi2 den büyüktür")
    print("Hala if bloğunun içindeyim")

if sayi1 == sayi2:
    print("iki sayi eşittir")
else:
    print("sayi1 sayi2 den küçüktür")


