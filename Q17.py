import cookielib , urllib2
import sys
from urllib2 import urlopen
import urllib
import requests
from collections import Counter
import bz2
import xmlrpclib

control = 1

if control == 0:
    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

    data = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')

    #print cookies

    much_more_cookies = []

    flag = 0
    content = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345', auth=('huge', 'file'))
    a = content.content
    b = a.decode("utf-8")
    b = b.split(' ')

    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

    data = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')

    #print cookies
    much_more_cookies.append(cookies)
    while flag == 0 :
        result = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' +b[len(b)-1]
        request = urlopen(result)    
        a = request.read()
        b = a.decode("utf-8")
        b = b.split(' ')
        if a == "that's it.":
            flag = 1
        #print ''.join(b)

        cookies = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

        data = opener.open(result)

        #print cookies
        much_more_cookies.append(cookies)

    #much_more_cookies = ''.join(much_more_cookies)
    record = []
    for i in much_more_cookies:
        for j in i:
            print j.value
            record.append(j.value)
    print ''.join(record)
if control == 1:
    input_bz = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
    input_bz = urllib.unquote_plus(input_bz)
    output = bz2.decompress(input_bz)

    print output
    conn = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print conn.system.listMethods()
    print conn.system.methodHelp('phone')
    print conn.system.methodSignature('phone')
    print conn.phone('Leopold')
    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

    data = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
    print cookies
    for i in cookies:
        print 'check:' , i 
        i.value = 'the flowers are on their way'

    data = opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php')
    print data.read()