import pymysql
import re
from pymysql.converters import escape_string

# Modify:修改数据库配置
conn = pymysql.connect(
    host='localhost',
    user='loganchen',
    password='8023ghoul',
    db='dev',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

# Modify:修改此处文件路径为导出的聊天记录txt文件路径
with open(r"C:\Users\ChenYonghong\Desktop\backup\CYH\秤砣妈妈.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.*\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        # Modify:修改两个名称为你们各自的昵称
        if (line.startswith('秤砣妈妈') or line.startswith('CYH')) and re.match(reg, line):
            filter_lines.append(line.strip())

for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{escape_string(content)}')"
    cur.execute(insert_sql)
conn.commit()
