from review import Review

class Movie:
    _all_movies = []

    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = title
        self._reviews = []
        self.__class__._all_movies.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or len(new_title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = new_title

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        reviews_list = []
        for review in reviews:
            if isinstance(review, int):
                review = Review(viewer=None, movie=self, rating=review)
            elif not isinstance(review, Review):
                raise TypeError("Reviews must be instances of the Review class")
            reviews_list.append(review)
        self._reviews = reviews_list


    @property
    def reviewers(self):
        return list(set([review.viewer for review in self._reviews]))

    def average_rating(self):
        if len(self._reviews) == 0:
            return 0
        total = sum([review.rating for review in self._reviews])
        return total / len(self._reviews)

    @classmethod
    def highest_rated(cls):
        if len(cls._all_movies) == 0:
            return None
        return max(cls._all_movies, key=lambda movie: movie.average_rating())
