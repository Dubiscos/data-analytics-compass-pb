# Estatísticas  
Serve para coletar, apresentar, interpretar  
Bibliotecas python estatística: NumPy, RPy, Scipy, Pychem, Pandas, Matplotlib, Seaborn  
População – todos os elementos (indivíduos, itens ou objetos) cuja as características estejam sendo estudadas  
Censo – conjunto de características obtidas de todos os membros da população  
Amostra – parte coletada a partir da população  
# Gráficos de barras:  
Variáveis qualitativas, formado por retângulos horizontais iguais  
Objetivo de comparar grandezas entre categorias (designações extensas)  
Plt.barh() – criar gráfico de barras horizontal  
Plt.bar() – criar gráfico de barra vertical  
Plt.variavavellabel – nomeia as barras  
# Gráficos de setores:  
Divide um círculo em setores proporcionais as frequências observadas nas categorias  
Plt.pie() – criar gráfico de setores  
# Gráficos de linhas:  
Para series cronológicas  
Plt.plot() – cria gráfico de linha  
# MTC:  
Medida descritiva para resumir dados  
Se calculadas a partir de dados populacionais temos parâmetros  
Se calculada a partir de dados amostrais temos estimadores ou estatísticas  
# MD:  
Dados apresentam semelhanças e variabilidades  
Permitem identificar até que ponto os resultados se concentram ou não ao redor da tendencia central de um conjunto de observações  
Md auxiliam as medidas de tendencia central a escrever melhor os dados  
Indicam o quanto os dados estão ou não próximos uns do outros  
Precisa de uma mtc e md para descrever adequadamente dados  
Amplitudade total: é a diferença entre o maior e o menor valor observado, não leva em considerações valores intermediários  
Amplitude interquartílica: diferença entre o primeiro r o terceiro quartil, média mais estável do que a amplitude total, abrange 50% dos dados, útil para detectar valores discrepantes  
Desvio médio: diferença entre cada valor observado e a média, soma dos desvios pé igual a zero (precisa tirar o modulo), devemos desconsiderar os sinais utilizando o modulo e media dessas diferenças  
Variância e desvio padrão: algumas propriedades matemáticas para o desvio médio possuem desvantagens, assim utilizando a variância  
Coeficiente de variação: indica a variabilidade da medida em relação da media  

# MA:    
Construção de um histograma, interessado em saber a forma de distribuição dos dados  
Classificações de frequências: simétrica, assimétrica negativa, assimétrica positiva  
Medidas de curtose: quantifica a concentração ou dispersão dos valores de um conjunto de dados em relação as medidas de tendência central, mede o grau de achatamento de uma distribuição, complementar as informações de dispersão  
Calssficiação de achatamento:   
Leptocúrtica são dados muito concentrados em torno do centro (K < 0,263)  
Mesocúrtca são dados levemente concentrados em torno do centro ( K = 0,263)  
Platicúrtica são dados pouco concentrados em torno do centro (K > 0,263)  
Boxplot é um gráfico que utiliza cinco medidas estatísticas: valor mínimo, valor máximo, mediana, primeiro quartil, terceiro quartil. Assim oferece a ideia de posição, dispersão, assimetria, caudas, dados discrepantes.  
 