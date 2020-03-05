from Movie import Movie, Actor, Director
from crawler import director_page_crawler


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


try:
    result = director_page_crawler("https://www.imdb.com/name/nm0634240/")
    pretty(result)
except Exception as e:
    print(str(e))
