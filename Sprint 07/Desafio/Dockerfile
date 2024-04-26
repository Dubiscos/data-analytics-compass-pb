FROM python:3.9-slim

WORKDIR /app

COPY ingestao_s3.py /app/
COPY movies.csv /app/
COPY series.csv /app/

RUN pip install boto3

CMD ["python", "ingestao_s3.py"]
