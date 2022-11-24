import os
from tabulate import tabulate
from utils import *

def main():
    table = [['===== Adaflix ====='], ['1 - Adicionar filme'], ['2 - Atualizar filme'], ['3 - Excluir filme'], ['4 - Buscar filme'], ['5 - Listar filmes'], ['6 - Limpar tela'], ['7 - Sair']]
    while True:
        movies = get_movies()
        print(tabulate(table, tablefmt="heavy_grid"))
        try:
            option = int(input("> "))
        except:
            continue
        if option == 1:
            add_movie(movies)
        elif option == 2:
            change_movie_info(movies)
        elif option == 3:
            delete_movie(movies)
        elif option == 4:
            find_movie(movies)
        elif option == 5:
            list_movies(movies)
        elif option == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif option == 7:
            break
        else:
            print('Opção escolhida inválida. Por favor, tente novamente...')

main()
