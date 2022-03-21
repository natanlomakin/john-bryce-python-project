
class User(object):

    def __init__(self, user_list):
        self.__user_name = user_list[0]
        self.__user_id = user_list[1]

    def __str__(self):
        return f'user name:{self.__user_name} user id:{self.__user_id}'

    def get_user_name(self):
        return self.__user_name

    def get_user_id(self):
        return self.__user_id
