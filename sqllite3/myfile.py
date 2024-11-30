import sqlite3
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute( """
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,    
               name TEXT,
               age INTEGER ) """ )
data = [
    ("iqra", 2),
    ("iru", 3),
    ("ib", 4)
]

# cursor.executemany("INSERT INTO users(name,age) VALUES (?,?)",data)

# cursor.executemany("UPDATE users SET age = ? WHERE name = ?",(22,'iqra'))

connection.commit()

cursor.execute("SELECT * FROM users")
r = cursor.fetchall()
for row in r:
    print(r[0])

cursor.close()
connection.close()
