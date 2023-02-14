import json
from pprint import pprint
import requests


class Api:
    MOVIE_NAME = "hulk"
    MOVIE_YEAR = "2008"
    url = f"https://www.omdbapi.com/?t={MOVIE_NAME}&y={MOVIE_YEAR}&apikey=1d7b9f59"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.text
    response_dict = json.loads(response_json)
    poster = response_dict['Poster']
    correct_name = response_dict['Title']
    correct_year = response_dict['Year']
    description = response_dict['Plot']
    duration = response_dict['Runtime']

    def __init__(self, poster, correct_name, correct_year, description, duration):
        self.poster = poster
        self.correct_name = correct_name
        self.correct_year = correct_year
        self.description = description
        self.duration = duration
        print(poster)


Api("poster", "correct_name", "correct_year", "description", "duration")


