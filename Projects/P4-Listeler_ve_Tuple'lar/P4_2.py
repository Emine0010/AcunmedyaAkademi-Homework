# Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.
liste= []
for i in range (0,5):
    kelime = input("Lütfen kelime giriniz: ")
    liste.append(kelime)

liste.reverse()
print("Ters sıralı kelimeler:")
for kelime in liste:
    print(kelime)
