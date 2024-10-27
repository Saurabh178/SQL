import mysql.connector
import csv

with open('Customers.csv') as file:
    file=csv.reader(file, delimiter=',')
    next(file)                      #to skip first file which contains header
    all_value=[]

    for row in file:
        value= (row[0], row[1], row[2],row[3])
        all_value.append(value)

conn=mysql.connector.connect(host='localhost', username='root', password='178@SAurabh', database='Practice')
my_cursor=conn.cursor()

query_read='select * from `customer`'
query_insert='''insert into `insurance`  (`idx`, `PatientID`, `age`, `gender`, `bmi`, `bloodpressure`, 
                `diabetic`, `children`, `smoker`, `region`, `claim`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''


#my_cursor.execute(query_read)
my_cursor.executemany(query_insert, all_value)
res=my_cursor.fetchall()

conn.commit()
conn.close()
