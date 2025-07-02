import random
import sqlite3
from idlelib.colorizer import prog_group_name_to_tag

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE  TABLE IF NOT EXISTS users( 
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    elo INTEGER,
    username,TEXT
)
''')
conn.commit()
def add_user (user_id,name,age,elo,username):
    cursor.execute('''
        INSERT INTO users (id,name,age,elo,username)
        VALUES(?,?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET
            name  = excluded.name,
            age = excluded.age,
            elo = excluded.elo,
            username = excluded.username
        ''',(user_id,name,age,elo,username))
    conn.commit()
def get_name ():
    t = cursor.execute('''
        SELECT name,elo,age,username FROM users
    ''')
    return t.fetchall()

