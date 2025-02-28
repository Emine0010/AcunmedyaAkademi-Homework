print ("Hello World")

#Değişenler
name = "Emine" #string , str
print(name)
# python -> type-safe olmayan bir dildir.
age = 21 #integer,int
print(age)
print(type(age))
age ="abc"
print(age)
#
print(type(age))

#operatörler
#matematiksel (aritmetik) operatörler
rate = 49.56 #float,double

print(1+1)
print(5-2)
print(25/5) #bölme işlemi
print(5*5)
print(25//5) #tam bölme işlemi (aşağıya yuvarlar)
print(36 % 5) #mod alma operatörü
print(5**3) #üssü almak

#

#atama operatörleri
a="abc"
a='abc' #tek tırnak ile çift tırnak aynı şey
number = 5

print(number)
number +=5 #number = number + 5 
number -=2 
print(number)
number /=4 #float 
number *= 10 
print(number)
#

#karşılaştırma operatörleri
is_valid = True # boolean,bool
print(1==1)
print(1!=1)
print (10 < 5)
print(10 >= 10)
#

#Mantıksal operatörler, => and,or,not
 # and => iki durumunda true olması dışındaki durumları false yapar
print(1==1 and 1==2) #true & false = false
print(1==1 and 10>5) #true & true = true
print(1!=1 and 5>10) #false & false = false

print(1==1 or 5>10) #true | false = true
print(1!=1 or 5>10) # false | false = false
print ( (1==1 and 2>5) or 6>6 and (10>5 or 5==5)) #false
print ( False or 6>6 and (10>5 or 5==5)) 
print (False and (10>5 or 5==5)) 

print(not 1==1)
print(1!=1)
#

students = ["Salih" , "Bayram" , "Muhammed" , "Ahmed" , 1 , True , 50.5]
print(students)
students.append("Fatma")
print(students)
students.pop()
print(students)

#indexing
print(students[0])
#print(students[50]) #hata aldı ve kapandı