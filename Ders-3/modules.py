# built-in modules -> pythona yüklü gelen ( math , date )
# local modules -> projede bizim ürettiğimiz dosyalar (oop.py)
# paket yöneticisnde bulunan 3. taraf kütüphaneler 

#
#import math  # math kütüphanesini komple import et
from math import sqrt as karekök , cos # math kütüphanesinden sqrt fonk. import et
# alias -> takma at ( as ile: sqrt yi karekök ismi olarak kullandım)
import oop
import requests

#print(math.sqrt(25))
print(karekök(25))
print(cos(90))

# car1 = oop.Car("Volvo")
# car1.increase_speed(50)

response = requests.get("https://google.com")
print(response.status_code)