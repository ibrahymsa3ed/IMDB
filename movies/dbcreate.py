import sqlite3


class Dbcreate:
    conn = ""
    cursor = ""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print("Opened database successfully")

    def createTable(self):
        table = """CREATE TABLE IF NOT EXISTS MOVIES
         (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         MOVIE_NAME           TEXT    NOT NULL,
         MOVIE_YEAR            TEXT     NOT NULL,
         MOVIE_POSTER           TEXT    NOT NULL,
         MOVIE_DESCRIPTION            TEXT     NOT NULL,
         MOVIE_DURATION            FLOAT     NOT NULL
         );"""
        self.cursor.execute(table)
        self.conn.commit()
        print("Table created successfully")

    def connection(self):
        return self.conn

    def cursorr(self):
        return self.cursor




