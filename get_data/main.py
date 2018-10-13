import pymysql

# ------------database config------------------
user = ''
pwd = ''
host = 'test'
database = 'dachuang'


def query_select_all(sql_line):
    db = pymysql.connect(host, user, pwd, database, charset='utf8')
    cur = db.cursor()
    cur.execute(sql_line)
    db.close()
    return cur.fetchall()


def get_by_id(list_id):
    if type(list_id) == str and list_id is 'all':
        sql_line_nav = 'select name from nav'
    elif type(list_id) == list:
        sql_line_nav = 'select name from nav where id in ' + str(tuple(list_id))
    results = query_select_all(sql_line_nav)
    name = ''
    for i in results:
        name += '`' + i[0] + '`,'
    name = name[:-1]
    sql_line_all = 'select ' + name + 'from all_swm'
    return query_select_all(sql_line_all)

