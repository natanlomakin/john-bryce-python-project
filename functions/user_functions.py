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

def generate_file_by_user(list ,user_name ,user_id ,game_name):
    for i in range(len(list)):
        if list[i].get_user_name() == user_name:
            file1 = open(f'{user_name}.txt', 'w')
            file1.write(f'{user_name} ')
            file1.write(f'{user_id}\n')
            for i in game_name:
                file1.write(f'{i}\n')
            file1.close()

def add_game_to_existing_file(user_name ,game_name):
    file1 = open(f'{user_name}.txt', 'a')
    for i in game_name:
        file1.write(f'{i}\n')
    file1.close()