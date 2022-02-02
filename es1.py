import json
try:
    dati=json.load(open("file2.json"))
    print(dati)
    tupla=()
    a=0
    b=0
    lista=list()
    tupla=()
    for i in range(0,len(dati)):
        var=list(dati[i])
        #print(x)
        for j in range(0,len(var)):
            if(int(var[j])%2==0):
                b=b+int(var[j])
            else:
                a=a+int(var[j])
        lista.append('('+str(a)+','+str(b)+')')
        a=0
        b=0
    tupla=tuple(lista)
    print(tupla)
except(IOError):
    print("Errore nell'apertura del file")