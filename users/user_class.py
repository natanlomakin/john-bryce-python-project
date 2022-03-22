
class User(object):

    def __init__(self, user_list):
        self.__user_name = user_list[0]
        self.__user_id = user_list[1]

    def __str__(self):
        return f'user name:{self.__user_name} user id:{self.__user_id}'

    def get_user_name(self):
        """
        this function returns the value of parameter 'user name'
        of the object from user class
        :return:
        """
        return self.__user_name

    def get_user_id(self):
        """
        this function returns the value of parameter 'user id'
        of the object from user class
        :return:
        """
        return self.__user_id
