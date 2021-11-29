# Descritor-Analise-SP
Relevância: o consumo de bebidas alcoólicas é presente na vida de muitas pessoas, e as motivações pelo uso são fatores importantes. Nesse framework, queremos explorar uma motivação indireta, o clima, e como ele influencia as pessoas a consumirem álcool. O código tem como objetivo consultar os dados do Dataframe escolhido para relacionar o consumo com fatores climáticos. 

Framework: O código tem como base a classe mãe “DescritorTabela”, sua função “init” tem pré setado o caminho do Dataframe, a renomeação das colunas, transformação da coluna “Data” em valor “datatime” e transformação das demais colunas em valor numérico. Todas as outras funções tem como objetivo consultar os dados solicitados como (Consumo em litros, temperatura e precipitação) e o dia correspondente do mesmo. 

Limitações: No nosso framework, tivemos algumas limitações, nos quais cabem eventos específicos iguais em datas diferentes, por exemplo a mesma temperatura máxima em um ou mais dias. Além disso, ainda é necessária uma filtragem melhor entre os métodos da classe em relação ao inteiro conjunto de dados, para trazer uma visão macro entre as informações do Dataframe, através de análises estatísticos por exemplo. Resolvemos esse problema parcialmente com a criação da função “pesquisar_por_data” onde o usuário pode pesquisar uma data específica (no ano de 2015), retornando todos os valores do Dataframe. 

Para utilização do Framework basta digitar em seu python console “pip install descritor-analise-sp".
