import json
from pprint import pprint
import requests


class Test5:

    def imdb_movie(self, movie_name, movie_year):
        MOVIE_NAME = movie_name
        MOVIE_YEAR = movie_year
        url = f"https://www.omdbapi.com/?t={MOVIE_NAME}&y={MOVIE_YEAR}&apikey=1d7b9f59"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.text
        response_dict = json.loads(response_json)
        print(response_dict)
        poster = response_dict['Poster']
        correct_name = response_dict['Title']
        correct_year = response_dict['Year']
        description = response_dict['Plot']
        duration = response_dict['Runtime']
        return correct_name, correct_year, poster, description, duration





