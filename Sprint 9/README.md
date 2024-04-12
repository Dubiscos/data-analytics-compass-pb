# Modelagem de Dados Relacionais

## Conceito e Modelo Relacional
O conceito deriva da teoria de conjuntos, representando dados como uma coleção de tabelas (entidade/relação) e suas linhas (tuplas) com valores de atributos. O Modelo Entidade-Relacionamento de Peter P. Chen explora a ideia de entidades no mundo real e seus relacionamentos, dividindo-se em "coisas tangíveis", funções e eventos.

## Objeto de Dados ou Entidade
Uma representação genérica de um componente do mundo real, armazenando informações relevantes para uma organização, podendo ser tangível ou intangível.

## Atributo
Propriedades que descrevem uma entidade, classificados como simples, compostos, monovalorados ou multivalorados, derivados e chaves.

## Relacionamento
Associações entre entidades, expressas por verbos e caracterizadas por cardinalidades como um para um, um para muitos ou muitos para muitos.

## Tipos de Modelos de Dados
Conceitual, lógico e físico, cada um representando diferentes níveis de abstração e detalhamento sobre os dados e seus relacionamentos.

## Integridade
Mantida por meio de restrições, como integridade de domínio e referencial, garantindo a precisão e consistência dos dados.

## Documentação e Normalização
Importância da documentação clara e precisa dos elementos do modelo, juntamente com a aplicação das formas normais (1FN, 2FN, 3FN) para evitar redundância e anomalias nos dados.

# Modelagem Dimensional

## Introdução
A modelagem dimensional é uma técnica essencial para a construção de Data Warehouses, projetada para facilitar o consumo de dados por ferramentas analíticas como OLAP (Processamento Analítico Online). Este resumo aborda conceitos fundamentais que permeiam a modelagem dimensional, independentemente das tecnologias específicas envolvidas.

## Granularidade
A granularidade dos dados define o nível de detalhamento em um modelo dimensional, influenciando diretamente o custo e a velocidade das consultas. Enquanto sistemas transacionais (OLTP) registram dados em nível atômico, a análise requer agregação dos dados em diferentes perspectivas.

## Modelagem Dimensional
Um sistema dimensional suporta alto volume de acesso via consultas, composto por elementos como fatos, dimensões e métricas. Os fatos representam medidas numéricas associadas a eventos de negócio, enquanto as dimensões fornecem contexto descritivo. Métricas são quantificações atribuídas aos fatos, sujeitas a funções agregadoras.

## Operações OLAP em Cubos
Operações como segmentação, divisão, aumento/diminuição de foco e pivô são essenciais para análises multidimensionais em cubos OLAP, permitindo visualizações detalhadas dos dados.

## Modelos Star Schema e Snowflake Schema
O Star Schema é um modelo dimensional com tabelas de fatos centralizadas, otimizado para consultas de alto desempenho. Em contraste, o Snowflake Schema normaliza hierarquias de dimensões, minimizando redundâncias de dados. Ambos os modelos têm impacto na performance e complexidade das consultas.

## Técnicas de Modelagem Dimensional
A transformação de um modelo relacional (OLTP) para um modelo dimensional envolve a reestruturação de tabelas de fatos e dimensões, simplificando consultas analíticas.
