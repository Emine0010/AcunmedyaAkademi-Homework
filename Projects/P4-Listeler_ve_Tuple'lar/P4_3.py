# Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın.
liste =[]
for i in range(0,6):
    eleman = input("Lütfen bir liste elemanı giriniz: ")
    liste.append(eleman)

print(liste)
yeni_liste = list(set(liste))
print(yeni_liste)