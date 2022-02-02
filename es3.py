cubi=[n**3 for n in range(10)]
print(cubi)
def funPari(x):

    if(x%2==0):
        return True
    else:
        return False
p=filter(funPari,cubi)
pari=list(p)
print(pari)

def moltiplicazione(a):
    return a*3    
moltip=map(moltiplicazione,pari)
print(list(moltip))