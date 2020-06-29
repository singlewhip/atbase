# -*- coding: utf-8 -*-
# @Time     : 2020/6/29 22:10
# @Author   : lc
import MySQLdb

conn = MySQLdb.Connect(host='47.103.53.14', port=int(3306), user='root', passwd='123456')
db = 'atbase'
cur = conn.cursor()
if not cur.execute("SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME='" + db + "'"):
    sql_create_db = "create database " + db + " DEFAULT CHARSET utf8 COLLATE utf8_general_ci"
    cur.execute(sql_create_db)
cur.close()