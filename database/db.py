import pymysql
from pymysql.cursors import DictCursor



keys = open('database/db.txt').read().splitlines()
host     = keys[0]
user     = keys[1]
password = keys[2]
db       = keys[3]


dbh = pymysql.connect(
    host = host,
    user = user,
    password = password,
    db = db,
    charset = 'utf8mb4',
    cursorclass = DictCursor,
    autocommit  = True
)


def execute(sql):
    print(sql)
    try:
        with dbh.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            out_data = {
                'status': 'ok', 
                'data': rows
            }
    except Exception as e:
        out_data = {
            'status': 'error',
            'data': str(e)
        }

    return out_data