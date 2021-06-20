# https://docs.python.org/3/library/sqlite3.html

import sqlite3

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()

res = cur.execute("SELECT * FROM users")

for row in res:
    print(row)


res = cur.execute("SELECT * FROM users").fetchone()
print(res)


username = "user1"
res = cur.execute("SELECT * FROM users WHERE username = '%s'" % username)  # sql injection

# qmark style  (q: question)
res = cur.execute("select * from users where username = ? ", ("user1",))

# qmark style with executemany
users = [
    ("user4",'pass4'),
    ("user5",'pass5')
]

#res = cur.executemany("Insert into users values (?, ?) ", users)

# name style
cur.execute("select * from users where username=:key", {"key": "user3"})
print(cur.fetchall())




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn.row_factory = dict_factory
cur = conn.cursor()
res = cur.execute("SELECT * FROM users").fetchone()
print(res, type(res))



conn.commit() # save change
conn.close()



