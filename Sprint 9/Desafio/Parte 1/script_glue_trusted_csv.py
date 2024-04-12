import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark = SparkSession.builder \
    .appName("Refinamento de CSV") \
    .getOrCreate()

schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

df = spark.read.csv("s3://etl-desafio-eduardo/RAW/Local/CSV/movies/2024/03/18/movies.csv", schema=schema, sep="|", header=True)

df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

df_filtered = df.filter((df.genero.contains("Sci-Fi")) | (df.genero.contains("Fantasy")))

df_filtered = df_filtered.dropDuplicates(["id"])

df_filtered = df_filtered.filter(df.tempoMinutos > 50)

df_filtered = df_filtered.filter(df.numeroVotos > 10)

df_filtered = df_filtered.drop('generoArtista','personagem', 'anoNascimento', 'anoFalecimento', 'titulosMaisConhecidos', 'numeroVotos', 'profissao', 'nomeArtista')

df_filtered = df_filtered.na.drop()

df_filtered = df_filtered.orderBy("anoLancamento")

df_filtered = df_filtered.coalesce(1)

df_filtered.show(10)

nome_arquvio = "s3://etl-desafio-eduardo/TRT/Movies/movies_refinado_csv/"

df_filtered.write.parquet(nome_arquvio, mode="overwrite")

spark.stop()

job.commit()