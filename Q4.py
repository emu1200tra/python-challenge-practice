import sys


def main():
    #f = file('test_case.txt' , 'r')
    #w = open('contest1.txt' , 'w')
    from urllib2 import urlopen
    import re
    from collections import Counter
    flag = 0
    request = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=72198")
    a = request.read()
    b = a.decode("utf-8")
    b = b.split(' ')
    while flag == 0 :
        result = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' +b[len(b)-1]
        request = urlopen(result)    
        a = request.read()
        b = a.decode("utf-8")
        b = b.split(' ')
        if b[len(b)-1] == '</html>':
            flag = 1
        print ''.join(b)
    b = ''.join(b)
    print b
    #d = re.findall('[a-z]', b)
    #print ''.join(d)
    #result = Counter(d)
    #sorted(result.elements())
    #print result
    
    #    w.write(line)

    #w.close
    #f.close
if __name__ == '__main__':
    main()
