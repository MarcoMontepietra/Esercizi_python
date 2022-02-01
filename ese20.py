import os
n=input('Inserisci un numero intero: ')
try:
    num=int(n)
except ValueError:
    print('Non è un numero intero!!!')
    os._exit(1)
i=0
while(i<num):
    print('*',end='')
    i+=1
print('\nfinito')