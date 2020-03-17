from setup_crawler import director_crawler_handler
from Movie import *
try:
    director = director_crawler_handler("https://www.imdb.com/name/nm3227090/")
    print(director)
    print(director.str_movies())
except Exception as e:
    print(str(e))
