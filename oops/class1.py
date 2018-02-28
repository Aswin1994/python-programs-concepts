# Blueprint of Object
# Object is a property of class
# Constructor is function will be invoked when we are creating the object for the class
class Example:
    def __init__(self):
        print "This is constructor"
    def add(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        print "sum of %d + %d=%d"%(self.a,self.b,self.c)
obj=Example()
obj.add(10,20)
