#!C:\Python27\python.exe
import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","aswin")
if sqlcon:
    print "Connected the MySQL "
    cursor=sqlcon.cursor()
    cursor.execute("select version()")
    data=cursor.fetchone()
    print "database version:%s" %data
    sqlcon.close()
else:
    print "Not Connected"
    
