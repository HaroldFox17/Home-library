# Клас для роботи з БД

import sqlite3


class DBHandler:  # Клас для роботи з БД
    def __init__(self):
        self.db = "project17.db"

    def add_edition(self, name, author, typ, genre, place, year):  # Додати видання
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO books(name, authors, place, genres, types, year) VALUES(?, ?, ?, ?, ?, ?)""",
                     (name, author, place, genre, typ, year))
        conn.commit()
        conn.close()

    def delete_edition(self, ide):  # Видалити видання
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""DELETE FROM books WHERE id=?""", (ide,))
        conn.commit()
        conn.close()

    def redact_edition(self, ide, name, author, typ, genre, place, year):  # Редагувати видання
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""UPDATE books SET name=?, authors=?, place=?, genres=?, types=?, year=? WHERE id=?""",
                     (name, author, place, genre, typ, year, ide))
        conn.commit()
        conn.close()

    def add_author(self, name):  # Додати автора
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO authors(name) VALUES(?)""", (name,))
        conn.commit()
        conn.close()

    def delete_author(self, ida):  # Видалити автора
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""DELETE FROM authors WHERE id=?""", (ida,))
        conn.commit()
        conn.close()

    def redact_author(self, ida, name):  # Редагувати автора
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""UPDATE authors SET name=? WHERE id=?""",
                     (name, ida))
        conn.commit()
        conn.close()

    def add_type(self, name):  # Додати вид
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO types(name) VALUES(?)""", (name,))
        conn.commit()
        conn.close()

    def delete_type(self, idt):  # Видалити вид
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""DELETE FROM types WHERE id=?""", (idt,))
        conn.commit()
        conn.close()

    def redact_type(self, ida, name):  # Редагувати вид
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""UPDATE types SET name=? WHERE id=?""",
                     (name, ida))
        conn.commit()
        conn.close()

    def add_genre(self, name):  # Додати жанр
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO genres(name) VALUES(?)""", (name,))
        conn.commit()
        conn.close()

    def delete_genre(self, idt):  # Видалити жанр
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""DELETE FROM genres WHERE id=?""", (idt,))
        conn.commit()
        conn.close()

    def redact_genre(self, ida, name):  # Редагувати жанр
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""UPDATE genres SET name=? WHERE id=?""",
                     (name, ida))
        conn.commit()
        conn.close()

    def add_place(self, name):  # Додати місце
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO places(name) VALUES(?)""", (name,))
        conn.commit()
        conn.close()

    def delete_place(self, idt):  # Видалити місце
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""DELETE FROM places WHERE id=?""", (idt,))
        conn.commit()
        conn.close()

    def redact_place(self, ida, name):  # Редагувати місце
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""UPDATE places SET name=? WHERE id=?""",
                     (name, ida))
        conn.commit()
        conn.close()

    def search(self, name="", genre="", author="", typ="") -> str:  # Пошук
        s = ""
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM books""")
        res = curs.fetchall()
        l = res
        if name != "":
            k = [i for i in l]
            for i in k:
                if name.lower() not in i[1].lower():
                    l.remove(i)
        if genre != "":
            k = [i for i in l]
            for i in k:
                if genre.lower() not in i[4].lower():
                    l.remove(i)
        if author != "":
            k = [i for i in l]
            for i in k:
                if author.lower() not in i[2].lower():
                    l.remove(i)
        if typ != "":
            k = [i for i in l]
            for i in k:
                if typ.lower() not in i[5].lower():
                    l.remove(i)
        for i in l:
            j = [str(k) for k in i]
            s += "/".join(j)+"\n\n\n"
        conn.close()
        return s
