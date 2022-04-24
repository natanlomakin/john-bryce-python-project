from functions import game_functions, user_functions, file_relocation
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
to see the highest rating games enter 'rating'\n""")
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
        users_file_name = input("""enter the name of the users database you want to open (in these project its 'users.txt'): """)
        users_list = user_functions.file(users_file_name)
        add_create_new = input("""to add a game to an existing user library enter "add", 
to create a new library for an existing user enter "create"
to add a new user to the data base enter "new user":\n""")
        if add_create_new == 'create':
            user_name = input('enter the users name you would like to create a library for (must be an existing user from the users database): ')
            user_id = input('enter the users id: ')
            game_name_list = []
            game_name_list.append(input("enter the game name you want to add(enter 'done' when finished): "))
            while game_name_list[len(game_name_list)-1] != 'done':
                game_name_list.append(input('enter the game name you want to add: '))
            game_name_list.remove('done')
            user_functions.generate_file_by_user(users_list ,user_name ,user_id, game_name_list)
            file_relocation.user_library_file_relocation(user_name)
        elif add_create_new == 'add':
            user_name = input('enter the users name you would like to add the games to (must be an existing user from the users database): ')
            game_name_list = []
            game_name_list.append(input("enter the game name you want to add(enter 'done' when finished): "))
            while game_name_list[len(game_name_list) - 1] != 'done':
                game_name_list.append(input('enter the game name you want to add: '))
            game_name_list.remove('done')
            user_functions.add_game_to_existing_file(user_name,game_name_list)
        elif add_create_new == 'new user':
            new_user_name_to_add = input('enter the users first and last name: ')
            new_user_id_to_add = input('enter the users id: ')
            user_functions.add_new_user_to_users_DB(users_file_name, new_user_name_to_add, new_user_id_to_add)
        else:
            print('error enter a valid action')

    menu = input("""hi, what would you like to do next?
    to see the games list enter 1
    to add a game to a users library enter 2
    to exit enter 3\n""")








