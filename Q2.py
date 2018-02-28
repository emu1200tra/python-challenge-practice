import sys

def main():
    f = open('contest' , 'w')
    from urllib2 import urlopen
    import re
    from collections import Counter
    request = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

    a = request.read()

    b = a.decode("utf-8")

    f.write(b)

    d = re.findall('[a-z]', b)
    print ''.join(d)
    result = Counter(d)
    sorted(result.elements())
    print result
    
    

if __name__ == '__main__':
    main()
