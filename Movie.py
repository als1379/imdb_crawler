class Actor:
    actors = []

    def __init__(self, name):
        self.name = name
        self.movies = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


class Movie:
    movies = []

    def __init__(self, title, year, genres, rate, rate_num):
        self.title = title
        self.year = year
        self.director = None
        self.actors = []
        self.genres = []
        self.genres = genres
        self.rate = rate
        self.rate_num = rate_num

    def add_actor(self, actor):
        self.actors.append(actor)
        actor.movies.append(self.__str__())

    def __str__(self):
        return self.title + "(" + self.year + ")" + " " + self.rate

    def __repr__(self):
        return self.title + "(" + self.year + ")" + " " + self.rate

    def show_actors(self):
        actors_ = []
        for actor in self.actors:
            actors_.append(actor.name)
        return actors_


class Director:
    directors = []

    def __init__(self, name, photo, age, nation):
        self.name = name
        self.photo = photo
        self._movies = []
        self.age = age
        self.nation = nation

    def add_movie(self, movie):
        movie.director = self
        self._movies.append(movie)

    def str_movies(self):
        movies = []
        for movie in self._movies:
            movies.append(movie.__str__())
        return movies

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.nation

    def __repr__(self):
        return self.name + " " + str(self.age) + " " + self.nation

    @property
    def movies(self):
        return self._movies
