import csv
import MySQLdb
data = {
    "service" : [],
    "package" : [""],
    "origin" : [] ,
    "destination" : []
}
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="hassen",         # your username
                     passwd="hassen",  # your password
                     db="csvfileproject")
cur = db.cursor()

csv_reader = csv.reader("file.txt", delimiter=',')
for row in csv_reader:
    data.get( "service").append(row[1])
    data.get("package").append(row[2])
    data.get("origin").append(row[3])
    data.get("destination").append(row[4])
    print("price is " + row[1]*row[2]*row[3]*row[4])
    sql ="INSERT INTO `data` (`service`, `package`,`origin`,`destination`) VALUES (%s, %s,%s, %s)"
    cur.execute(sql,(row[1],row[2],row[3],row[4]))

