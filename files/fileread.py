fileread=open("aswin.txt","r+") 
fileread=open("aswin.txt","r+")
fileread=open("aswin.txt","r+")
freadline=fileread.readlines()
print "%s" % (freadline)
192.168.1.4
position=fileread.tell()
print "Current File Position is:",position
192.168.1.4
position=fileread.seek(5)
print "Current File Position is:",position
192.168.1.4
position=fileread.tell()
print "Current File Position is:",position

