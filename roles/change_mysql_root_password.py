#!/usr/bin/python
import MySQLdb
import sys
password=sys.argv[1]
#db=MySQLdb.connect("localhost","root",password,"mysql")
db=MySQLdb.connect("localhost","root")
cursor = db.cursor()
sql="GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY '"+password+"';"
sql1="GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '"+password+"';"
cursor.execute(sql)
cursor.execute(sql1)
cursor.close()
db.close()
