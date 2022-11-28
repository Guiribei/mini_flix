import csv
import os
from tabulate import tabulate

def display_menu()->None:
    
    """
    Function to display the program's menu.

    With tabulate library, prints in the terminal a list containing options for the user.

    Parameters
    ----------
    None
        It's a function that doesn't require any argument to be called.

    Returns
    -------
    None
        It does nothing but printing something at the screen, so it's a None return.

    """
    MENU = [['======== Adaflix ========='], 
    ['1 - Add movie'], 
    ['2 - Update movie'], 
    ['3 - Delete movie'], 
    ['4 - Search movie'], 
    ['5 - List movies'],
    ['6 - Look for a genre'],
    ['7 - Clear screen'], 
    ['8 - Exit']]

    print(tabulate(MENU, tablefmt="heavy_grid"))


def check_database()->None:

    """
    Function to check the csv file.

    Verifies the existence of a place where to extract informations from. If 
    there is no source file, it creates an empty csv to ensure the reading 
    of the next function.

    Parameters
    ----------
    None
        It's a function that doesn't require any argument to be called.

    Returns
    -------
    None
        It doesn't return anything.

    """
    if os.path.exists('./movies.csv') == False:
        with open("movies.csv", "w") as file:
            pass


def get_movies()->dict:

    """
    Function that reads the csv file.

    Brings data from the csv file to the program as a dictionary. The value 
    is stored at a variable named movies.

    Parameters
    ----------
    None
        It's a function that doesn't require any argument to be called.

    Returns
    -------
    movies : dict
        It returns a dictionary in which each key is a movie name and each value
        is another dictionary containing movie attributes.

    """
    movies = {}
    with open("movies.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            movies[row[0]] = {'director':row[1], 'genre':row[2], 'year':row[3]}
    return movies


def update_file(movies: dict)->None:

    """
    Function that appends the csv file.

    After each change in the dictionary variable that carries the programs data,
    this function can update the infomation back in the csv file.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    with open("movies.csv", "a", newline = "", encoding='utf-8') as file:
        for name in movies:
            data = [name,movies[name]['director'], movies[name]['genre'], movies[name]['year']]
            writer = csv.writer(file)
            writer.writerow(data)


def rewrite_file(movies: dict)->None:

    """
    Function that writes in the csv file.

    After each change in the dictionary that carries the programs data,
    this function can rewrite the infomation that was in the csv file.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    with open("movies.csv", "w", newline = "", encoding='utf-8') as file:
        for name in movies:
            data = [name,movies[name]['director'], movies[name]['genre'], movies[name]['year']]
            writer = csv.writer(file)
            writer.writerow(data)


def find_movie(movies: dict)->None:

    """
    Function that looks for a specific movie at the data set.

    It first prints a statement and prompts a movie entry. After stripping and
    titling the string from input, it checks if there is a key in the dictionary
    with that name. If it finds one, returns the movie's information.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    print("\n==Buscar filme==")
    if len(movies.keys()) > 0:
        name = input("Enter the movie that should be found: ").strip().title()
        if name in movies:
            print(f"The movie was found and the information follows below\n\
==========================================\n\
    Name: {name}\n\
    Director: {movies[name]['director']}\n\
    Genre: {movies[name]['genre']}\n\
    Year: {movies[name]['year']}\n\
==========================================\n")
        else:
            print(f"There is no movie with the name {name}")
    else:
        print("There are no movies registerd")


def add_movie(movies: dict)->None:

    """
    Function that adds a movie to the data set.

    It reads a movie's name, director, genre and year from user input. After that,
    the function update_file() is called to append the csv file with the new info.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    while True:
        name = input("Enter a movie: ").strip().title()
        if name in movies:
            print('This movie has already been registered. Please try again...')
        else:
            movies = {name:{'director':input("Enter the movie's director: ")\
                .strip().title(), 'genre':input("Enter the movie's genre: ")\
                    .strip().title(), 'year':input("Enter the movie's year: ")\
                        .strip().title()}}
            update_file(movies)
            print("The movie {} has been successfully registered!\n".format(name))
            break


def change_movie_info(movies: dict)->None:

    """
    Function that changes the information related to a movie.

    If there is already a movie registered at the database, it looks for a key
    that matches the input from the user and then prints the information avaliable.
    After that it prompts for a new set of atributes for that movie, calling the
    rewrite_file() function to make the csv file up to date.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    print("\n==Alterar filme==")
    if len(movies.keys()) > 0:
        name = input("Enter the movie to update: ").strip().title()
        if name in movies:
            print(f"\nThe movie was found and the information follows below\n\
==========================================\n\
    Name: {name}\n\
    Director: {movies[name]['director']}\n\
    Genre: {movies[name]['genre']}\n\
    Year: {movies[name]['year']}\n\
==========================================\n")
            movies[name]['director'] = input("Enter the movie's director: ")\
                .strip().title()
            movies[name]['genre'] = input("Enter the movie's genre: ")\
                .strip().title()
            movies[name]['year'] = input("Enter the movie's year: ")\
                .strip().title()
            rewrite_file(movies)
            print(f"The new info is\n\
==========================================\n\
    Name: {name}\n\
    Director: {movies[name]['director']}\n\
    Genre: {movies[name]['genre']}\n\
    Year: {movies[name]['year']}\n\
==========================================\n")
        else:
            print(f"There is no movie named {name}")
    else:
        print("There are no movies registerd")


def delete_movie(movies: dict)->None:

    """
    Function that deletes a movie.

    If there is already a movie registered at the dataset, it prompts the user
    a movie name. In case it finds, the movie is deleted from the dictionary. The
    rewrite_file() function is called to make sure csv contains the updated info.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    print("\n==Excluir filme==")
    if len(movies.keys()) > 0:
        name = input("Enter the name of the movie to be deleted: ")\
            .strip().title()
        if name in movies:
            del movies[name]
            rewrite_file(movies)       
            print('The movie has been deleted')
        else:
            print(f"There is no movie named {name}")
    else:
        print("There are no movies registerd")


def list_all_movies(movies: dict)->None:

    """
    Function that shows all movies registerd at the dataset.

    If the database is not empty, it prints the whole list of registered movies.
    If there are none, it prints a message to warn the user.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    print("============ Movies List =============")
    if len(movies.keys()) > 0:
        for movie in movies:
            print(f"Movie:\t{movie}\n\
\tDirector: {movies[movie]['director']}\n\
\tGenre: {movies[movie]['genre']}\n\
\tYear: {movies[movie]['year']}\n\
==========================================")
    else:
        print("There are no movies registerd")


def find_genres(movies: dict) -> None:

    """
    Function that looks for a specific movie genre in the catalog.

    Prompts the user a genre requested. It loops through the dictionary trying to
    find the genre specified. It prints a list of movies that matched that search.
    If not is find, it prints a message saying that category was not found.

    Parameters
    ----------
    movies : dict
        The only parameter is the dictionary read from the csv file, obtained
        from get_movies() function.

    Returns
    -------
    None
        It doesn't return anything.

    """
    genre = input("What movie genre do you want to watch? ").strip().title()
    movies_found = []
    for k, v in movies.items():
        if v['genre'] == genre:
            movies_found.append(k)
    if len(movies_found) == 0:
        print(f"\nThere are no movies in the category {genre}\n")
    else:
        print(f"\nMovies found on {genre} category:\n\
==========================================\n\
{sorted(movies_found)}\n\
==========================================\n")
