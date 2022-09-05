# Challenge-RankMyApp
Repositório criado para o PS de Cientista de Dados da RankMyApp. De antemão, adianto que umo dashboard interativo foi gerado para solução deste desafio e o mesmo pode ser acessado [clicando aqui](https://desafio-rank-my-app-st5shwubpq-rj.a.run.app).

## Etapa 1 - EDA + Data Preparation
O objetivo desta etapa é entender mais sobre os dados de entrada bem como fazer as manipulações necessárias para realizar futuras análises sem quaisquer problemas sintáticos dos dados. A minha primeira busca então foi por valores ausentes, que são comumente encontrados mas, nesta aplicação, os dados de entrada não possuíam valores ausentes. Como o problema de negócio é relacionado apenas aos dados obtidos no canal o orgânico, realizei uma filtragem utilizando a coluna "Acquisition Channel", deixando apenas todos os registros cuja a condição "Acquisition Channel" == "Organic" era satisfeita.

Por fim, realizando as últimas análises nos dados já filtrados, na premissa de que alguma inconsistência poderia ter persistido, percebi que havia uma registro datado de "31/09/2019". Obviamente, tive que remover esse absurdo, visto que Setembro só possui 30 dias.

## Etapa 2 - Data Enrichment
Visando agregar e facilitar insights futuros, vi que para esse problema em específico poderia ser útil saber quais os dias da semana que possuem mais downloads, por exemplo. Da forma primitiva com que os dados estavam dispostos, essa informação poderia ser obtida. Sendo assim, criei uma coluna ("Referent Week Day") que diz a qual dia da semana aquela amostra de dados se refere. 


Ao final dessas etapas, é gerado um arquivo csv que pode ser encontrado na pasta "data", de nome "final_data.csv". Esse é o conjunto de dados que será utilizado para obtenção dos insights e criação do dashboard.