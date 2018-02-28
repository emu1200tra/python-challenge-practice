import sys
import xmlrpclib

conn = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print conn.system.listMethods()
print conn.system.methodHelp('phone')
print conn.system.methodSignature('phone')
print conn.phone('Bert')