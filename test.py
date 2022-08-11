import pymysql

db = pymysql.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    charset= 'utf8',
    db = "inspirational"
)
cursor = db.cursor()

sql = '''CREATE TABLE test ( 
id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
email varchar(255), 
department varchar(255) 
) 
''' 

# cursor.execute(sql)

sql = '''insert into test
 (email, department)
values
("lm@am.com", "beuty");
'''

cursor.execute(sql)
db.commit()

db.close()