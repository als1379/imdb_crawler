

class Movie:
    num_of_movies = 0

    def __init__(self, title, year, genres, rate):
        self.title = title
        self.year = year
        self.director = None
        self.actors = []
        self.genres = genres
        self.rate = rate
        self.actors = []
        self.id = self.num_of_movies
        self.num_of_movies += 1

    def add_actor(self, actor):
        actor.movies.append(self)
        self.actors.append(actor)


class Director:
    num_of_directors = 0

    def __init__(self, name, photo, age, nation):
        self.name = name
        self.photo = photo
        self.movies = []
        self.age = age
        self.nation = nation
        self.id = self.num_of_directors
        self.num_of_directors += 1

    def add_movie(self, movie):
        movie.director = self
        self.movies.append(movie)


class Actor:
    num_of_actors = 0

    def __init__(self, name, age, nation):
        self.name = name
        self.movies = []
        self.age = age
        self.nation = nation
        self.id = self.num_of_actors
        self.num_of_actors += 1