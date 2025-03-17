# 1den 100’e kadar olan tüm asal sayıları bulan bir program yazın.
for i in range (2,101):
    is_prime = True 
    for k in range (2,i):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
         print(i,end=" ")
