from django.shortcuts import render
from django.conf import settings
import requests
import .models MovieReview , Movie
import requests
from bs4 import BeautifulSoup

# Estabilidade dos Dados: Dados que mudam frequentemente (como classificações ao vivo ou resenhas recentes) podem ser melhores para chamadas dinâmicas, enquanto dados que não mudam (como título, elenco, ano) podem ser armazenados para evitar chamadas repetitivas.


def insert_api_sql(api):
    for _ in range(api):
        for j in range(api):

            # verificar se esse filme ja essta armazenado
            
            # insert in my database
            movie = Movie(

            )
            movie.save()

# chama a api e armazena as informaçoes em um diciconario
def get_api_movie():
    movies = []

    api_key = settings.OMDB_API_KEY

    url = f"http://www.omdbapi.com/?apikey=[yourkey]&"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        for info in range(data):
            # armazenar as informaçoees em um banco de dados

            return movies    
    else:
        return None
    
# Função para fazer web scraping de resenhas
def get_movie_reviw(movie_url):
    response = requests.get(movie_url)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    revies = []
    revies_elements = soup.find_all('div', class_='review_text')

    for revies in revies_elements:
        revies.append(revies.text.strip())

    return revies

"""Filtragem Colaborativa com scikit-learn O algoritmo de filtragem colaborativa usa dados de classificação de usuários para encontrar padrões. Passos: Crie uma matriz de usuários e filmes, onde cada célula contém a classificação que o usuário deu a um filme. Use um algoritmo de fatoração de matriz, como Singular Value Decomposition (SVD), para prever classificações. xemplo com scikit-learn: "" ""
