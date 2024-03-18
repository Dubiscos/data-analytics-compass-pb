import sys
import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

df_df = df.toDF()

df_uppercase = df_df.withColumn('nome', upper(df_df['nome']))

print("Contagem de linhas:", df.count())

df_group = df_df.groupBy('ano', 'sexo').agg({'total': 'sum'})
print("Contagem de nomes por ano e sexo:")
df_group.show()

df_df = df_df.withColumn('total', col('total').cast('double'))

df_group = df_df.groupBy('ano', 'sexo').agg({'total': 'sum'})
print("Contagem de nomes por ano e sexo:")
df_group.show()

df_sorted = df_df.sort(df_df['ano'].desc())

nome_fem = df_sorted.filter(df_sorted['sexo'] == 'F').groupBy('nome').sum('total').orderBy('sum(total)', ascending=False).first()
print("Nome feminino com mais registros:", nome_fem['nome'])

nome_masc = df_sorted.filter(df_sorted['sexo'] == 'M').groupBy('nome').sum('total').orderBy('sum(total)', ascending=False).first()
print("Nome masculino com mais registros:", nome_masc['nome'])

df_total_ano = df_df.groupBy('ano').agg({'total': 'sum'})
print("Total de registros por ano:")
df_total_ano.show()

df_10 = df_sorted.limit(10)
print("Primeiras 10 linhas:")
df_10.show()

dynamic_frame_uppercase = DynamicFrame.fromDF(df_uppercase, glueContext, "dynamic_frame_uppercase")

df_partitioned = dynamic_frame_uppercase.toDF()

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
target_path_timestamped = f"{target_path}_{timestamp}"

df_partitioned.write.partitionBy('sexo', 'ano').format('json').save(target_path_timestamped)

job.commit()