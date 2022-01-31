import math
n1=int(input('Inserire il primo numero: '))
n2=int(input('Inserire il secondo numero: '))
n3=int(input('Inserire il terzo numero: '))
maggiore=0
minore=0
somma=0
radice=0
if(n1>n2):
    if(n1>n3):
        maggiore=n1
    else:
        maggiore=n3
else:
    if(n2>n3):
        maggiore=n2
if(n1<n2):
    if(n1<n3):
        minore=n1
    else:
        minore=n3
else:
    if(n2<n3):
        minore=n2
        
media=(n1+n2+n3)/3
radice=math.sqrt(n1+n2+n3)
print('Maggiore: '+str(maggiore))
print('Minore: '+str(minore))
print('Media: '+str(media))
print('Radice quadrata della somma: '+str(radice))