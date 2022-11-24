import csv

def get_movies()->dict:
    movies = {}
    with open("movies.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            movies[row[0]] = {'diretor':row[1], 'genero':row[2], 'ano':row[3]}
    return movies


def update_file(movies:dict)->None:
    with open("dici.csv", "a", newline = "", encoding='utf-8') as file:
        for name in movies:
            data = [name,movies[name]['diretor'], movies[name]['genero'], movies[name]['ano']]
            writer = csv.writer(file)
            writer.writerow(data)


def rewrite_file(movies:dict)->None:
    with open("dici.csv", "w", newline = "", encoding='utf-8') as file:
        for name in movies:
            data = [name,movies[name]['diretor'], movies[name]['genero'], movies[name]['ano']]
            writer = csv.writer(file)
            writer.writerow(data)


def find_movie(movies: dict)->None:
    print("\n==Buscar filme==")
    if len(movies.keys()) > 0:
        name = input("Digite o filme que deve ser encontrado: ").title()
        if name in movies:
            print('\nO filme foi encontrado e as informações seguem abaixo\n')
            print('==========================================')
            print(f'Nome: {name}')
            print(f"Diretor(a): {movies[name]['diretor']}")
            print(f"Gênero: {movies[name]['genero']}")
            print(f"Ano: {movies[name]['ano']}")
            print('==========================================\n')
        else:
            print(f"Não existe filme cadastrado com o nome {name}")
    else:
        print("Não existe nenhum filme cadastrado no sistema")


def add_movie(movies: dict)->None:
    while True:
        name = input("Digite o nome do filme: ").title()
        if name in movies:
            print('Este filme já foi cadastrado. Por favor, tente novamente..')
        else:
            movies = {name:{'diretor':input("Digite o(a) diretor(a) do filme: ").title(), 'genero':input("Digite o gênero do filme: ").title(), 'ano':input("Digite o ano do filme: ").title()}}
            update_file(movies)
            print("O filme {} foi cadastrado com sucesso!\n".format(name))
            break


def change_movie_info(movies: dict)->None:
    print("\n==Alterar filme==")
    if len(movies.keys()) > 0:
        name = input("Digite o filme que deve ser alterado: ").title()
        if name in movies:
            print('\nO filme foi encontrado e as informações seguem abaixo')
            print('==========================================')
            print(f'Nome: {name}')
            print(f"Diretor: {movies[name]['diretor']}")
            print(f"Gênero: {movies[name]['genero']}")
            print(f"Ano: {movies[name]['ano']}")
            print('==========================================\n')
            movies[name]['diretor'] = input("Digite o(a) diretor(a) do filme: ").title()
            movies[name]['genero'] = input("Digite o gênero do filme: ").title()
            movies[name]['ano'] = input("Digite o ano do filme: ").title()
            update_file(movies)
            print('As novas informações são:\n')
            print('==========================================')
            print(f'Nome: {name}')
            print(f"Diretor(a): {movies[name]['diretor']}")
            print(f"Gênero: {movies[name]['genero']}")
            print(f"Ano: {movies[name]['ano']}")
            print('==========================================\n')
        else:
            print(f"Não existe filme cadastrado com o nome {name}")
    else:
        print("Não existe nenhum filme cadastrado no sistema")


def delete_movie(movies: dict)->None:
    print("\n==Excluir filme==")
    if len(movies.keys()) > 0:
        name = input("Digite o nome do filme que deve ser excluído: ").title()
        if name in movies:
            del movies[name]
            rewrite_file(movies)       
            print('O filme foi apagado')
        else:
            print("Não existe um filme cadastrado com o nome {}".format(name))
    else:
        print("Não existe nenhum filme cadastrado no sistema")


def list_movies(movies):
    print("\n============ Lista de Filmes =============")
    if len(movies.keys()) > 0:
        for movie in movies:
            print("Filme {}".format(movie))
            print("\tDiretor(a): {}".format(movies[movie]['diretor']))
            print("\tGênero: {}".format(movies[movie]['genero']))
            print("\tAno: {}".format(movies[movie]['ano']))
            print('==========================================')
    else:
        print("Não existe nenhum filme cadastrado no sistema")
