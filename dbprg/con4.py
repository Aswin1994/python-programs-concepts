#!C:\Python27\python.exe
import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","aswin")
if sqlcon:
    print "Connected the MySQL "
    cursor=sqlcon.cursor()
    sql= "select * from student"
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            name=row[0]
            id=row[1]
            totalmarks=row[2]
            grade=row[3]
            print "%s %s %d %s"%(name,id,totalmarks,grade)
            
    
    except:
        print"unable to fetch data"    
    sqlcon.close()
else:
    print "Not Connected"
    
