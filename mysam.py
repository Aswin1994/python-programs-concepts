#!/Python27/python
import cgi
form=cgi.FieldStorage()
a=(form.getvalue('a'))
b=(form.getvalue('b'))
c=int(form.getvalue('c'))
d=int(form.getvalue('d'))
e=int(form.getvalue('e'))
f=int(form.getvalue('f'))
g=int(form.getvalue('g'))
h=int(form.getvalue('h'))
total=c+d+e+f+g+h
average=total/6
if average>=90:
            grade="A Grade"
elif average>=70 and average<90:
            grade="B Grade"
elif average>=50 and average<70:
            grade="C Grade"
else:
     grade="Fail"
print "student name:%s"%(a)
print "student id:%s"%(b)
print "Total Marks:%d"%(total)
print "Average is:%d"%(average)
print "Grade is:%s"%(grade)
