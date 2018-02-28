import sys

def check(check_char):
    if (check_char >= 'A') and (check_char <= 'Z'):
        return 1
    else:
        return 0

def check2(check_char):
    if (check_char >= 'a') and (check_char <= 'z'):
        return 1
    else:
        return 0

def main():
    f = file('test_case.txt' , 'r')
    #w = open('write_result1.txt' , 'w')
    from urllib2 import urlopen
    import re
    from collections import Counter
    #request = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

    #a = request.read()

    #b = a.decode("utf-8")

    #f.write(b)

    #d = re.findall('[a-z]', b)
    #print ''.join(d)
    #result = Counter(d)
    #sorted(result.elements())
    #print result
    counter = 0
    list_char = []
    small_char = []
    record = []
    for line in f:
        for i in range(0 , len(line)):
            list_char.append(line[i]) 
    for i in range(0 , len(list_char)):
        if (list_char[i] >= 'a') and (list_char[i] <= 'z'):
            small_char.append(i)
    for i in range(0 , len(small_char)):
        if (small_char[i] == 3):
            if(check(list_char[small_char[i]-3]) + check(list_char[small_char[i]-2]) + check(list_char[small_char[i]-1]) + check(list_char[small_char[i]+3]) + check(list_char[small_char[i]+2]) + check(list_char[small_char[i]+1]) + check2(list_char[small_char[i]+4]) == 7):
                counter += 1
                record.append(list_char[small_char[i]])
        elif (small_char[i] == (len(list_char) - 4)):        
            if(check(list_char[small_char[i]-3]) + check(list_char[small_char[i]-2]) + check(list_char[small_char[i]-1]) + check(list_char[small_char[i]+3]) + check(list_char[small_char[i]+2]) + check(list_char[small_char[i]+1]) + check2(list_char[small_char[i]-4]) == 7):
                counter += 1
                record.append(list_char[small_char[i]])
        elif (small_char[i] > 3) and (small_char[i] < (len(list_char) - 4)):
            if(check(list_char[small_char[i]-3]) + check(list_char[small_char[i]-2]) + check(list_char[small_char[i]-1]) + check(list_char[small_char[i]+3]) + check(list_char[small_char[i]+2]) + check(list_char[small_char[i]+1]) + check2(list_char[small_char[i]-4]) + check2(list_char[small_char[i]+4]) == 8):
                counter += 1
                record.append(list_char[small_char[i]])
    record = ''.join(record)
    print counter , record
    #    w.write(line)

    #w.close
    f.close
if __name__ == '__main__':
    main()
