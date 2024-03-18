import boto3
import os
from datetime import datetime

def upload_to_s3(file_path, bucket_name, s3_key, aws_access_key_id, aws_secret_access_key, aws_session_token):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token
    )
    s3 = session.client('s3')
    s3.upload_file(file_path, bucket_name, s3_key)

def main():
    bucket_name = 'etl-desafio-eduardo'
    raw_zone = 'RAW/Local/CSV'
    local_directory = '/app'
    aws_access_key_id = 'ASIA47CR3GWEQGNHFL2J'
    aws_secret_access_key = 'cbAq2ueNASRGzcCB7/icxfgAeThko2XJHn8GO12p'
    aws_session_token = 'IQoJb3JpZ2luX2VjENH//////////wEaCXVzLWVhc3QtMSJIMEYCIQDKs7i1TQpmGOkPbNhwR9Bwq+JOLCaZsecin4pdoSuF+wIhAJJSwRm8Ab3GnAkyLibLWGQg4zhsFyc331OzmMnu5tOdKq4DCNn//////////wEQABoMODkxMzc3MzY2NDA5IgxrbCObuyQ2iN6EtC4qggOxEm4CoQth1DsXXQ4xr5k58JHyDOuCw2QtyokEFRuDeSg2aCwWFUdJL9kKdK2/lX5Q4wODuMnLIriRV4SdbblGsnd6WjQF13pDAb9rNF7b8vnXczW3R0IyX0MWpUS35tIzqjYmok88I72+1HLJd1Z06GzBhl0sbHqIOg3p4yhDYVx69BfVgAdW/hQVyTChYJHsSMtJXCbMCF1/8bRxMTEbzdjmo7MB250W7MbIIBF6pBemtgmrj1rV0GIZpjSm/ih3eYpE3HaaY2NUF1yKx+ldmeI3smlDGCNlMekbItvSJrlR5dyfeFGlhsly++DVjhA9QGx4EpFeIZDzpxh5HNPJK2NBJmRxx8QF9ho2h3ssHhZBgFDgUgeo7lX5XerlFMlbvZEvs+5MOgHDF9MUNiL7+dQ6TLMCh/tXj1o7MVimFpKlb72zuVDPztDorycsp/Hz7k5dHk9LKdCMRj3axpV84GITUJTJtULX8en8pk38Rk4AzNkBu0eqMKQ1WcKrR0R76DCN1OGvBjqlAbFejtZgNt+2RbGWqPt2C13nPfPJOUSOiZHnluClzCtNL1VG8jEF0vOvR9iY1lz+RYlf9I0NWvAWvs4yXmRlEtS8cgv2GMDVckZ277Q49fOrMaglTDcIdvViGGDZJJs/uLBvZzeonL4ZhtHTMAcoZi8eBE6QqqHAGujgvZEDxzeLkvxAdN8aY7HtlzsprKyv/NLUsEN7W6dNxVVr1H/CHq+CMhJVxg=='

    files = ['movies.csv', 'series.csv']
    
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(local_directory, file)
            
            data_source = file.split('.')[0].lower()
            
            current_date = datetime.now().strftime('%Y/%m/%d')
            s3_key = f'{raw_zone}/{data_source}/{current_date}/{file}'
            
            upload_to_s3(file_path, bucket_name, s3_key, aws_access_key_id, aws_secret_access_key, aws_session_token)
            print(f'Arquivo {file} carregado para o S3 com sucesso em: s3://{bucket_name}/{s3_key}')

if __name__ == "__main__":
    main()

    