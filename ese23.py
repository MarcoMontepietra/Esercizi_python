import os
a=input('Inserisci lato a: ')
try:
    num1=int(a)
    if(num1<0):
        print(a+' è <0!')
        os._exit(1)
except ValueError:
    print(a+' non è un numero intero!')
    os._exit(1)
b=input('Inserisci lato b: ')
try:
    num2=int(b)
    if(num2<0):
        print(b+' è <0!')
        os._exit(1)
except ValueError:
    print(b+' non è un numero intero!')
    os._exit(1)
    
for i in range(0,num2):
    if(i==0 or i==num2-1):
        for j in range(0,num1):
            print('* ', end='')
        print('\n', end='')
    else:
        for j in range(0,num1):
            if(j==0 or j==num1-1):
                print('* ',end='')
            else:
                print('  ',end='')
        print('\n', end='')