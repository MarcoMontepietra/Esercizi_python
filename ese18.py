import os
num=input('Inserire un valore tra 1 e 12: ')
try:
    mese=int(num)
except ValueError:
   print('Non è un numero intero!')
   os._exit(1)
if(mese<1 or mese>12):
    print('Valore non valido')
    os._exit(1)
    
if(mese<=3 or mese==12):
    print('Inverno')
elif(mese>3 and mese<=6):
    print('Primavera')
elif(mese>6 and mese<=9):
    print('Estate')
else:
    print('Autunno')
