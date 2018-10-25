import pymysql
import numpy
# ------------database config------------------
user = 'dc_user'
pwd = '!($(!))!'
host = '106.14.9.14'
database = 'dachuang'
nav_table = 'data'
data_table = 'data44'


def query_select_all(sql_line):
    db = pymysql.connect(host, user, pwd, database, charset='utf8')
    cur = db.cursor()
    cur.execute(sql_line)
    db.close()
    return cur.fetchall()


def get_by_id(list_id):
    if type(list_id) == str and list_id is 'all':
        sql_line_nav = 'select name from ' + nav_table
    elif type(list_id) == list:
        sql_line_nav = 'select name from ' + nav_table + ' where id in (' + str(list_id)[1:-1] + ')'
    results = query_select_all(sql_line_nav)
    name = ''
    for i in results:
        name += '`' + i[0] + '`,'
    name = name[:-1]
    sql_line_all = 'select ' + name + 'from ' + data_table
    # print(sql_line_all)
    return numpy.array(query_select_all(sql_line_all))

print(get_by_id([1,2,3,4]))
