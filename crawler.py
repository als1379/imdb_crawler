import requests
from bs4 import BeautifulSoup
import datetime
from functools import wraps


def crawler_decorator(crawler):
    @wraps(crawler)
    def wrapper(url, *args, **kwargs):
        print(crawler.__name__, "start crawl in", url)
        return crawler(url, *args, **kwargs)

    return wrapper


@crawler_decorator
def director_page_crawler(url):
    director = {}
    r = requests.get(url)
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

        movies = []
        for i in movies_links:
            if 'class' in str(i) or 'TV Series' in str(i):
                continue
            movie_url = i['href']
            movie_name = i.text
            movie = {'name': movie_name, 'url': movie_url}
            movies.append(movie)
        director['movies'] = movies

    except Exception:
        raise Exception('This page is not director page')

    return director


@crawler_decorator
def movie_page_crawler(url):
    movie = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        #      movie's title and year
        title = soup.find(id="ratingWidget")

        movie['title'] = title.find('p').text.split('\n')[2].strip()

        year = title.find('p').text.split('\n')[3].strip()
        year = year[1:-1]
        numeric_year = int(year)

        movie['year'] = year

        #      movie rate and num of user ratings
        rate = soup.find(class_="ratingValue")
        rate_ = rate.find('strong')['title'].split('based on')[0].strip()
        num_of_rating = rate.find('strong')['title'].split('based on')[1].split('user rating')[0].strip().split(',')
        num_of_rating_ = "".join(num_of_rating)

        movie['rate'] = rate_

        movie['rates_num'] = num_of_rating_

        #      rates num filter
        if int(movie['rates_num']) < 10000:
            return {}

        #       movie's poster
        poster = soup.find(class_="poster")

        movie['poster'] = poster.find_all('img')[0]['src']

        #      movie's genres
        genres = soup.find(class_="title_block")
        genres = genres.find(class_="subtext")
        genres = genres.find_all('a')
        genres_list = []
        for i in range(len(genres) - 1):
            genres_list.append(genres[i].text)

        movie['genres'] = genres_list

        #   short movie filter
        if 'Short' in genres_list:
            return {}

        #     actors
        actors = soup.find(class_="cast_list")
        actors = actors.find_all(class_="primary_photo")
        actors_list = []
        for actor in actors:
            actor_ = actor.fetchNextSiblings()
            actor_ = actor_[0].find_all('a')[0].text
            actors_list.append(str(actor_).strip())

        movie['actors'] = actors_list

    except Exception as e:
        raise Exception("this is not movie url")
    return movie


