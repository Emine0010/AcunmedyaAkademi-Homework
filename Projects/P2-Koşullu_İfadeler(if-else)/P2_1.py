# Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
def even_or_od (number):
    if number % 2 == 0 :
        return print(f"{number} çift sayıdır")
    return print(f"{number} tek sayıdır")

count = 5 
while count> 0 :
    number = int(input("sayı giriniz: "))
    even_or_od(number)
    count -= 1 