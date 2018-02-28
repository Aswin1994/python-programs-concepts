a=input("enter A:")
b=input("enter B:")
c=input("enter C:")
print "logical operators"
if a>b and a>c:
    print"A is greater"
elif b>a or b>c:
    print"B is greater"
else:
    print"condition failed"
if not(a==b==c):
             print"success"
else:
    print"un successfull"
d=a&b
e=a|b
f=a^b
g=a&~b,a&~c;
h=a>>4,b>>2;
i=c<<3,b<<2;
print"%d & %d="%(a,b),d
print"%d | %d="%(a,b),e
print"%d ^ %d="%(a,b),f
print"%d ~ %d="%(a,b),g
print"%d >>4,>>2 %d"%(a,b),h
print"%d <<3,<<2 %d"%(c,b),i

   
