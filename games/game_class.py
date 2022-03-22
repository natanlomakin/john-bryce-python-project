class Game(object):

    def __init__(self, game_list):
        self.__name = game_list[0]
        self.__genre = game_list[1]
        self.__publisher = game_list[2]
        self.__developer = game_list[3]
        self.__platform = game_list[4]
        self.__price = game_list[5]
        self.__releaseDate_year = game_list[6][6:]
        self.__releaseDate_month = game_list[6][3:5]
        self.__releaseDate_day = game_list[6][0:2]
        self.__rating = game_list[7]

    def __len__(self):
        return len(self)

    def __str__(self):
        return f'{self.__name},{self.__genre},{self.__publisher},{self.__developer},{self.__platform},{self.__price},{self.__releaseDate_day}.{self.__releaseDate_month}.{self.__releaseDate_year},{self.__rating}'

    def get_name(self):
        """
        this function returns the value of parameter 'name'
        of the object from game class
        :return:
        """
        return self.__name

    def get_genre(self):
        """
        this function returns the value of parameter 'genre'
        of the object from game class
        :return:
        """
        return self.__genre

    def get_publisher(self):
        """
        this function returns the value of parameter 'publisher'
        of the object from game class
        :return:
        """
        return self.__publisher

    def get_developer(self):
        """
        this function returns the value of parameter 'developer'
        of the object from game class
        :return:
        """
        return self.__developer

    def get_platform(self):
        """
        this function returns the value of parameter 'platform'
        of the object from game class
        :return:
        """
        return self.__platform

    def get_price(self):
        """
        this function returns the value of parameter 'price'
        of the object from game class
        :return:
        """
        return self.__price

    def get_release_date_year(self):
        """
        this function returns the value of parameter 'release date year'
        of the object from game class
        :return:
        """
        return self.__releaseDate_year

    def get_release_date_month(self):
        """
        this function returns the value of parameter 'release date month'
        of the object from game class
        :return:
        """
        return self.__releaseDate_month

    def get_release_date_day(self):
        """
        this function returns the value of parameter 'release date day'
        of the object from game class
        :return:
        """
        return self.__releaseDate_day

    def get_rating(self):
        """
        this function returns the value of parameter 'rating'
        of the object from game class
        :return:
        """
        return self.__rating
