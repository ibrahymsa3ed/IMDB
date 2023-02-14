from example import MoviesDb


class moviesCrud(MoviesDb):
    def __init__(self):
        super().__init__("movies.db")
        super().createTable()
        self.conn = super().conn


moviesCrud()