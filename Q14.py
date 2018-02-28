import sys
from PIL import Image
from time import sleep
image = Image.open('wire.png')
result = Image.new('RGB' , (100 , 100))

(a , b) = image.size

flag = 0
max_counter = 99
counter = 1
first = 1
counter2 = 0
place = [0 , 0]
for i in range(0 , a):
  tmp = image.getpixel((i , 0))
  if first == 1:
    print place
    result.putpixel(place , tmp)
    place[0] += 1
    if place == [100 , 0]:
      place = [99 , 1]
      flag = 1
      first = 0
  else:
    print place , 'check:' , counter , ':' , max_counter
    #sleep(0.1)
    if flag == 0:
      result.putpixel(place , tmp)
      place[0] += 1
      counter += 1
      if counter > max_counter:
        counter = 1
        flag = (flag + 1) % 4
        counter2 += 1
        
        place[0] = place[0] - 1
        place[1] = place[1] + 1
        if counter2 == 2:
          max_counter -= 1
          counter2 = 0
    elif flag == 1:
      result.putpixel(place , tmp)
      place[1] += 1
      counter += 1
      if counter > max_counter:
        counter = 1
        flag = (flag + 1) % 4
        counter2 += 1
        
        place[0] = place[0] - 1
        place[1] = place[1] - 1
        if counter2 == 2:
          max_counter -= 1
          counter2 = 0
    elif flag == 2:
      result.putpixel(place , tmp)
      place[0] -= 1
      counter += 1
      if counter > max_counter:
        counter = 1
        flag = (flag + 1) % 4
        counter2 += 1
        
        place[0] = place[0] + 1
        place[1] = place[1] - 1
        if counter2 == 2:
          max_counter -= 1
          counter2 = 0
    elif flag == 3:
      result.putpixel(place , tmp)
      place[1] -= 1
      counter += 1
      if counter > max_counter:
        counter = 1
        flag = (flag + 1) % 4
        counter2 += 1
        
        place[0] = place[0] + 1
        place[1] = place[1] + 1
        if counter2 == 2:
          max_counter -= 1
          counter2 = 0
result.show()