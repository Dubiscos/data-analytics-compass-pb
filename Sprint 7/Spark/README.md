# SPARK

## O que é
Ferramenta de processamento de dado (não é uma data storage)
Distribuido em um Cluster
Dados em HDFS ou Cloud

## Componentes
Machine Learning (Mlib)
SQL (Spark SQL)
Processamento em Streaming
Processamento de Grafos (GraphX)

## Estrutura
Drive: Inicializa SparkSession, solicita recursos computacionais do cluster Manager, transforma as operações em DAGs, distribui estas pelos executers
Manager: Gerencia os recusos do cluster. Quatro possíveis: built-in standalone, YARN, Mesos e Kubernetes
Executer: roda em cada node do cluster executando as tarefas

## Formatos
Parquet - Colunar, padrão do Spark
ORC - Colunar, padrão do Hive
Avro - Linha

Muitos atributos e mais escrita = linha
Menos atributos e mais leitura = coluna

## RDD - Resilient Distributed Datasets
Estrutura básica de baixo nível
Dados "imutáveis", distribuídos pelo cluster
Em memória
Pode ser persistindo em disco
Tolerante a falha
Operações sobre um RD criam um novo RDD

Complexo e verboso
Otimização difícil pelo Spark

## Dataframe
Tabelas com linhas e colunas
Imutáveis
Com schama conhecido
Lihagem preservada
Colunas podem ter tipos diferentes
Existem análises comuns: Ahrupar, ordenar, filtrar
Spark pode otimizar estas analises através de planos de execução

## Comandos

*importante* o spark apenas executa o comando quando encontrar o ";"

NOME(escolha de nome) = spark.read.loado("caminho do arquivo") = carrega o arquivo para o spark

spark.sql("create database NOME BD") = cria um banco de dados
spark.sql("use NOME BD") = para usar o banco de dados

NOME.write.saveAsTable("NOME") = cria dataframes e salvar dentro do banco de dados (criando cada dataframe dento do databse cria uma DW)

spark.sql("show tables").show() = mostra as tabelas criadas dentro do banco de dados
spark.sql("select * from NOME").show() = seleciona todas as colunas da tabela escolhida e mostra com show (teste de tabela)

