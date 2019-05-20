import pymysql
import pandas as pd
import matplotlib.pyplot as plt
# 连接数据库
con = pymysql.connect(host='localhost',
                      user='root',
                      password='cjm2hef',
                      db='transformer',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)
print("数据库连接成功")
with con:
    cur = con.cursor()
    # 利用select distinct 语句返回所有唯一不同的GISID，保存在列表中
    cur.execute("select distinct(GISID) from data")
    gisid_list = cur.fetchall()
    print(gisid_list)
    i = 0
    for row in gisid_list:
        cur.execute("select * from data where GISID=%s" % row['GISID'])
        data=cur.fetchall()
        df = pd.DataFrame(data)
        df.plot(x='DATADATE',y='YGFZL')
        plt.savefig('pic_save//%s.png'% row['GISID'])
        plt.close('all')#解决图片打开过多导致内存溢出程序中断
        i+=1
        print(i)
