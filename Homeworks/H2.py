faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"
print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = int(input ("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade)) #python da kullanıcıdan alınan girdiler varsayılan olarak str dir
vade = vade + 12

#String interpolation 
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print (f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = input("İsminizi giriniz")
metin = "Merhaba {name}".format(name = isim) #Süslü parantezli olan yere atadığımız şey geliyor
print(metin)

# f-string
metin = f"Hoşgeldiniz{1+1}"
print(metin)

# Listeler
dizi = ["İhtiyaç kredisi",10,5.2,True]
print(dizi)

krediler = ["İhtiyaç kredisi", "Taşıt kredisi","Konut kredisi"]
print(type(krediler))

print(krediler[0])
# print(krediler[5]) = out of range hatası

print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel kredi") #listenin sonuna eleman ekler
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop() #listenin son elemanını siler
print(krediler)

krediler.pop(0) # 0. indexini siler
print(krediler)

krediler.append("Taşıt kredisi") # içine girdiğimiz değeri siler 2 tane aynısı varsa il gördüğünü siler
print(krediler)

krediler.remove("Taşıt kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"]) #dizimize birden fazla eleman ekleyebiliyoruz
print(krediler)

# DÖNGÜLER
# for döngüsü

for i in range (10): # i 0 dan başlıcak 10 dan küçük olduğu sürece devam edicek 10 dahil değil
    print(i)

for i in range (5,10): # 5 den başlıcak 10 dan küçük olduğu sürece devam edicek
    print(i)

for i in range (0,50,10): # O dan (ilk yazılan yer) 50 ye (ikinci yazılan yer) kadar 10 ar 10 ar (son yazılan yer) artarak ilerlicek = 0-10-20-30-40 (50 dahil değil)
    print(i)
    
# range fonksiyonu integer değerlerle çalışır float olmaz hata alırız
# for i in range(0.1,0.5):
    # print(i)

krediler = ["İhtiyaç kredisi", "Taşıt kredisi","Konut kredisi"]
for kredi in krediler:
    print(kredi)

for i in range (len(krediler)):
    print(krediler[i])

# while döngüsü
i = 0 
while i < 10 :
    print("x")  
    i += 1 # i++ yoktur pythonda
print("y")

while True:
    print("x")
    break

i = 0 
while i < len(krediler):
    if krediler[i] == "Konut kredisi":
        break
    print(krediler[i])
    i += 1

i = 0 
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "Konut kredisi":
        break

# FONKSİYONLAR

fiyat = 100
indirim = 20
#definition define
# void 
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Emine")
sayHello("Mustafa")
sayHello("Furkan")

# return
def calculateAndReturn(prize,discount):
    return prize - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

fonk1 = calculateWithParams(100,50)
fonk2 = calculateAndReturn(300,100)
print(f"144.satır:{fonk1}")
print(f"145.satır:{fonk2}")

