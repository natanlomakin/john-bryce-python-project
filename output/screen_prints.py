from functions import game_functions

def sorting_options(ls ,sort_order ,users_choice):
    """
    this function gets a list of the available games and sorts it by
    the users choice in ascending or descending order.
    returns a new sorted list.
    :param ls: available games list
    :param sort_order: users choice of ascending or descending order
    :param users_choice: users choice of sorting
    :return: new sorted list
    """

    print('name,genre,publisher,developer,platform,price,release Date,rating\n')
    if users_choice == 'genre':
        for i in game_functions.sort_by_genre(ls, sort_order):
            print(i,'\n')
    if users_choice == 'name':
        for i in game_functions.sort_by_name(ls, sort_order):
            print(i,'\n')
    if users_choice == 'publisher':
        for i in game_functions.sort_by_publisher(ls, sort_order):
            print(i,'\n')
    if users_choice == 'developer':
        for i in game_functions.sort_by_developer(ls, sort_order):
            print(i,'\n')
    if users_choice == 'platform':
        for i in game_functions.sort_by_platform(ls, sort_order):
            print(i,'\n')
    if users_choice == 'price':
        for i in game_functions.sort_by_price(ls, sort_order):
            print(i,'\n')
    if users_choice == 'rating':
        for i in game_functions.sort_by_rating(ls, sort_order):
            print(i,'\n')
    if users_choice == 'release date':
        for i in game_functions.sort_by_release_date(ls, sort_order):
            print(i,'\n')

def most_common_genre(ls):
    """
    this function gets a list of available games and prints the most common genre
    :param ls: available games list
    :return: most common genre
    """

    print('most common genre is:',game_functions.most_common_genre(ls),'\n')

def highest_rating_games(ls):
    """
    this function gets a list of available games and prints the highest rated games
    :param ls: list of available games
    :return: highest rated game
    """

    lst, rating = game_functions.highest_rating(ls)
    for i in lst:
        print('highest rating games with a rating of',rating,'are:\n')
        print(i)
