# Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
liste = []
for i in range (0,5):
    sayi=int(input("Lütfen bir sayı giriniz: "))
    liste.append(sayi)

print(f"Toplam       : {sum(liste)}")
print(f"Ortalama     : {(sum(liste))/ len(liste)}")
print(f"En büyük sayı: {max(liste)}")
print(f"En küçük sayı: {min(liste)}")