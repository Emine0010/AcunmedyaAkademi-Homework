# Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.
def hesapla(sayi_1, sayi_2 ,operatör ):
    if operatör == "+":
        return print(sayi_1 + sayi_2)
    elif operatör == "-":
        return print(sayi_1 - sayi_2)
    elif operatör == "*":
        return print(sayi_1 * sayi_2)
    elif operatör == "/":
        if sayi_2 == 0:
            print("Payda 0 olamaz.Lütfen geçerli bir sayi giriniz")
            sayi_2= int(input("Number2: "))
        return print(sayi_1 / sayi_2)

count = 5 
while count >0 :
    sayi_1 = int(input("number1: "))
    sayi_2 = int(input("Number2: "))
    operatör = input("işlem: ")
    hesapla ( sayi_1 , sayi_2 , operatör)
    count -= 1