import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","ash")
if sqlcon:
    print "connected to my sql"
    cursor=sqlcon.cursor()
    cursor.execute("drop table if exists employee")
    sql="""create table employee(name varchar(20),id varchar(20),salary int)"""
    cursor.execute(sql)
    sqlcon.close()
else:
    print "not connected"
