#file opening and closing
file = open("aswin.txt", "wb")
print "Name of the file: ", file.name
print "Closed or not : ", file.closed
print "Opening mode : ", file.mode
file.close()
print "Closed or not : ", file.closed


# Writing and Reading from files
file=open("aswin.txt","wb")
file.write("Python is Interpreted Language")
file.close()





