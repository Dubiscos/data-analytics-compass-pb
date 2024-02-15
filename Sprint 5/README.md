# RELATORIO  

## Aspectos economicos da cloud  

Os aspectos econômicos na nuvem focalizam duas áreas: valor comercial e gerenciamento financeiro na nuvem.  

Valor comercial inclui todos os componentes que promovem os negocios dos cliente.  
Gerenciamente financeiro na nuvem se concentra em ajudar os clientes da aws a terem sucesso no gerenciamento financeiro na infraestrutura da nuvem.  

A conversa e a análise do valor comercial ajudam você a abordar os componentes financeiros que normalmente são as principais preocupações dos clientes em potencial.  
O cliente precisa ter todos os dados necessários para tomar uma decisão de compra com confiança.  
Abordar as preocupações relacionadas ao componente financeiro e progredir para uma prova de conceito é o objetivo da interação sobre o valor comercial.  

O valor é entregue por meio de atividades, como provas de conceito, revisões de arquitetura, migração de cargas de trabalho e assim por diante.  

O Cloud Value Framework é composto de cinco pilares: redução de custo, produtividade da equipe, resiliência operacional, agilidade empresarial e sustentabilidade.  
- A redução de custos é realizada evitando as infraestruturas on-premises com grandes gastos fixos e reduzindo a variável de gastos contínuos usando as economias de escala das ofertas da AWS.  
- A produtividade da equipe é medida em resultados maiores pela equipe do mesmo tamanho porque muito do trabalho tático anterior não é mais necessário.  
- A resiliência operacional é conquistada com maior disponibilidade e segurança e menor tempo de inatividade.  
- A agilidade empresarial consiste nos novos produtos, nas novas expansões de geolocalização ou de mais recursos dos produtos existentes que os clientes podem fornecer.  
- A sustentabilidade é a redução do impacto ambiental das operações de TI.  

## Reducao de custos

A redução de custos se refere a quanto os clientes pagam pela TI tradicional em comparação com o que pagariam usando a AWS, em números reais.  
Uma ferramenta para informar é a analise de redução de custos.  

A superprovisão e a subprovisão não são mais problemas. Os clientes alinham a infraestrutura, serviços e custos aos padrões de uso.  

Três modelos de preços gerais para a compra de recursos de computação do Amazon Elastic Compute Cloud (Amazon EC2):  

- Os preços de instâncias sob demanda permitem que os clientes paguem pela capacidade computacional que realmente usam por hora, sem compromissos de longo prazo. É possível usar esse modelo de preços para cargas de trabalho com vários graus de disponibilidade, como um ambiente de sandbox ou de um projeto com um cronograma limitado. Se os requisitos de disponibilidade média de instâncias do Amazon EC2 forem maiores que aproximadamente 70 horas por semana, poderá ser mais vantajoso colocar esses ambientes em um modelo de preços diferente.  

- O Savings Plans e as instâncias reservadas são modelos flexíveis que oferecem preços mais baixos em comparação com os preços sob demanda, em troca de compromissos de uso específico em um período de um a três anos.  

- As Spot Instances do Amazon EC2 oferecem capacidade computacional de reserva na nuvem AWS, com grandes descontos em comparação com as instâncias sob demanda. As Spot Instances permitem economizar até 90% em comparação com as instâncias sob demanda e são melhores para cargas de trabalho tolerantes a falhas, como processamento em batch, renderização e cargas de trabalho em contêiner.  

Ao realizar uma análise da redução de custo, você precisa considerar as muitas facetas do processo. Uma das facetas mais importantes é garantir que todos os stakeholders estejam incluídos na primeira conversa e sejam mantidos no loop continuamente. Isso significa que TI, finanças e outros membros da organização envolvidos na adoção da nuvem devem ser incluídos na reunião inicial.  

O uso de percentuais realistas ajuda a dimensionar um ambiente da AWS baseado no que o cliente realmente precisa, em vez de simplesmente replicar todos os servidores on-premises na nuvem.  

Uma análise de redução de custos calcula o custo total de propriedade para comparar a execução de um ambiente de TI tradicional completo on-premises com a implantação da AWS. Use uma análise de redução de custos para ajudar o cliente a comparar custos e criar um caso de negócio para fazer a transição para a AWS.  

## Produtividadeda equipe

No Cloud Value Framework, a produtividade da equipe se refere à eficiência adquirida com a redução ou a eliminação das tarefas não mais necessárias com os serviços de nuvem.   
Os recursos dos clientes podem migrar para um trabalho mais estratégico.  

A AWS analisa seis categorias principais de funções relacionadas à TI: servidor, rede, armazenamento, aplicativo, instalações e segurança.  
As três primeiras funções de TI, servidor, rede e armazenamento, são centradas no gerenciamento da infraestrutura de hardware. As funções comuns incluem administradores, implementadores e engenheiros. A produtividade da equipe também inclui funções de aplicativos cobertas por funções como database administrators, AppDev, QA e funções de suporte. As funções de instalações abrangem principalmente o gerenciamento das instalações e incluem funções para clientes que têm um data center on-premises. Por fim, as funções de segurança ajudam as empresas a garantir que sua infraestrutura atenda aos padrões de conformidade, normativos e corporativos.  

## Resiliencia operacional  

A resiliência operacional é o benefício conquistado com a melhoria na disponibilidade e na segurança.   
Isso representa mais tempo ativo, menos tempo de inatividade e risco reduzido.  

Custos de tempo de inatividade incluem:  
- Taxas de terceiros  
- Substituição de equipamentos  
- Custos incidentais após o ocorrido  
- Atividades e custos de recuperação  
- Custos de detecção associados à descoberta inicial e investigações subsequentes  
- Equipe de TI improdutiva e custos de usuários finais  
- Perda de receita  
- Custos de interrupção dos negócios  
- E muito mais   

Muitas vezes, as causas do tempo de inatividade não são os ataques externos. O tempo de inatividade costuma ocorrer porque a demanda de serviços excede a capacidade da infraestrutura para atendê-la. É por isso que o tempo de inatividade geralmente ocorre durante os horários de pico, enquanto o banco de dados está com um número excessivo de consultas.  

As organizações de TI com resiliência operacional dependem da integridade de quatro pilares: operações, segurança, software e infraestrutura.   

Algumas causas principais de falhas operacionais. Elas incluem:   
- Erros humanos, como a falta de procedimentos claramente definidos ou privilégios de usuário  
- Erros de configuração nas definições do hardware ou do sistema operacional e scripts de inicialização  
- Erros de procedimentos, como restaurar o backup incorreto ou esquecer-se de reiniciar um dispositivo  
- E acidentes comuns no data center, como tropeçar nos cabos, derrubar o equipamento ou desconectar dispositivos  

A AWS usa a automação; gerencia serviços de ponta a ponta; proporciona a visibilidade de todo o sistema para uso, desempenho e métricas operacionais; usa a configuração de segurança e de governança dos recursos da AWS e monitora o acesso à API.  

Algumas das causas de violações de segurança. Elas incluem:  
- Malware, como worms e vírus  
- Ataques de rede, como portas abertas e pacotes fragmentados  
- Aplicativos ou sistemas operacionais sem aplicação de patches  
- Problemas de segurança, como divulgações de senhas e credencias não armazenadas com segurança  
- E autenticação precária ou limitada  

A AWS tem um modelo de segurança que compartilha as responsabilidades de segurança com os clientes. Nesse modelo, a AWS é responsável pela segurança de tudo, do nível do hipervisor ao sistema operacional.  

Isso ajuda a reduzir os riscos de segurança de várias maneiras, como:  
- Usar a automação e as ferramentas da AWS para ajudar os clientes a minimizar os riscos de segurança mais graves, incluindo DDoS  
- Fornecer o serviço AWS Identity Access Management (IAM) para gerenciar centralmente usuários e credenciais  
- Usar uma lista de mais de 30 certificações e credenciamentos de conformidade para ajudar nossos clientes a criarem ambientes seguros e em conformidade  

Algumas causas comuns de falhas na resiliência do software. Elas incluem:  
- Esgotamento de recursos, como processos descontrolados, vazamentos de memória e aumento de arquivos  
- Erros de computação ou de lógica, como referências incorretas, indicadores corrompidos e erros de sincronização  
- Monitoramento inadequado, como inabilidade de identificar problemas  
- Atualizações com falha, como intercompatibilidade e integrações  

Para fornecer resiliência de software, a AWS:  
- Oferece implantações azuis/verdes que permitem reversões rápidas  
- Automatiza a integração e o fluxo de trabalho de entrega contínuos  
- Executa implantações de código menores para reduzir bugs de unidade, de integração e do sistema  
- Fornece recursos atuais e seguros com aplicação de patches do sistema operacional  
- Cria e gerencia um conjunto de recursos relacionados da AWS  

Algumas causas de falhas na infraestrutura. Elas incluem:  
- Falha de hardware de servidores, armazenamento ou redes  
- Desastres naturais, como furacões, inundações e terremotos  
- Interrupções de energia, como falha no fornecimento de energia e nas baterias  
- Ataques volumétricos, como DDoS e amplificação do Sistema de nomes de domínio (DNS)  

A AWS ajuda a reduzir falhas na infraestrutura de várias maneiras.  
- A AWS continua a expandir nossa infraestrutura e lidera o setor em melhorias de data centers em grande escala.  
- Nossos clientes podem executar aplicativos e fazer failover em várias zonas de disponibilidade e regiões.  
- Os sistemas da AWS são criados para serem altamente disponíveis e duráveis.  
- Como padrão, cada zona de disponibilidade em cada região é conectada de modo redundante a vários provedores de trânsito de camada 1.  
- Cada instância de computação é atendida por duas fontes de energia independentes, cada uma com serviço público, fonte de alimentação ininterrupta e gerador de energia de backup.  

## Agilidade empresarial  

A agilidade empresarial significa entregar mais, por exemplo, responder mais rapidamente, fazer mais experiências e entregar resultados no mesmo tempo ou antes.  

A "falha rápida" permite que uma organização encerre cada iniciativa com falha sem o trabalho e os recursos desperdiçados associados a um ambiente on-premises não flexível.  

## Sustetabilidade  

A sustentabilidade significa evitar o esgotamento dos recursos naturais para manutenção do balanço ecológico.  

## Gerencimaneto financeiro na nuvem  

O gerenciamento financeiro na nuvem inclui quatro pilares:  

- A medição e a responsabilidade focalizam o estabelecimento da transparência de custos e a responsabilidade por meio das etapas necessárias para garantir a visibilidade dos gastos.  
- A otimização de custos focaliza a identificação de desperdícios, a criação de arquiteturas compatíveis com a nuvem que são dimensionadas com base na demanda e na melhoria da eficiência de custos.  
- O planejamento e o forecast focalizam a obtenção de uma melhor compreensão dos custos associados às necessidades de TI atuais e futuras, o que promove planejamento financeiro e empresarial mais preciso.  
- As operações financeiras na nuvem focalizam a identificação e o investimento em pessoas, processos, ferramentas e automação para oferecer suporte ao gerenciamento financeiro na nuvem.  

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Computação da AWS  

Instâncias do EC2 = componentes básicos  
Aplicar AMIs para personalizar  
Configurar o auto scaling e o balanceamento de carga  
Pagar pelo que é usado  

## Armazenamento da AWS  

Amazon EBS fornece discos para instâncias e replica cada volume do EBS após a criação  
Amazon S3 é para armazenamento em massa, como imagens, videos, código e tem alta disponibilidade e velocidade de acesso, alem de ter camadas diferente com base na frequencia para acessar.  
Amazon Glacier armazenamento de backup de longa data   

## Banco de dados  

Substituir as tarefas diárias de gerenciamento por processos de valor agregado  

## Redes  

VPC = rede virtual na nuvem  
Sub-redes públicas e privadas   
ACLs de rede  
Grupos de segurança  

## Segurança  

Modelo de responsabilidade compartilhada da AWS  
Ferramentas de segurança  
AWS IAM  
Orientação de conformidade  

## Resumo  

Os usuários da AWS podem criar e gerenciar recursos na plataforma de três formas. Todas as três opções são criadas em uma interface de programação de aplicativo (API) comum, semelhante ao REST, que serve como base da AWS.   

O AWS Management Console fornece uma interface gráfica avançada para a maioria dos recursos oferecidos pela AWS. Ele facilita o gerenciamento de nuvem de todos os aspectos da conta da AWS do cliente, incluindo o monitoramento dos gastos mensais por serviço, o gerenciamento de credenciais de segurança ou até mesmo a configuração de novos usuários do IAM.  

A AWS Command Line Interface (AWS CLI) fornece um conjunto de utilitários que podem ser executados por meio de um programa de comando no Linux, Mac ou Windows. A CLI é uma ferramenta de código aberto que fornece comandos para interagir com os serviços da AWS.  

Os AWS software development kits (SDKs) são pacotes que dão acesso à AWS em uma variedade de linguagens de programação populares. A AWS gerencia a infraestrutura como código usando os SDKs e as APIs subjacentes a eles. Esses SDKs específicos da linguagem contêm APIs com as quais os clientes podem incorporar a grande variedade de serviços de nuvem AWS em seu código sem escrever as funções por conta própria.  

## Descobertas  

As conversas voltadas para o cliente se enquadram em três categorias distintas, com base em marcos típicos do ciclo de vendas.  
- A descoberta é a reunião de coleta de informações para ajudar você a compreender os desafios dos clientes.  
- Depois que todas as informações necessárias que identificam as metas e os pontos problemáticos do cliente forem coletadas, você se reunirá com o cliente novamente para apresentar suas descobertas e propor uma ou mais soluções da AWS. Na verdade, isso pode acabar se tornando várias reuniões, dependendo da necessidade de ajustes na solução.  
- Assim que o cliente concordar com uma solução em potencial, você perguntará se ele gostaria de avançar com uma prova de conceito (POC), na qual avaliará a solução em seu próprio ambiente.    
