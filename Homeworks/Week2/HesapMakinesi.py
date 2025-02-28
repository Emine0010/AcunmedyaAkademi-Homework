def hesap_makinesi(number1,number2,sembol):
    if sembol== "+":
         return print(number1 + number2)
    elif sembol == "-":
         return print(number1 - number2)
    elif sembol == "*":
         return print(number1 * number2)
    elif sembol == "/":
        if y == 0 :
           print("Bölme işlemi için ikinci sayı 0 olamaz") 
        else:
            return print(number1 / number2)
    else:
         print("Geçersiz işlem türü!!!")
         

count = 10     
while count > 0:
    number1 = int (input ("İlk sayıyı giriniz: "))
    number2 = int (input ("İkinci sayıyı giriniz: "))
    sembol = input ("Bir işlem türü seçiniz: ")    
    hesap_makinesi(number1,number2,sembol)
    count -= 1
