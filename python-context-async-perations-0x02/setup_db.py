import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')


cursor.execute("INSERT INTO users (name, age) VALUES ('Sara', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Youssef', 45)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Amina', 22)")

conn.commit()
conn.close()
