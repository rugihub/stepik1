# coding: utf-8

import psycopg2 as pg2

conn = pg2.connect(database='dvdrental', user='postgres', password='db')

cur = conn.cursor()

cur.execute('CREATE DATABASE lecture')

conn.close()
"""
conn = pg2.connect(dbname = 'postgres', user='brad')
conn.set_session(autocommit = True)

cur = conn.cursor()
cur.execute('CREATE DATABASE lecture')

cur.close() # optional, closing connection always closes any associated cursors
conn.close()


conn = pg2.connect(database='lecture', user='brad')

cur = conn.cursor()

query1 = '''
        CREATE TABLE logins (
            userid integer
            , tmstmp timestamp
            , type varchar(10)
        );
        '''

cur.execute(query1)

query2 = '''
        COPY logins 
        FROM '/Users/brad/Dropbox/Galvanize/sql-python/data/lecture-example/logins01.csv' 
        DELIMITER ',' 
        CSV;
        '''

cur.execute(query2)

query3 = '''
        SELECT *
        FROM logins
        LIMIT 20;
        '''

cur.execute(query3)

cur.fetchone()

cur.fetchmany(5)

cur.fetchall()

cur.execute('SELECT Count(*) FROM logins')

cur.fetchall()


import os

query4 = '''
        COPY logins 
        FROM %(file_path)s
        DELIMITER ',' 
        CSV;
        '''

folder_path = '/Users/brad/Dropbox/Galvanize/sql-python/data/lecture-example/'

fnames = os.listdir(folder_path)

for fname in fnames:
    path = os.path.join(folder_path, fname)
    cur.execute(query4, {'file_path': path})

# ## NEVER use + or % to reformat strings to be used with .execute

num = 579
terribly_unsafe = "SELECT * FROM logins WHERE userid = " + str(num)
print(terribly_unsafe)

date_cut = "2014-08-01"
horribly_risky = "SELECT * FROM logins WHERE tmstmp > %s" % date_cut
print(horribly_risky)
## Python is happy, but if num or date_cut included something malicious
## your data could be at risk

cur.commit()

cur.close()
conn.close()
"""
