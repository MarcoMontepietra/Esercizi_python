valore=False
while valore==False:
    n=input('Inserisci l\'altezza: ')
    try:
        num=int(n)
        if(num>0 and num<9):
            valore=True
        else:
            print(n+' non è compreso tra 0 e 9!')
            valore=False
    except ValueError:
        print(n+' non è un numero intero!')
        valore=False

cont=0
for i in range(1,num+1):
    for j in range(1,num - i+1):
        print(' ',end='')
    cont=1
    for k in range(num-i+1,num+1):
        print(str(cont),end='')
        cont=cont+1
    cont=i-1
    for k in range(num-i+2,num+1):
         print(str(cont),end='')
         cont=cont-1
    print('\n', end='')
        
        