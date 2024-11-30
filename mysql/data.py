import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="sqlpassword@123",
    database="mydatabase"
)

cursor = db.cursor()

# cursor.execute("CREATE TABLE customers (name VARCHAR(30), address VARCHAR(100))")
# cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO INCREMENT PRIMARY KEY")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
 ('harry', 'treet 4'),
 ('Amy', ' st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('iqra', 'Green Grass 1'),
 ('ira', 'Sky st 331'),
 ('qamar', 'One way 98'),
 ('Vicky', 'Yellow Garden 2')
]
cursor.executemany(sql,val)
db.commit()



# cursor.execute("SHOW TABLES")
# for x in cursor:
#     print(x)
