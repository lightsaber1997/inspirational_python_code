import pandas as pd
import pymysql

# read excel file
excel_data = pd.read_excel("adm_code.xls", sheet_name=0)

# connect to mysql
db = pymysql.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    charset= 'utf8',
    db = "inspirational"
)
cursor = db.cursor()


row_index = 1

for row in excel_data[1:].itertuples():
    si = row[2]
    gu = row[4]
    dong = row[6]

    sql = '''insert into korea_sigudong
    (si, gu, dong)
    values
    '''

    sql += f'("{si}", "{gu}", "{dong}")'
    #print(sql)
    cursor.execute(sql)



    row_index += 1
    if row_index > 10:
        pass
        # break








db.commit()

db.close()