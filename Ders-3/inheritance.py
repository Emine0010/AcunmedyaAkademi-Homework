class Vehicle():
    def __init__(self,model):
        self.model=model
    def start(self):
        print(f"{self.model} başlatlıyor..")
class Car(Vehicle):
    def some_car_functıon():
        print("car functıon")
    def start(self): # method overriding -> Polymporishm (Araştırma)
        print(f"Araba başlatılıyor..")

class Truck(Vehicle):
    def __init__(self, model ,capacity):
        super().__init__(model)
        self.capacity = capacity

    def load_weight(self):
        print("Kamyonete yükleniyor..")
       

car1 = Car("Toyota")
car1.start()
car1.some_car_functıon()

truck1 = Truck("Scania",500)
truck1.start()
truck1.load_weight()


# Polymporishm
class Kedi:
    def ses_cikar(self):
        return "Miyav!"

class Kopek:
    def ses_cikar(self):
        return "Hav hav!"

# Polymorphism kullanımı
hayvanlar = [Kedi(), Kopek()]
for hayvan in hayvanlar:
    print(hayvan.ses_cikar())  # Farklı sınıflar, aynı metod adı