import sys

def main():
    #f = file('test_case.txt' , 'r')
    #w = open('contest.txt' , 'w')
    
    from urllib2 import urlopen
    import re
    import zipfile
    from time import sleep
    
    f = zipfile.ZipFile('channel.zip')
    data = f.read('90052.txt')
    print data
    data = data.split(' ')
    print data[len(data)-1]
    comment = []
    comment.append(f.getinfo('90052.txt').comment)
    while 1:
        string = data[len(data)-1] + '.txt'   
        data = f.read(string)
        print data
        data = data.split(' ')
        comment.append(f.getinfo(string).comment)
        if data[len(data)-1] == '46145':
            break
    
    print ''.join(comment)
    #request = urlopen("http://www.pythonchallenge.com/pc/def/channel.html")
    #a = request.read()
    #b = a.decode("utf-8")
    
    
    #d = re.findall('[a-z]', b)
    
    #w.write(b)

    #w.close
    #f.close
if __name__ == '__main__':
    main()
