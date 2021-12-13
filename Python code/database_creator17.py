# Створення тестової БД

import sqlite3


conn = sqlite3.connect("project17.db")
curs = conn.cursor()
curs.execute("""CREATE TABLE books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
authors TEXT,
place TEXT,
genres TEXT,
types TEXT,
year INTEGER)""")
curs.execute("""CREATE TABLE authors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT)""")
curs.execute("""CREATE TABLE genres(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT)""")
curs.execute("""CREATE TABLE places(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT)""")
curs.execute("""CREATE TABLE types(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT)""")
conn.commit()
for i in range(1, 6):
    curs.execute("""INSERT INTO books(name, authors, place, genres, types, year) VALUES(?, ?, ?, ?, ?, ?)""",
                 (f"name{i}", f"author{1+i//2},author{2+i//2},", f"place{1 + i//3}", f"genre{1+i//3},genre{2+i//3}",
                  f"type{i}", 2000+i))
    curs.execute("""INSERT INTO authors(name) VALUES(?)""", (f"author{i}",))
    curs.execute("""INSERT INTO genres(name) VALUES(?)""", (f"genre{i}",))
    curs.execute("""INSERT INTO types(name) VALUES(?)""", (f"type{i}",))
    curs.execute("""INSERT INTO places(name) VALUES(?)""", (f"place{i}",))
conn.commit()
