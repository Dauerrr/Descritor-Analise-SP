# Descritor
Relevância: o consumo de bebidas alcoólicas é presente na vida de muitas pessoas, e as motivações pelo uso são fatores importantes. Nesse framework, queremos explorar uma motivação indireta, o clima, e como ele influencia as pessoas a consumirem álcool. O código tem como objetivo consultar os dados do Dataframe escolhido para relacionar o consumo com fatores climáticos. 

Framework: O código tem como base a classe mãe “DescritorTabela”, dentro dela existe diversos métodos como “preparar_df” que renomeia as colunas, transforma a coluna “Data” em valor “datatime” e transforma as demais colunas em valor numérico. Todos os outros métodos têm como objetivo consultar os dados solicitados como (Consumo em litros, temperatura e precipitação) e o dia correspondente do mesmo. Existe também outras duas classes filhas “DescritorRemoto e DescritorLocal” que diversificam a obtenção dos dados. 

Para utilização do Framework basta digitar em seu Python console “pip install FrameWorkConsumo==0.0.1".
