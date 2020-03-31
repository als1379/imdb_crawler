from crawler import director_page_crawler, movie_page_crawler, top_250_crawler, best_directors_crawler
from Movie import Actor, Movie, Director
import concurrent.futures


def actor_handler(actors_name):
    for actor in Actor.actors:
        if actor.name == actors_name:
            return actor
    actor = Actor(actors_name)
    Actor.actors.append(actor)
    return actor


def movie_crawler_handler(url):
    try:
        movie_crawl_result = movie_page_crawler(url)
        for _movie in Movie.movies:
            if _movie.title == movie_crawl_result['title']:
                return _movie
        movie = Movie(movie_crawl_result['title'], movie_crawl_result['year'],
                      movie_crawl_result['genres'], movie_crawl_result['rate'],
                      movie_crawl_result['rates_num'])
        for actor in movie_crawl_result['actors']:
            movie.add_actor(actor_handler(actor))
        Movie.movies.append(movie)
        return movie
    except Exception as e:
        print(str(e))
        raise e


def director_crawler_handler(url):
    try:
        director_crawl_result = director_page_crawler(url)
        for _director in Director.directors:
            if _director.name == director_crawl_result['name']:
                return _director
        director = Director(director_crawl_result['name'], director_crawl_result['photo'],
                            director_crawl_result['age'], director_crawl_result['nation'])
        print(director)
        movie_urls = []
        for i in director_crawl_result['movies']:
            movie_urls.append("https://www.imdb.com" + i['url'])
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            movies = executor.map(movie_crawler_handler, movie_urls)
            print("crawl complete")
        for movie in movies:
            print(movie)
        Director.directors.append(director)
        return director
    except Exception as e:
        print(str(e))


def get_director_links(top_250_url, best_directors_url):
    top_250_links = get_director_links_in_top_250(top_250_url)
    best_links = get_best_directors_link(best_directors_url)
    return top_250_links + best_links


def get_director_links_in_top_250(url):
    director_links = top_250_crawler(url)
    return director_links


def get_best_directors_link(url):
    director_links = best_directors_crawler(url)
    return director_links
