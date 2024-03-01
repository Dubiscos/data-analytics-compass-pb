# Data Analytics Fundamentals

## análise de dados e soluções de avaliação de dados

Avaliação é um exame detalhado de algo para entender sua natureza ou determinar suas características essenciais. 
Avaliação de dados é o processo de compilar, processar e analisar dados para que você possa usá-los para tomar decisões.
Análise é a avaliação sistemática de dados. 
Análise de dados é o processo analítico específico sendo aplicado.

O componente de coleta é onde os serviços montam dados de várias fontes.
O componente de armazenamento armazena dados em repositórios.
O componente de processamento é onde os serviços manipulam dados nas formas necessárias.
O componente de consumo é onde os dados são apresentados nos formatos necessários.

## Volume: armazenamento de dados

Há três classificações amplas de tipos de origem dos dados:
Dados estruturados são organizados e armazenados na forma de valores que são agrupados em linhas e colunas de uma tabela.
Dados semiestruturados muitas vezes são armazenados em conjuntos de pares de chave-valor que são agrupados em elementos em um arquivo.
Dados não estruturados não são estruturados de forma consistente. Alguns dados podem ter uma estrutura semelhante a dados semiestruturados, mas outros podem conter apenas metadados.

## Amazon S3

Esse serviço é um serviço de armazenamento de objetos, o que significa que você pode armazenar praticamente qualquer tipo de objeto com dados dentro dele.
Ele é escalável e pode chegar ao tamanho que você precisar.
As pessoas usam o Amazon S3 para sites, aplicativos para dispositivos móveis e Data Analytics.

Bucket - são como pastas de arquivos, só que maiores, melhor organizados e com mais mecanismos de segurança. São contêineres lógicos para objetos.

Com o Amazon S3, você pode separar a maneira como armazena os dados da maneira como os processa. Isso é conhecido como: desacoplar o armazenamento do processamento. Você pode ter buckets separados para os dados brutos, resultados de processamento temporários e resultados finais.
Com Amazon S3, você pode acessar qualquer um desses locais de armazenamento de um processo, em paralelo, sem afetar negativamente os outros processos.
O Amazon S3 torna-se o local central para armazenar conjunto de dados analíticos, fornecendo acesso a vários processos analíticos ao mesmo tempo. Isso permite que a solução evite o processo longo de movimentação de dados entre o sistema de armazenamento e o sistema de processamento.

Os benefícios do Amazon S3 são:
    - Armazenamento de qualquer coisa;
    - Armazenamento seguro de objetos;
    - Acesso HTTP nativamente on-line;
    - Escalabilidade ilimitada; 
    - Durabilidade de 99,999999999%.

Uma chave de objeto é um identificador exclusivo de um objeto em um bucket.

Cada URL de objeto do Amazon S3 contém o bucket e a chave de objeto do item. Uma chave de objeto é o identificador exclusivo de um objeto no bucket. Não há chave de usuário ou token de acesso integrado ao próprio URL.

Amazon Kinesis para dados de streaming e dispositivos AWS Snowball para grandes volumes de dados locais.
O AWS Glue para entender os dados dentro do seu data lake, prepará-los e carregá-los de forma confiável em datastores. Depois que o AWS Glue cataloga seus dados, eles são imediatamente pesquisáveis, podem ser consultados e estão disponíveis para processamento de ETL.

Um data lake na AWS pode ajudar a:
- Coletar e armazenar qualquer tipo de dados, em qualquer escala e com baixo custo;
- Proteger os dados e evitar acesso não autorizado;
- Catalogar, pesquisar e encontrar os dados relevantes em um repositório central;
- Executar novos tipos de avaliação de dados com rapidez e facilidade;
- Usar um amplo conjunto de mecanismos analíticos para análise única, streaming em tempo real, análise preditiva, IA e machine learning.

O AWS Lake Formation facilita a configuração de um data lake seguro em dias.
O AWS Lake Formation é um serviço que organiza e faz curadoria de dados dentro de data lakes do Amazon S3. Esse serviço garante a segurança e a conformidade de itens dentro do lake, bem como orquestra trabalhos de transformação utilizando o data lake e outros serviços AWS.

Os data lakes do Amazon S3 são um repositório centralizado para dados de todos os tipos. Dados estruturados, semiestruturados e não estruturados podem encontrar uma residência segura no Amazon S3.

O Amazon Redshift permite configurar e implantar um novo data warehouse em minutos.
O Redshift Spectrum permite combinar seu Data lake e o seu Data Warehouse como se fosse uma única fonte de dados.

O Amazon EMR File System, o EMRFS, pode catalogar dados dentro de um data lake no S3 e a partir do sistema de arquivos do Hadoop on-premises ao mesmo tempo.

Um subconjunto de dados de um data warehouse é chamado de data mart. Os data marts se concentram em apenas um assunto ou uma área funcional.

## Velocidade: processamento de dados

Batch é utilizado quando há uma grande quantidade de dados para processar e precisa realizar isso em determinados intervalos.
Streaming significa processar dados em um fluxo contínuo, ou seja, o processamento de dados que são gerados continuamente em pequenos conjuntos de dados, medido em kilobytes.

Amazon Kinesis Data Firehose e o Amazon Kinesis Data Streams, que são usados para consumir o fluxo de dados e carregar o fluxo de dados em datastore analíticos.

Processamento em batch: processa grandes quantidades de dados de uma só vez. Isso requer um sistema que possa coletar e armazenar esses dados até que o sistema de processamento possa lidar com tudo isso.
Processamento periódico: processa cargas de trabalho irregulares imprevisíveis. A impossibilidade de prever essas cargas de trabalho sobrecarrega os sistemas de big data.
Processamento quase em tempo real: processa pequenos picos de dados que devem ser coletados e processados em minutos após a coleta.
Processamento em tempo real: processa pequenos picos de dados continuamente. Esses dados devem ser apresentados à fase de análise em instantes após a coleta.

O Aamazon Glue é um serviço de ETL totalmente gerenciado, que categoriza, limpa, enriquece e move dados de maneira confiável, entre vários armazenamento de dados.

Hadoop Common é o conjunto de utilitários e bibliotecas Java que oferecem suporte a outros módulos do Hadoop. Essas bibliotecas ajudam a abstrair o sistema de arquivos dos componentes de processamento. Esses arquivos e scripts Java são necessários para iniciar o Hadoop.
O Hadoop Distributed File System (HDFS) é o sistema de arquivos distribuídos que armazena os dados em um ambiente de alta taxa de transferência de nós da comunidade. Essa arquitetura garante acesso aos dados do aplicativo com largura de banda agregada alta.
O Hadoop YARN é o framework de gerenciamento de recursos responsável por programar e executar trabalhos de processamento.
O Hadoop MapReduce é um sistema baseado em YARN que permite o processamento paralelo de grandes conjuntos de dados no cluster.

O AWS Lambda permite executar código sem provisionar ou gerenciar servidores. Você paga apenas pelo tempo de computação consumido, sem haver cobrança quando o código não está em execução.
O Amazon EMR fornece um framework Hadoop gerenciado que torna fácil, rápido e econômico processar grandes quantidades de dados em instâncias do Amazon EC2 dinamicamente escaláveis.

O Amazon Kinesis Data Firehose é a maneira mais fácil de capturar, transformar e carregar streams de dados em datastores da AWS para análises quase em tempo real usando ferramentas existentes de business intelligence.
O Amazon Kinesis Data Streams permite criar aplicativos personalizados e em tempo real para processar streams de dados usando frameworks comuns de processamento de streams.
O Amazon Kinesis Video Streams facilita o streaming seguro de vídeos a partir de dispositivos conectados à AWS, onde podem ser usados para análise, machine learning (ML) e outros processamentos.
O Amazon Kinesis Data Analytics é a maneira mais fácil de processar streams de dados em tempo real com SQL ou Java sem precisar aprender novas linguagens de programação ou frameworks de processamento.

O Amazon Athena é um serviço de consultas interativas que facilita a análise de dados no Amazon S3 usando o SQL padrão. O Athena é sem servidor, portanto, não há infraestrutura para gerenciar e você paga apenas pelas consultas executadas.
O Amazon QuickSight é um serviço de business intelligence (BI) rápido e desenvolvido para a nuvem que facilita o fornecimento de informações a todos em sua organização.

## Variedade: estruturas e tipos de dados

Dados estruturados são quentes, imediatamente prontos para serem analisados. 
Dados semiestruturados são mornos. Alguns estarão prontos para uso e outros podem precisar de limpeza ou pré-processamento. Dados não estruturados são um oceano congelado, repleto de tudo o que você precisa, mas separado por todo tipo de coisa de que você não precisa.

O Amazon RDS facilita a configuração, operaração e scaling de um banco de dados relacional na nuvem, tem tudo o que você pode precisar para um banco de dados OLTP altamente eficiente.

Os dados de arquivos de texto puro são armazenados sem estrutura rígida.
Os dados OLTP são estruturados para fins de entrada de dados.
Os dados OLAP são estruturados para fins de recuperação de dados.

O Amazon Neptune é um serviço de banco de dados de grafo rápido, confiável e totalmente gerenciado que facilita a criação e a execução de aplicativos que funcionam com conjuntos de dados altamente conectados.

Um data warehouse multidimensional é mais adequado para um banco de dados relacional.
Os arquivos de log são geralmente produzidos na forma de arquivos XML ou JSON, que são muito adequados para armazenamento em um banco de dados de documentos.
Os dados coletados de sites de jogos on-line geralmente são muito rápidos em geração e temporários por natureza. Esses dados são adequados para um banco de dados de chave-valor.
Os dados transacionais de um serviço de assinatura social podem ser armazenados em um banco de dados relacional, mas devido ao componente social, seriam mais adequados às vantagens obtidas usando um banco de dados de grafo.

Os bancos de dados não relacionais são otimizados para computação e são bons em scaling horizontal. O design de dados para bancos de dados não relacionais é um documento desnormalizado, uma coluna ampla ou com base em chave-valor. Por fim, bancos de dados não relacionais são comumente usados para aplicativos móveis e web OLTP, mas não para sistemas de negócios OLTP.

## Veracidade: limpeza e transformação

Os esquemas lógicos se concentram nas restrições a serem aplicadas aos dados no banco de dados. Isso inclui a organização de tabelas, visualizações e verificações de integridade.
Os esquemas físicos se concentram no armazenamento real de dados em disco ou em um repositório de nuvem. Esses esquemas têm detalhes sobre os arquivos, índices, tabelas particionadas, clusters e muito mais.

O estágio de compartilhamento é aquele em que os consumidores obtêm acesso aos dados na forma de relatórios. A maioria dos consumidores terá uma boa ideia de quais números devem ser. Se os consumidores não encontrarem o que esperam, questionarão a validade dos dados.

A integridade relacional garante que ambos os membros de uma relação permaneçam consistentes.
A integridade da entidade garante que os valores em um campo permaneçam consistentes.
Um esquema de informações é um banco de dados de metadados que contém informações sobre todos os objetos do banco de dados.
Um esquema lógico lista as restrições, relações e propriedades de tabelas e exibições em um banco de dados.

ACID é um acrônimo para Atomicidade, Consistência, Isolamento e Durabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.
A conformidade com ACID impõe consistência em todas as instâncias de um banco de dados antes que a alteração esteja disponível aos usuários.

BASE é um acrônimo para BAsicamente disponível, eStado flexível, Eventualmente consistente. É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.
A conformidade com BASE impõe consistência eventual em todas as instâncias de um banco de dados. Isso deixa as alterações de dados disponíveis muito mais rápidas do que outros métodos de consistência.

O Amazon EMR é uma abordagem mais prática para criar seu pipeline de dados. Esse serviço fornece uma plataforma robusta de coleta e processamento de dados. Para usar esse serviço, sua equipe deve ter sólido conhecimento técnico e know‑how. A vantagem dele é que você pode criar um pipeline personalizado para atender às suas necessidades de negócios. Além disso, os custos de infraestrutura podem ser menores do que executar a mesma carga de trabalho no AWS Glue.

O AWS Glue é uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR. Isso torna o serviço ideal para tarefas simples de ETL, mas você não terá tanta flexibilidade quanto teria com o Amazon EMR. Você também pode usar o AWS Glue como um metastore para seus dados transformados finais usando o AWS Glue Data Catalog. Esse catálogo é uma substituição de uma metastore do Hive.

## Valor: relatórios e business intelligence

Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. Esse termo geralmente é sinônimo de análise de dados.

A análise operacional é uma forma de análise usada especificamente para recuperar, analisar e relatar dados para operações de TI. O uso de algoritmos matemáticos e outras inovações para extrair informações significativas do mar de dados brutos coletados por tecnologias de gerenciamento e monitoramento

O Amazon DynamoDB é o local de armazenamento dos dados do aplicativo. O AWS Data Pipeline orquestra o fluxo de dados e a preparação para uso no Amazon SageMaker. Em seguida, você pode treinar um modelo de ML para usar os dados no Amazon SageMaker para fazer previsões em tempo real com base na atividade do usuário.

O Amazon QuickSight é um serviço analítico de negócios rápido, fácil de usar e desenvolvido para a nuvem que permite que todos os funcionários de uma empresa criem exibições, executem avaliações únicas e extraiam rapidamente informações empresariais de seus dados, a qualquer momento, em qualquer dispositivo.
Com o Amazon QuickSight, é possível fazer upload de arquivos CSV e Excel; conectar-se a aplicativos de software como serviço (SaaS), como o Salesforce; acessar bancos de dados on-premises, como o SQL Server, o MySQL e o PostgreSQL; e utilizar de forma contínua suas origens de dados da AWS, como o Amazon Redshift, o Amazon RDS, o Amazon Aurora, o Amazon Athena e o Amazon S3.

# Data Analytics on AWS

## Market Opportunity

Collect: Amazon Kinesis Data Streams, Amazon Kinesis Data Firehose, AWS Snowball, AWS Direct Connect
Store: Amazon S3, Amazon S3 Glacier, Amazon DynamoDB, Amazon RDS, Amazon ED, Amazon CloudSearch, Amazon Aurora
Process/ Analyze: Amazon EMR, Amazon Athena, Amazon Redshift, Amazon Kinesis Data Analytics, Amazon SageMaker
Visualize: Amazon QuickSight
Automate: AWS Database Migration Service, AWS Glue

## Analytics Solutions on AWS

Data, visualization, engagement, and machine learning
- AWS Data Exchange, Amazon QuickSight, Amazon Pinpoint, Amazon SageMaker, Amazon Comprehend, Amazon Polly, Amazon Lex, Amazon Rekognition, Amazon Translate
Analytics
- Amazon Redshift, Amazon EMR(Spark and Presto), Aws Glue (Spark and Python), Amazon Athena, Amazon ES, Amazon Kinesis Data Analytics
Data lake infrastructure and management
- Amazon S3/ S3 Glacier, AWS Lake Formation, AWS Glue
Data movement
- AWS Database Migration SErvice, AWS Snowball, AWS Snowmobile, Amazon Kinesis Data Firehose, Amazon Kinesis Data Streams, Amazon Managed Streaming for Apache Kafka

Data Analytics services
- Amazon Athena - Serveless interactive query service in using SQL
- AWS Glue - Prepare and load data
- AWS Data Exchange - Find and subscribe to thisd-party data in the cloud
- Amazon SageMaker - Build, train, and deploy machine learning models at scale

Managed Services for open source
- Amazon EMR - Easily run open source data applications
- Amazon Managed Straming for Apache Kafka - Build real-time streaming data pipelines and applications
- Amazon ES - Deploy, monitor, and troubleshoot applications at scale, using tools of preference

# Amazon Redshift

Amazon Redshift is a fully managed, columnar cloud data warehouse. You can use it to run complex analytical queries on large datasets through massively parallel processing (MPP) technology.

Amazon Redshift is an efficient solution to the challenge of collecting, storing, and analyzing all structured or semi-structured data. You can view historical trends and gain new insights in real time. It also provides the ability to run predictive analytics on your datasets, including third-party datasets you are allowed to access.

# Why Analytics for Games

