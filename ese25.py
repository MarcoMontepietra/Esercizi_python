valore=False
while valore==False:
    n=input('Inserisci un numero: ')
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

x=list(n)
print(x)

for i in range(len(x)):
    j=int(x[i])
    print(str(j),end=' ')
    for j in range (0,j):
        print('*',end='')
    print('\n')