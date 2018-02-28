import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","ash")
if sqlcon:
    print"connected to mysql"
    cursor=sqlcon.cursor()
    sql="select * from employee"
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            name=row[0]
            id=row[1]
            salary=row[2]
            print"%s %s %d"%(name,id,salary)
    except:
        print"unable"
    sqlcon.close()
else:
    print"Not connected"
