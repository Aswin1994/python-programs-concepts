import MySQLdb
sqlcon=MySQLdb.connect("localhost","root","root","ash")
if sqlcon:
    print"connected to mysql"
    cursor=sqlcon.cursor()
else:
    print"Not connected"
