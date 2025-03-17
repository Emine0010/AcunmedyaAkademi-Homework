# Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
def faktöriyel_hesapla(sayı):
    toplam = 1
    for i in range(1,sayı+1):
        toplam *=i
    print(toplam)
        
count = 5 
while count >0 :
    sayı = int(input("Bir sayı giriniz: ")) 
    faktöriyel_hesapla(sayı)
    count -= 1 

