
def asal_mi(x):
    if x<2:
        return print(f"{x} Asal sayı değildir1")
    for i in range(2, x):
        if x % i == 0:
            return print(f"{x} Asal sayı değildir") 
    return print(f"{x} Asal sayıdır")


count = 5
while count>0:
    x = int(input("Lütfen bir sayı giriniz: "))
    asal_mi(x)
    count -= 1




