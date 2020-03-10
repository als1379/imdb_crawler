from Movie import Movie, Director
from crawler import Crawler
try:
    print("hello")
    crawler = Crawler("https://www.imdb.com/name/nm0000233/")
    result = crawler.director_page_crawler()
    director = Director(result['name'], result['photo'], result['age'], result['nation'])
    print(director)
    for i in result['movies']:
        try:
            url = "https://www.imdb.com" + i['url']
            crawler.url = url
            m_result = crawler.movie_page_crawler()
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
    director.show_movies()
except Exception as e:
    print(str(e))

