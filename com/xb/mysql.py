import traceback

import pymysql

try:
    db=pymysql.connect(host="192.168.0.105",user="root",password="123456",database="dev")
    cursor=db.cursor()
    cursor.execute("select * from t_consignment_commodity limit 10")
    res=cursor.fetchmany(2)
    print(res)
except:
    traceback.print_exc()
    print("error")

