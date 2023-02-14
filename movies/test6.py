from dbcreate import Dbcreate


class Crud(Dbcreate):

    def __init__(self):
        super().__init__("IMDB.db")
        super().createTable()
        self.con = super().cursor

    def insert(self, MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, MOVIE_DURATION):
        super().connection().execute(f'''INSERT INTO MOVIES (MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, 
        MOVIE_DURATION) VALUES ('{MOVIE_NAME}',{MOVIE_YEAR}, '{MOVIE_POSTER}', '{MOVIE_DESCRIPTION}', '{MOVIE_DURATION}')''')
        super().connection().commit()
        print("data inserted")
        super().connection().close()

    def select(self, MOVIE_NAME, MOVIE_YEAR):
        movies = super().connection().execute(
            f'''SELECT * FROM MOVIES WHERE MOVIE_NAME LIKE '%{MOVIE_NAME}%' AND MOVIE_YEAR LIKE '%{MOVIE_YEAR}%' ''')

        for movie in movies:
            print(movie)



    def delete(self, MOVIE_NAME):
        super().connection().execute(f'''DELETE FROM MOVIES WHERE MOVIE_NAME='{MOVIE_NAME}' ''')
        super().connection().commit()
        print("deleted")

    def update(self, MOVIE_NAME, MOVIE_NAME_UPDATE, MOVIE_YEAR_UPDATE, MOVIE_POSTER_UPDATE, MOVIE_DESCRIPTION_UPDATE,
               MOVIE_DURATION_UPDATE):
        super().connection().execute(
            f'''UPDATE MOVIES SET MOVIE_NAME='{MOVIE_NAME_UPDATE}', MOVIE_YEAR='{MOVIE_YEAR_UPDATE}',MOVIE_POSTER='{MOVIE_POSTER_UPDATE}',MOVIE_DESCRIPTION='{MOVIE_DESCRIPTION_UPDATE}',MOVIE_DURATION='{MOVIE_DURATION_UPDATE}' WHERE MOVIE_NAME LIKE '%{MOVIE_NAME}%' ''')
        super().connection().commit()
        print("Total number of rows updated :", super().connection().total_changes)
#Crud().insert('inception', '2008', 'URL', 'ACTION', '1:45')
#Crud().insert('hulk', '2010', 'URL', 'ACTION', '1:45')
#Crud().select('Hulk', 2008)
#Crud().delete('hulk')
# Crud().update('incep', 'Inception', 'June 2008', 'url.png', 'Adventure', '118')
