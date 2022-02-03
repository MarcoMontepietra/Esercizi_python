import os
def vendi_libri(x,array,lista):
    if x in array and array[x]>1:
        array[x]=array[x]-1
        print('Libro venduto con successo')
        return True
    elif x in array and array[x]<=1:
        del array[x]
        print('Libro venduto con successo')
        return True
    else:
        lista.append(x)
        print('Il libro non è disponibile')
        return False


libri={'Harry Potter':5,'Il Signore degli anelli':7,'IT':3,'Cars':1,'Alla ricerca di Nemo':1,'Ironman':2,'Teoria delle pseudoscienze':20,'La vita di Pi':8,'Manuale della patente A e B':26}
libOrdinare=list()
print(libri)
c=2
while c!=1:
    c=input('Inserire 1 per uscire 2 per continuiare: ')
    if int(c)==1:
        os._exit(1)
    else:
        l=input('Inserisci il titolo del libro: ')
        libro=str(l)
        vendi_libri(libro,libri,libOrdinare)
        print(libri)
        print(libOrdinare)
