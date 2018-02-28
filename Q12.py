import sys
from time import sleep


file = open('evil2.gfx' , 'rb')

data = file.read()
file.close()
#print data[1::5]


for i in range(0 , 5):
  file = open(str(i)+'.jpg' , 'wb')
  file.write(data[i : : 5])
  file.close()