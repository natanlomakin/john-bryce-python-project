import os

def user_library_file_relocation(user_name):
    """
    the function checks if there is an existing library for the given
    user name in the main directory, if exists the file will be moved
    to the correct directory 'user_librarys'
    :param user_name: user name
    :return: move users library to correct directory
    """
    destination = os.getcwd() + f'\\user_librarys\\{user_name}.txt'
    source = os.getcwd() + f'\\{user_name}.txt'
    if os.path.exists(source):
        os.replace(source, destination)
    else:
        return None