<h1 align="center"> Projeto de um pipeline de dados para um construtora </h1>

<img alt="Static Badge" src="https://img.shields.io/badge/Status-Em_andamento-yellow"> <img alt="Static Badge" src="https://img.shields.io/badge/Vers%C3%A3o-0.5-yellow"> <br>
<img alt="Static Badge" src="https://img.shields.io/badge/VS_Code-007ACC?logo=visualstudiocode"> <img alt="Static Badge" src="https://img.shields.io/badge/Google_Cloud-4285F4?logo=googlecloud&logoColor=white"> <br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white"> <img alt="Static Badge" src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white"> <img alt="Static Badge" src="https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi"> <br>

<br>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Projeto consiste em construir um pipeline de dados comerciais que extrai dados de uma API, aplica as devidas transformações e enriquecimentos necessários, e em seguida realiza a carga desses dados no Google BigQuery, onde os dados ficam disponiveis para serem consumidos por dashboards no Power BI.</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;Na pasta raiz temos os código de entrypoints, que servem como inicializadores (gatilhos) de cada fluxo de dados, para serem autoamizados no CloudRun do google.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Na pasta extratores ficam os códigos responsáveis por fazer a conexão com a API e a extração dos dados necessários. Os mesmos são extraídos no formato .json.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Na pasta transformadores temos os códigos que fazem a transformação dos .json para um DataFrame no pandas, e de acordo com a necessidade de consumo desses dados, é feito tratamento e enriquecimento dessas tabelas com os dados.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Na pasta carregadores temos o código que faz a conexão com o bigquery, permitindo que seja feita a carga das tabelas para o mesmo.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;A pasta fluxos contem os codigos que "orquestram" cada pipeline, ou seja, para cada fluxo de dados que é desejado, o código faz a sequencia de extração, transformação, enriquecimento e carregamento utilizando as funções criadas em cada um dos códigos das etapas citadas anteriorimente, fazendo assim o código trabalhar de forma modular.</p>
<br>

A imagem abaixo teve varios dados retirados e/ou modificados de forma propósital afim de manter o sigilo.
<img src="https://prnt.sc/FlA2qzJt5d9i" alt="Exemplo de um dashboard confeccionado com os dados do pipeline.">
