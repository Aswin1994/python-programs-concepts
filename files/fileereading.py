import socket
str=socket.gethostbyname(socket.gethostname())
fileread=open("string.py","r+")
a=fileread.read()
print a.count(str)


f = open("string.py")
l = [x for x in f.readlines() if x != "\n"]
print str(0)


mynewhandle = open("string.py", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if str(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    else:
        x=theline.find("192.168.1.2",0,str(theline))
        if x!=-1:
            print theline
        else:
            print "Not Found"
        
mynewhandle.close()



