# DOCKER
O que é docker?  
Reduz complexidade de setup de aplicações  
Configura containers que são como servidores para rodar aplicações  
Mais velocidade na configuração de ambiente dev  
Pouco tempo gasto em manutenção  
Livra do Matrix from hell  
Matriz from Hell:   
Tipos de volumes:  
Anônimos(anonymous) - diretórios criados pela flag -v, pro3em com um nome aleatório  
Nomeados(named) – soa volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente  
Blind mounts - uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informamos um diretório para este fim  

Containers: pacote de código que pode executar uma ação.  
Containers utilizam imagens para executar  
Múltiplos containers podem rodar juntos  
Imagem é o “projeto” que será executado, possui todas as instruções   
Container é o Docker rodando alguma imagem  
Fluxo: programamos uma imagem e a executamos por meio de um container  
Porta 80 é a porta padrão para acesso web  

YAML: linguagem de serialização  
Usada para arquivos de configuração, inclusive do Docker, para configurar o Docker composse.  

# Comandos:  
Docker ps ou Docker container ls – exibe containers executados no momento  
-a – mostra containers executados na maquina  
-l -mostra os últimos containers  
-d - Execução do container em background  
-i - Modo interativo. Mantém o STDIN aberto mesmo sem console anexado  
-t - Aloca uma pseudo TTY  
--rm - Automaticamente remove o container após finalização (Não funciona com -d)  
--name - Nomear o container  
Stop – para desliga o container  
Start – inicio o container  

# Docker Compose:   
Ferramenta para rodar múltiplos containers  

Comandos composse:  
Docker-composse up – roda a estrutura em compose  
Ctrl + c – para o composse no terminal  
-d – roda em background    
Docker-composse down – para os containers em background  
 
#Docker Swarm:  
Ferramenta para orquestrar containers, pode escalar horizontalmente    
O famoso cluster  
Facilidade do swarm para outros orquestradora é que todos os comandos são semelhantes ao do Docker  
Nodes – instancia que participa do swarm  
Manager node – node que gerencia os demais nodes  
Worker node – node que trabalha na função manager  
Service - conjunto de tasks que o manager node manda o work node executar  
Task – comandos que são executados nos nodes  

# Comandos:   
Docker swarm init – inicia o swarm  
--advertise-addr – declara o IP do servidos (faz com que a instancia/máquina vire um node e também transforme o node em um manager)  
Docker node ls – verifca os nodes ativos  
Docker sevice create –name <name> <imagem> - inicia um serviço  
Docker Swarm  
Docker service create –name <name> -p <porta> - cria serviço  
Docker service ls – lista os serviços  
Docker service rm <nome> - remove serviços  
Docker create –name <nome> --replicas <numero> <imagem> - criar serviço com um número maior de replicas  
Docker swarm leave – para de executar o swarm em uma instancia  
Docker node rm <id> - remove um node do ecossistema Swarm  
Docker Stack deply -c <arquivo.yaml> <nome> - roda compose com swarm  
Docker service update –imagem <imagem> <serviço> - atualiza as configurações do nodes (nodes com status active recebem atualizações)  
--network <rede> - cria uma rede  
Decker service update –network <rede> <nome> - conectar serviços que já estão em execução a uma rede    
Kubernetes : Ferramenta de orquestração de containers  
Control plane – onde é gerenciado o controle dos processos dos nodes  
Nodes – máquinas que são gerenciadas pelo control plane  
Deployment – a execução de uma imagem/projeto em um pod  
Pod – um ou mais containers que estão em um node  
Services – serviços que expoe os pods ao mundo externo  
Kubectl – cliente de linha de comando para o kubernetes  
Minikube start –driver=<driver> - inicia o minikube  
Minikube stop – para minikube  
Minikube dashboard – acessa o dashboard (detalhes do projetos)  
Kubectl create deployment <nome> --image=<imagem> - para rodas os containers das aplicações nos pods  
Kubectl get deployments – verifica os deploys  
Kubectl get podes – verifica os pods  
Kubectl describe pods – detalhes sobre pods  
Kubectl congi view – verfica como o kubernetes esta configurado  
Kubectl expose deploymente <nome> --type=<tipo> --port+<port> - cria uma serviço e expõe os pods  
