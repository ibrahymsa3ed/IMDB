from crud import Crud
from api import Api
movie_name = "hulk"
movie_year = "2008"
movie = Api().imdb_movie(f"%{movie_name}%", f"%{movie_year}%")



#Crud().update(f'{movie_name}', movie[0], movie[1], movie[2], movie[3], movie[4])
Crud().select(f'{movie_name}', f'{movie_year}')