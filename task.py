# 0- class to create sqlite db and table for movies
# 1- class to inherit from 1 and have the 4 CRUD functions (movie name, movie year)
# 2- script or class to insert few movies to the table in the db
# 3- class to communicate with the movies api and return (poster, correct name,correct year,  description, duration)
# 4- from class 3 a script to update the movie record in the db with the data returned

# result

# print(find_movie(movie_name, movie_year))
"""
Movie Name:
Movie Year:
Movie Poster url:
Movie description:
Movie Duration: XHours and X mins



"""
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """CREATE TABLE MOVIES
         (ID INT PRIMARY KEY     NOT NULL,
         MOVIE_NAME           TEXT    NOT NULL,
         MOVIE_YEAR            TEXT     NOT NULL,
         MOVIE_POSTER           TEXT    NOT NULL,
         MOVIE_DESCRIPTION            TEXT     NOT NULL,
         MOVIE_DURATION            TEXT     NOT NULL
         );"""

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
