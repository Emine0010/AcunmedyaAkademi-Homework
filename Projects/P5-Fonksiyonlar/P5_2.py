# Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın.
def palindrom_mu(kelime):
    if kelime == kelime[::-1]:
        return print(f"{kelime} -> polindrom sayıdır")
    return print(f"{kelime} -> polindrom değildir")

for i in range(0,5):
    kelime = input("Lütfen bir kelime giriniz: ")
    palindrom_mu(kelime)
