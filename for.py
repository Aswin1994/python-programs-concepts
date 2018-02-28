a=["10","20","30"]
for i in a:
    print i

for j in "phython":
    print j

subjects=["java","phython","php"]
for a in subjects:
    print a

a=["10","20","30"]
for index in range(len(a)):
    print a[index]
    #print a[1]
    
print "even num"
for a in range(10):
    if a%2==0:
        print "Even Number %d"%(a)


for x in range(1,10):
    if x==5:
        break
    else:
        print x

for x in range(1,10):
    if x%2==0:
        continue
    else:
        print x
