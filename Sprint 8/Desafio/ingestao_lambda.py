import pandas as pd
import requests
import boto3
from IPython.display import display
import datetime

api_key = "e0fde975e6c6b60fe970a7b06dd80790"
movie_ids = ["1103", "10061", "438631", "693134","180", "78", "335984"]

filmes = []

for movie_id in movie_ids:
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie_response = requests.get(movie_url)
    movie_data = movie_response.json()

    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
    credits_response = requests.get(credits_url)
    credits_data = credits_response.json()

    diretores = []
    if 'crew' in credits_data:
        for crew_member in credits_data['crew']:
            if crew_member['job'] == 'Director':
                diretores.append(crew_member['name'])

    providers_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={api_key}&language=pt-BR"
    providers_response = requests.get(providers_url)
    providers_data = providers_response.json()

    alt_titles_url = f"https://api.themoviedb.org/3/movie/{movie_id}/alternative_titles?api_key={api_key}&language=pt-BR"
    alt_titles_response = requests.get(alt_titles_url)
    alt_titles_data = alt_titles_response.json()
    alt_titles = []
    if 'titles' in alt_titles_data:
        for title_info in alt_titles_data['titles']:
            alt_titles.append(title_info['title'])

    reviews_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={api_key}&language=en-US"
    reviews_response = requests.get(reviews_url)
    reviews_data = reviews_response.json()

    if 'title' in movie_data:
        onde_assistir = None
        results = providers_data.get('results', {}) 
        for provider_data in results.get('BR', {}).get('flatrate', []):
            onde_assistir = provider_data.get('provider_name')
            break

        criticas = []
        for review in reviews_data['results'][:1]:
            criticas.append(review['content'])

        df = {'Titulo': movie_data['title'],
              'Data de lançamento': movie_data['release_date'],
              'Diretor' : diretores,
              'Orçamento': movie_data['budget'],
              'Titulos alternativos': alt_titles,
              'Critica': criticas,
              'Onde assistir': onde_assistir}
        filmes.append(df)

df = pd.DataFrame(filmes)
display(df)

s3 = boto3.client('s3',
                  aws_access_key_id='YOUR_ACCESS_KEY',
                  aws_secret_access_key='YOUR_SECRET_KEY',
                  region_name='YOUR_REGION')

num_parts = 7
part_size = len(df) // num_parts

bucket_name = 'data-lake-do-fulano' 

for i in range(num_parts):
    start_idx = i * part_size
    end_idx = start_idx + part_size
    part_df = df[start_idx:end_idx]

    part_json = part_df.to_json(orient='records', force_ascii=False, indent=1)
    current_date = datetime.datetime.now().strftime('%Y/%m/%d')
    file_path = f'raw/tmdb/json/{current_date}/{movie_ids[i]}/movie_data_part_{i+1}.json'

    s3.put_object(Bucket=bucket_name, Key=file_path, Body=part_json.encode('utf-8'))

    print(f'JSON data has been saved to {file_path} in S3 bucket: {bucket_name}')
