import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring, monotonically_increasing_id

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dim_filme_path = "s3://etl-desafio-eduardo/Refined/dim_filme/"
dim_data_path = "s3://etl-desafio-eduardo/Refined/dim_data/"
fato_path = "s3://etl-desafio-eduardo/Refined/fato/"

trusted_json = spark.read.parquet("s3://etl-desafio-eduardo/TRT/Movies/movies_refinado_json/data_coleta=2024-04-10/")
trusted_csv = spark.read.parquet("s3://etl-desafio-eduardo/TRT/Movies/movies_refinado_csv/")

dim_filme_df = trusted_json.select(
    col("id").alias("ID_Filme"),
    col("Titulo"),
    col("Diretor").getItem(0).alias("Diretor"),
    col("Genero"),
    col("Critica"),
    col("ondeAssistir"),
    col("titulosAlternativos").getItem(0).alias("TituloAlternativo")
)

dim_data_df = trusted_json.select(
    ("dataLancamento"),
    substring(col("dataLancamento"), 1, 4).alias("Ano"),
    substring(col("dataLancamento"), 6, 2).alias("Mês"),
    substring(col("dataLancamento"), 9, 2).alias("Dia")
).distinct()
dim_data_df = dim_data_df.withColumn('id', monotonically_increasing_id() + 1)

fato_df = trusted_json.join(trusted_csv,
                             trusted_json.id == trusted_csv.id,
                             "left") \
    .select(trusted_json.id.alias("ID_Filme"),
            trusted_json.dataLancamento,
            trusted_json['Orçamento'])

fato_df = fato_df.join(dim_data_df, fato_df.dataLancamento == dim_data_df.dataLancamento, "inner") \
    .drop("dataLancamento", "Ano", "Mês", "Dia").withColumnRenamed('id', 'id_data')

dim_filme_df.write.mode("overwrite").parquet(dim_filme_path)
dim_data_df.write.mode("overwrite").parquet(dim_data_path)
fato_df.write.mode("overwrite").parquet(fato_path)

spark.stop()

job.commit()