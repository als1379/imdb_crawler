from Movie import Movie, Director
from crawler import *
try:
    result = director_page_crawler("https://www.imdb.com/name/nm3227090/")
    director = Director(result['name'], result['photo'], result['age'], result['nation'])
    print(director)
    for i in result['movies']:
        try:
            url = "https://www.imdb.com" + i['url']
            m_result = movie_page_crawler(url)
            if m_result == {}:
                continue
            movie = Movie(m_result['title'], m_result['year'],
                          m_result['genres'], m_result['rate'],
                          m_result['rates_num'], m_result['actors'])
            director.add_movie(movie)
            print(movie)
            print(movie.actors)
        except Exception as e:
            print(str(e))
    print(director.show_movies())
    print(director.movies[1].actors)
except Exception as e:
    print(str(e))

