import requests



def busca_avatar(usario):
    """
    busca o avatar de um usuário no Github
    :param usario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(busca_avatar('david0407j'))