import difflib



data = open("delta.txt")

#data = f.read()

#0-52  109

data1 = []
data2 = []

for line in data:
    data1.append(line[0:len(line)/2].strip())
    data2.append(line[len(line)/2:len(line)].strip())
    
    if data1[-1] == '':
        data1.pop()
    if data2[-1] == '':
        data2.pop()

data.close()

print 'check'
diff = list(difflib.ndiff(data1 , data2))

in1 = []
in2 = []
in12 = []
print 'cehck2'
for i in diff:
    if i[0] == ' ':
        in12.extend(i[2:].split())
    if i[0] == '+':
        in1.extend(i[2:].split())
    if i[0] == '-':
        in2.extend(i[2:].split())
print 'check3'
p1 = open('p1.png' , 'wb')
p2 = open('p2.png' , 'wb')
p3 = open('p3.png' , 'wb')

for i in in1:
    p1.write(chr(int(i , 16)))
for i in in2:
    p2.write(chr(int(i , 16)))
for i in in12:
    p3.write(chr(int(i , 16)))

p1.close()
p2.close()
p3.close()
