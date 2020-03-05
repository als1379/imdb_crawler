from Movie import Movie, Actor, Director
import requests
from bs4 import BeautifulSoup
import datetime


def director_page_crawler(url):
    director = {}
    r = requests.get(url)
    print(r.url)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        #       director's photo
        image = soup.find(id='name-poster')
        director['photo'] = image['src']

        #      director's name
        name = soup.find(class_='itemprop')
        director['name'] = name.text

        #      director's age
        age = soup.find(id="name-born-info")
        director['age'] = int(datetime.datetime.now().year) - int(str(age.find_all('a')[1].text))

        #      director's nation
        nation = soup.find(id="name-born-info")
        director['nation'] = nation.find_all('a')[2].text.split(',')[-1].strip()

        #      director movies
        movies_div = soup.find(id="filmo-head-director")
        movies_div = movies_div.fetchNextSiblings()
        movies_links = movies_div[0].find_all('a')
    except Exception:
        raise Exception('This page is not director page')
    movies = []
    for i in movies_links:
        if 'class' in str(i) or 'TV Series' in str(i):
            continue
        movie_url = i['href']
        movie_name = i.text
        movie = {'name': movie_name, 'url': movie_url}
        movies.append(movie)
    director['movies'] = movies

    return director


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
