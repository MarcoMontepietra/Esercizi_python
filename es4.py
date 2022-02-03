import json 
try:
    dati=json.load(open("file4.json"))
    print(dati)
    lista=list()
    for i in range(0,len(dati)):
        lista=lista+list(dati[i])
    print(lista)
    lista_copia=list()
    flag=False
    for i in range(0,len(lista)):
        flag=False
        for j in range(0,len(lista_copia)):
            if(lista[i]==lista_copia[j]):
                flag=True
        if flag==False:
            lista_copia.append(lista[i])
    print(lista_copia)
    
    lista_copia2=list(lista_copia)
    listone=list()
    
    for i in range(0,len(lista_copia)):
        listone.append([])
        for j in range(1,len(lista_copia)+1):
            if j==1:
                var=lista_copia[0]
            if j!= len(lista_copia):
                lista_copia[j-1]=lista_copia[j]
                listone[i].append(lista_copia[j-1])
            else:
                lista_copia[j-1]=var
                listone[i].append(lista_copia[j-1])
    print(listone)

except(IOError):
     print("Errore nell'apertura del file")

  












'''
    for i in range(0,len(lista_copia)):
        for j in range(1,len(lista_copia)):
            if j==(len(lista_copia)-1):
                val=lista_copia[0]
                lista_copia[len(lista_copia)-1]=val
            else:
                lista_copia[j-1]=lista_copia[j]
        listone[i]=lista_copia
    print(listone)
'''   
'''
     for j in range(0,len(lista_copia)):
                for h in range(1,len(lista_copia)):
                    lista_copia[]
                listone=listone+lista_copia
    '''