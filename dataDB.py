import sqlite3

con = sqlite3.connect("dataa.db")
print("Database opened successfully")

con.execute(
    "create table dataa (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, elso TEXT, masodik TEXT, szoveg TEXT NOT NULL)")

print("Table created successfully")

con.close()