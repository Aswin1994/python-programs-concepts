#!C:\Python27\python.exe
import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","aswin")
if sqlcon:
    print "Connected the MySQL "
    cursor=sqlcon.cursor()
    sql= """insert into student values('aswin','12cse13','75','A')"""
    try:
        cursor.execute(sql)
        sqlcon.commit()
    except:
        sqlcon.rollback()    
    sqlcon.close()
else:
    print "Not Connected"
    
