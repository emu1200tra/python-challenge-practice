import sys
from PIL import Image

image = Image.open('mozart.gif')
result = image.copy()

print max(image.histogram()) , image.size
data = image.histogram()
#height = 480
record = []
for i in range(0 , len(data)):
  if data[i] % 480 == 0 and data[i] != 0:
    record.append(i)

print record , data[record[0]]

#for i in range(0 , 640):
#  for j in range(0 , 480):
#    result.putpixel((i , j) , 195)
#result.show()
tmp = []
for i in range(0 , 480):
  for j in range(0 , 640):
    if image.getpixel((j , i)) == 195:
      for k in range(j , 640):
        tmp.append(image.getpixel((k , i)))
      for l in range(0 , j):
        tmp.append(image.getpixel((l , i)))
      for m in range(0 , 640):
        result.putpixel((m , i) , tmp[m])
      tmp = []
      break

result.show()