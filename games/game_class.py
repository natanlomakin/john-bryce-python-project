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
        return self.__name

    def get_genre(self):
        return self.__genre

    def get_publisher(self):
        return self.__publisher

    def get_developer(self):
        return self.__developer

    def get_platform(self):
        return self.__platform

    def get_price(self):
        return self.__price

    def get_realese_date_year(self):
        return self.__releaseDate_year

    def get_realese_date_month(self):
        return self.__releaseDate_month

    def get_realese_date_day(self):
        return self.__releaseDate_day

    def get_rating(self):
        return self.__rating
