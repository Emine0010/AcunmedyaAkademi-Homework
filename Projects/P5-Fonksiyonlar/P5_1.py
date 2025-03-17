# Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan bir hesap makinesi fonksiyonu yazın.
def hesap_makinesi(number1,number2):
    if number2 != 0 :
        print("Toplam  :", (number1 + number2))
        print("Fark    :", (number1 - number2))
        print("Çarpım  :", (number1 * number2))
        print("Bölüm   :", (number1 / number2))
    else:
        print("Tanımsız..(Bölme için number2 sıfır olamaz)")
        number2 = int(input("Geçerli bir sayı giriniz: "))
        hesap_makinesi(number1,number2)
  
number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))  
hesap_makinesi(number1, number2)