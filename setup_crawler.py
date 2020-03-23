from crawler import director_page_crawler, movie_page_crawler, top_250_crawler
from Movie import Actor, Movie, Director


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
        for i in director_crawl_result['movies']:
            movie_url = "https://www.imdb.com" + i['url']
            try:
                director.add_movie(movie_crawler_handler(movie_url))
                print("crawl complete")
            except Exception as e:
                print(str(e))
        Director.directors.append(director)
        return director
    except Exception as e:
        print(str(e))


def top_250_crawler_handler(url):
    try:
        director_links = top_250_crawler(url)
        print(director_links)
        for link in director_links:
            print(link)
            director = director_crawler_handler(link)
            print(director, "complete")
    except Exception as e:
        print(str(e))