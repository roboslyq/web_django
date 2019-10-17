import pymysql

'''格式1'''
host = "47.93.201.88"  # 数据库服务器名称或IP
user = "test_user"
password = "1q2w3e4r(A"
database = "web_django"

#  格式1：只传值不传Key
conn = pymysql.connect(host, user, password, database)

# 格式2：传key
conn = pymysql.connect(host=host, user=user, password=password, database=database)

'''
游标的使用
'''
cursor_1 = conn.cursor()  # 获取游标
res = cursor_1.execute("select * from auth_user")  # 执行语句
print(cursor_1.fetchone())  # 结果是元组,fetchone()获取查询结果
