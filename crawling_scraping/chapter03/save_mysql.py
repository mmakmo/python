import MySQLdb


conn = MySQLdb.connect(host='127.0.0.1', db='scraping', user='user', passwd='pass', charset='utf8mb4')

c = conn.cursor()

c.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
''')

c.execute('INSERT INTO cities VALUES(%s, %s, %s)', (1, '上海', 24150000))

c.execute('INSERT INTO cities VALUES(%(rank)s, %(city)s, %(population)s)', {'rank': 2, 'city': 'カラチ', 'population': 2350000})

c.executemany('INSERT INTO cities VALUES(%(rank)s, %(city)s, %(population)s)', [
    {'rank': 3, 'city': '北京', 'population': 21516000},
    {'rank': 4, 'city': '天津', 'population': 14722100},
    {'rank': 5, 'city': 'イスタンブル', 'population': 14160467},
])

conn.commit()

c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

conn.close()
