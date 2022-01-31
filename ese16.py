import math
import os
n=input('inserire un numero(>0): ')
try:
    int(n)
except ValueError:
    print('Il numero inserito non è un intero')
    os._exit(1)
if(int(n)>0):
    radice= math.sqrt(int(n))
    print('La radice quadrata di '+str(n)+' vale: '+str(radice))
else:
    print('Il numero inserito non è > 0!!!')