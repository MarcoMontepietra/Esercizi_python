valore=False
while valore==False:
    n=input('Inserisci un numero intero: ')
    try:
        num=int(n)
        if(num>0):
            valore=True
        else:
            print(n+' non è >0!')
            valore=False
    except ValueError:
        print(n+' non è un numero intero!')
        valore=False
i=0

while(i<num):
    print('*',end='')
    i+=1
print('\nfinito')