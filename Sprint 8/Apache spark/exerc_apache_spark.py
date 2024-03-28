from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import expr, year, to_date, col, when

# Definindo SparkSession
spark = SparkSession \
            .builder \
            .master("local[*]") \
            .appName("Exercicio Intro") \
            .getOrCreate()

# ETAPA 1: Ler o arquivo nomes_aleatorios.txt e carregá-lo em um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# ETAPA 2: Exibir o Schema do DataFrame
df_nomes.printSchema()

# ETAPA 3: Renomear a coluna para "Nomes" e mostrar 10 linhas do DataFrame
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

# ETAPA 4: Adicionar coluna "Escolaridade" com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", expr("CASE WHEN rand() <= 0.33 THEN 'Fundamental' WHEN rand() <= 0.67 THEN 'Medio' ELSE 'Superior' END"))

# ETAPA 5: Adicionar coluna "Pais" com valores aleatórios de países da América do Sul
paises_sulamerica = ['Brasil', 'Argentina', 'Colombia', 'Chile', 'Peru', 'Venezuela', 'Equador', 'Bolivia', 'Paraguai', 'Uruguai', 'Guiana', 'Suriname']
df_nomes = df_nomes.withColumn("Pais", expr("array({})[int(rand() * size(array({})))]".format(', '.join(["'{}'".format(pais) for pais in paises_sulamerica]), ', '.join(["'{}'".format(pais) for pais in paises_sulamerica]))))

# ETAPA 6: Adicionar coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", expr("cast(1945 + rand() * (2010 - 1945 + 1) as int)"))

# Exibir 10 nomes do dataframe resultante
df_nomes.show(10)

# ETAPA 7: Selecionar as pessoas que nasceram neste século
df_select = df_nomes.filter(col("AnoNascimento") >= 2000)
df_select.show(10)

# ETAPA 8: Repetir o processo da Etapa 7 utilizando Spark SQL
df_select_sql = df_nomes.filter("AnoNascimento >= 2000")
df_select_sql.show(10)

# ETAPA 9: Contar o número de pessoas da geração Millennials (nascidos entre 1980 e 1994)
millennials_count = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print("Número de pessoas da geração Millennials:", millennials_count)

# ETAPA 10: Repetir o processo da Etapa 9 utilizando Spark SQL
millennials_count_sql = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print("Número de pessoas da geração Millennials (usando Spark SQL):", millennials_count_sql)

# ETAPA 11: Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações especificadas

# Criar uma coluna para identificar a geração de cada pessoa
df_nomes = df_nomes.withColumn("Generacao",
                               when((col("AnoNascimento") >= 1944) & (col("AnoNascimento") <= 1964), "Baby Boomers")
                               .when((col("AnoNascimento") >= 1965) & (col("AnoNascimento") <= 1979), "Geração X")
                               .when((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994), "Millennials")
                               .when((col("AnoNascimento") >= 1995) & (col("AnoNascimento") <= 2015), "Geração Z")
                               .otherwise("Outra"))

# Contar a quantidade de pessoas de cada país para a geração Millennials
generation_counts = df_nomes.filter(col("Generacao") == "Millennials").groupBy("Pais").count().orderBy("Pais")
generation_counts.show()
