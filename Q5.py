import sys
import pickle

def main():
    #f = file('test_case.txt' , 'r')
    #w = open('contest.txt' , 'w')
    
    from urllib2 import urlopen
    import re
    from collections import Counter
    
    request = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    #a = request.read()
    #b = a.decode("utf-8")
    #print b
    data = pickle.load(request)
    print data[1][1][1]
    for i in range(0 , len(data)):
        for j in range(0 , len(data[i])):
            for k in range(0 , data[i][j][1]):
                sys.stdout.write(data[i][j][0])
        sys.stdout.write("\n")
       
    #print pickle.load(b)
    
    #d = re.findall('[a-z]', b)
    #print ''.join(d)
    #result = Counter(d)
    #sorted(result.elements())
    #print result
    
    #w.write(b)

    #w.close
    #f.close
if __name__ == '__main__':
    main()
