import socket
f = open('ipadd.py','r')
line_num=0
str=socket.gethostbyname(socket.gethostname())
print "Search String is Found in line Number:"
for line in f.readlines():
    line_num += 1
    if line.find(str) >= 0:
        print line_num
