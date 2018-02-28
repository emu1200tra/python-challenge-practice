import sys
import re
from time import sleep

tmp = []
arr = ['1']
counter = 0
record = '0'
result = ['1']

while 1:
  i = 0
  while i < len(arr):
    record = arr[i]
    j = i
    #print 'i:' , i , 'arr:' , len(arr)
    while j < len(arr) and record == arr[j]:
      #print 'check:' , arr[j]
      j += 1
      counter += 1

    tmp.append(str(counter))
    tmp.append(record)
    i += counter
    counter = 0
    
  sleep(0.8)
  arr = tmp
  tmp = []
  result.append(''.join(arr))
  if len(result) == 31:
    break
  print 'result:' , result
  print 'len:' , len(result)
print result[30]
print len(result[30])
