import os
mese=input('Inserire il mese: ')
giorno=input('Inserire giorno: ')
try:
    numMese=int(mese)
    numGiorno=int(giorno)
except ValueError:
   print('Non è un numero intero!')
   os._exit(1)
if(numMese<1 or numMese>12):
    print('Valore non valido')
    os._exit(1)
if(numGiorno<1 or numGiorno>31):
    print('Valore non valido')
    os._exit(1)
if(numMese==2 and numGiorno>28) or((numMese==4 or numMese==6 or numMese==9 or numMese==11)and numGiorno>30):
    print('Valore non valido')
    os._exit(1)
    
if(numMese<3):
    print('Inverno')
elif numMese==3:
    if numGiorno<21:
        print('Inverno')
    else:
        print('Primavera')
elif numMese<6:
    print('Primavera')
elif numMese==6:
    if numGiorno<21:
        print('Primavera')
    else:
        print('Estate')
        
elif numMese<9:
    print('Estate')
elif numMese==9:
    if numGiorno<21:
        print('Estate')
    else:
        print('Autunno')

elif numMese<12:
    print('Inverno')
elif numMese==12:
    if numGiorno<21:
        print('Autunno')
    else:
        print('Inverno')