def text_write(fileName,text):
    with open (fileName, "w" , encoding="utf-8") as file:
        file.write(text+ "\n")

def text_read(fileName) :
   with open (fileName , "r" , encoding="utf-8") as file:
     içerik= file.read()
     print ("\n Dosya İçeriği:\n"+ içerik)

def text_append(fileName):
   with open (fileName ,"a" , encoding="utf-8") as file:
     count = 5
     while count > 0 :
        file.write(input("Eklemek istediğiniz metni giriniz: ")+"\n")
        count -= 1
       
   
def text_okusatır(fileName):
   with open (fileName ,"r" , encoding="utf-8") as file: 
    print("\n Dosya Satır Satır Okuma:")
    for satir in file:
        print(satir.strip()) 
    


fileName = "file.txt"
text = input("Yazmak istediğiniz metni giriniz: ")


text_write(fileName,text)
text_read(fileName)
text_append(fileName)
text_okusatır(fileName)




    
