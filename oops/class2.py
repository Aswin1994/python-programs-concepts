class studentinfo:
    def __init__(self,value):
        self.value=value
    def getStudentDetails(self):
        self.name=raw_input("Enter Name:")
        self.rollno=raw_input("Enter RollNo:")
        self.department=raw_input("Enter Department:")
    def getMarkDetails(self):
        self.m1=input("Enter Mark1:")
        self.m2=input("Enter Mark2:")
        self.m3=input("Enter Mark3:")
    def calculate(self):
        self.total=self.m1+self.m2+self.m3
        self.average=self.total/3
        if self.average>=90:
            self.grade="A Grade"
        elif self.average>=70 and self.average<90:
            self.grade="B Grade"
        elif self.average>=50 and self.average<70:
            self.grade="C Grade"
        else:
            self.grade="Fail"
    def display(self):
        print "%s"%(self.value)
        print "**********************************"
        print "Student Name is:%s"%(self.name)
        print "Student RollNo is :%s"%(self.rollno)
        print "Department isd:%s"%(self.department)
        print "***********************************"
        print "Student MArk1:%d"%(self.m1)
        print "Student MArk2:%d"%(self.m2)
        print "Student MArk3:%d"%(self.m3)
        print "***********************************"
        print "Total Marks:%d"%(self.total)
        print "Average is:%d"%(self.average)
        print "Grade is:%s"%(self.grade)
obj=studentinfo("STUDENT INFORMATION")
obj.getStudentDetails()
obj.getMarkDetails()
obj.calculate()
obj.display()

        
