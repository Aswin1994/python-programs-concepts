import os
for x in os.listdir(os.getcwd()):
    if x.endswith(".py"):
        print x


for x in os.listdir(os.getcwd()):
    if x.endswith(".py"):
        file=open(x,"r")
        print "Name of the file: ", file.name
        print "Closed or not : ", file.closed
        print "Opening mode : ", file.mode
        file.close()
        print "Closed or not : ", file.closed
        
    
