import requests
import pandas as pd

from IPython.display import display



api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMGZkZTk3NWU2YzZiNjBmZTk3MGE3YjA2ZGQ4MDc5MCIsInN1YiI6IjY1ZjlmYWYwNzc3NmYwMDE0OTEyYTk4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PrMrISdJ6L9a5sIjcMnsuK2FEb9EwELhWMw5U5e44Tw"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"



response = requests.get(url)
data = response.json()



filmes = []



for movie in data['results']:
df = {'Titulo': movie['title'],
'Data de lançamento': movie['release_date'],
'Visão geral': movie['overview'],
'Votos': movie['vote_count'],
'Média de votos:': movie['vote_average']}



filmes.append(df)



df = pd.DataFrame(filmes)
display(df)