# sınıflar (class)
# özellikler  #attribute

class Car():
    model = ""

    # Constructor (YAPICI METHOD)
    def __init__(self,model, year=2025): #ilgili obje üretildiği an çalışır
        self.__model = model 
        self.year = year #default parametre 
    
    def start(self): #self -> classın kendisini ifade eder
        print(f"{self.__model} {self.year} arabası başlatılıyor..")   #self.model class daki modeldir sadece model yazsak fonksiyonun içindeki modeldir
    
    def increase_speed(self, amount):
        print(f"Hız arttırılıyor: {amount}")
    
    def set_model (self,model): # salt-yazılabilir
        if len(model) < 2:
            print( "Model ismi 2 haneden kısa olamaz")
            return
        self.__model = model 
    def get_model(self): # salt-okunur
        return self.__model


car1 = Car("Toyota",2010) #Instance (örnek)
car1.set_model("abcd")
car1.__model = "Abc" #KAPSÜLLEME ( ENCAPSULATION ) # set
print( car1.model ) # get
#car1.model = "Toyota"
car1.start()
car1.increase_speed(10)

car2 = Car("Hyundai")
# car2.model = "Hyundai"
car2.start()
car2.increase_speed(50)

