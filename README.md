# Challenge-RankMyApp
Repositório criado para o PS de Cientista de Dados da RankMyApp. De antemão, adianto que umo dashboard interativo foi gerado para solução deste desafio e o mesmo pode ser acessado [clicando aqui](https://desafio-rank-my-app-st5shwubpq-rj.a.run.app).

## Etapa 1 - EDA + Data Preparation
O objetivo desta etapa é entender mais sobre os dados de entrada bem como fazer as manipulações necessárias para realizar futuras análises sem quaisquer problemas sintáticos dos dados. A minha primeira busca então foi por valores ausentes, que são comumente encontrados mas, nesta aplicação, os dados de entrada não possuíam valores ausentes. Como o problema de negócio é relacionado apenas aos dados obtidos no canal o orgânico, realizei uma filtragem utilizando a coluna "Acquisition Channel", deixando apenas todos os registros cuja a condição "Acquisition Channel" == "Organic" era satisfeita.

Por fim, realizando as últimas análises nos dados já filtrados, na premissa de que alguma inconsistência poderia ter persistido, percebi que havia uma registro datado de "31/09/2019". Obviamente, tive que remover esse absurdo, visto que Setembro só possui 30 dias.

## Etapa 2 - Data Enrichment
Visando agregar e facilitar insights futuros, vi que para esse problema em específico poderia ser útil saber quais os dias da semana que possuem mais downloads, por exemplo. Da forma primitiva com que os dados estavam dispostos, essa informação poderia ser obtida. Sendo assim, criei uma coluna ("Referent Week Day") que diz a qual dia da semana aquela amostra de dados se refere (Segunda-feira, Terça-feira, ...). 


Ao final dessas etapas, é gerado um arquivo csv que pode ser encontrado na pasta "data", de nome "final_data.csv". Esse é o conjunto de dados que será utilizado para obtenção dos insights e criação do dashboard.

## Etapa 3 - Dashboard
Para a criação do dashboard, optei por utilizar o Dash do Plotly, juntamente com o Flask e o Docker para a estruturação final e o Cloud Run do GCP para a hospedagem do dashboard. Na minha visão, a utilização do Dash, sobretudo de componentes Plotly, HTML, CSS e JS permite a construção de dashboards mais esteticamente limpos, bonitos, simples, interativos e leves. Dessa forma, as visualizações são bem mais personalizáveis (o limite é a imaginação do Cientista de Dados) visto que tal tecnlogia está a mais baixo nível que um PowerBI, por exemplo.

### Tela 1 - Periodic Analisys
Essa tela mostra algumas métricas que fazem sentido quando são analisadas por um período maior que 1 dia, ou seja, nos projetam um comportamento geral de um período especificado. As métricas mostradas são:
<ul>
    <li><strong>Total Views:</strong> Total de visualizações naquele período;</li> 
    <li><strong>More accum. views:</strong> Qual o dia da semana que possui mais visualizações acumuladas no período especificado;</li>
    <li><strong>Less accum. views:</strong> Qual o dia da semana que possui menos visualizações acumuladas no referido período;</li>
    <li><strong>Total Installations:</strong> Total de instalações(downloads) naquele período;</li>     
    <li><strong>More accum. installs:</strong> Qual o dia da semana que possui mais instalações acumuladas no período especificado;</li>
    <li><strong>Less accum. installs:</strong> Qual o dia da semana que possui menos instalações acumuladas no referido período;</li>
    <li><strong>Boom view days:</strong> Quantidade de dias, no período especificado, que possuem mais visualizações que a média de visualizações do período;</li>
    <li><strong>Boom installs days:</strong> Quantidade de dias, no período especificado, que possuem mais instalações que a média de instalações do período;</li>
    <li><strong>Best views day:</strong> Dia com mais visualizações no período fornecido;</li>
    <li><strong>Best installs day:</strong> Dia com mais instalações no período fornecido;</li>
    <li><strong>Worst views day:</strong> Dia com menos visualizações no período fornecido;</li>
    <li><strong>Worst installs day:</strong> Dia com menos instalações no período fornecido;</li>
</ul>