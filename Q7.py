import sys

from PIL import Image

def main():
    #f = file('test_case.txt' , 'r')
    #w = open('contest.txt' , 'w')
    
    #from urllib2 import urlopen
    
    imag = Image.open('oxygen.png')
    data = []
    data_clear = []
    for i in range(0 , 629):
        data.append(imag.getpixel((i , 48)))

    #print data
    data_clear.append(imag.getpixel((0 , 48)))
    for i in range(5 , len(data) , 7):
        data_clear.append(imag.getpixel((i , 48)))
        #print i
        

    #print data_clear
    print data_clear[0][0]
    result = []
    for i in range(0 , len(data_clear)):
        result.append(str(unichr(data_clear[i][0])))

    print ''.join(result)
    
    new_data = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    for i in range(0 , len(new_data)):
        result.append(str(unichr(new_data[i])))

    print ''.join(result)

    #w.write(data)
    #request = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.html")
    #a = request.read()
    #b = a.decode("utf-8")
    
    
    #d = re.findall('[a-z]', b)
    
    #w.write(b)

    #w.close
    #f.close
if __name__ == '__main__':
    main()
