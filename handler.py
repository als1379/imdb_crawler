import save_and_load_to_db
import setup_crawler


def update_directors_link():
    directors_links = setup_crawler.get_director_links("https://www.imdb.com/chart/top/", "https://www.imdb.com/list/ls064396556/")
    save_and_load_to_db.save_directors_links(directors_links)


def start():
    links = save_and_load_to_db.load_directors_links()
