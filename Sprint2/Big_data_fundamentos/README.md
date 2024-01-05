## Matéria
Big Data Fundamentos

## Relatório
Nesse curso aprendi a estrutruta de uma bid data deste sua origem até o ponto para agrupamento. Banco de dados relacionais e NoSQL e modos de armazenamento como Data Warehouse e Data Lake. Fundamentos de Cloud Computing, Machine Larning, MLOps, DataOps, DaaS, Data Mesh e passos de projetos Big Data.

## Anotações

Capitulo 2

Big Data = 4V = Volume, Velocidade, Variedade, Veracidade.

O que é: Grande volume de dados que podem ser processados por banco de dados ou aplicações de processamento tradicionais.

Poder ajudar a encontrar padrões.
Big Data precisa de harmonia entre os 4V, se não tiver Nâo é Big Data.

- Big Data é a matéria-prima, dados
- Ciência de dados é um conjunto de técnicas para análise de dados.

Ciência de dados + Big Data = Big Data Analytics

Capitulo 3

Volume: é critico em Big Data

Armazenamento tem custo, definir o que armazenar.

Caso os dados possam ser e/ou são estruturados antes do armazenamento = Data Warehouse
Caso não são e/ou não podem ser estruturados antes do armazenamento = Data Lake ou Data Store

Banco de dados Relacionais: são estruturados e com schema (organização dos dados) bem definido.
O Schema é definido e criado antes do armazenamento.

Banco de dados NoSQL: os dados podem ser semi ou não estruturados e que outros tipos de relacionamentos podem existir entre os dados.
Não precisa definir o Schema antes do armazenmento ou o Schema é definido no momento de armazenamento.

Data Warehous é um sistema de armazemaneot que conecta e harmoniza grandes quantidades de dados de muitas fontes diferente.
Ajuda a tomar decisões

Data souces = Data Warehouse = Analysis, Reporting, Data Mining

Beneficios DW: Melhor análise de negócios, consulta mais rápida, melhoria de qualidade dos dados, visão histórica.

Data Lake é um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados.
Permite diferentes tipos de percepções sobre dados.
Podemos importar dados DW para Data Lake e vice-versa.

DW usa ETL(Extração, transformação e carga)
Data Lake usa ELT(Extração, carga e transformação)

Data Lake e DW podem fazer parte de uma grande estrutura central de armazenamento chamada DataHub

Beneficios Data Lake: Armazenamento em formato bruto, importação de qualquer quantiade de dados em tempo real, repositório central para todos os dados da empresa, sem necessidade de movimentação de dados.

Beneficios Data Store: Armazenamento de variados tipos de dados, flexibilidade, suporte a dados semi-estruturados, custo total menor.

Capitulo 4

Cluster de computadores é um conjunto de servidores com um memso propósito visando fornecer um tipo de serviço, como armazenamento ou processamento de dados.
Aumenta de forma considerável a capacidade computacional.

Capitulo 5

Cloud Computing é a entrega de serviços de computação que inclui servidores, aramzenamentos, banco de dados, rede, software, análise e intelig~encia pela intenret para oferecer recursos flexiveis, inovação e economia de escala.

Capitulo 6

Machine Larning é uma sub-área de IA e da ciência de computação que se concentra no uso de dados e algoritmos para imitar a forma como os humanos aprendem, melhorando gradativamente sua precisão.

MLOps é um conjunto de práticas para colaboração e comunicação.
Normalmene é tarefa do engenheiro de ML.
Operação do fluxo de trabalaho em ML.

DataOps é um conceito mais recente  que abrange toda a operação de dados de uma empresa.
É uma metodologia ágil e orientada a processos para desenvolver e entregar análises.

Capitulo 7

Data as a Service (DaaS) é uma estratégia de gerencimaneto de dados que visa alavancar os dados como um ativo de negócios para maior agilidade  no processo de análise.
Fornece uma maneira de gerenciar as grandes quantidade de dados que as organizações geram todos os didas e fornece essas informações para tomada de decisões baseados em dados.

Beneficios de DaaS: Monetização de dados, redução de custos, caminho mais rápido para inovação, agilidade no processo de decisão baseado em dados, menor risco no uso de dados, criação de uma cultura Data-Driven.

Data Mesh é uma abordagem para projetar e desenvolver arquitetura de dados.
Tem arquitetura descentralizada, diferente de DW e DL.
Trata dados como um produto, com cada fonte tendo seu próprio gerente/proprietário de produtos de dados.

Capitulo 8

ETL: Extrair e seguir com o a transformação para depois carregar, pode gerar um gargalo de dados.
ELT: Extrai e carrega em seguida, depois transforma os dados desejados, tem vazão mais rápida.

Capitulo 9

Passos de um projeto Big Data

1- Definição do Business Case
2- Planejamento do projeto
3- Definição dos requisitos técnicos
4- Criação de um "Total Business Value Assesmente"