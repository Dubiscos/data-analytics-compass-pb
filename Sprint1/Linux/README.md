## Matéria
Linux

## Relatório
Aprendi nesse módulo como utilizar e configurar a Virtual Machine. O básico do funcionamento e configuração do sistema Linux e seus comandos principais do terminal como criação e edição de diretórios e arquivos, download de programas e significado das permissões.  

## Comandos Linux (Ubuntu)

sudo = comando para permisão de super usuário  
su = alterar entre usários (padrão root)  

clear = limpa linhas terminal
pwd = mostra caminho completo do diretório atual  

crtl + c = cancela ação  
crtl + shift + c = copia  
crtl + shift + v = copia  

cd = mudar diretórios  
cd - = retorna diretório  
cd~ = volta home  
cd /(nome diretorio1)/(nome diretorio2)/ = caminho entre diretórios  

ls = lista itens dentro do diretorio  
ls -L = lista com detalhes  
ls -lh = lista com tamanho  
ls -a = lista arquivos ocultos  
ls -m = lista divido por virgulas  
ls -R = lista mostrando os itens nos subdiretórios  

cat = mostra arquivo  
cat > nome.txt = cria  
cat nome > nome2 = junta em uma novo (nome3.txt)  
cat nome4 >> nome3 = junta no final do aquivo nome3  

touch = modifica hora de modificação arquivo  

man + comando = abre manual de todas as utlizaçaões do comando exemplo: man ls  

crtl+r = busca comandos já utilizados anteriormentes  

mkdir = criação de um unico ou mais diretórios  
rmdir = deleta diretório vázio  
cp = copia arquivos e diretórios (colocar primeiro doc/dir de copia e em seguida doc/dir de destino (copiar um diretório inteiro colocar -R))  
mv = mover arquivos  

sudo apt-get upddate = atualiza todos os repositórios instalados  
sudo apt-get upgrade = atualiza todos os aplicativos instalados  
sudo apt-get install (nome aplicativo) = instala o aplicativo    
sudo apt-get purge (nome aplicativo) = remove o aplicativo  
sudo apt-get autoremove = remove arquivos que não mais necessarios (recomendado roda 1x por mês)  
apt-cache search (nome aplicativo (ideal espeficiar versão ou modelo) = busca aplicativos possiveis para instalar  

# Siglas permissões  

utilizar comando chmod args arquico/diretório

d = diretório
r = read  
w = write  
x = execute  
*- = sem permissão*

1 222 333 444  
1 = dir ou arquivo  
222 = permissões do dono  
333 = permissões do grupo  
444 = permissões do usuário  

args saõ representados por:  

*+ = adicionar permissão*  
*- = remove permissão*  
= = substitui as permissões anteriores  
u = dono do arquivo  
g = grupo  
o = outros  
a = todos  

exemplo: chmod o=x = concede permissão de executar para outros  

utilizar comando chmod xxx arquico/diretório  

0 = sem permissão ---  
1 = executar --x  
2 = escrever -w-  
3 = ler e executar -wx  
4 = ler r--  
5 = ler e executar r-x  
6 = ler e escrever rw-  
7 = ler, escrever e executar rwx  
