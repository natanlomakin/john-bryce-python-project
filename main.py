from functions import game_functions, user_functions
from output import screen_prints

menu = input("""hi, what would you like to do?
to see the games list enter 1
to add a game to a users library enter 2
to exit enter 3\n""")

while menu == '1' or menu == '2':

    if menu == '1':

        games_file_name = input('enter the name of the games file you want to open:')
        games_list = game_functions.open_file(games_file_name)
        games_menu_options = input("""to sort the games list enter 'sort'
to see the most popular genre enter 'popular'
to see the highest rating games enter 'rating'""")
        if games_menu_options == 'sort':
            sort_choice = input("""select by what to sort the list:
                    1.name
                    2.genre
                    3.publisher
                    4.developer
                    5.platform
                    6.price
                    7.release date
                    8.rating\n""")

            sort_order = input("""select how you want to sort:
                    1.'up' for ascending order
                    2.'down' for descending order\n""")
            screen_prints.sorting_options(games_list, sort_order, sort_choice)
        if games_menu_options == 'popular':
            screen_prints.most_common_genre(games_list)
        if games_menu_options == 'rating':
            screen_prints.highest_rating_games(games_list)


    if menu == '2':
        users_file_name = input('enter the name of the users file you want to open: ')
        users_list = user_functions.file(users_file_name)
        add_create = input("""to add a game to an existing file enter "add" 
to create a new library enter create:\n""")
        if add_create == 'create':
            user_name = input('enter the users name you would like to create a library for: ')
            user_id = input('enter the users id: ')
            game_name_list = []
            game_name_list.append(input('enter the game name you want to add(enter done when finished): '))
            while game_name_list[len(game_name_list)-1] != 'done':
                game_name_list.append(input('enter the game name you want to add: '))
            game_name_list.remove('done')
            user_functions.generate_file_by_user(users_list ,user_name ,user_id, game_name_list)
        elif add_create == 'add':
            user_name = input('enter the users name you would like to add the games to: ')
            game_name_list = []
            game_name_list.append(input('enter the game name you want to add(enter done when finished): '))
            while game_name_list[len(game_name_list) - 1] != 'done':
                game_name_list.append(input('enter the game name you want to add: '))
            game_name_list.remove('done')
            user_functions.add_game_to_existing_file(user_name,game_name_list)
        else:
            print('error enter a valid action')

    menu = input("""hi, what would you like to do next?
    to see the games list enter 1
    to add a game to a users library enter 2
    to exit enter 3\n""")








