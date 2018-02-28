a=input("enter A:")
b=input("enter B:")
list=[1,2,3,4,5]
if a in list:
    print"available"
else:
    print"un available"
    
x=input("enter A:")
y=input("enter B:")
c=float(x)
d=float(y)
print id(c)
print id(d)
if c is d:
    print"%d and %d is same"%(c,d)
if c is not d:
    print"%d and %d is not equal"%(c,d)
if id(c)==id(d):
    print"%d and %d are same type"%(c,d)
else:
    print"failed"
