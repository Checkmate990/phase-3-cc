class Viewer:
    _all_usernames = set()

    def __init__(self, username):
        if not isinstance(username, str) or len(username) < 6 or len(username) > 16:
            raise Exception("Username has to be a string between 6 and 16 characters")
        if username in self.__class__._all_usernames:
            raise Exception("Username must be unique")
        self._username = username
        self._reviews = []
        self._reviewed_movie = []
        self.__class__._all_usernames.add(username)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str) or len(new_username) < 6 or len(new_username) > 16:
            raise ValueError("Username has to be a string between 6 and 16 characters")
        if new_username != self._username and new_username in self.__class__._all_usernames:
            raise ValueError("Username must be unique")
        self.__class__._all_usernames.remove(self._username)
        self.__class__._all_usernames.add(new_username)
        self._username = new_username

    @property
    def reviews(self):
        return self._reviews

    @property
    def reviewed_movies(self):
        return self._reviewed_movie

    def reviewed_movie(self, movie):
        from movie import Movie
        if not isinstance(movie, Movie):
            raise TypeError("Argument has to be an instance of the Movie class")
        return movie in self._reviewed_movie



    def rate_movie(self, movie, rating):
        from review import Review
        for review in self._reviews:
            if review.movie == movie:
                review.rating = rating
                return
        review = Review(viewer=self, movie=movie, rating=rating)
        self._reviews.append(review)
        self._reviewed_movie.append(movie)
