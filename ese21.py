valore=False
while valore==False:
    n=input('Inserisci un numero intero: ')
    try:
        num=int(n)
        valore=True
    except ValueError:
        print(n+' non è un numero intero!')
        valore=False
i=0

while(i<num):
    print('*',end='')
    i+=1
print('\nfinito')
