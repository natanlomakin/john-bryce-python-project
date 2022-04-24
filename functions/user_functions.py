import os
from users import user_class


def file(file_name):
    """
    this function gets the name of the file you want to open and
    than return a list of row number X to the 'Game' module in order
    to create a new objective
    :param file_name: name of the file to open
    :return: list of row number X
    """

    users_info_list = []
    users_file = open(file_name)
    all = users_file.readlines()
    for i in range(1, len(all)):
        users_info_list.append(user_class.User(all[i].split(',')))
    users_file.close()
    return users_info_list

def generate_file_by_user(users_list ,user_name ,user_id ,game_name_list):
    """
    this function gets a list of existing users, a user name and id
    to create a new library for the given user name and id and adds
    the games given.
    the function checks if there is an existing library for the given
    user name, if it already exists an error message will be printed
    if it doesnt exist a new user library file will be created.
    :param users_list: list of existing users
    :param user_name: user name to create a library file for
    :param user_id: user id to create a library file for
    :param game_name_list: list of games to add to the users library file
    :return: create a new user library file if not existing or
             print an error message if exists
    """

    destination = os.getcwd() + f'\\user_librarys\\{user_name}.txt'
    user_exist = False
    if os.path.exists(destination):
        print('this user already has library')
    else:
        for i in range(len(users_list)):
            if users_list[i].get_user_name() == user_name:
                user_exist = True
        if user_exist:
            file1 = open(f'{user_name}.txt', 'w')
            file1.write(f'{user_name}')
            file1.write(',')
            file1.write(f'{user_id}\n')
            for i in game_name_list:
                file1.write(f'{i}\n')
            file1.close()
        else:
            print('the user name given is not in the users file\nplease add the user to the users file first')
#                else:
#                    print('the user name given is not in the users file\nplease add the user to the users file first')



def add_game_to_existing_file(user_name ,game_name):
    """
    this function gets a user name and checks if a library for him exists,
    if exists it will add the games that were given,
    if the user doesnt have a library it will print an error message.
    :param user_name: users name
    :param game_name: list of games to add
    :return: adds the games to the user library
    """

    path = os.getcwd() + f'\\user_librarys\\{user_name}.txt'
    if os.path.exists(path):
        existing_file = open(os.getcwd() + f'\\user_librarys\\{user_name}.txt', 'a')
        for i in game_name:
            existing_file.write(f'{i}\n')
        existing_file.close()
    else:
        print('the user name given has no existing library\n')

def add_new_user_to_users_DB(file_name, user_name, user_id):
    """
    this function gets a new user name and id to add to
    the users data base.
    :param file_name: users data base file name
    :param user_name: user name to add
    :param user_id: user id to add
    :return: adds the user name and id values to the users data base
    """

    users_file = open(file_name, 'a')
    users_file.write(f'\n{user_name},')
    users_file.write(f'{user_id}')
    users_file.close()
