# reference type ve value type
a = 1
b = a 
b +=10
print(a)
print(b)

list1 = ["Ahmet", "Azra","Emine"]
list2 = list1

list2.append("Fatma")

print(list1)
print(list2)

# reference - value type 
# immutabla - mutable

# döngüler- iterasyon(iteration)
for i in range(5): #indentation, indent #for x adet satırla çalışabilir 
    print(i)
    print("Merhaba")
print("for bitti")

print("********")
for i in range (5,10):
    print(i)

for i in range (5,10,2):
    print(i)

# { }

print("*******")

#döngüyü kırmak => manuel bitirmek 
for i in range (0,100):
    if i == 50:
        break #döngüyü kır # bu iterasyonda (i=50) bu satırdan aşağısını çalıştırmadan döngüyü bitir.
    print(i)

for i in range (0,100):
    if i ==50 :
        continue  # bu iterasyonda(i=50) bu satırdan aşağısını çalıştırmadan bir sonraki iterasyona geç
    print(i)

#iteration , index
for student in list1:
    if i =="Emine":
        continue
    print(student)

# while
# Koşullarla çalışır
# Sonsuz döngü tehlikesi

# while True:  #infinitive loop (sonsuz döngü) kapatmak için ctrl c kullan 
#     print("While....") 

i = 5
while i <=10 :
    print(i)
    i+=1
    if i ==6:
        break
i = 5
while i <=10:
    i+=1
    if i ==6 :
        continue
    print(i)

# şart-koşul bloklerı
age = 18
# kural1 => tek çıktı !!
# kural2 => yukarıdan aşağıya ilk doğru koşul
if age >= 18:
    print("Giriş Yapabilirsiniz")
elif age == 18:
    print("Ay kontrolü yapılıyor")
else:
    print("Giriş yapamazsınız")

    