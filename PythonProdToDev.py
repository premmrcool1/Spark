import pyodbc
import csv


SourceConn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLExpress;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

SourceCursor = SourceConn.cursor()
SourceCursor.execute('SELECT  * FROM dbo.samp')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLExpress;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

x=len(SourceCursor.description)
for row in SourceCursor:
        print(row[1])
        s1 = ''
        i = 0;
        while i < x:
            if i == x - 1:
                s1 = s1 + '?'
            else:
                s1 = s1 + '?,'
            i = i + 1
        print(s1)
        t1 = 'dbo.samp'
        stmt = 'insert into ' + t1 + ' values( ' + s1 + ')'
        print(row)
        print(stmt)
        cursor.execute(stmt, row)
