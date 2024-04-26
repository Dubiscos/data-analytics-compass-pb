from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import expr, year, to_date, col, when

spark = SparkSession \
            .builder \
            .master("local[*]") \
            .appName("Exercicio Intro") \
            .getOrCreate()

# ETAPA 1
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# ETAPA 2
df_nomes.printSchema()

# ETAPA 3
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

# ETAPA 4
df_nomes = df_nomes.withColumn("Escolaridade", expr("CASE WHEN rand() <= 0.33 THEN 'Fundamental' WHEN rand() <= 0.67 THEN 'Medio' ELSE 'Superior' END"))

# ETAPA 5
paises_sulamerica = ['Brasil', 'Argentina', 'Colombia', 'Chile', 'Peru', 'Venezuela', 'Equador', 'Bolivia', 'Paraguai', 'Uruguai', 'Guiana', 'Suriname']
df_nomes = df_nomes.withColumn("Pais", expr("array({})[int(rand() * size(array({})))]".format(', '.join(["'{}'".format(pais) for pais in paises_sulamerica]), ', '.join(["'{}'".format(pais) for pais in paises_sulamerica]))))

# ETAPA 6
df_nomes = df_nomes.withColumn("AnoNascimento", expr("cast(1945 + rand() * (2010 - 1945 + 1) as int)"))

df_nomes.show(10)

# ETAPA 7
df_select = df_nomes.filter(col("AnoNascimento") >= 2000)
df_select.show(10)

# ETAPA 8
df_select_sql = df_nomes.filter("AnoNascimento >= 2000")
df_select_sql.show(10)

# ETAPA 9
millennials_count = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print("Número de pessoas da geração Millennials:", millennials_count)

# ETAPA 10
millennials_count_sql = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print("Número de pessoas da geração Millennials (usando Spark SQL):", millennials_count_sql)

# ETAPA 11
df_nomes = df_nomes.withColumn("Generacao",
                               when((col("AnoNascimento") >= 1944) & (col("AnoNascimento") <= 1964), "Baby Boomers")
                               .when((col("AnoNascimento") >= 1965) & (col("AnoNascimento") <= 1979), "Geração X")
                               .when((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994), "Millennials")
                               .when((col("AnoNascimento") >= 1995) & (col("AnoNascimento") <= 2015), "Geração Z")
                               .otherwise("Outra"))

generation_counts = df_nomes.filter(col("Generacao") == "Millennials").groupBy("Pais").count().orderBy("Pais")
generation_counts.show()
