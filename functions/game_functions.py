from games import game_class

def open_file(file_name):
    """
    this function gets the name of the file you want to open and
    than return a list of row number X to the 'Game' module in order
    to create a new objective
    :param file_name: name of the file to open
    :return: list of row number X
    """
    games_info_list = []
    games_file = open(file_name,)
    all = games_file.readlines()
    for i in range(1, len(all)):
        games_info_list.append(game_class.Game(all[i].split(',')))
    games_file.close()
    return games_info_list

def sort_by_genre(list, up_down):
    """
    this functions arranges the games data by genre by an
    ascending or descending order according to the users choice
    :param list: gets the list of games
    :param up_down: users arrangement choice (up for ascending, down for descending)
    :return: an arranged list of the games
    """
    new_list = []
    if up_down == 'up':
        letter = 97
        while letter <= 122:
            for i in range(len(list)):
                if ord(list[i].get_genre()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter += 1
    elif up_down == 'down':
        letter = 122
        while letter >= 97:
            for i in range(len(list)):
                if ord(list[i].get_genre()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def sort_by_name(list, up_down):
    """
        this functions arranges the games data by name of the game by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        letter = 97
        while letter <= 122:
            for i in range(len(list)):
                if ord(list[i].get_name()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter += 1
    elif up_down == 'down':
        letter = 122
        while letter >= 97:
            for i in range(len(list)):
                if ord(list[i].get_name()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def sort_by_publisher(list, up_down):
    """
        this functions arranges the games data by publisher by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        letter = 97
        while letter <= 122:
            for i in range(len(list)):
                if ord(list[i].get_publisher()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter += 1
    elif up_down == 'down':
        letter = 122
        while letter >= 97:
            for i in range(len(list)):
                if ord(list[i].get_publisher()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def sort_by_developer(list, up_down):
    """
        this functions arranges the games data by developer by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        letter = 97
        while letter <= 122:
            for i in range(len(list)):
                if ord(list[i].get_developer()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter += 1
    elif up_down == 'down':
        letter = 122
        while letter >= 97:
            for i in range(len(list)):
                if ord(list[i].get_developer()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def sort_by_platform(list, up_down):
    """
        this functions arranges the games data by platform by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        letter = 97
        while letter <= 122:
            for i in range(len(list)):
                if ord(list[i].get_platform()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter += 1
    elif up_down == 'down':
        letter = 122
        while letter >= 97:
            for i in range(len(list)):
                if ord(list[i].get_platform()[0]) == letter:
                    new_list.append(list[i])
                else:
                    continue
            letter -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def sort_by_price(list, up_down):
    """
        this functions arranges the games data by price by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        min_price = 0
        while min_price <= 100:
            for i in range(len(list)):
                if int(list[i].get_price()) == min_price:
                    new_list.append(list[i])
                else:
                    continue
            min_price += 1
    elif up_down == 'down':
        min_price = 100
        while min_price >= 0:
            for i in range(len(list)):
                if int(list[i].get_price()) == min_price:
                    new_list.append(list[i])
                else:
                    continue
            min_price -= 1
    return new_list

def sort_by_rating(list, up_down):
    """
        this functions arranges the games data by rating by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        min_rating = 0
        while min_rating <= 10:
            for i in range(len(list)):
                if int(list[i].get_rating()) == min_rating:
                    new_list.append(list[i])
                else:
                    continue
            min_rating += 1
    elif up_down == 'down':
        min_rating = 10
        while min_rating >= 0:
            for i in range(len(list)):
                if int(list[i].get_rating()) == min_rating:
                    new_list.append(list[i])
                else:
                    continue
            min_rating -= 1
    return new_list

def sort_by_release_date(list, up_down):
    """
        this functions arranges the games data by the release date by an
        ascending or descending order according to the users choice
        :param list: gets the list of games
        :param up_down: users arrangement choice (up for ascending, down for descending)
        :return: an arranged list of the games
        """
    new_list = []
    if up_down == 'up':
        year = 2000
        month = 1
        day = 1
        while year <= 2022:
            for i in range(len(list)):
                if int(list[i].get_realese_date_year()) == year:
                    while month <= 12:
                        if int(list[i].get_realese_date_month()) == month:
                            while day <= 30:
                               if int(list[i].get_realese_date_day()) == day:
                                   new_list.append(list[i])
                                   day = 31
                                   month = 13
                               else:
                                   day += 1
                                   continue
                            day = 1
                        else:
                            month += 1
                            continue
                    month = 1
                else:
                    continue
            day = 1
            month = 1
            year += 1
    elif up_down == 'down':
        year = 2022
        month = 12
        day = 30
        while year >= 2000:
            for i in range(len(list)):
                if int(list[i].get_realese_date_year()) == year:
                    while month >= 1:
                        if int(list[i].get_realese_date_month()) == month:
                            while day >= 1:
                                if int(list[i].get_realese_date_day()) == day:
                                    new_list.append(list[i])
                                    day = 0
                                    month = 0
                                else:
                                    day -= 1
                                    continue
                            day = 30
                        else:
                            month -= 1
                            continue
                    month = 12
                else:
                    continue
            day = 30
            month = 12
            year -= 1
    else:
        print("""please enter 'up' or 'down'""")
    return new_list

def most_common_genre(list):

    genre_lst = []
    for i in range(len(list)):
        if list[i].get_genre() not in genre_lst:
            genre_lst.append(list[i].get_genre())
    genre_lst_cnt = [0] * len(genre_lst)
    for i in range(len(list)):
        for j in range(len(genre_lst)):
            if list[i].get_genre() == genre_lst[j]:
                genre_lst_cnt[j] += 1
    return genre_lst[genre_lst_cnt.index(max(genre_lst_cnt))]

def highest_rating(list):
    max_rating = 0
    highest_rating_ls = []
    for i in range(len(list)):
        if int(list[i].get_rating()) >= max_rating:
            max_rating = int(list[i].get_rating())
    for i in range(len(list)):
        if int(list[i].get_rating()) == max_rating:
            highest_rating_ls.append(list[i].get_name())
    return highest_rating_ls, max_rating