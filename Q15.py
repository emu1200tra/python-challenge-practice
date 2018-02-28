import sys
from datetime import date
from time import sleep

list_year = range(1006 , 1997)
wanted_year = []
record = []

for i in range(0 , len(list_year)):
  if (list_year[i] % 100 != 0) and (list_year[i] % 10 == 6) and (list_year[i] % 4 == 0):
    wanted_year.append(list_year[i])
  elif (list_year[i] % 400 == 0) and (list_year[i] % 10 == 6) and (list_year[i] % 4 == 0):
    wanted_year.append(list_year[i])

print 'wanted:' , wanted_year

for i in range(0 , len(wanted_year)):
  day = date(wanted_year[i] , 1 , 26)
  if day.weekday() == 0:
    record.append(wanted_year[i])

for i in range(0 , len(record)):
  print record[i]