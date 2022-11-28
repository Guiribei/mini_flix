# Loads the functions to be used from an aux file
from utils import *

def main():

    ''' Main function'''

    while True:

        # Ensures there is a csv file with the info
        check_database()
        
        # Prompts a menu to the user
        display_menu()
        
        # Makes a dictionary to handle the csv file content
        movies = get_movies()

        # Ensure the user inputs a number
        try:
            option = int(input("> "))
        except:
            print('\nEnter the number that corresponds to the desired option: ')
            continue

        # Chooses the option according to the entry
        if option == 1:
            add_movie(movies)
        elif option == 2:
            change_movie_info(movies)
        elif option == 3:
            delete_movie(movies)
        elif option == 4:
            find_movie(movies)
        elif option == 5:
            list_all_movies(movies)
        elif option == 6:
            find_genres(movies)
        elif option == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif option == 8:
            break

        # Prompts a error message in case of a number different from all the options above
        else:
            print('Invalid option. Please, try again...')

main()