from dbcreate import Dbcreate


class Crud(Dbcreate):
    conn = ""

    def __init__(self):
        super().__init__("Movies")
        super().createTable()
        self.conn = super().cursor

    def insert(self,MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, MOVIE_DURATION):

        insert_query = """INSERT INTO MOVIES (MOVIE_NAME, MOVIE_YEAR, MOVIE_POSTER, MOVIE_DESCRIPTION, MOVIE_DURATION)
                       VALUES
                       ('{MOVIE_NAME}', '{MOVIE_YEAR}','{MOVIE_POSTER}', '{MOVIE_DESCRIPTION}', '{MOVIE_DURATION}');"""
        self.conn.execute(insert_query)
        self.conn.commit()
        print("Data Inserted in the table: ")


Crud().insert("hulk", "hulk", "hulk", "hulk", "hulk" )
