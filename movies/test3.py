import sqlite3
conn = sqlite3.connect('imdb.db')
cursor = conn.cursor()
print("Opened database successfully")
table = """CREATE TABLE IF NOT EXISTS MOVIES
         (
         
         MOVIE_NAME           TEXT    NOT NULL,
         MOVIE_YEAR            TEXT     NOT NULL,
         MOVIE_POSTER           TEXT    NOT NULL,
         MOVIE_DESCRIPTION            TEXT     NOT NULL,
         MOVIE_DURATION            TEXT     NOT NULL
         );"""
cursor.execute(table)

print("Table created successfully")
conn.execute('''INSERT INTO MOVIES (MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, 
        MOVIE_DURATION) VALUES ('hulk', 'hulk', 'hulk', 'hulk', 'hulk')''')
conn.execute('''INSERT INTO MOVIES (MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, 
        MOVIE_DURATION) VALUES ('hulk2', 'hulk2', 'hulk2', 'hulk2', 'hulk2')''')
conn.execute('''INSERT INTO MOVIES (MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, 
        MOVIE_DURATION) VALUES ('hulk3', 'hulk3', 'hulk3', 'hulk3', 'hulk3')''')
print("Data Inserted in the table: ")
conn.commit()
conn.close()