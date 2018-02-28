import sys
from PIL import Image
from time import sleep

image = Image.open('cave.png')

(a , b) = image.size

odd = Image.new('RGB' , (a/2 , b/2))
even = Image.new('RGB' , (a/2 , b/2))

for i in range(0 , a):
  for j in range(0 , b):
    tmp = image.getpixel((i , j))
    if (i + j) % 2 == 0:
      even.putpixel((i/2 , j/2) , tmp)
    else:
      odd.putpixel((i/2 , j/2) , tmp)

even.show()
sleep(10)
odd.show()