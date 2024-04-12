import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import col, explode, regexp_replace, concat_ws, to_date, collect_list, lit
from pyspark.sql.window import Window

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark = SparkSession.builder \
    .appName("Refinamento de JSON") \
    .getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("Titulo", StringType(), True),
    StructField("Data de lançamento", StringType(), True),
    StructField("Diretor", ArrayType(StringType()), True),
    StructField("Genero", ArrayType(StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True)
    ])), True),
    StructField("Orçamento", IntegerType(), True),
    StructField("Titulos alternativos", ArrayType(StringType()), True),
    StructField("Critica", ArrayType(StringType()), True),
    StructField("Onde assistir", StringType(), True)
])

df = spark.read.option("multiline", "true").schema(schema).json("s3://etl-desafio-eduardo/RAW/tmdb/json/2024/04/10/")

df = df.withColumn("Genero", explode(col("Genero"))) \
                 .withColumn("Genero", col("Genero.name")) \
                 .withColumn("Genero", regexp_replace(col("Genero"), "Science Fiction", "Sci-fi"))

window_spec = Window.partitionBy('id')
df = df.withColumn('genero_concatenado', concat_ws(', ' , collect_list('Genero').over(window_spec)))

df = df.drop('Genero')
df = df.dropDuplicates()
df = df.withColumnRenamed('genero_concatenado', 'Genero')

df = df.withColumnRenamed("Data de lançamento", "dataLancamento") \
                         .withColumnRenamed("Titulos alternativos", "titulosAlternativos") \
                         .withColumnRenamed("Onde assistir", "ondeAssistir")

colunas_desejadas = ["id", "Titulo", "dataLancamento", "Diretor", "Genero", "Orçamento", "titulosAlternativos", "Critica", "ondeAssistir"]
df = df.select(*colunas_desejadas)

df = df.withColumn('data_coleta', to_date(lit('2024-04-10')))
df.write.partitionBy('data_coleta').mode('overwrite').parquet('s3://etl-desafio-eduardo/TRT/Movies/movies_refinado_json/')

spark.stop()

job.commit()