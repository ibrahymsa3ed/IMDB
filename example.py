import sqlite3

conn = ""


class MoviesDb:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def createTable(self):
        self.conn.execute('''CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 AGE            INT     NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL);''')
