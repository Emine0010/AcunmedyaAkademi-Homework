# Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın
def notunu_hesapla(puan):
    if 90 <= puan <=100 :
        return print("Notunuz A dır")
    elif 80 <= puan <= 89:
        return print("Notunuz B dır")
    elif 70 <= puan <= 79 :
        return print ("Notunuz C dir")
    elif 60 <= puan <= 69 :
        return print("Notunuz D dir")
    return print("Notunuz F dir")

count = 5 
while count>0:
    puan = int(input("Notunuzu giriniz: "))
    notunu_hesapla(puan)
    count -= 1