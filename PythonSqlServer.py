import pyodbc
import csv

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLExpress;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor.execute('SELECT TOP (1000) * FROM dbo.samp')

#for row in cursor:
 #   print(row)
with open('C:\\Users\\pnagaraja3\\Desktop\\Learning\\samp.csv') as csv1:
    first_line = csv1.readline()
    ncol = first_line.count(',') + 1
    print(ncol)
    csv1.close()
with open('C:\\Users\\pnagaraja3\\Desktop\\Learning\\samp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            s1=''
            i =0;
            while i < ncol:
             if i == ncol -1:
                 s1=s1+'?'
             else:
                s1=s1+'?,'
             i = i + 1
            print(s1)
            t1='dbo.samp'
            stmt='insert into ' + t1 + ' values( ' + s1 +')'
            print(row[0],row[1])
            cursor.execute(stmt,row[0],row[1])
            line_count += 1
            conn.commit()
    print(f'Processed {line_count} lines.')