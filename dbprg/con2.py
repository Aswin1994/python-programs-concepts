#!C:\Python27\python.exe
import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","aswin")
if sqlcon:
    print "Connected the MySQL "
    cursor=sqlcon.cursor()
    cursor.execute("drop table if exists student")
    sql="""create  table student (name varchar(20),id varchar(20),
            totalmarks int,grade varchar(20))"""
    cursor.execute(sql)
    
    sqlcon.close()
else:
    print "Not Connected"
    
