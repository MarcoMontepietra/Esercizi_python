import math
x1=input('Inserire x1: ')
y1=input('Inserire y1: ')
print('primo punto: ('+str(x1)+','+str(y1)+')')
x2=input('Inserire x2: ')
y2=input('Inserire y2: ')
print('secondo punto: ('+str(x2)+','+str(y2)+')')
dx=math.pow((int(x2)-int(x1)),2)
dy=math.pow((int(y2)-int(y1)),2)
distanza=math.sqrt(int(dx)+int(dy))
print('distanza Euclidea: '+str(distanza))