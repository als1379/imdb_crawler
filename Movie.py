

class Movie:
    num_of_movies = 0

    def __init__(self, title, year, genres, rate, rate_num, actor):
        self.title = title
        self.year = year
        self.director = None
        self.actors = []
        self.genres = []
        self.genres = genres
        self.rate = rate
        self.rate_num = rate_num
        self.actors = actor
        self.id = Director.add_id()

    @classmethod
    def add_id(cls):
        m_id = cls.num_of_movies
        cls.num_of_movies += 1
        return m_id

    def add_actor(self, actor):
        actor.movies.append(self)
        self.actors.append(actor)

    def __str__(self):
        return self.title + "(" + self.year + ")" + " " + self.rate


class Director:
    num_of_directors = 0

    def __init__(self, name, photo, age, nation):
        self.name = name
        self.photo = photo
        self._movies = []
        self.age = age
        self.nation = nation
        self.id = Director.add_id()

    @classmethod
    def add_id(cls):
        d_id = cls.num_of_directors
        cls.num_of_directors += 1
        return d_id

    def add_movie(self, movie):
        movie.director = self
        self._movies.append(movie)

    def show_movies(self):
        movies = []
        for movie in self._movies:
            movies.append(movie.__str__())
        return movies

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.nation

    @property
    def movies(self):
        return self._movies
