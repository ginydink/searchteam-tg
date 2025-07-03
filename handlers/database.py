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

cursor.execute('''
    CREATE  TABLE IF NOT EXISTS team( 
    id INTEGER PRIMARY KEY,
    team TEXT,
    mid_age INTEGER,
    description TEXT,
    usernam,TEXT
)
''')
conn.commit()
def add_team (user_id,team,mid_age,description,usernam):
    cursor.execute('''
        INSERT INTO team (id,team,mid_age,description,usernam)
        VALUES(?,?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET
            team  = excluded.team,
            mid_age = excluded.mid_age,
            description = excluded.description,
            usernam = excluded.usernam
        ''',(user_id,team,mid_age,description,usernam))
    conn.commit()
def get_team ():
    b = cursor.execute('''
        SELECT team,description,mid_age,usernam FROM team
    ''')
    return b.fetchall()

