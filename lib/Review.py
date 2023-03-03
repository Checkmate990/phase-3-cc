class Review:
    def __init__(self, viewer, movie, rating):
        from movie import Movie
        from viewer import Viewer
        if not isinstance(movie, Movie):
            raise Exception("Movie has to be an instance of the Movie class")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise Exception("Rating has to be an integer between 1 and 5")
        self._movie = movie
        self._rating = rating
        if viewer is None or isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer has to be an instance of the Viewer class")


    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise Exception("Rating has to be an integer between 1 and 5")

    @property
    def viewer(self):
        return self._viewer

    @property
    def movie(self):
        return self._movie
