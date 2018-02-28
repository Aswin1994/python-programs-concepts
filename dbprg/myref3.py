import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","ash")
if sqlcon:
    print"connected to mysql"
    cursor=sqlcon.cursor()
    sql="""insert into employee values('ravi','12tst6','30000')"""
    try:
        cursor.execute(sql)
        sqlcon.commit()
    except:
        sqlcon.rollback()
    sqlcon.close()
else:
    print"not connected"
